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

    agent_name = payload.get("agent_name") or payload.get("subagent_name") or "subagent"
    log_receipt(
        "SubagentStop",
        "activated",
        trigger="subagent_review_gate",
        notes=f"Subagent review gate ran for {agent_name}.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "SubagentStop",
            "additionalContext": (
                f"{agent_name} finished. Do not accept the result blindly. Summarize what it proved, what it changed, "
                "what still needs verification, and update `.claude/OBJECTIVE_CONTRACT.md` before deciding complete, "
                "iterate, or blocked."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
