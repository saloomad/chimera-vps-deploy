# CHECKPOINT - 2026-05-06 Phase 3 Research Bundle Builder

## What moved

- Phase 2 source proof matrix is clean on the VPS:
  - `ready = 14`
  - `usable_with_stale_helpers = 0`
  - `degraded = 0`
  - `blocked = 0`
- Added the first deterministic full research-bundle builder:
  - `scripts/build_research_bundle.py`
- Mirrored it to the live VPS:
  - `/root/openclawtrading/scripts/build_research_bundle.py`
- Ran it against live VPS reports.

## Live proof

Command:

```bash
cd /root/openclawtrading
python3 scripts/build_research_bundle.py --reports-dir /root/openclawtrading/reports/auto
```

Outputs:

- `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
- `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.md`

Verified result:

- symbol: `SOLUSDT`
- bundle quality: `strong`
- sections emitted: `14`
- source matrix: `ready=14`, `degraded=0`, `blocked=0`
- Part 2 technical structure: `SOLUSDT`, fresh, includes `15m`, `1h`, `4h`, `1d`, `1w`
- Part 13 final posture: `no_trade`
- Part 13 veto owner: `DEEZOH_SCREENER_CONSUMPTION.json`
- Part 13 cross-lane conflicts: `5`
- smoke test passed:
  - `python3 scripts/tests/research_bundle_contract_smoke.py --bundle /root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
  - result: `ok=true`, symbol `SOLUSDT`, sections `14`
- live chain wiring added:
  - `/root/openclawtrading/scripts/run_desk_observability_chain.sh` now calls source matrix refresh, bundle build, and bundle smoke at the tail
- direct tail-command proof passed:
  - refreshed `BUNDLE_SOURCE_PROOF_MATRIX.json`, `RESEARCH_BUNDLE_latest.json`, and `RESEARCH_BUNDLE_latest.md` at `2026-05-06T04:34:12Z`
- readability upgrade passed:
  - bundle now has top-level `executive_summary`
  - every section now has `section_summary`
  - markdown starts with a decision-readable executive summary before the JSON payloads
  - live rebuilt at `2026-05-06T04:54:08Z`
  - executive decision: `no_trade`
  - entry state: `READY_TO_TRADE`
  - entry confidence: `VERY LOW`
  - macro verdict: `STAY OUT`
  - strategy evidence quality: `no_promoted_strategy_support`
  - smoke test remained `ok=true`
- bounded refresh command added and proven:
  - `/root/openclawtrading/scripts/run_research_bundle_refresh.sh`
  - refreshes source matrix, rebuilds bundle, and runs smoke test
  - completed under a 60-second timeout
  - refreshed bundle files at `2026-05-06T04:55:42Z`
- desk-chain tail now calls the bounded refresh script
- crontab has no standalone `run_research_bundle_refresh.sh` entry yet
- trader-useful summary upgrade passed:
  - Part 3 now includes indicator verdict, direction, entry grade, next trigger, invalidation, and overbought/oversold timeframe read
  - Part 4 now includes derivatives quality, Fear and Greed, total OI, extreme funding, liquidation signal count, and nearest maxpain/liquidation read
  - Part 6 now includes macro verdict, recommendation, confidence, reason, and cross-asset verdict
  - Part 9 now includes macro alignment, TP-only state, alert eligibility, and invalidation
  - Part 10 now includes setup status, score, distance, zone, R:R, and alignment
  - Part 11 now includes entry, stop, targets, score, macro verdict, and alert owner
  - live rebuilt at `2026-05-06T15:54:26Z`
  - source matrix returned to `ready=14`, `usable_with_stale_helpers=0`, `degraded=0`, `blocked=0`
  - smoke test remained `ok=true`
- refresh drift repair:
  - `run_research_bundle_refresh.sh` now refreshes `DEEZOH_SCREENER_CONSUMPTION.json`
  - it refreshes `LIQUIDATION_SUMMARY.json` through the fallback writer
  - it refreshes `DEEZOH_BUNDLE_TAIL_CONSUMPTION.json`
- strict section-quality gates added and proven:
  - `scripts/tests/research_bundle_contract_smoke.py` now checks required core fields for Parts 3, 4, 6, 9, 10, and 11
  - live refresh passed at `2026-05-06T16:14:15Z`
  - source matrix stayed `ready=14`, `usable_with_stale_helpers=0`, `degraded=0`, `blocked=0`
  - Part 11 now separates current macro from entry-surface macro so stale context is not mislabeled as current
  - latest Part 11 summary: `Current macro says MIXED; entry surface macro says MIXED`
  - latest bundle-tail posture: `wait`, workflow `range_rotation`, conflicts `2`
