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
]
REQUIRED_DOCS = [
    ROOT / "docs" / "GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md",
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
PLATFORM_KEYWORDS = {
    ROOT / "platforms" / "windows-codex" / "AGENTS.md": ["github-coordination-gate", "task-transition-publish"],
    ROOT / "platforms" / "windows-codex" / "CHIMERA_BOOTSTRAP.md": ["chimera-windows-live", "github-coordination-gate"],
    ROOT / "platforms" / "claude-code" / "AGENTS.md": ["github-coordination-gate", "task-transition-publish"],
    ROOT / "platforms" / "claude-code" / "CHIMERA_BOOTSTRAP.md": ["github-coordination-gate", "chimera-vps-deploy"],
    ROOT / "platforms" / "kimi-vps" / "AGENTS.md": ["github-coordination-gate", "chimera-linux-live"],
    ROOT / "platforms" / "kimi-vps" / "CHIMERA_BOOTSTRAP.md": ["github-coordination-gate", "task-transition-publish"],
    ROOT / "platforms" / "opencode" / "AGENTS.md": ["github-coordination-gate", "task-transition-publish"],
    ROOT / "platforms" / "opencode" / "CHIMERA_BOOTSTRAP.md": ["github-coordination-gate", "platform-live-repo-router"],
    ROOT / "platforms" / "space-agent" / "AGENTS.md": ["github-coordination-gate"],
    ROOT / "platforms" / "opencowork" / "local-bundle" / "chimera-enforcement-bundle" / "README.md": ["github-coordination-gate"],
}


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
        "platform_files": platform_file_checks(),
        "local_skill_mirrors": local_skill_mirror_checks(),
        "vps_skill_mirrors": vps_skill_checks(),
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
