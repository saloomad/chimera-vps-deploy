---
name: github-coordination-gate
description: Force each Chimera platform to fetch shared GitHub state at startup and before meaningful task changes, then update shared task state instead of relying on local memory. Use when starting work, resuming work, switching tasks, or checking publish status.
---

# GitHub Coordination Gate

Use this skill on every platform before meaningful work starts and again before moving to another meaningful task.

## Purpose

GitHub is the shared coordination truth, not private memory.

This skill exists so platforms always read:

- `handoffs/`
- `session-states/`
- `publish-queue/`

before they continue or switch work.

## Startup Rule

Before meaningful work:

1. fetch or pull the shared coordination repo
2. read the newest handoff
3. read every file in `session-states/`
4. read every file in `publish-queue/`
5. identify the first unfinished or unpublished slice that belongs to the current objective

## Task-Transition Rule

Before leaving one meaningful task for another, publish one of these states:

- `published-ready`
- `in-progress-not-ready`
- `blocked-needs-follow-up`

Minimum shared update:

1. update `session-states/<platform>.yaml`
2. update `publish-queue/<platform>.yaml` when code is not ready to publish

Do not wait for session end.

## Repo Ownership Rule

Use the correct repo for the correct truth:

- `saloomad/chimera`
  - project code and project-level work
- `saloomad/chimera-vps-deploy`
  - cross-platform coordination, shared skills, handoffs, and platform mirrors
- `saloomad/chimera-windows-live`
  - Windows live config, scripts, and platform-only agent state
- `saloomad/chimera-linux-live`
  - Linux live config, OpenClaw runtime surfaces, cron, and platform-only agent state

## Proof Commands

Windows:

```powershell
python C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py startup-summary --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy
python C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py validate-platform --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy --platform windows-codex
python C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py sync-and-publish --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy --platform windows-codex --repo-root C:\Users\becke\claudecowork
```

Linux:

```bash
python3 /root/chimera-deploy/scripts/github_coordination_guard.py startup-summary --coordination-root /root/chimera-deploy
python3 /root/chimera-deploy/scripts/github_coordination_guard.py validate-platform --coordination-root /root/chimera-deploy --platform kimi-vps
```

## Platform Notes

- Windows Codex and Claude Code should read this through their startup docs and hook surfaces.
- Windows Codex can also run the recurring runner:
  - `C:\Users\becke\claudecowork\scripts\run_windows_codex_github_coordination_sync.ps1`
- OpenCowork should read this through the enforcement bundle and stop/start hooks.
- Kimi VPS should read this before live runtime continuation.
- OpenCode and Space Agent should use this through startup docs and wrapper checks because their hook surfaces are weaker.

## Related Files

- `C:\Users\becke\claudecowork\chimera-vps-deploy\session-states\README.md`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\publish-queue\README.md`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\workflows\GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md`

---
*github-coordination-gate v1.0 | 2026-05-04 | Chimera shared skill*
