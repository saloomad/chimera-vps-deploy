#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_REPOS = [
    "saloomad/chimera",
    "saloomad/chimera-vps-deploy",
    "saloomad/chimera-windows-live",
    "saloomad/chimera-linux-live",
]
REQUIRED_SKILLS = [
    "github-coordination-gate",
    "task-transition-publish",
    "platform-live-repo-router",
    "task-change-readiness-gate",
    "coordination-artifact-lifecycle-guard",
]
REQUIRED_DOCS = [
    ROOT / "docs" / "GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md",
    ROOT / "docs" / "GITHUB_COORDINATION_ARCHITECTURE_2026-05-04.md",
    ROOT / "docs" / "GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md",
    ROOT / "docs" / "GITHUB_COORDINATION_TEST_AND_MONITOR_RUNBOOK_2026-05-04.md",
    ROOT / "workflows" / "GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md",
]
LOCAL_SKILL_MIRROR_ROOTS = [
    Path(r"C:\Users\becke\.codex\skills"),
    Path(r"C:\Users\becke\.claude\skills"),
    Path(r"C:\Users\becke\.openclaw\skills"),
]
VPS_SKILL_ROOTS = [
    "/root/.kimi/skills",
    "/root/.openclaw/kimi-skills",
    "/root/openclawtrading/skills",
]
VPS_COORDINATION_ROOT = "/root/chimera-deploy"
PLATFORM_KEYWORDS = {
    ROOT / "platforms" / "windows-codex" / "AGENTS.md": ["github-coordination-gate", "task-transition-publish"],
    ROOT / "platforms" / "windows-codex" / "CHIMERA_BOOTSTRAP.md": ["chimera-windows-live", "github-coordination-gate"],
    ROOT / "platforms" / "claude-code" / "AGENTS.md": ["github-coordination-gate", "task-transition-publish", "task-change-readiness-gate"],
    ROOT / "platforms" / "claude-code" / "CHIMERA_BOOTSTRAP.md": ["github-coordination-gate", "chimera-vps-deploy"],
    ROOT / "platforms" / "kimi-vps" / "AGENTS.md": ["github-coordination-gate", "chimera-linux-live", "task-change-readiness-gate"],
    ROOT / "platforms" / "kimi-vps" / "CHIMERA_BOOTSTRAP.md": ["github-coordination-gate", "task-transition-publish"],
    ROOT / "platforms" / "opencode" / "AGENTS.md": ["github-coordination-gate", "task-transition-publish", "task-change-readiness-gate"],
    ROOT / "platforms" / "opencode" / "CHIMERA_BOOTSTRAP.md": ["github-coordination-gate", "platform-live-repo-router"],
    ROOT / "platforms" / "space-agent" / "AGENTS.md": ["github-coordination-gate", "task-change-readiness-gate"],
    ROOT / "platforms" / "opencowork" / "local-bundle" / "chimera-enforcement-bundle" / "README.md": ["github-coordination-gate", "task-change-readiness-gate"],
    ROOT / "platforms" / "opencode" / "project-bundle" / "README.md": ["validate_task_transition.ps1", "objective-start"],
}
VPS_RUNTIME_KEYWORDS = {
    "/root/.openclaw/workspace/AGENTS.md": ["github-coordination-gate", "task-change-readiness-gate", "/root/chimera-deploy"],
    "/root/openclawtrading/AGENTS.md": ["github-coordination-gate", "task-change-readiness-gate", "/root/chimera-deploy"],
    "/root/.openclaw/workspace/hooks/message-router/handler.js": ["github_coordination_guard.py", "task-change gate", "kimi-vps"],
    "/root/.openclaw/workspace/hooks/mandatory-bootstrap/handler.js": ["GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md", "GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md"],
}
VPS_COORDINATION_PATHS = [
    f"{VPS_COORDINATION_ROOT}/scripts/github_coordination_guard.py",
    f"{VPS_COORDINATION_ROOT}/workflows/GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md",
    f"{VPS_COORDINATION_ROOT}/docs/GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md",
    f"{VPS_COORDINATION_ROOT}/docs/GITHUB_COORDINATION_ARCHITECTURE_2026-05-04.md",
    f"{VPS_COORDINATION_ROOT}/docs/GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md",
    f"{VPS_COORDINATION_ROOT}/docs/GITHUB_COORDINATION_TEST_AND_MONITOR_RUNBOOK_2026-05-04.md",
    f"{VPS_COORDINATION_ROOT}/session-states/kimi-vps.yaml",
    f"{VPS_COORDINATION_ROOT}/publish-queue/kimi-vps.yaml",
]

