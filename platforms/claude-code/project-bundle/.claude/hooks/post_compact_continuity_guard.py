import json

from receipt_logger import log_receipt


def main() -> int:
    log_receipt(
        "PostCompact",
        "activated",
        trigger="continuity_restore",
        notes="Post-compact continuity guard reminded the session to restore objective and PM truth after compaction.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PostCompact",
            "additionalContext": (
                "After compaction, restate the objective contract, next step, stop condition, and PM truth source. "
                "Do not continue as if context is still implicit."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
