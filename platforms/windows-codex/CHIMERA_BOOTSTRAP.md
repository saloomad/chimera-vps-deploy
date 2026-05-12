# Chimera Codex Bootstrap

Updated: 2026-05-12
Purpose: startup truth for Windows Codex as the control plane across Windows, Linux home, GitHub, and Kimi VPS.

## Read Order

1. Read this file first.
2. Read `chimera-vps-deploy/docs/DEPLOYMENT_TIERS.md`.
3. Read `platform-access-and-sync-guide`.
4. Read `github-manager`.
5. Read the newest handoff in `chimera-vps-deploy/handoffs/`.

## Platform Truth

- Windows is the control plane.
- Linux home is the draft-and-test lane.
- Kimi VPS is the finished tested execution lane.

## Connection Truth

- Linux home: `ssh open-claw@100.116.214.127`
- Kimi VPS: `ssh root@100.67.172.114`

## Repo And Path Truth

- Windows workspace: `C:\Users\becke\claudecowork`
- Shared deploy repo: `C:\Users\becke\claudecowork\chimera-vps-deploy`
- Linux-home draft repo: `/home/open-claw/openclawtrading`
- Linux-home clean staging gate: `/home/open-claw/openclawtrading-staging`
- VPS live repo or runtime path: `/root/openclawtrading`

## Branch Truth

- `main` = shared integration
- `staging` = Linux-home test gate
- `production` = live-only branch for VPS consumption

## Windows Responsibility

Use Windows for:

- shared coordination
- branch and publish decisions
- GitHub merges
- handoffs
- shared docs and skills
- diff review before promotion

## Required Skills

- `platform-access-and-sync-guide`
- `github-manager`
- `codex-runtime-router`
- `agent-session-resume`

## Practical Rule

If the user says `sync`, `which platform`, `linux home`, `vps`, or `how do we move this forward`, read `platform-access-and-sync-guide` first.
