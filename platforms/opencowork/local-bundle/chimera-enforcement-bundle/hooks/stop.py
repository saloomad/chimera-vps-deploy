import json
import os
import re
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"
CONTRACT = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"


def log_receipt(status: str, *, decision: str = "", trigger: str = "", notes: str = "") -> None:
    if not LOGGER.exists():
        return
    subprocess.run(
        [
            sys.executable,
            str(LOGGER),
            "--platform",
            "opencowork-local",
            "--surface",
            "hook",
            "--name",
            "Stop",
            "--status",
            status,
            "--decision",
            decision,
            "--trigger",
            trigger,
            "--notes",
            notes,
            "--project-dir",
            str(PROJECT_DIR),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def active_contract() -> bool:
    if not CONTRACT.exists():
        return False
    text = CONTRACT.read_text(encoding="utf-8", errors="replace")
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def main() -> int:
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    if not active_contract():
        log_receipt("passed", decision="allow", trigger="no_active_objective", notes="Stop allowed.")
        return 0

    log_receipt("blocked", decision="deny", trigger="active_objective_guard", notes="Stop blocked while objective is active.")
    print(
        json.dumps(
            {
                "decision": "block",
                "reason": "The objective contract is still active. Review and update it before stopping.",
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
