# CHECKPOINT_2026-05-07 Part 7 Ready And Fast Closeout Simulation

## Objective

Continue the open Chimera bundle productization work by:

- upgrading `Part 7` and `Part 14` to genuine `ready` status if possible
- adding a fast lifecycle simulation so closeout logic can be tested without waiting for a real paper trade

## Completed Work

- updated `scripts/run_research_bundle_refresh.sh`
  - added economic calendar refresh stage
  - added `current_focus_full_lifecycle_smoke` stage
- updated `scripts/build_bundle_source_proof_matrix.py`
  - Part 11 now consumes `CURRENT_FOCUS_FULL_LIFECYCLE_SMOKE.json`
- updated `scripts/build_research_bundle.py`
  - Part 11 now carries the fast full-lifecycle proof in both payload and summary
- updated `scripts/tests/research_bundle_contract_smoke.py`
  - requires the new Part 11 full-lifecycle fields
  - no longer has the recursive bundle-smoke dependency
- updated `scripts/tests/paper_alert_acceptance_smoke.py`
  - added fallback from `ACTIVE_SETUPS.json` and candle price
- updated `scripts/tests/current_focus_full_lifecycle_smoke.py`
  - now writes proof into the isolated workspace first
  - then rebuilds the bundle on top of that proof

## Live Proof

Confirmed on VPS:

- `CURRENT_FOCUS_FULL_LIFECYCLE_SMOKE.json`
  - `ok: true`
  - `closed_result: WIN_TP2`
  - `lifecycle_phase: closeout`
  - `bundle_smoke_ok: true`
- isolated workspace bundle Part 11
  - `source_status: ready`
  - `alert_owner: entry-watch`
  - `current_focus_full_lifecycle_smoke_ok: true`
- live bundle after refresh
  - `overall_data_quality: strong`
  - `Part 7: ready`
  - `Part 11: ready`
  - `Part 14: ready`

## Main Decision

Do not weaken the rule first.

Result:

- `Part 7` was repaired to `ready` through fresh source flow
- `Part 14` is `ready`
- accelerated closeout proof now exists as a real live test lane instead of waiting for a natural trade

## Remaining Project Work

1. use the new fast closeout lane plus real paper closeouts to improve:
   - learning queue recommendations
   - review/debug recommendations
   - weak instructions or handoff rules
2. compare synthetic closeout lessons vs real closeout lessons once a natural paper trade finishes
3. if needed later, extend the accelerated lane with alternative outcomes like:
   - loss stop
   - breakeven
   - thesis stop before activation
