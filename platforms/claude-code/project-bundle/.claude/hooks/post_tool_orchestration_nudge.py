import json
import re
import sys
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"


def contract_active() -> bool:
    if not CONTRACT_PATH.exists():
        return False
    text = CONTRACT_PATH.read_text(encoding="utf-8", errors="replace")
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    if not contract_active():
        return 0

    tool_name = str(payload.get("tool_name", ""))
    log_receipt(
        "PostToolUse",
        "activated",
        trigger=tool_name.lower(),
        notes="Post-tool proof reminder ran while an objective contract was active.",
    )

    out = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                "An active objective contract exists. After this tool step, update `.claude/OBJECTIVE_CONTRACT.md` "
                "with current_slice, last_proof, current_phase, next_step, and review_outcome. "
                "Make test or proof explicit if the tool changed the system."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
