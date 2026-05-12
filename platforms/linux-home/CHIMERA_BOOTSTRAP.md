# Home Linux PC Bootstrap

Platform: Home Linux PC
Preferred reachable host from Windows as of 2026-05-12: `100.116.214.127`
Role: Draft and test lane
Updated: 2026-05-12

## Read First

1. `chimera-vps-deploy/docs/DEPLOYMENT_TIERS.md`
2. `chimera-vps-deploy/platforms/linux-home/AGENTS.md`
3. newest `chimera-vps-deploy/handoffs/CHECKPOINT_*.md`
4. `chimera-vps-deploy/skills/platform-access-and-sync-guide/SKILL.md`

## Current Repo Truth

- active draft repo in use: `/home/open-claw/openclawtrading`
- clean staging gate target: `/home/open-claw/openclawtrading-staging`
- older `/home/open-claw/chimera` path is not the active Git repo from this pass

## Quick Start

### Draft lane

```bash
cd /home/open-claw/openclawtrading
git status
git branch --show-current
```

### Clean staging gate

```bash
cd /home/open-claw/openclawtrading-staging
git status
git checkout staging
git pull origin staging
```

## What This Machine Is For

Use Linux home for:

- first drafts
- Linux-native tests
- backtests or replay checks
- validating `staging` before `production`

Do not treat this machine as the live runtime.

## Safe Promotion Shape

1. Windows reviews and packages the slice.
2. Ready work reaches `main`.
3. Windows promotes `main` to `staging`.
4. Linux home tests `staging` from the clean staging gate.
5. If it passes, Linux home fast-forwards `production`.
6. Kimi VPS consumes `production`.

## Clean Staging Gate Rule

Do not validate `staging` from the same dirty draft workspace that holds active experiments.

Use one of:

- a clean second checkout
- a clean Git worktree

Preferred path in this workflow:

- `/home/open-claw/openclawtrading-staging`

## Troubleshooting

### "Draft repo is dirty"

That is expected during active work.
Do not use that as the staging validation lane.

### "Staging gate is missing"

Create a clean gate from the main repo:

```bash
cd /home/open-claw/openclawtrading
git fetch origin
git worktree add /home/open-claw/openclawtrading-staging -B staging origin/staging
```

### "Production should move but Linux home is unavailable"

Windows may do a bounded manual override, but the reply must say plainly why Linux-home validation was bypassed.
