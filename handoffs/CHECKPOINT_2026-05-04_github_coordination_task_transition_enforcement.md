# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Codex / Windows Codex
- **Ended at**: 2026-05-04T00:00:00Z
- **Platform**: Windows Codex
- **Session focus**: Enforce shared GitHub coordination at task transitions instead of waiting for session end

## Original Goal
Stop agents from keeping meaningful work only in local memory or local files while moving to a new task, and make every platform read shared GitHub coordination state before meaningful work starts.

## Completed Work
- [x] Updated the GitHub workflow contract so task transitions, not only session end, require a shared publish decision.
- [x] Added a new task-transition workflow:
  - `workflows/codex/task-transition-shared-publish-loop.md`
- [x] Created the canonical shared coordination surfaces in `chimera-vps-deploy`:
  - `session-states/`
  - `publish-queue/`
- [x] Added per-platform starter state files for:
  - Windows Codex
  - Windows Claude
  - OpenCowork local
  - Kimi VPS
  - OpenCode
- [x] Added `scripts/github_coordination_guard.py` to provide:
  - startup summary across handoffs, session states, and publish queue
  - per-platform coordination validation
  - self-test scenarios
- [x] Updated shared docs and platform mirrors:
  - `docs/CROSS_PLATFORM_STANDARD.md`
  - `platforms/windows-codex/AGENTS.md`
  - `platforms/kimi-vps/AGENTS.md`
  - `platforms/opencode/AGENTS.md`
  - `platforms/claude-code/project-bundle/.claude/ORCHESTRATION_HOOKS.md`
- [x] Updated Claude Code hook logic to:
  - require shared coordination reads at session start
  - remind task-transition updates after meaningful tool steps
  - block stop when coordination is stale relative to the objective contract
- [x] Updated OpenCowork hook bundle to carry the same shared coordination rule and stale-stop guard.

## Partially Done
- [~] The enforcement is proven locally through self-tests, syntax checks, startup summary, and live per-platform validation, but it is not yet pushed as publish-ready code from this session.

## Not Done
- [ ] Mirror the same stronger enforcement into any remaining non-hook platforms that later gain a callable native guard surface.
- [ ] Decide whether the local root-repo experimental `.github/session-states/` surfaces should be retired or converted into simple pointers to the shared coordination repo to avoid drift.

## Decisions Made
- **Decision**: use task transitions, not session end, as the mandatory shared publish boundary. | **Why**: continuous sessions still lose context when they change tasks.
- **Decision**: keep per-platform `publish-queue/<platform>.yaml` files even when no debt remains. | **Why**: fixed file ownership is easier to validate and avoids "missing file" ambiguity.
- **Decision**: use a shared guard script plus hook integration where native hook surfaces exist. | **Why**: reminders alone were the failure mode that already proved too weak.

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `workflows/codex/github-publish-and-shared-sync.md` | Windows workspace | Added task-transition publish contract and enforcement rules. |
| `workflows/codex/task-transition-shared-publish-loop.md` | Windows workspace | New workflow for changing tasks without losing shared truth. |
| `chimera-vps-deploy/session-states/*` | Shared | New canonical per-platform shared task state surfaces. |
| `chimera-vps-deploy/publish-queue/*` | Shared | New per-platform publish-debt surfaces. |
| `chimera-vps-deploy/scripts/github_coordination_guard.py` | Shared | New validation and startup-summary guard. |
| `chimera-vps-deploy/docs/CROSS_PLATFORM_STANDARD.md` | Shared | Added shared coordination structure and task-transition contract. |
| `chimera-vps-deploy/platforms/windows-codex/AGENTS.md` | Shared | Added GitHub coordination gate for Windows Codex. |
| `chimera-vps-deploy/platforms/kimi-vps/AGENTS.md` | Shared | Added GitHub coordination gate for Kimi VPS. |
| `chimera-vps-deploy/platforms/opencode/AGENTS.md` | Shared | Added GitHub coordination gate for OpenCode. |
| `chimera-vps-deploy/platforms/claude-code/project-bundle/.claude/ORCHESTRATION_HOOKS.md` | Shared | Documented new session-start and stale-stop enforcement. |
| `chimera-vps-deploy/platforms/claude-code/project-bundle/.claude/hooks/*.py` | Shared | Wired startup summary, task-transition nudge, and stale coordination stop-block. |
| `chimera-vps-deploy/platforms/opencowork/local-bundle/chimera-enforcement-bundle/hooks/*.py` | Shared | Wired matching shared coordination reminders and stale coordination stop-block. |

## Proof
- `python chimera-vps-deploy/scripts/github_coordination_guard.py self-test`
  - all scenarios pass:
    - active with current queue passes
    - missing queue fails
    - stale state fails
    - complete with false queue passes
- `python chimera-vps-deploy/scripts/github_coordination_guard.py startup-summary --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy`
  - produced live cross-platform summary from handoffs, session states, and publish queue
- `python chimera-vps-deploy/scripts/github_coordination_guard.py validate-platform --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy --platform <platform>`
  - passed for all current platform files
- `py_compile`
  - passed for the shared guard and the updated stop/start hook files

## Sync Status
- **GitHub status**: local only
- **Other platforms that should pull this**: Windows Claude, OpenCowork local, Kimi VPS, OpenCode, future Windows Codex threads
- **What still needs sync**: commit and push the changed workflow and shared coordination repo files when this slice is approved for publish

## Next Actions (for next agent)
1. **[PRIORITY]** Decide whether to commit and push this coordination slice now or leave it as visible publish debt.
2. **[HIGH]** If pushed, update the local root experimental session-state surfaces so they point at `chimera-vps-deploy/session-states/` and do not compete with the shared truth.
3. **[HIGH]** Pull these changes on the other platforms and confirm their startup path actually reads the new shared coordination files.
4. **[MEDIUM]** Extend the same guard pattern to any additional platform with a real callable hook or wrapper surface.

## Skills to Read Before Starting
- [x] `codex-runtime-router`
- [x] `objective-orchestration-loop`
- [x] `agent-session-resume`

## Live System State (if applicable)
- Shared coordination repo now contains canonical `session-states/` and `publish-queue/` starter files
- Guard script local proof is green
- Hook-level enforcement is stronger for Claude Code and OpenCowork than before this pass

## Reading List for Next Agent
- `C:\Users\becke\claudecowork\workflows\codex\github-publish-and-shared-sync.md`
- `C:\Users\becke\claudecowork\workflows\codex\task-transition-shared-publish-loop.md`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\session-states\README.md`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\publish-queue\README.md`
