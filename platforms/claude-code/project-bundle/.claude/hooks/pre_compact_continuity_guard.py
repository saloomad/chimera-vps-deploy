import json

from receipt_logger import log_receipt


def main() -> int:
    log_receipt(
        "PreCompact",
        "activated",
        trigger="continuity_capture",
        notes="Pre-compact continuity guard reminded the session to capture objective, proof, PM, and next-step state.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PreCompact",
            "additionalContext": (
                "Before compaction, capture the current objective contract, current slice, proof path, PM state, "
                "and next step. If project truth changed, update the continuity and PM surfaces before losing context."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