- entry alert owner proof added and proven:
  - latest `ENTRY_SIGNALS.json` mtime: `2026-05-06T16:19:28Z`
  - latest `RESEARCH_BUNDLE_latest.json` mtime: `2026-05-06T16:19:29Z`
  - Part 11 stores the execution contract under `answer.entry_core`
  - alert owner: `entry-watch`
  - alert state: `ALERT_ELIGIBLE`
  - alert-on-entry-zone: `true`
  - required confirmations:
    - price reaches the `90.545-91.455` entry zone
    - bearish rejection candle at the zone
  - do-not-chase rule is present in the alert trigger contract
  - strict smoke test passed again with `ok=true`, symbol `SOLUSDT`, sections `14`
- entry-watch live decision proof added and proven:
  - added `scripts/entry_watch_monitor.py`
  - mirrored it to `/root/openclawtrading/scripts/entry_watch_monitor.py`
  - `run_research_bundle_refresh.sh` now calls it after `desk_contract_bridge.py`
  - `run_research_bundle_refresh.sh` now logs per-stage start, finish, and duration so timeout causes are visible
  - new output: `/root/openclawtrading/reports/auto/ENTRY_WATCH_STATUS.json`
  - live price source priority: Bitget futures, Bitget spot, Binance fallback
  - paper-safe boundary: writes watch status and only appends `PRICE_ALERTS.json` if all required alert conditions pass; does not open trades
  - latest live decision at `2026-05-06T16:57:37Z`: `WAIT_PRICE_ZONE`
  - SOLUSDT price was `89.235`, planned short zone was `90.545-91.455`, distance to zone was `1.468%`
  - `should_alert=false`, `price_alert_written=false`
  - required price-zone confirmation was waiting; required candle-pattern confirmation was waiting
  - optional RSI confirmation passed; optional MACD confirmation did not pass
  - Part 11 now includes `answer.entry_core.entry_watch`
  - strict smoke test now requires the entry-watch fields and passed
  - source matrix Part 11 now includes `ENTRY_WATCH_STATUS.json`
  - source matrix stayed `ready=14`, `usable_with_stale_helpers=0`, `degraded=0`, `blocked=0`
- stale path repair:
  - `scripts/fast_price_check.py` no longer contains `/home/open-claw` paths
  - it now points at `/root/openclawtrading` and `/root/.openclaw`
  - it is not scheduled unless a separate cadence is approved
- paper lifecycle proof added and proven:
  - added `scripts/tests/paper_lifecycle_contract_smoke.py`
  - mirrored it to `/root/openclawtrading/scripts/tests/paper_lifecycle_contract_smoke.py`
  - output: `/root/openclawtrading/reports/auto/PAPER_LIFECYCLE_SMOKE.json`
  - test uses isolated temporary report directories and the real `ExecutionEngine`
  - `live_reports_mutated=false`
  - target case opened one paper trade, hit target 1, moved stop to breakeven, and closed target 2 as `WIN_TP2`
  - stop case opened one paper short and closed it at stop as `LOSS_STOP`
  - both cases wrote closed ledger, trade history, and critic review inside the isolated workspace
  - `run_research_bundle_refresh.sh` now runs `paper_lifecycle_contract_smoke`
  - source matrix Part 11 now includes `PAPER_LIFECYCLE_SMOKE.json`
  - Part 11 bundle now includes `answer.entry_core.paper_lifecycle_smoke_ok=true`
  - strict bundle smoke now requires the paper-lifecycle fields and passed
  - latest integrated proof at `2026-05-06T17:32:21Z`: source matrix `ready=14`, bundle sections `14`, smoke `ok=true`
- accepted-alert paper-open proof added and proven:
  - added `scripts/tests/paper_alert_acceptance_smoke.py`
  - mirrored it to `/root/openclawtrading/scripts/tests/paper_alert_acceptance_smoke.py`
  - output: `/root/openclawtrading/reports/auto/PAPER_ALERT_ACCEPTANCE_SMOKE.json`
  - test copies current live SOLUSDT reports into a temporary workspace
  - simulated accepted alert:
    - `ENTRY_WATCH_STATUS.decision=FIRE_ALERT`
    - `PRICE_ALERTS.status=ACCEPTED_FOR_PAPER_SMOKE`
    - `PIPELINE_STATE.phase=ACTIVATE`
  - real `ExecutionEngine` then opened one paper trade in the temporary workspace
  - accepted setup: `SOLUSDT_short_0`
  - entry: `91.0`
  - stop: `93.0`
  - targets: `87.0` and `84.0`
  - temp active open count: `1`
  - temp paper open count: `1`
  - temp history count: `0`
  - `live_reports_mutated=false`
  - live counts after proof stayed paper open `0`, paper closed `0`, active trades `0`, trade history `0`
  - `run_research_bundle_refresh.sh` now runs `paper_alert_acceptance_smoke`
  - source matrix Part 11 now includes `PAPER_ALERT_ACCEPTANCE_SMOKE.json`
  - Part 11 bundle now includes `answer.entry_core.paper_alert_acceptance_smoke_ok=true`
  - strict bundle smoke now requires accepted-alert paper-open fields and passed
  - latest integrated proof at `2026-05-06T17:57:53Z`: source matrix `ready=14`, bundle sections `14`, smoke `ok=true`
