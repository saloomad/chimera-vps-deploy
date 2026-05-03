import json

from receipt_logger import log_receipt


def main() -> int:
    log_receipt(
        "InstructionsLoaded",
        "activated",
        trigger="starter_stack",
        notes="Confirmed instruction-layer load and reminded the session to use the starter stack and control-layer workflow when needed.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "InstructionsLoaded",
            "additionalContext": (
                "The instruction layer is loaded. For meaningful work, use the starter stack: "
                "prompt-upgrade-engineer, sal-communication-contract, vibe-coding-operator, and "
                "objective-orchestration-loop. If the work edits instructions, config, hooks, skills, "
                "workflows, detectors, or compaction behavior, also use critical-change-guard and "
                "critical-config-instruction-and-compaction-guard-loop.md."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
