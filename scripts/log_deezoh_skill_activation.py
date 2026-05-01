#!/usr/bin/env python3
"""Append a machine-readable Deezoh coach-suite activation receipt."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write a JSONL activation receipt for the Deezoh coach suite."
    )
    parser.add_argument("--trigger", required=True, help="What user or system cue triggered the skill.")
    parser.add_argument("--skill-selected", required=True, help="Skill or stack selected.")
    parser.add_argument("--platform", required=True, help="Platform where activation happened.")
    parser.add_argument(
        "--enforcement-level",
        required=True,
        choices=["advisory", "required", "live_intervention"],
        help="How strongly the skill was enforced.",
    )
    parser.add_argument(
        "--proof-result",
        required=True,
        choices=["pass", "fail", "partial"],
        help="Outcome of the activation or smoke check.",
    )
    parser.add_argument("--notes", default="", help="Short plain-English note.")
    parser.add_argument(
        "--output",
        default="C:/Users/becke/claudecowork/trace/deezoh_skill_activation_receipts.jsonl",
        help="JSONL file to append to.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    record = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "trigger": args.trigger,
        "skill_selected": args.skill_selected,
        "platform": args.platform,
        "enforcement_level": args.enforcement_level,
        "proof_result": args.proof_result,
        "notes": args.notes,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")
    print(json.dumps(record, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
