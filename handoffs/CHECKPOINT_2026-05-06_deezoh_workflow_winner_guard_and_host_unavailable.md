# CHECKPOINT - 2026-05-06 Deezoh Workflow Winner Guard And Host Unavailable

## What moved in this pass

- resumed from the current Deezoh/Hermes improvement owner instead of reopening the already-closed no-trade same-cycle proof
- re-ran the bounded local workflow-family, observation, and provenance suites
- found a real Deezoh reasoning regression in `scripts/deezoh_question_engine.py`
  - `macro_data_degraded_mode` still selected `data_degraded_watch` but crowned `winner = short`
  - `screener_failed_breakout_short` still selected `liquidity_trap` but crowned `winner = short`
- patched the comparison winner logic so explicit protection workflows now force `winner = no_trade` without renaming the structural workflow
- attempted a bounded live VPS re-check, but `ssh root@100.67.172.114` timed out, so this run classified the host as unavailable rather than claiming a live agent regression

## Why this matters

This closed a real local reasoning-quality gap.

Before the fix, Deezoh could preserve the right workflow label while still teaching itself the wrong winner on the same cycle. That is more dangerous than a wording bug because it weakens no-trade protection exactly where the workflow says caution should dominate.

This run did not produce fresh live proof because the VPS was unreachable from the current machine. That absence is a reachability boundary, not evidence that Deezoh or Hermes regressed live.

## What ran

### Local proof

- `python scripts/tests/deezoh_specialist_workflow_alignment_smoke.py`
- `python scripts/tests/deezoh_observation_suite_smoke.py`
- `python scripts/tests/deezoh_provenance_contract_smoke.py`

### Live probe

- `ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=8 root@100.67.172.114 "echo VPS_OK && cd /root/openclawtrading && python3 --version && ls reports/auto | tail -n 20"`

## What changed

- Updated `scripts/deezoh_question_engine.py`
  - protection workflows now force `winner = no_trade` inside `build_decision_comparison` for:
    - `macro_selected_workflow = data_degraded_mode`
    - `screener_selected_workflow = no_trade_protection`
    - `screener_selected_workflow = failed_breakout_short`

## Proved

- local proof is green again:
  - `deezoh_specialist_workflow_alignment_smoke`
  - `deezoh_observation_suite_smoke`
  - `deezoh_provenance_contract_smoke`
- repaired branch outputs now stay aligned:
  - `data_degraded_watch -> winner = no_trade`
  - `liquidity_trap` from `failed_breakout_short -> winner = no_trade`

## Still open

- retry bounded live VPS proof when `root@100.67.172.114` is reachable again
- prove one real spawned-specialist branch under the active Deezoh workflow without weakening the strict `actually_spawned_specialists = []` rule for report-only cycles
- Hermes recurrence remains scheduler-owner debt and still needs approval before any live scheduler mutation
- liquidity promotion and `long_short_skew` coverage remain separate evidence-chain owners after this Deezoh ranking fix