- current-setup management and exit proof added and proven:
  - added `scripts/tests/paper_current_setup_management_smoke.py`
  - mirrored it to `/root/openclawtrading/scripts/tests/paper_current_setup_management_smoke.py`
  - output: `/root/openclawtrading/reports/auto/PAPER_CURRENT_SETUP_MANAGEMENT_SMOKE.json`
  - test copies current SOLUSDT live reports into a temporary workspace
  - it simulates accepted alert, opens current setup, moves copied pipeline to `MANAGE`, hits target 1, moves stop to breakeven, then hits target 2
  - accepted setup: `SOLUSDT_short_0`
  - entry: `89.0`
  - stop: `91.0`
  - targets: `85.0` and `82.0`
  - close result: `WIN_TP2`
  - close price: `81.99`
  - PnL: `7.88%`
  - achieved R:R: `3.5`
  - temp paper closed count: `1`
  - temp history count: `1`
  - temp critic count: `1`
  - temp active open count after exit: `0`
  - `live_reports_mutated=false`
  - live counts after proof stayed paper open `0`, paper closed `0`, active trades `0`, trade history `0`
  - `run_research_bundle_refresh.sh` now runs `paper_current_setup_management_smoke`
  - source matrix Part 11 now includes `PAPER_CURRENT_SETUP_MANAGEMENT_SMOKE.json`
  - Part 11 bundle now includes `answer.entry_core.paper_current_setup_management_smoke_ok=true`
  - strict bundle smoke now requires current-setup management fields and passed
  - latest integrated proof at `2026-05-06T18:20:47Z`: source matrix `ready=14`, bundle sections `14`, smoke `ok=true`
- live alert boundary observed:
  - current `ENTRY_WATCH_STATUS.decision=FIRE_ALERT`
  - `PRICE_ALERTS.json` contains fresh `NEW` alerts for `SOLUSDT_short_0`
  - live price was inside the current short zone and required confirmations passed
  - Deezoh / pipeline remained `WAIT` / `no_trade`
  - execution did not open a live paper trade because `Deezoh phase WAIT is not an execution phase`
  - this preserves the safety rule: entry-watch wakes the desk, but Deezoh/final decision controls execution permission
- final-decision handoff proof added and proven:
  - added `scripts/tests/final_decision_handoff_smoke.py`
  - mirrored it to `/root/openclawtrading/scripts/tests/final_decision_handoff_smoke.py`
  - output: `/root/openclawtrading/reports/auto/FINAL_DECISION_HANDOFF_SMOKE.json`
  - test is read-only and checks live report files after entry-watch alerting
  - latest live proof at `2026-05-06T18:47:22Z`:
    - `ENTRY_WATCH_STATUS.decision=FIRE_ALERT`
    - latest alert status `NEW`
    - alert `auto_enter=false`
    - gate owner after alert `Deezoh final decision`
    - handoff result `preserved_no_trade_wait`
    - Deezoh decision `no_trade`
    - pipeline phase `WAIT`
    - execution phase `WAIT`
    - execution opened `0`
    - live paper open `0`
    - live active open `0`
    - live trade history `0`
  - allowed final actions after alert are now explicit:
    - `keep_no_trade`
    - `promote_activate`
    - `reject_alert_with_reason`
  - `run_research_bundle_refresh.sh` now runs `final_decision_handoff_smoke`
  - source matrix Part 13 now includes `FINAL_DECISION_HANDOFF_SMOKE.json`
  - Part 13 bundle now includes `answer.final_decision_handoff_smoke_ok=true`
  - Part 13 summary includes `Post-alert handoff preserved_no_trade_wait; gate owner Deezoh final decision; execution opened 0`
  - strict bundle smoke now requires final-decision handoff fields and passed
  - latest integrated proof at `2026-05-06T18:47:22Z`: source matrix `ready=14`, bundle sections `14`, smoke `ok=true`
- strategy learning feedback proof added and proven:
  - added `scripts/build_strategy_learning_feedback.py`
  - added `scripts/tests/strategy_learning_feedback_smoke.py`
  - mirrored both to `/root/openclawtrading/scripts/`
  - output: `/root/openclawtrading/reports/auto/STRATEGY_LEARNING_FEEDBACK.json`
  - `run_research_bundle_refresh.sh` now refreshes strategy evidence, builds strategy learning feedback, smokes it, refreshes lifecycle learning queue, refreshes lifecycle context, and refreshes symbol lifecycle state
  - Part 12 source matrix now includes `STRATEGY_LEARNING_FEEDBACK.json`
  - Part 12 bundle now includes `answer.strategy_learning_core`
  - strict bundle smoke now requires the strategy learning fields
  - latest integrated proof at `2026-05-06T22:39:14Z`:
    - source matrix `ready=14`, `usable_with_stale_helpers=0`, `degraded=0`, `blocked=0`
    - strict bundle smoke `ok=true`, symbol `SOLUSDT`, sections `14`
    - Part 12 source status `ready`
    - strategy learning feedback `ok=true`
    - Deezoh strategy use `do_not_promote_for_entry`
    - strategy evidence quality `no_promoted_strategy_support`
    - next backtest items `6`
    - lifecycle learning queue items `3`
  - learning queue issues now include:
    - `no_closed_trade_yet`
    - `strategy_edge_not_promoted_for_current_setup`
    - `process_lesson_can_be_used_but_trade_edge_cannot`
  - Deezoh may learn process rules now, but must not treat paper smokes as strategy edge
