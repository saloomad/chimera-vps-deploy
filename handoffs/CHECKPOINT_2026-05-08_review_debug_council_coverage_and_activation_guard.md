# CHECKPOINT - 2026-05-08 Review Debug Council Coverage And Activation Guard

## Objective

Continue the open review/debug/simulation improvement objective by finishing the real remaining work:

- make Plugin Eval callable locally
- complete the first Chimera adversarial scenario packs
- add real council-run artifacts instead of script-only proof
- add lifecycle invariant coverage
- harden the actual activation gate so active-trade promotion requires explicit trigger legality

## What landed

- `scripts/plugin_eval_local.py`
- updated `scripts/plugin_eval_local.ps1`
- `scripts/build_chimera_council_case.py`
- `scripts/run_chimera_council_trace_coverage.py`
- expanded `scripts/run_chimera_review_debug_scenario_pack.py`
- expanded `scripts/tests/chimera_lifecycle_invariants.py`
- `scripts/tests/chimera_lifecycle_activation_guard_smoke.py`
- activation-legality hardening in `scripts/build_chimera_lifecycle_context.py`
- three additional saved council families:
  - `chimera_no_trade_should_win_contradictory_regime`
  - `chimera_stale_helper_false_promotion`
  - `chimera_wrong_symbol_or_side_promotion`
- updated skills:
  - `review-debug-simulation-orchestrator`
  - `chimera-review-debug-orchestrator`
  - `chimera-lifecycle-review-council`

## Key proof

Local:

- `python scripts/tests/chimera_lifecycle_activation_guard_smoke.py` -> `PASS`
- `python scripts/tests/chimera_lifecycle_invariants.py` -> `PASS`
- `python scripts/run_chimera_council_trace_coverage.py` -> `PASS`
- `python scripts/run_chimera_review_debug_scenario_pack.py` -> `PASS`
- all 3 updated skills validate with `quick_validate.py`
- Plugin Eval wrapper works locally for both main skills
- post-compaction Plugin Eval scores:
  - `review-debug-simulation-orchestrator` -> `95/100`
  - `chimera-review-debug-orchestrator` -> `91/100`

VPS:

- mirrored updated skills to:
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
- mirrored updated scripts, fixtures, and traces to the live VPS surfaces
- `python3 /root/openclawtrading/scripts/tests/chimera_lifecycle_activation_guard_smoke.py` -> `PASS`
- `python3 /root/openclawtrading/scripts/run_chimera_council_trace_coverage.py` -> `PASS`
- `python3 /root/openclawtrading/scripts/run_chimera_review_debug_scenario_pack.py` -> `PASS`

## Important lesson from this pass

The first VPS proof failed because a timed-out bulk copy left stale runtime files in place.

Real fix:

- inspect the live runtime files directly for the new guard strings
- recopy the missing files explicitly
- only then trust the VPS rerun

## Remaining project work

1. Reduce the token budget of:
   - `chimera-review-debug-orchestrator`
2. Add observed-usage benchmarking so Plugin Eval is backed by measured runs, not only static analysis.
3. Repair the repo-backed publish path so this work can move under the user’s `main`-first rule.

## GitHub / publish note

- Repo-backed files changed in this pass.
- No safe `main` publish happened in this pass.
- Current work is present locally, mirrored to Windows skill roots, and mirrored to the live VPS/runtime surfaces, but GitHub/main publication is still open.
