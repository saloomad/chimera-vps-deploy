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
            "PreCompact",
            "--status",
            "activated",
            "--trigger",
            "continuity_capture",
            "--notes",
            "OpenCowork pre-compact continuity hook ran.",
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
            "hookEventName": "PreCompact",
            "additionalContext": (
                "Before compaction, capture the objective contract, proof path, PM state, and next step so the session "
                "can resume from files instead of memory."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
