# CHECKPOINT - 2026-05-06 Screener Routing And Deezoh Consumption Proof

## What landed

- recreated a broader thread heartbeat after the earlier premature close
- upgraded `divergence_scanner_v2.py` so live divergence rows carry:
  - `signal_family`
  - `analysis_depth_hint`
  - `dominant_timeframe`
  - `timing_state`
  - `top_signal`
  - lead divergence metadata
  - specialist targets and questions
- fixed the live VPS root-layout import/path bug in `divergence_scanner_v2.py`
- upgraded `scripts/build_scout_report.py` so richer divergence routing survives into the screener outputs
- improved opportunity-row routing so `analysis_depth_hint` can influence the first owner instead of every name looking the same
- added `scripts/simulate_deezoh_screener_consumption.py`
- generated live VPS `DEEZOH_SCREENER_CONSUMPTION.json`
- updated:
  - `agents/screener/WORKFLOW.md`
  - `agents/deezoh/WORKFLOW.md`
  - `chimera-vps-deploy/handoffs/ORCHESTRATION_ISSUES.md`
  - `research/platforms/2026-05-06-screener-routing-and-deezoh-consumption-proof.md`

## Live proof

Host:

- `root@100.67.172.114`

Live rebuilt artifacts:

- `/root/openclawtrading/reports/auto/DIVERGENCES.json`
- `/root/openclawtrading/reports/auto/SCOUT_REPORT.json`
- `/root/openclawtrading/reports/auto/SHORTLIST_REVIEW.json`
- `/root/openclawtrading/reports/auto/DEEZOH_SCREENER_CONSUMPTION.json`

Key current proof results:

- best long now: `UUSDT LONG` -> `watch_only`
- best short now: `ASTERUSDT SHORT` -> `indicator_first`
- no-trade state still active:
  - workflow: `no_trade_protection`
  - verdict: `BALANCED_REVIEW`
- current consumption result:
  - `full_bundle_now_count = 0`
  - `specialist_first_count = 3`
  - `watch_only_count = 8`

This is the important behavior change:

- the screener no longer forces broad promotion into full bundles
- Deezoh can now see which names need chart first, indicator first, or only watch status

## Important open issue

- some saved `SCOUT_REPORT.json` long/short book rows still lag the richer first-owner metadata more than the in-memory builder state; the live proof artifact and shortlist layer are already stronger, but the broad books still need one more cleanup pass if we want every surface to match perfectly

## Next bounded step

1. finish the remaining saved-book metadata cleanup so `SCOUT_REPORT.json`, `SHORTLIST_REVIEW.json`, and `DEEZOH_SCREENER_CONSUMPTION.json` all tell the same owner/routing story
2. then continue `Part 11: Position Management And Risk`
3. then continue `Part 12: Final Decision`
