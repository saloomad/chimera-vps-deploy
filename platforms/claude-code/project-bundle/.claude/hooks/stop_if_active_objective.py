import json
import re
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"


def read_contract() -> str:
    if not CONTRACT_PATH.exists():
        return ""
    return CONTRACT_PATH.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    text = read_contract()
    if re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is None:
        log_receipt(
            "Stop",
            "passed",
            decision="allow",
            trigger="no_active_objective",
            notes="Stop hook allowed closeout because no active objective contract remained.",
        )
        return 0

    log_receipt(
        "Stop",
        "blocked",
        decision="deny",
        trigger="active_objective_guard",
        notes="Stop hook blocked premature closeout because the objective contract is still active.",
    )
    out = {
        "decision": "block",
        "reason": (
            "The objective contract is still marked active. Run the review step, update "
            "`.claude/OBJECTIVE_CONTRACT.md`, and set status to complete or blocked before stopping."
        ),
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