- strategy matrix source repair:
  - first attempt pointed `strategy_evidence_builder.py` at `TECHNICAL_STRUCTURE_BACKTEST_latest.json`
  - that file is a zone-engine replay, not a strategy matrix with `results`
  - `run_research_bundle_refresh.sh` now uses the latest `reports/historical_lab/strategy_matrix*.json`
  - current matrix source: `/root/openclawtrading/reports/historical_lab/strategy_matrix_live_btc_eth_sol_15m_1h_4h_1d_merged.json`
- expanded SOL strategy backtest proof added:
  - command owner: `trading_system/scripts/labs/strategy_backtest_lab.py`
  - output: `/root/openclawtrading/reports/historical_lab/strategy_matrix_expanded_sol_15m_1h_4h_1d_5000_20260506T2257Z.json`
  - tested `SOL/USDT` across `15m`, `1h`, `4h`, and `1d` with `--limit 5000`
  - live output mtime: `2026-05-06T22:59:42Z`
  - rows: `32`
  - verdict counts: `MARGINAL=4`, `INSUFFICIENT_DATA=4`, `REJECTED=24`
  - promoted strategies: `0`
  - marginal rows remained watch-only:
    - `rsi_mean_revert` `1h`: walk-forward PF `1.57`, sample `11`
    - `ema_ichimoku_rsi` `1d`: walk-forward PF `1.04`, sample `20`
    - `ema_cross_9_21_short` `1h`: walk-forward PF `0.96`, sample `9`
    - `stoch_rsi_bounce` `4h`: walk-forward PF `0.9`, sample `30`
  - interpretation: expanded SOL testing did not promote strategy confidence for the current setup
  - follow-up refresh command passed:
    - `timeout 520 scripts/run_research_bundle_refresh.sh`

## 2026-05-07 Strategy Probability / Deezoh Trigger Upgrade

- added probability-oriented strategy trigger playbook:
  - `scripts/build_strategy_trigger_playbook.py`
  - live mirror: `/root/openclawtrading/scripts/build_strategy_trigger_playbook.py`
  - output: `/root/openclawtrading/reports/auto/STRATEGY_TRIGGER_PLAYBOOK.json`
- expanded strategy signal quality from 4 cases to 40 cases:
  - symbol: `SOL/USDT`
  - timeframes: `15m`, `1h`, `4h`, `1d`, `1w`
  - output: `/root/openclawtrading/reports/auto/STRATEGY_SIGNAL_FAILURE_ANALYSIS.json`
  - comparison output: `/root/openclawtrading/reports/auto/STRATEGY_CONFIRMATION_POLICY_COMPARE.json`
- added strategy probability policy integration:
  - `scripts/build_strategy_probability_policy.py`
  - output: `/root/openclawtrading/reports/auto/STRATEGY_PROBABILITY_POLICY.json`
  - top-level compatibility fields include probability, support state, entry permission, and strategy block status
- updated entry-watch:
  - reads `STRATEGY_PROBABILITY_POLICY.json`
  - writes policy snapshot into `ENTRY_WATCH_STATUS.json`
  - blocks only alert firing until probability confirmations are met
  - does not block Deezoh from making a final probability/R:R decision
  - does not auto-enter
- current SOLUSDT proof:
  - focus: `SOLUSDT SHORT`
  - best trigger support: `ema_cross_9_21_short 1h probability_support`
  - backtest matrix: `40` cases
  - promoted passing strategies: `1`
  - combined probability estimate: `0.471`
  - historical edge state: `probability_support`
  - support state: `mixed_watch_only`
  - confirmation mode: `review_alert_only`
  - entry permission: `final_deezoh_decision_required`
  - strategy blocks trade: `false`
  - entry-watch decision: `WAIT_PROBABILITY_CONFIRMATION`
  - current reason: price is in zone, but probability policy requires `2` independent confirmations and `0` are proven
- lifecycle replay repair:
  - `scripts/build_chimera_lifecycle_context.py` now treats a closed trade with no active trade as `closeout` even when the copied pipeline phase is stale
  - fixed `loss_stop` outcome matrix failure
