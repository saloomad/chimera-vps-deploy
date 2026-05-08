# CHECKPOINT_2026-05-07 Orchestration Stop Rule Hardening

## Objective

Repair the orchestration rule that still allowed a continuation owner to be deleted while same-objective work remained open, then prove the fix and capture the Git branch/publication reality honestly.

## Completed Work

- patched source-of-truth skill:
  - `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md`
- added explicit rules:
  - `Same-Objective Remaining Work Rule`
  - `Heartbeat Delete Checklist`
  - `Dynamic Improvement Objective Mode`
  - explicit rejection of `second wave` / `future improvement` relabeling for still-required same-objective work
- patched instruction/workflow layers:
  - `C:\Users\becke\.codex\AGENTS.md`
  - `C:\Users\becke\claudecowork\workflows\codex\openclaw-role-orchestration-loop.md`
- patched deterministic policy layer:
  - `C:\Users\becke\claudecowork\scripts\orchestration_policy.py`
  - `C:\Users\becke\claudecowork\scripts\tests\orchestration_policy_matrix.py`
- logged the regression durably in:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\ORCHESTRATION_ISSUES.md`
- validated:
  - `python C:\Users\becke\claudecowork\scripts\tests\orchestration_policy_matrix.py`
  - `python -X utf8 C:\Users\becke\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\becke\.codex\skills\objective-orchestration-loop`
- mirrored the updated orchestration skill to:
  - `C:\Users\becke\.claude\skills`
  - `C:\Users\becke\.openclaw\skills`
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
- proved the live VPS mirrors contain:
  - `Same-Objective Remaining Work Rule`
  - `Heartbeat Delete Checklist`
  - `Dynamic Improvement Objective Mode`
- removed stale nested duplicate skill trees from:
  - source-of-truth `C:\Users\becke\.codex\skills\objective-orchestration-loop`
  - Windows Claude and OpenClaw local mirrors
  - shared mirror
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`

## Main Decision

Do not allow orchestration to call something `complete` while the same user objective still has meaningful open work, even if that work is described as:

- `second wave`
- `future improvement`
- `next phase`

If the user asked to keep improving or iterate until stronger, those items stay inside the same guarded objective until explicitly de-scoped.

New dynamic behavior:

- when the objective is improvement-oriented, orchestration should reselect the next bounded same-objective slice automatically
- it should not wait for the user to restate the next obvious improvement if the next slice is still safe, bounded, and part of the same request

## Git / Publish Reality

- current local branch: `add-remaining-files`
- local `main` and `origin/main` are both still at:
  - `b0033e48d4934195d2ed25867555d6cdc07b595f`
- current branch is ahead of `main` by `55` commits
- current branch is behind `main` by `10` commits
- this bounded orchestration fix was committed and pushed on the current branch as:
  - `5549fd3` - `[Codex] Harden dynamic orchestration iteration rules`

That means the reason no fresh work is showing up on `main` is not "GitHub is broken." The repo is still living on a long-lived feature branch instead of integrating back to `main`, which violates the branch strategy now documented in the workspace.

## Remaining Project Work

1. fix the publication path:
   - decide whether to rebase/merge `add-remaining-files` back into `main` safely
   - then make future bounded work publish with frequent commits instead of accumulating on the long-lived branch
2. run future real-session regression proof:
   - verify the heartbeat is not deleted when same-objective remaining work still exists
3. continue any still-open improvement objective under the corrected stop rule instead of silently collapsing it into a finished slice
