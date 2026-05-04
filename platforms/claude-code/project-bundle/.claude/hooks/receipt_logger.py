import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[2]
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"


def log_receipt(name: str, status: str, *, decision: str = "", trigger: str = "", notes: str = "") -> None:
    if not LOGGER.exists():
        return
    command = [
        sys.executable,
        str(LOGGER),
        "--platform",
        "claude-code-local",
        "--surface",
        "hook",
        "--name",
        name,
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
    ]
    try:
        subprocess.run(command, check=False, capture_output=True, text=True)
    except Exception:
        pass
