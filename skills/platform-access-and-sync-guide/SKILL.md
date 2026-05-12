---
name: platform-access-and-sync-guide
description: Use when deciding which Chimera platform should own work, how to connect to Windows, Linux home, or the Kimi VPS, where draft work should happen, how to move work across the three machines, or how to sync GitHub safely from draft to test to live execution.
---

# Platform Access And Sync Guide

Use this skill when the user asks:

- which platform to use
- how to connect to a platform
- how to move work from draft to test to live
- how Windows, Linux home, and Kimi VPS should divide responsibility
- how to sync work through GitHub without mixing unfinished draft work into the live runtime

## Purpose And When To Use

This skill is the shared front door for:

- platform choice
- platform access
- cross-platform progression
- GitHub sync across Windows, Linux home, and VPS
- draft versus test versus live execution routing

Use `linux-access` for VPS-only Linux commands.
Use `github-manager` for detailed Git and GitHub command flow.

## Platform Role Map

### Windows Codex

- Main conversation and control surface
- Main shared workspace: `C:\Users\becke\claudecowork`
- Use for coordination, shared docs, review, integration, handoffs, and cross-platform checks

### Linux Home

- Draft and test Linux machine
- Verified SSH path on 2026-05-12: `ssh open-claw@100.116.214.127`
- Older `192.168.1.203` timed out on 2026-05-12, so do not prefer it while the Tailscale path works
- Verified Linux home directory: `/home/open-claw`
- Verified Git repo in use on 2026-05-12: `/home/open-claw/openclawtrading`
- `/home/open-claw/chimera` exists but was not a Git repo on 2026-05-12, so do not treat it as the active source repo unless the user explicitly says that changed

### Kimi VPS

- Finished tested execution target
- Live SSH path: `ssh root@100.67.172.114`
- Live repo: `/root/openclawtrading`
- Live runtime workspace: `/root/.openclaw/workspace`
- Use for live services, live reports, runtime validation, and tested deploys only

## Platform Roles

### Windows

Use Windows for:

- talking with Sal
- deciding next steps
- comparing Linux home, GitHub, and VPS state
- reviewing diffs
- updating shared instructions, skills, handoffs, and PM files

### Linux Home

Use Linux home for:

- first drafts
- experiments
- local Linux-side testing
- risky or incomplete work that should not touch live execution yet

### Kimi VPS

Use Kimi VPS for:

- finished tested execution
- runtime services
- cron and systemd verification
- production truth checks

Do not use the VPS as the first-draft workspace unless the user explicitly asks for an emergency live repair.

## Connection Rules

### Windows

- You are already on this platform when working inside Windows Codex

### Linux Home

```bash
ssh open-claw@100.116.214.127
```

Useful first check:

```bash
ssh open-claw@100.116.214.127 "echo OK && whoami && pwd && test -d /home/open-claw/openclawtrading/.git && echo OPENCLAWTRADING_GIT"
```

### Kimi VPS

```bash
ssh root@100.67.172.114
```

Useful first check:

```bash
ssh root@100.67.172.114 "echo OK && whoami && pwd && test -d /root/openclawtrading/.git && echo OPENCLAWTRADING_GIT"
```

## Work Progression Across The Three Platforms

Use this default path unless the user explicitly wants a different route:

1. Start on Windows.
   - Clarify the objective.
   - Identify the right repo and platform.
   - Check for existing handoffs, dirty worktrees, or publish debt.
2. Build and test new work on Linux home first.
   - Keep rough work out of the live VPS.
   - Test Linux-side behavior there before calling it ready.
3. Bring the tested slice back through Windows.
   - Review the diff.
   - Update shared docs or handoffs if needed.
   - Decide whether it is ready for staging.
4. Use GitHub as the shared checkpoint.
   - `main` is the shared integration branch.
   - `staging` is the Linux-home test gate.
   - `production` is the live branch the VPS should consume.
