import json
import os
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"


def log_receipt() -> None:
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
            "InstructionsLoaded",
            "--status",
            "activated",
            "--trigger",
            "starter_stack",
            "--notes",
            "OpenCowork instruction-load hook ran.",
            "--project-dir",
            str(PROJECT_DIR),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def main() -> int:
    try:
        json.load(sys.stdin)
    except Exception:
        pass
    log_receipt()
    out = {
        "hookSpecificOutput": {
            "hookEventName": "InstructionsLoaded",
            "additionalContext": (
                "The instruction layer is loaded. For meaningful work, use the starter stack and, for control-layer "
                "changes, use critical-change-guard, the critical control-layer workflow, and codex-continuity-enforcer."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
