# CHECKPOINT - 2026-05-07 Chimera Review Debug Scenario Pack And Agent-Run Proof

## Objective

Continue the open review/debug/simulation improvement objective past the skill-contract layer by adding:

- real Chimera scenario packs
- lifecycle invariant tests
- a real saved agent-run council artifact
- an honest plugin-eval path that works on this machine

## What landed

- dedicated Chimera scenario-pack fixture roots
- `scripts/tests/chimera_lifecycle_invariants.py`
- `scripts/run_chimera_review_debug_scenario_pack.py`
- `scripts/plugin_eval_local.ps1`
- first real saved council run under:
  - `trace/review-debug/chimera-lifecycle/chimera_illegal_phase_promotion_shortcut/20260507T202500Z/`
- updated skill references in:
  - `chimera-review-debug-orchestrator`
  - `chimera-lifecycle-review-council`

## Key proof

Local:

- `python scripts/tests/chimera_lifecycle_invariants.py` -> `PASS`
- `python scripts/run_chimera_review_debug_scenario_pack.py` -> `PASS`
- `plugin_eval_local.ps1 analyze ...review-debug-simulation-orchestrator...` -> works
- `plugin_eval_local.ps1 analyze ...chimera-review-debug-orchestrator...` -> works

VPS:

- mirrored skill updates to:
  - `/root/openclawtrading/skills/...`
  - `/root/.openclaw/kimi-skills/...`
- mirrored scripts and fixtures to `/root/openclawtrading`
- mirrored the first council trace to repo and runtime workspace trace sinks
- `python3 /root/openclawtrading/scripts/run_chimera_review_debug_scenario_pack.py` -> `PASS`

## What the first real council said

For `chimera_illegal_phase_promotion_shortcut`, the deterministic lane and council both agreed:

- `WAIT` stayed the final state
- but the lifecycle contract still lets setup readiness imply too much
- the smallest real fix is to require an explicit entry-watch trigger object or activation-legal boolean before promotion beyond `WAIT`

## Remaining project work

1. Patch the actual entry-watch -> active-trade promotion gate in the live lifecycle flow so setup quality and activation legality are separate.
2. Add more saved live council runs for the other scenario families:
   - no-trade should win
   - stale helper false promotion
   - wrong symbol or wrong side promotion
3. Reduce token budget in the Chimera review/debug skills based on the plugin-eval warnings.

## GitHub / publish note

- Repo-backed files changed in this pass.
- No safe `main` publish happened in this pass because the repo is still on `add-remaining-files` and remains diverged from `main`.
- The work is present locally and mirrored to the VPS/runtime surfaces, but GitHub/main integration is still a separate open workflow repair.