REGISTRY_REQUIRED_ARTIFACTS = [
    "handoffs/CHECKPOINT_*.md",
    "session-states/*.yaml",
    "publish-queue/*.yaml",
    "skills/github-coordination-gate/SKILL.md",
    "skills/task-transition-publish/SKILL.md",
    "skills/task-change-readiness-gate/SKILL.md",
    "skills/platform-live-repo-router/SKILL.md",
    "skills/coordination-artifact-lifecycle-guard/SKILL.md",
    "workflows/GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md",
    "docs/GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md",
    "docs/GITHUB_COORDINATION_ARCHITECTURE_2026-05-04.md",
    "docs/GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md",
    "scripts/github_coordination_guard.py",
    "scripts/verify_github_coordination_system.py",
]


def run(cmd: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def repo_checks() -> list[dict[str, object]]:
    results = []
    for repo in REQUIRED_REPOS:
        rc, out, err = run(["gh", "repo", "view", repo, "--json", "nameWithOwner,isPrivate"])
        results.append(
            {
                "repo": repo,
                "ok": rc == 0,
                "details": out if out else err,
            }
        )
    return results


def skill_checks() -> list[dict[str, object]]:
    results = []
    for skill in REQUIRED_SKILLS:
        path = ROOT / "skills" / skill / "SKILL.md"
        results.append({"skill": skill, "ok": path.exists(), "path": str(path)})
    return results


def doc_checks() -> list[dict[str, object]]:
    return [{"path": str(path), "ok": path.exists()} for path in REQUIRED_DOCS]


def wrapper_checks() -> list[dict[str, object]]:
    targets = [
        ROOT / "platforms" / "claude-code" / "project-bundle" / ".claude" / "hooks" / "user_prompt_orchestration_gate.py",
        ROOT / "platforms" / "opencode" / "project-bundle" / "scripts" / "validate_task_transition.ps1",
        ROOT / "platforms" / "opencode" / "project-bundle" / ".opencode" / "commands" / "objective-start.md",
        ROOT / "platforms" / "space-agent" / "AGENTS.md",
    ]
    results = []
    for path in targets:
        results.append({"path": str(path), "ok": path.exists()})
    return results


def registry_checks() -> list[dict[str, object]]:
    registry_path = ROOT / "docs" / "GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md"
    if not registry_path.exists():
        return [{"path": str(registry_path), "ok": False, "missing_artifacts": REGISTRY_REQUIRED_ARTIFACTS}]

    text = registry_path.read_text(encoding="utf-8", errors="replace")
    missing = [artifact for artifact in REGISTRY_REQUIRED_ARTIFACTS if artifact not in text]
    needs_core_words = all(word in text for word in ["Purpose", "Automatic Reader Or Owner", "Trigger", "Proof Surface"])
    results = [{"path": str(registry_path), "ok": not missing and needs_core_words, "missing_artifacts": missing}]
    if not needs_core_words:
        results[0]["missing_artifacts"] = missing + ["registry headings incomplete"]
    return results


def platform_file_checks() -> list[dict[str, object]]:
    results = []
    for path, keywords in PLATFORM_KEYWORDS.items():
        if not path.exists():
            results.append({"path": str(path), "ok": False, "missing_keywords": keywords})
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        missing = [kw for kw in keywords if kw.lower() not in text]
        results.append({"path": str(path), "ok": not missing, "missing_keywords": missing})
    return results


def local_skill_mirror_checks() -> list[dict[str, object]]:
    results = []
    for root in LOCAL_SKILL_MIRROR_ROOTS:
        for skill in REQUIRED_SKILLS:
            path = root / skill / "SKILL.md"
            results.append({"path": str(path), "ok": path.exists()})
    return results


def vps_skill_checks() -> list[dict[str, object]]:
    results = []
    for root in VPS_SKILL_ROOTS:
        for skill in REQUIRED_SKILLS:
            remote_path = f"{root}/{skill}/SKILL.md"
            rc, out, err = run(["ssh", "root@100.67.172.114", f"test -f {remote_path} && echo ok || echo missing"])
            results.append({"path": remote_path, "ok": rc == 0 and out.strip() == "ok", "details": out if out else err})
    return results


def vps_coordination_path_checks() -> list[dict[str, object]]:
    results = []
    for remote_path in VPS_COORDINATION_PATHS:
        rc, out, err = run(["ssh", "root@100.67.172.114", f"test -f {remote_path} && echo ok || echo missing"])
        results.append({"path": remote_path, "ok": rc == 0 and out.strip() == "ok", "details": out if out else err})
    return results


def vps_runtime_file_checks() -> list[dict[str, object]]:
    results = []
    for remote_path, keywords in VPS_RUNTIME_KEYWORDS.items():
        remote_script = (
            "python3 - <<'PY'\n"
            "from pathlib import Path\n"
            f"path = Path({remote_path!r})\n"
            "if not path.exists():\n"
            "    print('__MISSING__')\n"
            "else:\n"
            "    print(path.read_text(encoding='utf-8', errors='replace'))\n"
            "PY"
        )
        rc, out, err = run(["ssh", "root@100.67.172.114", remote_script])
        if rc != 0 or out.strip() == "__MISSING__":
            results.append({"path": remote_path, "ok": False, "missing_keywords": keywords})
            continue
        lower = out.lower()
        missing = [kw for kw in keywords if kw.lower() not in lower]
        results.append({"path": remote_path, "ok": not missing, "missing_keywords": missing})
    return results


def vps_guard_check() -> list[dict[str, object]]:
    rc, out, err = run(
        [
            "ssh",
            "root@100.67.172.114",
            (
                "python3 /root/chimera-deploy/scripts/github_coordination_guard.py "
                "validate-platform --coordination-root /root/chimera-deploy --platform kimi-vps"
            ),
        ]
    )
    return [{"path": f"{VPS_COORDINATION_ROOT}/scripts/github_coordination_guard.py", "ok": rc == 0, "details": out if out else err}]


def state_checks() -> list[dict[str, object]]:
    guard = ROOT / "scripts" / "github_coordination_guard.py"
    platforms = ["windows-codex", "windows-claude", "opencowork-local", "kimi-vps", "opencode"]
    results = []
    for platform in platforms:
        rc, out, err = run(
            [
                sys.executable,
                str(guard),
                "validate-platform",
                "--coordination-root",
                str(ROOT),
                "--platform",
                platform,
            ]
        )
        results.append({"platform": platform, "ok": rc == 0, "details": out if out else err})
    return results


def main() -> int:
    payload = {
        "repos": repo_checks(),
        "skills": skill_checks(),
        "docs": doc_checks(),
        "registry": registry_checks(),
        "wrappers": wrapper_checks(),
        "platform_files": platform_file_checks(),
        "local_skill_mirrors": local_skill_mirror_checks(),
        "vps_skill_mirrors": vps_skill_checks(),
        "vps_coordination_paths": vps_coordination_path_checks(),
        "vps_runtime_files": vps_runtime_file_checks(),
        "vps_guard": vps_guard_check(),
        "platform_states": state_checks(),
    }
    print(json.dumps(payload, indent=2))
    ok = True
    for section in payload.values():
        for item in section:
            if not item.get("ok", False):
                ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