- lifecycle outcome matrix proof:
  - output: `/root/openclawtrading/reports/auto/CURRENT_FOCUS_LIFECYCLE_OUTCOME_MATRIX.json`
  - status: `PASS`
  - scenarios: `4`
  - passed: `4`
  - failed: `0`
  - scenarios: `WIN_TP2`, `LOSS_STOP`, `BREAKEVEN`, `THESIS_STOP`
- Part 7 source-matrix truth repair:
  - current news, catalyst, earnings, symbol news, and policy probability were fresh
  - `ECONOMIC_CALENDAR.json` remained a stale optional helper
  - Part 7 now stays `ready` when required live catalyst/news surfaces are fresh and no material event-risk gap exists
  - notes still show `policy lane status=proxy_only` and `policy official status=blocked_by_cme_anti_scraping`
- refresh path wiring:
  - `run_research_bundle_refresh.sh` builds the trigger playbook before the probability policy
  - it runs current-focus lifecycle smoke with `--skip-bundle-smoke`
  - the final bundle smoke remains the only bundle-quality gate after all sections are rebuilt
- live refresh-path proof:
  - `run_research_bundle_refresh.sh` log shows final `research_bundle_contract_smoke ok=true`
  - latest bundle: `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
  - symbol: `SOLUSDT`
  - sections: `14`
  - bundle quality: `strong`
  - source matrix Part 7/11/12/13: `ready`

### Remaining Same-Objective Work

- run the same strategy probability/playbook process across BTC and ETH, not only the current SOL focus
- add an optimizer pass that searches candidate confirmation filters instead of only comparing loose/balanced/strict templates
- add real closed-trade learning once a non-smoke paper trade closes naturally
- keep strategy advisory: it may support probability and alert strictness, but Deezoh remains final trade gate
- workspace registry refresh needs a tooling follow-up:
  - `python scripts/build_workspace_document_registry.py` hung for more than 5 minutes after this documentation update
  - the stuck local Python process was stopped
  - wiki `health.py --json` and `build_graph.py --no-infer` did complete
  - registry files were not refreshed in this pass
  - refreshed outputs:
    - `STRATEGY_LEARNING_FEEDBACK.json` at `2026-05-06T23:01:24Z`
    - `RESEARCH_BUNDLE_latest.json` at `2026-05-06T23:01:25Z`
  - Part 12 stayed `no_promoted_strategy_support`
  - Deezoh strategy guidance stayed `do_not_promote_for_entry`
- catalyst stale-helper repair:
  - first full refresh after strategy-feedback patch failed strict smoke because Part 7 / Part 14 had stale catalyst helper files
  - `run_research_bundle_refresh.sh` now runs `catalyst_agent/catalyst_agent.py` after news/calendar refresh
  - fallback is `catalyst_agent.py`, then `catalyst_contract_bridge.py`
  - this refreshed `CATALYST_REPORT.json` and `AI_CATALYST.json`
  - final rerun passed all 14 sections as ready
- heartbeat gate check at `2026-05-06T23:22Z`:
  - `TRADE_HISTORY.json` exists and has `0` trades
  - `PAPER_TRADES.json` exists and has `0` open and `0` closed trades
  - `ACTIVE_TRADES.json` exists and has `0` open trades
  - `ENTRY_WATCH_STATUS.json` decision is `WAIT_PRICE_ZONE`
  - `FINAL_DECISION_HANDOFF_SMOKE.json` still reports `preserved_no_trade_wait`
  - root crontab has no `run_research_bundle_refresh.sh` entry
  - review outcome: current heartbeat continuation is blocked on either a real closed trade or explicit scheduler approval
- approved continuation on `2026-05-07`:
  - standalone scheduler ownership was approved and installed
  - root crontab now includes:
    - `20,50 * * * * /usr/bin/flock -n /tmp/chimera_research_bundle_refresh.lock /usr/bin/timeout 520 /root/openclawtrading/scripts/run_research_bundle_refresh.sh >> /root/.openclaw/logs/research_bundle_refresh.log 2>&1 # research-bundle-refresh-standalone`
  - scheduler proof files are under `/root/openclawtrading/reports/auto/scheduler_proof/`
  - first scheduled-command proof failed strict bundle smoke because Part 2 degraded
  - root cause: standalone refresh did not own technical/chart dependency refresh; an attempted fallback chart refresh overwrote `CHART_ANALYSIS_latest.json` with `binance_ohlcv_fallback`
  - fix applied:
    - `run_research_bundle_refresh.sh` now refreshes `build_technical_structure_report.py` before source matrix and bundle build
    - `build_bundle_source_proof_matrix.py` now accepts fresh TradingView/tvremix-backed timeframe proof inside `TECHNICAL_STRUCTURE_latest.json`
  - final scheduled-command proof passed:
    - strict bundle smoke `ok=true`, symbol `SOLUSDT`, sections `14`
    - Part 2 status `ready`
    - Part 2 notes include `technical structure includes TradingView/tvremix-backed timeframe proof`
