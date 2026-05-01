#!/usr/bin/env python3
"""Rule-based preflight dispatcher for the Deezoh coach-suite."""

from __future__ import annotations

import argparse
import json
from typing import Any


TRADING_CUES = [
    "should i trade",
    "should we trade",
    "should i long",
    "should we long",
    "should i short",
    "should we short",
    "entry now",
    "enter now",
    "go long",
    "go short",
    "trade idea",
    "price is pumping",
    "pumped hard",
    "pump hard",
    "how to think better as a trader",
]

LEARNING_CUES = [
    "learn this",
    "learn that",
    "remember this",
    "remember that",
    "record this",
    "record that",
    "from now on",
    "you missed",
    "deezoh missed",
    "why did deezoh miss",
    "improve deezoh",
    "workflow gap",
    "better way to think",
    "teach deezoh",
]

MONITOR_CUES = [
    "why does this keep happening",
    "read the logs",
    "find optimizations",
    "make agents better at working with me",
    "i am inexperienced here",
    "what should have been caught",
    "learning the wrong lesson",
    "wrong user input",
    "agent edited files",
    "did not explain proof",
    "did not explain owner",
    "did not explain next action",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select the Deezoh coach-suite skill stack for an input.")
    parser.add_argument("--message", required=True, help="User or system message to classify.")
    parser.add_argument("--platform", default="unknown", help="Platform label for output context.")
    return parser.parse_args()


def has_any(text: str, cues: list[str]) -> bool:
    return any(cue in text for cue in cues)


def select_stack(message: str, platform: str) -> dict[str, Any]:
    text = message.lower()
    skills: list[str] = []
    reasons: list[str] = []
    enforcement = "advisory"

    if has_any(text, TRADING_CUES):
        skills.append("deezoh-trading-coach")
        reasons.append("trading decision or trader-improvement cue")
        enforcement = "live_intervention"

    if has_any(text, LEARNING_CUES):
        skills.append("deezoh-learning-mode")
        reasons.append("correction, workflow, or learning cue")
        enforcement = "required" if enforcement == "advisory" else enforcement

    if "learn" in text and has_any(text, TRADING_CUES):
        if "deezoh-learning-mode" not in skills:
            skills.append("deezoh-learning-mode")
        reasons.append("trading lesson request needs safe learning gate")
        enforcement = "required" if enforcement == "advisory" else enforcement

    if has_any(text, MONITOR_CUES):
        skills.append("vibe-coding-monitor")
        reasons.append("monitoring, repeated friction, or wrong-lesson cue")
        enforcement = "required" if enforcement == "advisory" else enforcement

    if "always mean" in text or "obvious" in text or "definitely" in text or "means buy" in text:
        if "vibe-coding-monitor" not in skills:
            skills.append("vibe-coding-monitor")
        reasons.append("strong certainty language needs wrong-lesson guard")
        enforcement = "required" if enforcement == "advisory" else enforcement

    if not skills:
        skills = ["deezoh-trading-coach"]
        reasons = ["default conservative fallback for ambiguous Deezoh coaching requests"]

    return {
        "platform": platform,
        "message": message,
        "selected_skills": skills,
        "reasons": reasons,
        "enforcement_level": enforcement,
    }


def main() -> int:
    args = parse_args()
    result = select_stack(args.message, args.platform)
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
