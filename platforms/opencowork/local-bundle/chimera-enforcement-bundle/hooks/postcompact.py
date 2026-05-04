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
            "PostCompact",
            "--status",
            "activated",
            "--trigger",
            "continuity_restore",
            "--notes",
            "OpenCowork post-compact continuity hook ran.",
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
            "hookEventName": "PostCompact",
            "additionalContext": (
                "After compaction, restate the objective, next step, stop condition, and PM truth source before continuing."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