5. Promote only finished tested work to the VPS.
   - Pull approved `production` onto the VPS.
   - Validate the live runtime there.

Short version:

`Windows plan and review -> Linux home draft and test -> Windows integration -> GitHub main -> staging test gate -> production -> VPS live execution`

## Sync And Handoff Contract

Use this order:

1. Inspect the source platform first.
   - `git status`
   - `git branch --show-current`
   - `git remote -v`
2. Use Windows as the GitHub control plane.
   - Windows owns merges, handoffs, branch decisions, and publish decisions.
3. Keep Linux home split into two roles when possible.
   - One dirty draft workspace for active experiments.
   - One clean checkout or clean worktree for `staging` test-gate work.
4. Let Linux home prove the slice before live promotion.
   - Do not pull `staging` into a dirty working tree.
5. Let the VPS consume tested code only.
   - The VPS should pull `production` only.
   - Do not treat the VPS as the place to clean up draft-state mess.

## GitHub Sync Rules

GitHub is the safest shared bridge between the three machines.

Recommended branch model:

- `main` = shared integration branch
- `staging` = Linux-home test gate
- `production` = live-only branch for VPS pulls

If Linux home is dirty, do not pull blindly on other machines.
   - First understand what changed.
   - Preserve the unfinished work before any reset, merge, or pull.

Recommended order:

1. Windows pulls latest `main`.
2. Work lands on `main` in bounded reviewed slices.
3. Windows promotes ready work from `main` to `staging`.
4. Linux home tests from a clean `staging` checkout or worktree.
5. If Linux home passes, promote `staging` to `production`.
6. VPS pulls `production` only.

## Dirty Worktree Guard

If Linux home has many local changes:

- do not treat GitHub as current truth until those changes are reviewed or published
- do not assume the VPS should pull anything yet
- snapshot the current state first with `git status`, branch name, and recent commits
- prefer small bounded publishes instead of one giant sync
- prefer a separate clean Linux-home checkout or worktree for staging instead of testing from the same dirty draft workspace

## Guardrails And Old Defaults To Reject

- Do not treat `192.168.1.203` as the preferred Linux-home host while `100.116.214.127` is the verified reachable path.
- Do not treat `/home/open-claw/chimera` as the active Git repo without rechecking it.
- Do not treat the VPS as the first-draft workspace.
- Do not let the same Linux-home checkout act as both the messy draft workspace and the clean staging gate.
- Do not call work cross-platform synced unless GitHub and the intended target platform were both updated.

## Reality Check Before Trusting Older Docs

If older files disagree with reality, prefer the verified live facts from the current pass:

- Linux home answered on `100.116.214.127`
- Linux home repo in use was `/home/open-claw/openclawtrading`
- `/home/open-claw/chimera` was not a Git repo on 2026-05-12
- Windows had no mounted `Z:` drive on 2026-05-12
- Kimi VPS live truth remains `root@100.67.172.114` and `/root/openclawtrading`

## When To Escalate

Pause and surface the risk before proceeding if:

- Linux home has large uncommitted changes and the user asks to sync everything
- the repo branch strategy in docs does not match the repo branch reality
- the VPS has local modifications
- a platform path in docs points at a repo that no longer exists or is no longer a Git repo

## What To Read Next

- `linux-access` for live VPS SSH and Linux command work
- `github-manager` for detailed Git and GitHub command flow
- `codex-runtime-router` for model, routing, and response-header rules
- `chimera-vps-deploy/docs/DEPLOYMENT_TIERS.md` for the current tiered branch model
- platform bootstraps under `chimera-vps-deploy/platforms/` when a platform-specific startup contract matters

## Done Contract

Do not call a three-platform sync complete unless:

1. the source platform was inspected
2. the target platform and target repo were named explicitly
3. GitHub sync status was stated honestly
4. the VPS was only used for finished tested work, or the reply clearly says why that rule was bypassed
