import json
import re
import sys
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"
MUTATING_TOOLS = {"Edit", "Write", "MultiEdit", "Bash"}
DANGEROUS_PATTERNS = [
    r"\brm\s+-rf\b",
    r"\bdel\s+/[a-z]*s",
    r"\brmdir\s+/[a-z]*s",
    r"\bremove-item\b.*-recurse",
    r"\bgit\s+reset\b",
    r"\bgit\s+checkout\s+--\b",
]


def read_contract() -> str:
    if not CONTRACT_PATH.exists():
        return ""
    return CONTRACT_PATH.read_text(encoding="utf-8", errors="replace")


def contract_active(text: str) -> bool:
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def build_context(tool_name: str, has_active_contract: bool) -> str:
    if tool_name == "Bash":
        if has_active_contract:
            return (
                "A meaningful objective is active. Before and after this shell step, keep the workflow, write scope, "
                "and proof chain explicit. If this step changes the system, update `.claude/OBJECTIVE_CONTRACT.md` "
                "with current_phase, last_proof, next_step, and review_outcome."
            )
        return (
            "This shell step can change the system. Before continuing, make sure you have chosen the workflow, stated "
            "the objective and done contract, and decided whether `.claude/OBJECTIVE_CONTRACT.md` should be active."
        )

    if has_active_contract:
        return (
            "A meaningful objective is active. Before this file change, keep the current slice tied to the real end "
            "objective and remember to update proof, dependent surfaces, and review state after the change."
        )

    return (
        "This file change may be meaningful work. Before continuing, make sure you have chosen the workflow, stated "
        "the objective and done contract, and activated `.claude/OBJECTIVE_CONTRACT.md` if this is more than a tiny fix."
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    tool_name = payload.get("tool_name", "")
    if tool_name not in MUTATING_TOOLS:
        return 0

    contract_text = read_contract()
    is_active = contract_active(contract_text)

    if tool_name == "Bash":
        command = str(payload.get("tool_input", {}).get("command", ""))
        lowered = command.lower()
        for pattern in DANGEROUS_PATTERNS:
            if re.search(pattern, lowered):
                log_receipt(
                    "PreToolUse",
                    "blocked",
                    decision="deny",
                    trigger="destructive_command_guard",
                    notes=f"Blocked risky bash command: {command[:160]}",
                )
                out = {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": (
                            "Blocked a destructive shell command. Use a safer, reversible path and keep the objective "
                            "contract and proof chain explicit."
                        ),
                    }
                }
                print(json.dumps(out))
                return 0

    log_receipt(
        "PreToolUse",
        "activated",
        trigger=tool_name.lower(),
        notes=f"Pre-tool guard ran for {tool_name}.",
    )

    out = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": build_context(tool_name, is_active),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
