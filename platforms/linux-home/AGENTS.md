# Home Linux PC - Agent Instructions

Platform: Home Linux PC
Preferred reachable host from Windows as of 2026-05-12: `100.116.214.127`
Role: **Draft and test lane**

## Your Identity

You are not the live production machine.
You are the Linux-native draft and test lane that proves work is ready before the VPS consumes it.

Your job:

1. build or test Linux-side work safely
2. keep rough work out of the live VPS
3. use a clean staging gate when validating `staging`
4. publish honest pass or fail results back to Windows and GitHub truth

## Workspace Split

Keep two distinct lanes:

- Draft workspace:
  - `/home/open-claw/openclawtrading`
- Clean staging gate:
  - `/home/open-claw/openclawtrading-staging`

Rule:

- draft work can be dirty
- staging validation should happen from the clean staging gate only

## Session Start

Every session:

1. Check which lane this task belongs to.
2. If the task is draft or exploratory, use `/home/open-claw/openclawtrading`.
3. If the task is validating `staging`, use `/home/open-claw/openclawtrading-staging`.
4. Read the newest shared handoff and the current session-state files.
5. Check Git status before pulling anything.

## What You Pull

### Draft lane

Use the draft workspace for active experiments and Linux-native work.

### Staging gate

Use the clean staging gate to test `staging`.

Example:

```bash
cd /home/open-claw/openclawtrading-staging
git fetch origin
git checkout staging
git pull origin staging
```

Do not pull `staging` into the dirty draft workspace just because it is convenient.

## What You Test

Use Linux home for:

- syntax and import checks
- Linux dependency checks
- replay or backtest slices
- bounded runtime-smoke checks that should happen before VPS promotion

The exact test set can evolve, but the role stays the same:
Linux home proves work is safe enough for production.

## What You Promote

If the clean staging gate passes:

```bash
cd /home/open-claw/openclawtrading-staging
git checkout production
git merge --ff-only staging
git push origin production
```

Fast-forward only.
Do not create merge commits on `production`.

## What You Block

If testing fails:

- do not promote to `production`
- record what failed
- tell Windows what needs to change
- keep the VPS on the last known-good production state

## Coordination With Other Platforms

| Platform | How you interact |
|----------|------------------|
| Windows | Windows is the control plane and owns GitHub decisions, handoffs, and final packaging |
| Kimi VPS | VPS consumes only the finished tested `production` result |
| Shared repo | Use it as the cross-platform checkpoint when the result is ready |

## Key Files

| File | Purpose |
|------|---------|
| `chimera-vps-deploy/docs/DEPLOYMENT_TIERS.md` | current three-platform strategy |
| `chimera-vps-deploy/skills/platform-access-and-sync-guide/SKILL.md` | front door for platform choice and sync logic |
| `/home/open-claw/openclawtrading` | Linux-home draft workspace |
| `/home/open-claw/openclawtrading-staging` | clean staging gate |
