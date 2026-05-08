# CHECKPOINT - 2026-05-08 Git CPU Reduction And Scheduler Fix

## What changed

- Diagnosed the current `git.exe` pressure on Windows:
  - active background git scans were being spawned by `Codex.exe`
  - the scheduled GitHub coordination task was not the main source of the repeated `status` and `ls-files` scans
- Reduced GitHub automation pressure:
  - changed `ChimeraWindowsCodexGithubCoordination` from every `15` minutes to hourly
  - added a mutex lock to `run_windows_codex_github_coordination_sync.ps1` so overlapping runs skip cleanly
  - fixed the mutex name bug so the scheduled task no longer exits immediately with PowerShell constructor failure
- Reduced repo-scan cost for both the main repo and deploy repo:
  - enabled `feature.manyFiles=true`
  - enabled `core.untrackedCache=true`
  - enabled `core.fsmonitor=true`
  - set `index.version=4`
  - confirmed the fsmonitor daemons are running
- Trimmed obvious generated junk from repeated untracked scans:
  - added local exclude entries for `.playwright-mcp/`, `__pycache__/`, and `*.pyc`
  - removed local `.playwright-mcp/`
  - removed deploy `scripts/__pycache__/`

## Live proof

- Current git process tree now shows:
  - two low-cost `git fsmonitor--daemon` helpers
  - lightweight `Codex.exe` background `status` / `ls-files` scans
  - no heavy zombie-style long-CPU git processes
- Current repo timing snapshot after tuning:
  - main repo:
    - `git status --short` about `5.7s`
    - `git ls-files --others --exclude-standard` about `0.8s`
  - deploy repo:
    - `git status --short` about `0.4s`
    - `git ls-files --others --exclude-standard` about `0.27s`
- Scheduled task proof:
  - task re-registered hourly
  - after the lock fix, `Last Result = 0`
  - task state returned to `Ready`
- Cleanup proof:
  - `.playwright-mcp/` no longer appears in current untracked output

## Real diagnosis

- The deepest remaining bottleneck is not the scheduler anymore.
- The main repo still has roughly:
  - `410` dirty paths
  - `230` untracked paths
- That means Codex background git scans are still inherently expensive because the workspace itself is very dirty, especially under:
  - `research/platforms`
  - `scripts/tests`
  - `research/chimera-knowledge-wiki`

## Remaining open work

- If more CPU reduction is needed beyond this pass, the next real improvement is not another git setting.
- The next improvement is repo hygiene:
  - publish, archive, or intentionally ignore the large remaining untracked documentation backlog
  - reduce the huge dirty-document surface in `research/platforms` and related roots
- Until that backlog is reduced, Codex will still keep doing background git scans against a large working tree.