- strategy signal/fakeout diagnostic added:
  - new script: `/root/openclawtrading/scripts/analyze_strategy_signal_failures.py`
  - current output: `/root/openclawtrading/reports/auto/STRATEGY_SIGNAL_FAILURE_ANALYSIS.json`
  - historical output: `/root/openclawtrading/reports/historical_lab/strategy_signal_failure_analysis_sol_latest.json`
  - tested `SOL/USDT` on:
    - `rsi_mean_revert` `1h`: `46` valid signals, `3` good, `4` partial good, `14` stop-first fakeouts, `5` fakeout warnings, `20` unclear
    - `ema_cross_9_21_short` `1h`: `34` valid signals, `5` good, `2` partial good, `8` stop-first fakeouts, `4` fakeout warnings, `15` unclear
    - `stoch_rsi_bounce` `4h`: `109` valid signals, `6` good, `9` partial good, `30` stop-first fakeouts, `18` fakeout warnings, `46` unclear
    - `ema_ichimoku_rsi` `1d`: `340` valid signals, `52` good, `32` partial good, `74` stop-first fakeouts, `74` fakeout warnings, `108` unclear
  - interpretation: strategy signals fire, but fakeout/unclear rates are too high for entry promotion
- strategy chart-window proof added:
  - new script: `/root/openclawtrading/scripts/render_strategy_signal_charts.py`
  - manifest: `/root/openclawtrading/reports/auto/STRATEGY_SIGNAL_CHARTS_MANIFEST.json`
  - output dir: `/root/openclawtrading/reports/historical_lab/strategy_signal_charts/`
  - chart count: `8`
  - includes one good and one fakeout chart window for each tested strategy/timeframe
- Deezoh strategy reasoning simulation added:
  - new script: `/root/openclawtrading/scripts/test_deezoh_strategy_reasoning.py`
  - output: `/root/openclawtrading/reports/auto/DEEZOH_STRATEGY_REASONING_SIM.json`
  - result: `ok=true`, scenarios `24`, failures `0`
  - expected behavior proven:
    - fakeouts become `reject_or_wait`
    - good historical examples become `conditional_watch_only`
    - missed moves become `learn_do_not_chase`
    - current bundle conflicts override isolated historical examples
  - Part 12 bundle integration upgraded:
    - includes `strategy_signal_diagnostic_core`
    - includes `deezoh_strategy_reasoning_core`
    - includes `strategy_signal_charts_manifest`
    - latest strict bundle smoke remains `ok=true`
    - latest Part 12 summary includes: `Signal diagnostic cases 4; chart windows 8; Deezoh reasoning sim True with failures 0`
  - final verification pass after integration:
    - exact scheduled command passed
    - strict bundle smoke `ok=true`, symbol `SOLUSDT`, sections `14`
    - `RESEARCH_BUNDLE_latest.json` mtime `2026-05-07T17:28:21Z`
    - Part 2 status `ready`
    - Part 12 status `ready`

## Why it matters

The system no longer stops at proving separate source files exist. It now has a real document-building step that packages all 14 sections into one Deezoh-consumable bundle.

## Files changed locally

- `scripts/build_research_bundle.py`
- `scripts/build_bundle_source_proof_matrix.py`
- `scripts/entry_watch_monitor.py`
- `scripts/fast_price_check.py`
- `scripts/tests/paper_lifecycle_contract_smoke.py`
- `scripts/tests/paper_alert_acceptance_smoke.py`
- `scripts/tests/paper_current_setup_management_smoke.py`
- `scripts/tests/final_decision_handoff_smoke.py`
- `scripts/build_strategy_learning_feedback.py`
- `scripts/tests/strategy_learning_feedback_smoke.py`
- `scripts/analyze_strategy_signal_failures.py`
- `scripts/test_deezoh_strategy_reasoning.py`
- `scripts/render_strategy_signal_charts.py`
- `scripts/build_lifecycle_learning_queue.py`
- `scripts/tests/research_bundle_contract_smoke.py`
- `scripts/run_research_bundle_refresh.sh`
- `scripts/run_desk_observability_chain.sh`
- `research/platforms/2026-05-06-phase3-research-bundle-builder-proof.md`
- `research/platforms/2026-05-06-final-decision-handoff-proof.md`
- `research/platforms/2026-05-07-strategy-learning-feedback-proof.md`
- `research/platforms/2026-05-07-strategy-signal-fakeout-and-deezoh-reasoning-proof.md`
- `chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-06_phase3_research_bundle_builder.md`

## Still open

