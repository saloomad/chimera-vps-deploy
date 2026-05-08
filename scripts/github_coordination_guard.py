#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import tempfile
import subprocess
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

SAFE_DOC_REPO_TYPES = ["main", "deploy"]
SAFE_DOC_PREFIXES = {
    "main": [
        "DOCUMENT_REGISTRY.md",
        "INDEX.md",
        "PROJECT_REGISTRY.md",
        "TASK_REGISTRY.md",
        "ACTION_LOG.md",
        "DELIVERY_JOURNAL.md",
        "WORKSPACE_FILE_OPERATING_RULES.md",
        "AGENT_NAVIGATION_MAP.md",
        "tracking/",
        "research/platforms/",
        "workflows/codex/",
    ],
    "deploy": [
        "handoffs/",
        "docs/",
    ],
}
SAFE_DOC_SUFFIXES = {".md", ".json", ".yaml", ".yml"}


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


def parse_list_yaml(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    current_list_key: str | None = None
    if not path.exists():
        return data
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(raw_line[4:].rstrip())
            continue
        current_list_key = None
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = []
            current_list_key = key
            continue
        if value.lower() == "true":
            data[key] = True
        elif value.lower() == "false":
            data[key] = False
        else:
            data[key] = value
    return data


def dump_simple_yaml(path: Path, payload: dict[str, object]) -> None:
    lines: list[str] = []
    for key, value in payload.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
            if not value:
                lines[-1] = f"{key}: []"
            continue
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
            continue
        lines.append(f"{key}: {value}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    result = subprocess.run(cmd, capture_output=True, text=True, check=False, cwd=str(cwd) if cwd else None)
    return result.returncode, (result.stdout or "").strip(), (result.stderr or "").strip()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sanitize_scalar_text(value: str) -> str:
    cleaned = "".join(ch if ch.isprintable() else "?" for ch in value)
    return " ".join(cleaned.split())


def normalize_remote_slug(url: str) -> str:
    cleaned = url.strip()
    if "github.com/" in cleaned and "@" in cleaned and cleaned.startswith(("https://", "http://")):
        cleaned = cleaned.split("@", 1)[1]
        cleaned = f"https://{cleaned}"
    if cleaned.endswith(".git"):
        cleaned = cleaned[:-4]
    if cleaned.startswith("https://github.com/"):
        return cleaned.removeprefix("https://github.com/")
    if cleaned.startswith("git@github.com:"):
        return cleaned.removeprefix("git@github.com:")
    return cleaned


def current_branch(repo_root: Path) -> str:
    rc, out, _ = run(["git", "-C", str(repo_root), "rev-parse", "--abbrev-ref", "HEAD"])
    return out if rc == 0 and out else "unknown"


def current_remote_slug(repo_root: Path) -> str:
    rc, out, _ = run(["git", "-C", str(repo_root), "remote", "get-url", "origin"])
    return normalize_remote_slug(out) if rc == 0 and out else "unknown"


def ahead_behind(repo_root: Path, branch: str) -> tuple[int, int]:
    rc, out, _ = run(["git", "-C", str(repo_root), "rev-list", "--left-right", "--count", f"origin/{branch}...HEAD"])
    if rc != 0 or not out:
        return 0, 0
    left, right = out.split()
    return int(left), int(right)


def changed_paths(repo_root: Path, limit: int = 25) -> list[str]:
    rc, out, _ = run(["git", "-C", str(repo_root), "status", "--porcelain"])
    if rc != 0 or not out:
        return []
    rows: list[str] = []
    for line in out.splitlines():
        raw = line[3:].strip() if len(line) >= 4 else line.strip()
        if "->" in raw:
            raw = raw.split("->", 1)[1].strip()
        if raw:
            cleaned = sanitize_scalar_text(raw.replace("\\", "/"))
            if cleaned.count("/357/") >= 1 and cleaned.count("/200/") >= 1:
                continue
            rows.append(cleaned)
    unique = []
    seen = set()
    for row in rows:
        if row not in seen:
            seen.add(row)
            unique.append(row)
        if len(unique) >= limit:
            break
    return unique


def is_safe_doc_path(path: str, repo_type: str) -> bool:
    normalized = path.replace("\\", "/").strip().lstrip("./")
    if not normalized:
        return False
    if repo_type not in SAFE_DOC_PREFIXES:
        return False
    prefixes = SAFE_DOC_PREFIXES[repo_type]
    suffix = Path(normalized).suffix.lower()
    return any(normalized == prefix or normalized.startswith(prefix) for prefix in prefixes) and suffix in SAFE_DOC_SUFFIXES


def build_publish_state(repo_root: Path) -> dict[str, object]:
    branch = current_branch(repo_root)
    target_repo = current_remote_slug(repo_root)
    behind, ahead = ahead_behind(repo_root, branch) if branch != "unknown" else (0, 0)
    changes = changed_paths(repo_root)
    publish_required = bool(changes or ahead > 0)
    if changes and ahead > 0:
        reason = f"Repo has {len(changes)} uncommitted path(s) and branch {branch} is ahead by {ahead}."
        next_action = "Review intended files, commit the bounded slice, then push with explicit refspec and verify branch parity."
        shared_status = "in-progress-not-ready"
    elif changes:
        reason = f"Repo has {len(changes)} uncommitted path(s) on branch {branch}."
        next_action = "Review intended files, commit the bounded slice, then push with explicit refspec and verify branch parity."
        shared_status = "in-progress-not-ready"
    elif ahead > 0:
        reason = f"Branch {branch} is ahead by {ahead} and still needs publish verification."
        next_action = "Push with explicit refspec and verify origin parity."
        shared_status = "in-progress-not-ready"
    elif behind > 0:
        reason = f"Branch {branch} is behind origin by {behind}; pull or reconcile before claiming ready."
        next_action = "Fetch and reconcile the branch before the next bounded slice."
        shared_status = "blocked-needs-follow-up"
        publish_required = True
    else:
        reason = "none"
        next_action = "Continue the next bounded slice from the current objective."
        shared_status = "published-ready"
    proof = f"repo={target_repo} branch={branch} ahead={ahead} behind={behind} local_changes={len(changes)}"
    return {
        "branch": branch,
        "target_repo": target_repo,
        "ahead": ahead,
        "behind": behind,
        "local_only_changes": changes,
        "publish_required": publish_required,
        "reason_not_published": reason,
        "shared_publish_status": shared_status,
        "proof": proof,
        "next_action": next_action,
    }


def sync_platform_state(
    coordination_root: Path,
    platform: str,
    repo_root: Path,
    current_task: str | None,
    status: str,
    review_outcome: str,
    next_action_override: str | None,
    proof_override: str | None,
) -> dict[str, object]:
    state_path = coordination_root / "session-states" / f"{platform}.yaml"
    queue_path = coordination_root / "publish-queue" / f"{platform}.yaml"
    existing_state = parse_list_yaml(state_path)
    existing_queue = parse_list_yaml(queue_path)
    publish_state = build_publish_state(repo_root)
    task_value = (
        current_task
        or str(existing_state.get("current_task") or existing_queue.get("current_task") or repo_root.name)
    )
    next_action = next_action_override or str(publish_state["next_action"])
    proof = proof_override or str(publish_state["proof"])
    state_payload = {
        "platform": platform,
        "project": "chimera",
        "status": status,
        "current_task": task_value,
        "review_outcome": review_outcome,
        "shared_publish_status": str(publish_state["shared_publish_status"]),
        "last_updated": utc_now(),
        "proof": proof,
        "next_action": next_action,
    }
    queue_payload = {
        "platform": platform,
        "project": "chimera",
        "publish_required": bool(publish_state["publish_required"]),
        "current_task": task_value,
        "reason_not_published": str(publish_state["reason_not_published"]),
        "local_only_changes": publish_state["local_only_changes"],
        "target_repo": str(publish_state["target_repo"]),
        "next_action": next_action,
    }
    dump_simple_yaml(state_path, state_payload)
    dump_simple_yaml(queue_path, queue_payload)
    return {
        "state_path": str(state_path),
        "queue_path": str(queue_path),
        "state": state_payload,
        "queue": queue_payload,
    }


def autopublish_coordination(coordination_root: Path, platform: str, commit_message: str | None) -> dict[str, object]:
    state_rel = Path("session-states") / f"{platform}.yaml"
    queue_rel = Path("publish-queue") / f"{platform}.yaml"
    run(["git", "-C", str(coordination_root), "add", "--", str(state_rel), str(queue_rel)])
    rc, out, _ = run(["git", "-C", str(coordination_root), "diff", "--cached", "--name-only"])
    if rc != 0:
        raise RuntimeError("Unable to inspect staged coordination changes.")
    staged = [line.strip() for line in out.splitlines() if line.strip()]
    branch = current_branch(coordination_root)
    if not staged:
        behind, ahead = ahead_behind(coordination_root, branch) if branch != "unknown" else (0, 0)
        return {
            "changed": False,
            "branch": branch,
            "ahead": ahead,
            "behind": behind,
            "pushed": False,
            "message": "No coordination-file changes needed publishing.",
        }
    message = commit_message or f"[Codex] Refresh {platform} coordination state"
    rc, commit_out, commit_err = run(
        [
            "git",
            "-C",
            str(coordination_root),
            "commit",
            "--only",
            "-m",
            message,
            "--",
            str(state_rel),
            str(queue_rel),
        ]
    )
    if rc != 0:
        raise RuntimeError(commit_err or commit_out or "Coordination commit failed.")
    rc, push_out, push_err = run(["git", "-C", str(coordination_root), "push", "--verbose", "origin", f"HEAD:{branch}"])
    if rc != 0:
        raise RuntimeError(push_err or push_out or "Coordination push failed.")
    behind, ahead = ahead_behind(coordination_root, branch) if branch != "unknown" else (0, 0)
    return {
        "changed": True,
        "branch": branch,
        "ahead": ahead,
        "behind": behind,
        "pushed": True,
        "commit": commit_out.splitlines()[-1] if commit_out else message,
        "push": push_out or push_err,
    }


def autopublish_safe_docs(repo_root: Path, repo_type: str, commit_message: str | None) -> dict[str, object]:
    if repo_type not in SAFE_DOC_REPO_TYPES:
        raise RuntimeError(f"Unsupported repo type for safe-doc autopublish: {repo_type}")
    branch = current_branch(repo_root)
    all_changes = changed_paths(repo_root, limit=500)
    allowed = [path for path in all_changes if is_safe_doc_path(path, repo_type)]
    blocked = [path for path in all_changes if path not in allowed]
    if not allowed:
        behind, ahead = ahead_behind(repo_root, branch) if branch != "unknown" else (0, 0)
        return {
            "changed": False,
            "repo_type": repo_type,
            "branch": branch,
            "ahead": ahead,
            "behind": behind,
            "pushed": False,
            "message": "No safe documentation changes needed publishing.",
            "allowed": [],
            "blocked": blocked[:25],
        }
    if blocked:
        behind, ahead = ahead_behind(repo_root, branch) if branch != "unknown" else (0, 0)
        return {
            "changed": False,
            "repo_type": repo_type,
            "branch": branch,
            "ahead": ahead,
            "behind": behind,
            "pushed": False,
            "message": "Skipped safe-doc autopublish because non-allowed changes are present in the same repo.",
            "allowed": allowed,
            "blocked": blocked[:25],
        }

    run(["git", "-C", str(repo_root), "add", "--", *allowed])
    rc, out, _ = run(["git", "-C", str(repo_root), "diff", "--cached", "--name-only"])
    if rc != 0:
        raise RuntimeError("Unable to inspect staged safe documentation changes.")
    staged = [line.strip() for line in out.splitlines() if line.strip()]
    if not staged:
        behind, ahead = ahead_behind(repo_root, branch) if branch != "unknown" else (0, 0)
        return {
            "changed": False,
            "repo_type": repo_type,
            "branch": branch,
            "ahead": ahead,
            "behind": behind,
            "pushed": False,
            "message": "No safe documentation changes were stageable.",
            "allowed": allowed,
            "blocked": [],
        }

    message = commit_message or f"[Codex] Auto-publish {repo_type} safe docs"
    rc, commit_out, commit_err = run(
        [
            "git",
            "-C",
            str(repo_root),
            "commit",
            "--only",
            "-m",
            message,
            "--",
            *allowed,
        ]
    )
    if rc != 0:
        raise RuntimeError(commit_err or commit_out or "Safe documentation commit failed.")
    rc, push_out, push_err = run(["git", "-C", str(repo_root), "push", "--verbose", "origin", f"HEAD:{branch}"])
    if rc != 0:
        raise RuntimeError(push_err or push_out or "Safe documentation push failed.")
    behind, ahead = ahead_behind(repo_root, branch) if branch != "unknown" else (0, 0)
    return {
        "changed": True,
        "repo_type": repo_type,
        "branch": branch,
        "ahead": ahead,
        "behind": behind,
        "pushed": True,
        "allowed": allowed,
        "blocked": [],
        "commit": commit_out.splitlines()[-1] if commit_out else message,
        "push": push_out or push_err,
    }


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

    sync_cmd = sub.add_parser("sync-platform-state")
    sync_cmd.add_argument("--coordination-root", required=True)
    sync_cmd.add_argument("--platform", required=True, choices=PLATFORMS)
    sync_cmd.add_argument("--repo-root", required=True)
    sync_cmd.add_argument("--current-task")
    sync_cmd.add_argument("--status", default="active")
    sync_cmd.add_argument("--review-outcome", default="iterate")
    sync_cmd.add_argument("--next-action")
    sync_cmd.add_argument("--proof")

    sync_publish_cmd = sub.add_parser("sync-and-publish")
    sync_publish_cmd.add_argument("--coordination-root", required=True)
    sync_publish_cmd.add_argument("--platform", required=True, choices=PLATFORMS)
    sync_publish_cmd.add_argument("--repo-root", required=True)
    sync_publish_cmd.add_argument("--current-task")
    sync_publish_cmd.add_argument("--status", default="active")
    sync_publish_cmd.add_argument("--review-outcome", default="iterate")
    sync_publish_cmd.add_argument("--next-action")
    sync_publish_cmd.add_argument("--proof")
    sync_publish_cmd.add_argument("--commit-message")

    safe_docs_cmd = sub.add_parser("autopublish-safe-docs")
    safe_docs_cmd.add_argument("--repo-root", required=True)
    safe_docs_cmd.add_argument("--repo-type", required=True, choices=SAFE_DOC_REPO_TYPES)
    safe_docs_cmd.add_argument("--commit-message")

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

    if args.command == "sync-platform-state":
        payload = sync_platform_state(
            Path(args.coordination_root),
            args.platform,
            Path(args.repo_root),
            args.current_task,
            args.status,
            args.review_outcome,
            args.next_action,
            args.proof,
        )
        print(json.dumps(payload, indent=2))
        return 0

    if args.command == "sync-and-publish":
        synced = sync_platform_state(
            Path(args.coordination_root),
            args.platform,
            Path(args.repo_root),
            args.current_task,
            args.status,
            args.review_outcome,
            args.next_action,
            args.proof,
        )
        publish = autopublish_coordination(Path(args.coordination_root), args.platform, args.commit_message)
        payload = {"synced": synced, "publish": publish}
        print(json.dumps(payload, indent=2))
        return 0 if publish.get("ahead") == 0 else 1

    if args.command == "autopublish-safe-docs":
        payload = autopublish_safe_docs(Path(args.repo_root), args.repo_type, args.commit_message)
        print(json.dumps(payload, indent=2))
        return 0 if payload.get("ahead") == 0 else 1

    if args.command == "self-test":
        return self_test()

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
