#!/usr/bin/env python3
"""Run a lightweight local proof pass for the Deezoh coach suite and log receipts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path("C:/Users/becke/claudecowork/chimera-vps-deploy")
LOGGER = ROOT / "scripts" / "log_deezoh_skill_activation.py"
DISPATCHER = ROOT / "scripts" / "select_deezoh_coach_skill.py"
TESTS = [
    (
        "trade_pushback",
        ["deezoh-trading-coach"],
        "BTC pumped hard. Should we long now?",
        "live_intervention",
        "pass",
    ),
    (
        "safe_learning_gate",
        ["deezoh-learning-mode", "vibe-coding-monitor"],
        "Learn this: BTC pumps always mean continuation.",
        "required",
        "pass",
    ),
    (
        "trade_and_learning_gate",
        ["deezoh-trading-coach", "deezoh-learning-mode", "vibe-coding-monitor"],
        "BTC just pumped hard and I want to long now. Learn that momentum means buy fast.",
        "live_intervention",
        "pass",
    ),
    (
        "interaction_monitoring",
        ["vibe-coding-monitor"],
        "The agent edited files but did not explain proof, owner, or next action.",
        "required",
        "pass",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write smoke receipts for the Deezoh coach suite.")
    parser.add_argument("--platform", default="codex-local", help="Platform label for receipts.")
    parser.add_argument(
        "--receipt-file",
        default="C:/Users/becke/claudecowork/trace/deezoh_skill_activation_receipts.jsonl",
        help="Receipt JSONL file.",
    )
    return parser.parse_args()


def log_receipt(trigger: str, skill: str, platform: str, enforcement: str, proof: str, note: str, receipt_file: str) -> None:
    subprocess.run(
        [
            sys.executable,
            str(LOGGER),
            "--trigger",
            trigger,
            "--skill-selected",
            skill,
            "--platform",
            platform,
            "--enforcement-level",
            enforcement,
            "--proof-result",
            proof,
            "--notes",
            note,
            "--output",
            receipt_file,
        ],
        check=True,
    )


def dispatch(prompt: str, platform: str) -> dict[str, object]:
    result = subprocess.run(
        [
            sys.executable,
            str(DISPATCHER),
            "--message",
            prompt,
            "--platform",
            platform,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def main() -> int:
    args = parse_args()
    for trigger, expected_skills, prompt, enforcement, proof in TESTS:
        dispatch_result = dispatch(prompt, args.platform)
        selected_skills = dispatch_result["selected_skills"]
        missing = [skill for skill in expected_skills if skill not in selected_skills]
        if missing:
            raise SystemExit(
                f"dispatcher missing expected skills for {trigger}: {missing}; selected={selected_skills}"
            )
        if dispatch_result["enforcement_level"] != enforcement:
            raise SystemExit(
                f"dispatcher enforcement mismatch for {trigger}: "
                f"expected={enforcement} actual={dispatch_result['enforcement_level']}"
            )
        note = f"Smoke scenario: {prompt} | dispatcher={','.join(dispatch_result['selected_skills'])}"
        for skill in expected_skills:
            log_receipt(
                trigger,
                skill,
                args.platform,
                dispatch_result["enforcement_level"],
                proof,
                note,
                args.receipt_file,
            )
            print(f"logged {skill} for {trigger} via dispatcher")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
