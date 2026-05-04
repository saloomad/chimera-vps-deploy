#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


PLATFORMS = [
    "windows-codex",
    "windows-claude",
    "opencowork-local",
    "kimi-vps",
    "opencode",
]


def parse_simple_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def latest_handoff_name(root: Path) -> str:
    handoffs = sorted((root / "handoffs").glob("CHECKPOINT_*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return handoffs[0].name if handoffs else "none"


def coordination_summary(root: Path) -> dict[str, object]:
    states = []
    queues = []
    for platform in PLATFORMS:
        state_path = root / "session-states" / f"{platform}.yaml"
        queue_path = root / "publish-queue" / f"{platform}.yaml"
        state = parse_simple_yaml(state_path)
        queue = parse_simple_yaml(queue_path)
        states.append(
            {
                "platform": platform,
                "status": state.get("status", "missing"),
                "current_task": state.get("current_task", "missing"),
                "shared_publish_status": state.get("shared_publish_status", "missing"),
                "last_updated": state.get("last_updated", "missing"),
            }
        )
        queues.append(
            {
                "platform": platform,
                "publish_required": queue.get("publish_required", "missing"),
                "current_task": queue.get("current_task", "missing"),
                "reason_not_published": queue.get("reason_not_published", "missing"),
            }
        )
    return {
        "latest_handoff": latest_handoff_name(root),
        "states": states,
        "queues": queues,
    }


@dataclass
class ValidationResult:
    ok: bool
    problems: list[str]


def validate_platform(root: Path, platform: str, contract_path: Path | None) -> ValidationResult:
    problems: list[str] = []
    state_path = root / "session-states" / f"{platform}.yaml"
    queue_path = root / "publish-queue" / f"{platform}.yaml"
    if not state_path.exists():
        problems.append(f"missing session state: {state_path}")
    if not queue_path.exists():
        problems.append(f"missing publish queue: {queue_path}")

    if contract_path is not None and contract_path.exists():
        contract_text = contract_path.read_text(encoding="utf-8", errors="replace")
        contract_mtime = contract_path.stat().st_mtime
        review_outcome = "iterate"
        status = "active"
        for line in contract_text.splitlines():
            lower = line.lower()
            if lower.startswith("review_outcome:"):
                review_outcome = line.split(":", 1)[1].strip().lower()
            if lower.startswith("status:"):
                status = line.split(":", 1)[1].strip().lower()

        if state_path.exists() and state_path.stat().st_mtime + 0.001 < contract_mtime:
            problems.append("session state is older than the objective contract")

        needs_queue = status == "active" or review_outcome in {"iterate", "blocked"}
        if needs_queue:
            if not queue_path.exists():
                problems.append("publish queue missing while objective still needs shared follow-through")
            elif queue_path.stat().st_mtime + 0.001 < contract_mtime:
                problems.append("publish queue is older than the objective contract")

    return ValidationResult(ok=not problems, problems=problems)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def self_test() -> int:
    scenarios: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "handoffs").mkdir(parents=True)
        write_text(root / "handoffs" / "CHECKPOINT_2026-05-04_test.md", "# test\n")
        import os

        for platform in PLATFORMS:
            write_text(
                root / "session-states" / f"{platform}.yaml",
                f"platform: {platform}\nproject: chimera\nstatus: active\ncurrent_task: test\nreview_outcome: iterate\nshared_publish_status: in-progress-not-ready\nlast_updated: 2026-05-04T00:00:00Z\nproof: test\nnext_action: test\n",
            )
            write_text(
                root / "publish-queue" / f"{platform}.yaml",
                f"platform: {platform}\nproject: chimera\npublish_required: true\ncurrent_task: test\nreason_not_published: test\nlocal_only_changes: []\ntarget_repo: saloomad/chimera\nnext_action: test\n",
            )

        contract = root / "OBJECTIVE_CONTRACT.md"

        write_text(contract, "status: active\nreview_outcome: iterate\n")
        base_ts = datetime(2026, 5, 4, 0, 0, tzinfo=timezone.utc).timestamp()
        fresh_ts = datetime(2026, 5, 4, 0, 5, tzinfo=timezone.utc).timestamp()
        os.utime(contract, (base_ts, base_ts))
        os.utime(root / "session-states" / "windows-codex.yaml", (fresh_ts, fresh_ts))
        os.utime(root / "publish-queue" / "windows-codex.yaml", (fresh_ts, fresh_ts))
        result = validate_platform(root, "windows-codex", contract)
        scenarios.append(("active_with_current_queue_passes", result.ok))

        write_text(contract, "status: active\nreview_outcome: iterate\n")
        queue = root / "publish-queue" / "windows-codex.yaml"
        queue.unlink()
        result = validate_platform(root, "windows-codex", contract)
        scenarios.append(("missing_queue_fails", (not result.ok) and any("publish queue" in p for p in result.problems)))

        write_text(
            root / "publish-queue" / "windows-codex.yaml",
            "platform: windows-codex\nproject: chimera\npublish_required: true\ncurrent_task: test\nreason_not_published: test\nlocal_only_changes: []\ntarget_repo: saloomad/chimera\nnext_action: test\n",
        )
        write_text(
            root / "session-states" / "windows-codex.yaml",
            "platform: windows-codex\nproject: chimera\nstatus: active\ncurrent_task: test\nreview_outcome: iterate\nshared_publish_status: in-progress-not-ready\nlast_updated: 2026-05-04T00:00:00Z\nproof: old\nnext_action: old\n",
        )
        old_state = root / "session-states" / "windows-codex.yaml"
        old_queue = root / "publish-queue" / "windows-codex.yaml"
        old_ts = datetime(2026, 5, 4, 0, 0, tzinfo=timezone.utc).timestamp()
        newer_ts = datetime(2026, 5, 4, 1, 0, tzinfo=timezone.utc).timestamp()
        contract_ts = datetime(2026, 5, 4, 2, 0, tzinfo=timezone.utc).timestamp()
        old_state.touch()
        old_queue.touch()
        contract.touch()
        # Apply deterministic mtimes after the writes above.
        os.utime(old_state, (old_ts, old_ts))
        os.utime(old_queue, (newer_ts, newer_ts))
        os.utime(contract, (contract_ts, contract_ts))
        result = validate_platform(root, "windows-codex", contract)
        scenarios.append(("stale_state_fails", (not result.ok) and any("session state" in p for p in result.problems)))

        write_text(contract, "status: complete\nreview_outcome: complete\n")
        done_ts = datetime(2026, 5, 4, 3, 0, tzinfo=timezone.utc).timestamp()
        os.utime(contract, (done_ts, done_ts))
        os.utime(old_state, (done_ts + 1, done_ts + 1))
        write_text(
            root / "session-states" / "windows-codex.yaml",
            "platform: windows-codex\nproject: chimera\nstatus: complete\ncurrent_task: test\nreview_outcome: complete\nshared_publish_status: published-ready\nlast_updated: 2026-05-04T03:00:01Z\nproof: done\nnext_action: none\n",
        )
        os.utime(root / "session-states" / "windows-codex.yaml", (done_ts + 1, done_ts + 1))
        queue.unlink()
        write_text(
            root / "publish-queue" / "windows-codex.yaml",
            "platform: windows-codex\nproject: chimera\npublish_required: false\ncurrent_task: none\nreason_not_published: none\nlocal_only_changes: []\ntarget_repo: saloomad/chimera\nnext_action: none\n",
        )
        os.utime(root / "publish-queue" / "windows-codex.yaml", (done_ts + 1, done_ts + 1))
        result = validate_platform(root, "windows-codex", contract)
        scenarios.append(("complete_with_false_queue_passes", result.ok))

    payload = {"self_test": [{"name": name, "passed": passed} for name, passed in scenarios]}
    print(json.dumps(payload, indent=2))
    return 0 if all(passed for _, passed in scenarios) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Shared Chimera GitHub coordination guard.")
    sub = parser.add_subparsers(dest="command", required=True)

    startup = sub.add_parser("startup-summary")
    startup.add_argument("--coordination-root", required=True)

    validate = sub.add_parser("validate-platform")
    validate.add_argument("--coordination-root", required=True)
    validate.add_argument("--platform", required=True, choices=PLATFORMS)
    validate.add_argument("--contract")

    sub.add_parser("self-test")

    args = parser.parse_args()

    if args.command == "startup-summary":
        summary = coordination_summary(Path(args.coordination_root))
        print(json.dumps(summary, indent=2))
        return 0

    if args.command == "validate-platform":
        contract = Path(args.contract) if args.contract else None
        result = validate_platform(Path(args.coordination_root), args.platform, contract)
        payload = {"ok": result.ok, "problems": result.problems}
        print(json.dumps(payload, indent=2))
        return 0 if result.ok else 1

    if args.command == "self-test":
        return self_test()

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
