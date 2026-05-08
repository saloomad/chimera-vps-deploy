# CHECKPOINT_2026-05-07 Screener To Bundle Selection Handoff

## Objective

Close the remaining live-process ambiguity between screener top picks, bundle focus, and active entry-watch focus by adding one explicit screener-to-bundle selection handoff.

## Completed Work

- created `scripts/build_bundle_selection_context.py`
- added new live artifact:
  - `reports/auto/BUNDLE_SELECTION_CONTEXT.json`
- integrated the new artifact into:
  - `scripts/run_research_bundle_refresh.sh`
  - `scripts/build_research_bundle.py`
  - `scripts/build_chimera_lifecycle_context.py`
  - `orchestration/lobster/chimera-trade-lifecycle.lobster`
  - `workflows/codex/chimera-screener-to-trade-document-flow.md`
  - `research/platforms/2026-05-06-chimera-trade-lifecycle-operator-guide.md`

## Key Logic Change

The system now explains why the bundle focus symbol is the right live focus even when it is not the latest screener top pick.

Current live proof case:

- screener best long: `UUSDT`
- screener best short: `ASTERUSDT`
- active bundle focus: `SOLUSDT`

New handoff result:

- `focus_symbol: SOLUSDT`
- `selection_mode: existing_focus_overrides_screener_top_pick`
- reasoning:
  - live entry/execution surfaces already focus `SOLUSDT`
  - `ENTRY_SIGNALS entry_state is READY_TO_TRADE`
  - `PIPELINE_STATE phase is WAIT`
  - `ACTIVE_SETUPS contains the same focus symbol`

## Proof

### Live artifact proof

Confirmed on VPS:

- `/root/openclawtrading/reports/auto/BUNDLE_SELECTION_CONTEXT.json`
- `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
- `/root/openclawtrading/reports/auto/CHIMERA_LIFECYCLE_CONTEXT.json`

Confirmed contents:

- bundle carries top-level `selection_context`
- Part 1 carries `answer.selection_context`
- lifecycle context carries `selection_context`
- lifecycle source reports now name `bundle_selection_context`

## Remaining Gap

The new selection handoff is working.

The bounded refresh chain still exits non-zero because the strict bundle smoke currently reports:

- `part 7 source_status is usable_with_stale_helpers`
- `part 14 source_status is usable_with_stale_helpers`

This is now classified as:

- section-quality/freshness debt
- not a missing screener-to-bundle fill path

## Next Best Step

1. decide whether Parts 7 and 14 should be upgraded from helper-grade to `ready`
2. if yes, patch those lanes or adjust the strict smoke only if helper-grade is truly acceptable by contract
3. keep `BUNDLE_SELECTION_CONTEXT.json` as the required screener-to-bundle provenance bridge
