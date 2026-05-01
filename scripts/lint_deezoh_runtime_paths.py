#!/usr/bin/env python3
"""Fail when Deezoh coach-suite files still reference stale OpenClaw hosts or paths."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


STALE_PATTERNS = [
    re.compile(r"/home/open-claw/"),
    re.compile(r"open-claw@"),
    re.compile(r"192\.168\.31\.194"),
    re.compile(r"192\.168\.1\.203"),
]


DEFAULT_TARGETS = [
    "C:/Users/becke/claudecowork/agents/deezoh/AGENTS.md",
    "C:/Users/becke/claudecowork/chimera-vps-deploy/skills/deezoh-trading-coach/SKILL.md",
    "C:/Users/becke/claudecowork/chimera-vps-deploy/skills/deezoh-learning-mode/SKILL.md",
    "C:/Users/becke/claudecowork/chimera-vps-deploy/skills/vibe-coding-monitor/SKILL.md",
    "C:/Users/becke/claudecowork/chimera-vps-deploy/skills/DEEZOH_COACH_SUITE_RUNTIME.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint Deezoh coach-suite files for stale runtime references.")
    parser.add_argument("paths", nargs="*", help="Optional file paths to lint.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    targets = [Path(p) for p in (args.paths or DEFAULT_TARGETS)]
    failures: list[str] = []
    for target in targets:
        if not target.exists():
            failures.append(f"missing file: {target}")
            continue
        text = target.read_text(encoding="utf-8", errors="replace")
        for index, line in enumerate(text.splitlines(), start=1):
            for pattern in STALE_PATTERNS:
                if pattern.search(line):
                    failures.append(f"{target}:{index}: stale reference -> {line.strip()}")
    if failures:
        print("lint failed")
        for failure in failures:
            print(failure)
        return 1
    print("lint passed")
    for target in targets:
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
