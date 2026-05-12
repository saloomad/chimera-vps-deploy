---
name: github-manager
description: Manage GitHub repos, commits, pushes, pulls, and cross-platform sync for Windows, Linux home, and Kimi VPS. Use when deciding how work should move through main, staging, and production without letting dirty local work leak into live execution.
---

# GitHub Manager

## Purpose

Use this skill for:

- GitHub pushes and pulls
- branch decisions
- cross-platform sync
- publish decisions
- merge and drift checks

## Core Philosophy

GitHub is the shared checkpoint.

Windows is the control plane.
Linux home is the draft and test lane.
Kimi VPS consumes finished tested work only.

## Repositories

| Repo | Windows Path | Linux Home Path | VPS Path | Purpose |
|------|--------------|-----------------|----------|---------|
| `chimera` | `C:\Users\becke\claudecowork` | `/home/open-claw/openclawtrading` | `/root/openclawtrading` or deployed runtime copy | main system |
| `chimera-vps-deploy` | `C:\Users\becke\claudecowork\chimera-vps-deploy` | n/a | `/root/chimera-deploy` | shared deploy scripts, handoffs, shared skills |

## Branch Contract

Use this model unless the user explicitly approves another route:

- `main` = shared integration branch
- `staging` = Linux-home test gate
- `production` = live branch or deployment source for the VPS

## Safe Three-Platform Flow

1. Windows pulls the latest shared truth.
2. Draft work happens on Linux home or in a bounded Windows slice.
3. Windows reviews and decides what is ready.
4. Ready work lands on `main`.
5. Windows promotes the approved slice from `main` to `staging`.
6. Linux home tests `staging` from a clean checkout or worktree.
7. If it passes, Linux home fast-forwards `production`.
8. Kimi VPS pulls or consumes `production` only.

## Dirty Worktree Rule

If Linux home has active local changes:

- do not pull `staging` into that same dirty tree
- do not treat the dirty draft tree as the clean promotion gate
- keep a separate clean staging checkout or worktree

Preferred shape:

- dirty draft repo: `/home/open-claw/openclawtrading`
- clean staging gate: `/home/open-claw/openclawtrading-staging`

## Authentication Rule

- Never leave GitHub tokens embedded in remote URLs.
- Prefer GitHub CLI, credential helpers, or other secret-safe auth surfaces.
- If a remote contains a token, rotate the secret and rewrite the remote URL.

Example safe remote:

```bash
git remote set-url origin https://github.com/saloomad/chimera.git
```

## Windows Control Plane Rule

Windows should own:

- merge decisions
- branch promotions
- handoffs
- publish decisions
- shared skill and instruction updates

Linux home should own:

- Linux-native draft work
- clean `staging` validation

Kimi VPS should own:

- runtime verification
- live services
- consumption of tested `production`

## Push Checklist

Before pushing:

1. run `git status`
2. confirm the current branch
3. confirm the intended target branch
4. confirm no secrets are being committed
5. confirm whether the result is:
   - local only
   - shared in repo but not pushed
   - committed and pushed

## Pull Checklist

Before pulling:

1. check whether the working tree is dirty
2. check which branch the machine should consume
3. if Linux home is validating `staging`, use the clean staging gate
4. if VPS is pulling code, confirm it is consuming `production` only

## Verification Rule

Do not claim cross-platform sync is complete unless:

1. the source change exists where it was authored
2. the shared GitHub or shared repo truth was updated when needed
3. the target platform received the intended version

If one of those is missing, say so plainly.