- standalone scheduler ownership for `run_research_bundle_refresh.sh` is approved, installed, smoke-proven, and still active
- multi-symbol BTC/ETH/SOL strategy probability/playbook expansion is complete and live refresh-proven
- continue the broader lifecycle proof into real closed-trade learning once a non-smoke paper trade closes naturally
- remaining strategy work should focus on confirmation-filter optimization, multi-symbol chart-window proof, R:R/alert replay, and Deezoh loosen/tighten behavior
- heartbeat continuation remains valid because Sal reopened the strategy/Deezoh objective for probability-weighted entries, confirmations, alerts, and risk/reward logic

## 2026-05-07 Multi-Symbol Strategy Probability Proof

- live refresh command completed at `2026-05-07T21:20Z`
- strict bundle smoke passed:
  - `ok=true`
  - symbol `SOLUSDT`
  - sections `14`
- latest bundle:
  - `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
  - mtime `2026-05-07T21:20:15Z`
- strategy playbook:
  - `/root/openclawtrading/reports/auto/STRATEGY_TRIGGER_PLAYBOOK.json`
  - rows `120`
  - symbols `BTCUSDT`, `ETHUSDT`, `SOLUSDT`
- signal diagnostics:
  - `/root/openclawtrading/reports/auto/STRATEGY_SIGNAL_FAILURE_ANALYSIS.json`
  - cases `120`
- Deezoh reasoning simulation:
  - `/root/openclawtrading/reports/auto/DEEZOH_STRATEGY_REASONING_SIM.json`
  - `ok=true`
  - scenarios `562`
  - failures `0`
- probability policy:
  - `/root/openclawtrading/reports/auto/STRATEGY_PROBABILITY_POLICY.json`
  - probability estimate `0.471`
  - strategy blocks trade `false`
- Part 12 status:
  - `ready`
  - summary includes `promoted passing strategies 8`, `Signal diagnostic cases 120`, `Deezoh reasoning sim True with failures 0`

Code changes behind this proof:

- `scripts/compare_strategy_confirmation_policies.py` accepts comma-separated analysis files and preserves symbol identity.
- `scripts/build_strategy_trigger_playbook.py` keys rows by symbol plus strategy/timeframe/direction so BTC, ETH, and SOL do not overwrite each other.
- `scripts/analyze_strategy_signal_failures.py` caches prepared symbol/timeframe data during multi-case runs.
- `scripts/test_deezoh_strategy_reasoning.py` treats `eligible_as_supporting_context_only` as watch/support-only, not unsafe promotion.
- `scripts/run_research_bundle_refresh.sh` prefers the multi-symbol compare file when it exists.

Current interpretation:

- strategy now supports Deezoh's probability, confirmation, and alert-strictness reasoning
- strategy does not auto-enter
- strategy does not hard-block a trade by itself
- current SOL focus remains review-only because independent confirmation is still insufficient
- Deezoh remains the final long/short/no-trade gate

## 2026-05-07 Entry / Alert / R:R Reasoning Replay

- added paper-safe replay script:
  - `/root/openclawtrading/scripts/test_deezoh_entry_alert_reasoning.py`
  - local source: `scripts/test_deezoh_entry_alert_reasoning.py`
- wired replay into:
  - `/root/openclawtrading/scripts/run_research_bundle_refresh.sh`
  - `/root/openclawtrading/scripts/build_research_bundle.py`
  - `/root/openclawtrading/scripts/build_bundle_source_proof_matrix.py`
- output:
  - `/root/openclawtrading/reports/auto/DEEZOH_ENTRY_ALERT_REASONING_SIM.json`
- replay proof:
  - `ok=true`
  - scenarios `6`
  - failures `0`
- scenario behaviors proven:
  - current live state can become `fire_review_alert_no_auto_entry`
  - missing confirmations stay `wait_probability_confirmation`
  - high R:R with one confirmation and low conflict can loosen to `loosen_to_review_alert_no_auto_entry`
  - confirmations met can fire a review alert
  - low R:R becomes `no_trade_bad_rr`
  - strategy block or fakeout pressure becomes `reject_or_wait`
- safety proof:
  - every scenario keeps `auto_enter=false`
  - `FIRE_ALERT` means review alert, not entry permission
  - `PAPER_TRADES.json` open `0`, closed `0`
  - `ACTIVE_TRADES.json` trades `0`
  - `TRADE_HISTORY.json` trades `0`
- final full refresh proof:
  - strict bundle smoke `ok=true`
  - symbol `SOLUSDT`
  - sections `14`
  - bundle quality `strong`
  - Part 11 source status `ready`
  - Part 12 source status `ready`
  - Part 11 summary includes `Entry/alert/R:R reasoning sim True with 0 failure(s)`
  - Part 12 summary includes `entry/alert/R:R sim True with failures 0`
- source matrix proof:
  - Part 11 note `entry alert reasoning sim ok=True scenarios=6 failures=0`
  - Part 12 note `entry alert reasoning sim ok=True failures=0`

Interpretation for next agents:

- Deezoh can loosen only into a review alert, not execution.
- R:R can raise the priority of a review question, but cannot override missing hard confirmation, invalidation, active veto pressure, or fakeout risk.
- Strategy remains probability support and alert-strictness input. It is not an execution switch.

## 2026-05-07 Confirmation Filter Optimizer Proof

- added optimizer script:
  - `/root/openclawtrading/scripts/optimize_strategy_confirmation_filters.py`
  - local source: `scripts/optimize_strategy_confirmation_filters.py`
- wired optimizer into:
  - `/root/openclawtrading/scripts/run_research_bundle_refresh.sh`
  - `/root/openclawtrading/scripts/build_research_bundle.py`
  - `/root/openclawtrading/scripts/build_bundle_source_proof_matrix.py`
- output:
  - `/root/openclawtrading/reports/auto/STRATEGY_CONFIRMATION_FILTER_OPTIMIZER.json`
- live optimizer proof:
  - source cases `120`
  - cases with viable filter `94`
  - tighten-preferred filters `70`
  - probability-improves filters `5`
  - rejected-best filters `19`
- full refresh proof after wiring:
  - strict bundle smoke `ok=true`
  - symbol `SOLUSDT`
  - sections `14`
  - bundle quality `strong`
  - Part 12 status `ready`
  - Part 12 summary includes `Optimizer viable filters 94/120; tighten-preferred 70; probability-improves 5`
  - source matrix Part 12 notes include `confirmation optimizer viable=94/120` and `confirmation optimizer tighten=70 probability_improves=5`
- safety proof:
  - optimizer only reads historical signal events and writes a report
  - `PAPER_TRADES.json` open `0`, closed `0`
  - `ACTIVE_TRADES.json` trades `0`
  - `TRADE_HISTORY.json` trades `0`

Interpretation for next agents:

- the optimizer searches real historical confirmation tags instead of relying only on loose/balanced/strict templates
- tighten-preferred filters should reduce fakeout pressure when the market is conflicted or confidence is weak
- probability-improves filters can help Deezoh loosen into review alerts when R:R and live structure agree
- rejected filters should not become mandatory requirements because they starve the strategy or fail to improve edge
- optimizer output is still advisory; Deezoh remains final gate

## 2026-05-08 Multi-Symbol Chart-Window Expansion

- updated chart renderer:
  - `/root/openclawtrading/scripts/render_strategy_signal_charts.py`
  - local source: `scripts/render_strategy_signal_charts.py`
- updated refresh wiring:
  - `/root/openclawtrading/scripts/run_research_bundle_refresh.sh`
- updated source matrix:
  - `/root/openclawtrading/scripts/build_bundle_source_proof_matrix.py`
- output:
  - `/root/openclawtrading/reports/auto/STRATEGY_SIGNAL_CHARTS_MANIFEST.json`
  - `/root/openclawtrading/reports/historical_lab/strategy_signal_charts/`
- final full refresh proof:
  - strict bundle smoke `ok=true`
  - symbol `SOLUSDT`
  - sections `14`
  - chart manifest mtime `2026-05-08T00:08:53Z`
  - bundle mtime `2026-05-08T00:12:09Z`
  - selected cases `12`
  - chart windows `24`
  - symbols `BTC/USDT`, `ETH/USDT`, `SOL/USDT`
  - chart render errors `0`
  - Part 12 source status `ready`
  - Part 12 summary includes `chart windows 24`
  - source matrix Part 12 includes `chart windows=24 symbols=BTC/USDT,ETH/USDT,SOL/USDT errors=0`
- safety proof:
  - chart renderer only reads historical market data and writes PNG/report artifacts
  - no live or paper trades were opened

Interpretation for next agents:

- chart windows are visual audit evidence for strategy good/fakeout classifications
- Deezoh should compare the current chart to these windows before trusting a strategy trigger
- chart evidence still cannot override invalidation, R:R, catalyst/macro conflict, or final no-trade discipline
- the prior same-objective chart expansion gap is now closed

Verification notes:

- VPS Python syntax check passed for the touched strategy, bundle, lifecycle, and entry-watch scripts.
- VPS shell syntax check passed for `scripts/run_research_bundle_refresh.sh`.
- Wiki health passed with no empty files and no index-sync gaps.
- Wiki graph rebuilt to `48` nodes and `79` edges.
- Workspace registry updater had a tooling blocker:
  - `python scripts/build_workspace_document_registry.py` timed out after `180` seconds in the prior pass and after `90` seconds in this pass.
  - It partially updated `DOCUMENT_REGISTRY.md`, `INDEX.md`, and `tracking/WORKSPACE_FILE_REGISTRY.md`.
  - Local helper processes spawned by the registry/coordination path were stopped after timeout.
  - Do not claim the registry refresh is fully proven until this updater is repaired or completes cleanly.
- Later registry retry completed successfully:
  - `python scripts/build_workspace_document_registry.py`
  - result: `Registry updated: 8377 tracked files`
  - current status: registry refresh is no longer the active blocker for this strategy slice.
