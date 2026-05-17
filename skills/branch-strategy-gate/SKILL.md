---
name: branch-strategy-gate
description: Use proactively on every platform before creating a new branch or starting work. Enforces the Chimera "main for integration, production for live" rule. All platforms commit to main; only promoted code reaches production. Feature branches are short-lived and risk-gated. Use when starting work, deciding whether to branch, reviewing branch hygiene, cleaning up stale branches, or promoting to production.
---

# Branch Strategy Gate

## Core Rule

**`main` = integration. `production` = live VPS runtime.**

All platforms work on `main`. Feature branches are allowed only when the risk profile justifies isolation. When used, they must be short-lived (max 3 days), clearly named, and deleted after merge. Only `production` branch code runs on the live VPS.

## Immediate Drift Rule

If the current branch is not `main`, do not treat that as normal.

You must say explicitly:

- current branch
- whether that violates the current Chimera rule
- whether the current work should return to `main` now or needs a separate integration step

Do not keep doing invisible meaningful work on a long-lived non-`main` branch without calling out the drift.

## The Two-Branch Model

```
main          ← all platforms commit here (integration)
   ↓
production    ← VPS pulls from here only (live runtime)
   ↑
v1.2.3 tag    ← rollback target if production breaks
```

**`main` is NOT live.** It is the shared workspace where all platforms integrate. The VPS cron job tracks `production`, not `main`.

## Why This Exists

The old pattern — every session creates a new branch — caused:
- Hidden work: Codex built 54 commits on `add-remaining-files` while Claude was on a different branch
- Merge conflicts: 9 conflicts when reconciling
- Reconstruction cost: 12 days of context had to be manually reconstructed
- Branch sprawl: 40+ stale branches with no clear ownership

## The Decision Gate

Before creating any branch, answer these questions in order:

### 1. Can this be done safely on `main`?

Work on `main` when **ALL** of these are true:
- The change is additive (new files, new scripts) OR a small bug fix
- Smoke tests exist and pass
- The change does not break existing paths or contracts
- The platform can commit and push frequently (at least once per session)
- Rollback is easy (git revert, or the change is isolated to new files)

### 2. Is a feature branch justified?

Create a feature branch **ONLY** when **ANY** of these are true:
- The change rewrites existing core contracts (path changes, data format changes)
- The change could break live trading or the active pipeline
- Multiple platforms need to review before merge
- The experiment is exploratory and may be abandoned
- The change spans more than 3 days of work

### 3. If branching, is the risk level correct?

| Risk | Branch Type | Max Lifetime | Required Review |
|------|------------|--------------|-----------------|
| Low | No branch, `main` | N/A | Smoke tests |
| Medium | `feature/<name>` | 2 days | Smoke tests + self-review |
| High | `experiment/<name>` | 3 days | Smoke tests + cross-platform review |
| Critical | `hotfix/<name>` | 1 day | Smoke tests + immediate merge + post-review |

## Naming Rules

- **Feature branches:** `feature/what-it-does` (e.g., `feature/exact-heatmap-extraction`)
- **Experiment branches:** `experiment/what-you-are-testing`
- **Hotfix branches:** `hotfix/what-broke`
- **Platform branches:** NEVER. Do not use `claude/...`, `codex/...`, `kimi/...` as branch names.

## Lifecycle Rules

1. **Start from latest `main`:** `git checkout main && git pull origin main`
2. **Commit frequently:** At least once per logical chunk, push at session end
3. **Keep it short:** If a branch lives longer than 3 days, either merge it or abandon it
4. **Merge requirements:**
   - Smoke tests pass
   - No merge conflicts with `main`
   - `git merge-tree` shows clean merge before PR
5. **After merge:** Delete the branch immediately (`git branch -d feature/name`)
6. **No orphan branches:** If a branch is abandoned, delete it within 24 hours

## Publish Visibility Rule

For meaningful work, do not stop at "a commit exists."

Also answer:

- is the commit visible on `main`
- if not, why not
- what exact integration step is still needed
- whether `production` promotion is intentionally deferred pending tests/approval

## Full Workflow: From Code to Live VPS

This is the complete path from development to live runtime:

```
1. WORK on main
   ├── All platforms commit here
   ├── Feature branches merge back to main
   └── Smoke tests run before every commit

2. TEST on main
   ├── Verify smoke tests pass
   ├── Check no broken paths or contracts
   └── Confirm ready for live

3. PROMOTE to production
   ├── Tag: git tag -a v1.2.3 -m "Release v1.2.3"
   ├── Fast-forward: git checkout production && git merge --ff-only main
   └── Push: git push origin production && git push origin --tags

4. VPS AUTO-UPDATES from production
   ├── Cron runs every 30 minutes
   ├── git checkout production && git pull origin production
   └── Live scripts now run promoted code
```

**Who does what:**
- **Claude/Codex/Kimi:** Work on `main`, commit frequently, run smoke tests
- **Sal (or designated human):** Decides when `main` is ready, runs the promote commands
- **VPS cron:** Automatically pulls `production` every 30 minutes — no manual action needed

**Emergency rollback:**
```bash
git checkout production && git reset --hard v1.2.2
git push --force-with-lease origin production
```
VPS will pick up the rolled-back `production` on next cron run.

## Platform-Specific Rules

### Claude Code (Windows interactive)
- Start every session with `git checkout main && git pull`
- Work on `main` by default; use feature branches only when justified
- Before ending session: commit, push to `main`, delete any temporary branches
- Promote to `production` only when explicitly asked by Sal

### Codex (Windows automation)
- Default to `main` for all automation work
- If a change is risky, the automation should create a PR to `main`, not commit directly
- Codex runs smoke tests before every commit
- Codex NEVER promotes to `production` — that requires human approval

### OpenClaw / Kimi (Linux VPS)
- VPS cron pulls `production` branch only, never `main`
- Live trading scripts run from `production`
- If testing a new script, use a local `feature/<name>` branch and symlink the test version
- Never run live trading from `main` or an experiment branch

### OpenCowork
- Follow the same rules as Claude Code
- Use shared skill roots for enforcement

## Proof Commands

Check branch hygiene:
```bash
# List all branches with last commit date
git for-each-ref --sort=-committerdate refs/heads/ --format='%(committerdate:short) %(refname:short)'

# Branches older than 7 days (candidates for deletion)
git for-each-ref --sort=-committerdate refs/heads/ --format='%(committerdate:short) %(refname:short)' | awk '$1 < "2026-05-01" {print}'

# Check if current branch is behind main
git log --oneline HEAD..main
```

## Enforcement

Every platform must:
1. Load this skill at session start
2. Justify any branch creation aloud
3. Set a reminder to merge or delete the branch within max lifetime
4. Run `git for-each-ref` at session start to spot stale branches

## Related Skills

- `github-coordination-gate` — shared state before work starts
- `platform-live-repo-router` — which repo owns the work
- `task-change-readiness-gate` — publish before switching tasks

---
*branch-strategy-gate v1.0 | 2026-05-06 | Chimera shared skill*
