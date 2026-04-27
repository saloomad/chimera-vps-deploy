---
name: github-manager
description: Manage GitHub repos, commits, pushes, and cross-platform sync. Use when any agent needs to push changes to GitHub, sync configs between Windows and VPS, update deploy repos, or manage version control. Triggers: push to github, sync repo, commit changes, git push, github update, deploy repo sync, cross-platform sync, pull changes, merge conflicts.
---

# GitHub Manager Skill — Cross-Platform Sync

## Purpose
Central skill for ALL agents on ALL platforms to push code, configs, and docs to GitHub, and to pull updates from other platforms.

## Philosophy
**GitHub is the single source of truth.** Windows and VPS each push their changes. Conflicts are resolved by the architect agent.

---

## Repositories

| Repo | Windows Path | VPS Path | Remote | Purpose |
|------|-------------|----------|--------|---------|
| `chimera` | `C:\Users\becke\claudecowork\` | `/root/openclawtrading/` | `saloomad/chimera` | Main trading system |
| `chimera-vps-deploy` | `C:\Users\becke\claudecowork\chimera-vps-deploy\` | `/root/chimera-deploy/` | `saloomad/chimera-vps-deploy` | VPS configs, systemd, cron, scripts |

---

## Platform Identity

Every commit MUST identify which platform created it:

```bash
# Windows commits
export GIT_COMMITTER_NAME="Windows Architect"
export GIT_COMMITTER_EMAIL="windows@chimera.local"
git commit -m "[Windows] description"

# VPS commits  
export GIT_COMMITTER_NAME="Kimi VPS"
export GIT_COMMITTER_EMAIL="vps@chimera.local"
git commit -m "[VPS] description"
```

---

## Authentication

### VPS (already configured)
```bash
# Token stored in /root/.chimera.env
cat /root/.chimera.env | grep GITHUB_TOKEN
```

### Windows (if needed)
```powershell
# GitHub CLI or token in git credential manager
gh auth status
```

---

## Workflows

### 1. Push Changes (Any Platform)

```bash
cd /root/chimera-deploy/  # or /root/openclawtrading/
git status
git add -A
# Review diff before commit
git diff --cached --stat
export GIT_COMMITTER_NAME="Kimi VPS"
git commit -m "[VPS] what changed and why"
git push origin main
```

**Before pushing:**
1. Check `git status` — only commit files you intended to change
2. NEVER commit `.env`, tokens, or API keys
3. If `git push` fails with "rejected", see Workflow 3 (Pull + Merge)

---

### 2. Pull Updates (Any Platform)

```bash
cd /root/chimera-deploy/
git fetch origin
git log --oneline HEAD..origin/main  # see what's coming
git pull origin main
```

**After pulling:**
1. Check if any files affect your platform
2. If systemd service files changed → `systemctl daemon-reload`
3. If scripts changed → test them
4. If configs changed → validate JSON

---

### 3. Resolve Merge Conflicts

```bash
cd /root/chimera-deploy/
git pull origin main
# CONFLICT message appears

# See conflicts
git status
# Edit conflicted files, keep correct version
# Mark resolved:
git add <file>
git commit -m "[VPS] merge conflict resolved"
git push origin main
```

**Conflict resolution rules:**
1. If conflict is in config → VPS config wins on VPS, Windows config wins on Windows
2. If conflict is in script → compare timestamps, newer wins
3. If unsure → ask architect agent, do NOT guess

---

### 4. Cross-Platform Sync (Full)

When Windows pushes changes that VPS needs:

```bash
# On VPS
cd /root/chimera-deploy/
git fetch origin
git log --oneline HEAD..origin/main --grep="Windows"
# Review each Windows commit
git pull origin main
# Test everything that changed
systemctl restart openclaw-gateway  # if gateway config changed
bash /root/chimera-deploy/scripts/gateway-watchdog.sh  # test scripts
```

When VPS pushes changes that Windows needs:

```powershell
# On Windows
cd C:\Users\becke\claudecowork\chimera-vps-deploy\git fetch origin
git log --oneline HEAD..origin/main --grep="VPS"
git pull origin main
# Review changes, test if applicable
```

---

## What to Commit

### Always Commit
- New skills and skill updates
- Agent TOOLS.md / IDENTITY.md changes
- Systemd service files
- Cron job definitions
- Scripts that are production-ready
- Documentation updates

### Never Commit
- API keys, tokens, secrets
- `.env` files
- Log files
- Temporary files
- Node_modules, __pycache__

---

## Sync Checklist (Run Weekly)

```bash
# On VPS
cd /root/chimera-deploy/
git status
if [ -n "$(git status --porcelain)" ]; then
    echo "Uncommitted changes on VPS — commit them"
    git add -A
    git commit -m "[VPS] weekly sync"
    git push origin main
fi

# Check if Windows has new changes
git fetch origin
git log --oneline HEAD..origin/main
# If output exists → pull and review
```

---

## Emergency: Force Sync (Only if repo is broken)

```bash
# Backup current work
cp -r /root/chimera-deploy /root/chimera-deploy.backup-$(date +%Y%m%d)
# Reset to remote
cd /root/chimera-deploy/
git fetch origin
git reset --hard origin/main
# Re-apply any local changes manually
```

---

## Quick Reference

| Action | Command |
|--------|---------|
| Check status | `git status` |
| See recent commits | `git log --oneline -10` |
| See what Windows changed | `git log --oneline --grep="Windows"` |
| See what VPS changed | `git log --oneline --grep="VPS"` |
| Push VPS changes | `git commit -m "[VPS] ..." && git push` |
| Pull latest | `git pull origin main` |
| Discard local changes | `git checkout -- <file>` |
| View diff | `git diff` |

---

*github-manager skill v2.0 | Cross-platform sync for Chimera*
