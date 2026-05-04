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
CONTROL_LAYER_MARKERS = [
    "agents.md",
    "claude.md",
    ".claude\\settings.json",
    ".claude/hooks/",
    ".claude/hooks\\",
    "opencode.json",
    ".opencode/",
    ".opencode\\",
    "plugin-registry.json",
    "\\skills\\",
    "/skills/",
    "\\workflows\\",
    "/workflows/",
    "task_registry.md",
    "project_registry.md",
    "continuation.md",
    "kanban.md",
]
PIPELINE_MARKERS = [
    "orchestration\\taskflow.json",
    "/root/.openclaw/",
    "\\hooks\\",
    "/hooks/",
    "openclawtrading",
    "hermes_runtime_bridge.py",
    "deezoh",
    "lobster",
    "standing order",
]


def read_contract() -> str:
    if not CONTRACT_PATH.exists():
        return ""
    return CONTRACT_PATH.read_text(encoding="utf-8", errors="replace")


def contract_active(text: str) -> bool:
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def payload_text(payload: dict) -> str:
    try:
        text = json.dumps(payload.get("tool_input", {}), ensure_ascii=False)
    except Exception:
        text = str(payload.get("tool_input", ""))
    return text.lower()


def has_any_marker(text: str, markers: list[str]) -> bool:
    return any(marker in text for marker in markers)


def classify_trigger(tool_name: str, payload: dict, has_active_contract: bool) -> str:
    text = payload_text(payload)
    if has_any_marker(text, CONTROL_LAYER_MARKERS):
        return "control_layer_change"
    if has_any_marker(text, PIPELINE_MARKERS):
        return "pipeline_surface_change"
    if not has_active_contract:
        return "mutating_tool_without_active_contract"
    return tool_name.lower()


def build_context(tool_name: str, has_active_contract: bool, trigger: str) -> str:
    if trigger == "control_layer_change":
        return (
            "This edit touches the control layer. Use `critical-change-guard` and "
            "`critical-config-instruction-and-compaction-guard-loop.md`, then update proof, continuity, and any "
            "dependent instruction or registry surfaces. If this change touches skills, workflows, or detectors, also "
            "check whether `codex-workflow-detector`, `codex-skill-opportunity-detector`, or "
            "`hook-opportunity-detector` should be consulted before you continue."
        )

    if trigger == "pipeline_surface_change":
        return (
            "This change touches runtime or pipeline ownership surfaces. Check whether "
            "`pipeline-enforcement-detector` and `openclaw-feature-router` should be consulted so hooks, Task Flow, "
            "Lobster, standing orders, commands, or review gates own the workflow in the right place."
        )

    if tool_name == "Bash":
        if has_active_contract:
            return (
                "A meaningful objective is active. Before and after this shell step, keep the workflow, write scope, "
                "and proof chain explicit. If this step changes the system, update `.claude/OBJECTIVE_CONTRACT.md` "
                "with current_phase, last_proof, next_step, and review_outcome. If the step reveals a repeated gap, "
                "load the workflow, skill, or hook detectors instead of leaving it as a manual reminder."
            )
        return (
            "This shell step can change the system. Before continuing, make sure you have chosen the workflow, stated "
            "the objective and done contract, and decided whether `.claude/OBJECTIVE_CONTRACT.md` should be active. "
            "For meaningful work, load `prompt-upgrade-engineer`, `vibe-coding-operator`, and "
            "`objective-orchestration-loop` first."
        )

    if has_active_contract:
        return (
            "A meaningful objective is active. Before this file change, keep the current slice tied to the real end "
            "objective and remember to update proof, dependent surfaces, and review state after the change. If this "
            "edit exposes a repeated pattern, load the detector skills before you close the slice."
        )

    return (
        "This file change may be meaningful work. Before continuing, make sure you have chosen the workflow, stated "
        "the objective and done contract, and activated `.claude/OBJECTIVE_CONTRACT.md` if this is more than a tiny "
        "fix. For meaningful work, use the starter stack: `prompt-upgrade-engineer`, "
        "`sal-communication-contract`, `vibe-coding-operator`, and `objective-orchestration-loop`."
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

    trigger = classify_trigger(tool_name, payload, is_active)
    log_receipt("PreToolUse", "activated", trigger=trigger, notes=f"Pre-tool guard ran for {tool_name}.")

    out = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": build_context(tool_name, is_active, trigger),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
