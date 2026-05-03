import json
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"


def read_contract() -> str:
    if not CONTRACT_PATH.exists():
        return "No objective contract file found yet. For meaningful multi-step work, create or update `.claude/OBJECTIVE_CONTRACT.md`, including unapproved_items and remaining_work."
    text = CONTRACT_PATH.read_text(encoding="utf-8", errors="replace").strip()
    if not text:
        return "Objective contract file exists but is empty."
    return "Current objective contract:\n\n" + text[:3000]


def main() -> int:
    log_receipt(
        "SessionStart",
        "activated",
        trigger="session_context_load",
        notes="Loaded objective contract context at session start.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": read_contract()
            + "\n\nCarry forward a short visible block in meaningful replies that shows objective status, unapproved items, and remaining work with brief plain-English descriptions.",
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
