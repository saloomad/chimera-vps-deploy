---
name: platform-live-repo-router
description: Route Chimera changes to the correct repo so shared coordination, project code, Windows live state, and Linux live state do not get mixed together. Use when deciding where a file belongs, where to push a change, or which repo another platform should pull.
---

# Platform Live Repo Router

Use this skill whenever a platform needs to decide where work belongs.

## Repo Map

### `saloomad/chimera`

Use for:

- project code
- project-specific docs
- project tests
- project workflows that belong with the codebase

### `saloomad/chimera-vps-deploy`

Use for:

- handoffs
- shared skills
- platform mirrors
- cross-platform coordination docs
- `session-states/`
- `publish-queue/`

### `saloomad/chimera-windows-live`

Use for:

- Windows-only live config
- Windows scripts
- Windows-only startup surfaces
- Windows-only local agent state that other platforms may need to inspect but not run

### `saloomad/chimera-linux-live`

Use for:

- Linux-only live config
- OpenClaw runtime files
- cron and systemd surfaces
- Linux-only startup surfaces

## Decision Rule

Ask two questions:

1. Is this shared coordination truth or runnable platform truth?
2. If runnable, is it Windows-only, Linux-only, or project code?

If it is only needed so other agents know what happened, it usually belongs in `chimera-vps-deploy`.

## Publish Rule

When in doubt:

- coordination metadata goes to `chimera-vps-deploy`
- runnable Windows state goes to `chimera-windows-live`
- runnable Linux state goes to `chimera-linux-live`
- project code stays in `chimera`

---
*platform-live-repo-router v1.0 | 2026-05-04 | Chimera shared skill*
