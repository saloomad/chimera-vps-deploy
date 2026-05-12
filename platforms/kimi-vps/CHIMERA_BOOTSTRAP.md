# Chimera Kimi VPS Bootstrap

Updated: 2026-05-12
Purpose: startup truth for the Kimi VPS as the live execution lane.

## Read Order

1. Read this file first.
2. Read `AGENTS.md` in the same folder.
3. Pull the latest `chimera-vps-deploy`.
4. Read the newest handoff.
5. Read `platform-access-and-sync-guide`.
6. Read `github-manager`.

## Platform Truth

- Windows is the control plane.
- Linux home is the draft-and-test lane.
- Kimi VPS is the finished tested execution lane.

## VPS Role

Your job is to:

- consume finished tested work only
- validate runtime behavior
- keep live services healthy
- avoid becoming the first-draft workspace

## Branch Truth

- consume `production` only
- never pull `main` or `staging` for normal live updates
- if the live runtime is an unpacked copy, treat the deploy repo and deployment workflow as the Git-facing source

## Native Paths

- deploy repo: `/root/chimera-deploy`
- live runtime path: `/root/openclawtrading`
- runtime extra skills: `/root/.openclaw/kimi-skills`

## Relationship To Linux Home

Linux home proves the slice before the VPS should consume it.

Do not assume Linux home is gone.
Do assume it is not the live runtime.

## Required Skills

- `platform-access-and-sync-guide`
- `github-manager`
- `codex-runtime-router`

## Practical Rule

If the user asks for a live fix, check whether it is:

- a bounded emergency runtime repair
- or work that should really go back to Linux home and Windows first
