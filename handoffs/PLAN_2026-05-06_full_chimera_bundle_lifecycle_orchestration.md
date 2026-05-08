# PLAN - Full Chimera Bundle Lifecycle Orchestration

Date: 2026-05-06
Owner: Codex
Status: active plan

## Prompt Enhanced

Raw intent:

- make the whole Chimera trading-document process work from ticker discovery through analysis, strategy edge, entry alerts, trade management, exit, review, and learning
- make every section useful to Deezoh
- prove every data source and script
- use expert council and iterate until the process works

Professional execution brief:

Build and prove a full research-bundle operating system:

1. discover symbols or tickers worth analysis
2. create or refresh one research bundle per symbol
3. route missing fields to the right specialist owner
4. fill every section with source, freshness, evidence, and Deezoh-useful interpretation
5. run strategy search and backtest by symbol, timeframe, regime, and setup family
6. let Deezoh compare long, short, and no-trade
7. convert the chosen path into trigger, alert, order, stop, target, leverage, and risk rules
8. monitor trigger state, paper execution, active trade management, exit, review, and learning
9. prove file read/write/consumer paths and keep the process monitored

## Council Decision

The architecture should be one lifecycle with multiple owned documents, not one giant document pretending to own everything.

Primary surfaces:

- `Screener Packet`
  - decides which tickers deserve a full bundle
- `Chimera Research Bundle`
  - one per symbol, owns analysis through final Deezoh decision
- `Entry / Active Trade State`
  - linked child surface after Deezoh chooses a watched or active setup
- `Strategy Evidence Ledger`
  - tracks strategy results by symbol, timeframe, regime, and setup family
- `Learning / Review Ledger`
  - records post-trade and post-simulation learning before promotion into durable rules

## Current Bundle Section Map

| Part | Goal | Deezoh question answered | Owner | Main source family |
|---|---|---|---|---|
| 1 Instrument And Context | identify symbol, trigger, asset, freshness | what are we analyzing and why? | Deezoh / orchestrator | user request, screener, watchlist |
| 2 Technical Structure | map price structure, zones, patterns | where is structure valid or broken? | chart-analyzer | Jackson, tvremix, local structure scripts |
| 3 Indicators And Momentum | interpret timing, exhaustion, reset, reversal | enter now, wait, or reversal risk? | indicator-analyst | local calculator, Bitget TA, divergence scripts, chart confirmation |
| 4 Derivatives And Positioning | read leverage and crowding | is positioning helping or trapping? | market-maker / derivatives | Bitget, Binance, Coinalyze, derivatives reports |
| 5 Liquidation Heat Map | map sweeps, magnets, max pain | where can price sweep or squeeze? | liquidation-vision-analyzer | CoinGlass/heatmap route, maxpain reports |
| 6 Macro And Cross-Asset | broad environment | does the market backdrop help or veto? | macro-bias | market-data, macro reports, DXY/SPX/gold/oil/yields |
| 7 Catalysts, News, Events | event and headline risk | what can move or distort this trade? | catalyst / news-monitor | catalyst reports, news feeds, calendars |
| 8 Structural / Market Intel | deeper flows and regime | what hidden market structure matters? | market-intel | stablecoins, dominance, flows, market context |
| 9 Risk And Invalidation | define thesis damage | what breaks the idea, what is noise? | risk-engine | Parts 2-8 plus book risk |
| 10 Setup Candidates | rank paths | best long, best short, best no-trade? | Deezoh | Parts 2-9 |
| 11 Execution Plan, Orders, And Risk | actionable trigger and risk plan | exact trigger, order, SL/TP, leverage, risk, alerts? | position-sizer + entry-watch | Part 10, Part 9, account state, chart/indicator timing |
| 12 Strategy And Historical Edge | strategy fit and backtest evidence | does this setup match a tested playbook? | strategy | strategy report, tracker, backtests, replay, playbooks |
| 13 Final Decision | final desk posture | activate, watch, wait, reject, or no-trade? | Deezoh | Parts 1-12 |
| 14 Optional Learning And Idea Overlays | optional outside context | what questions/cautions come from YouTube or ideas? | youtube-analyst + strategy | overlays, idea system, validated TradingView ideas |

Linked child surface:

| Surface | Goal | Owner |
|---|---|---|
| Entry / Active Trade State | manage watched trigger, paper entry, hold/reduce/trail/exit, and post-trade review | entry-watch + execution + risk-engine + Deezoh |

## Runtime Architecture

Use this ownership split:

- `cron`
  - wake-up only
  - refresh routine reports and call the durable owner
- `Task Flow`
  - durable lifecycle state across restarts
  - owns queues: routine check, watchlist, bundle, entry watch, active trade, review, learning
- `Lobster`
  - bounded deterministic subflows
  - owns fill-bundle, strategy-selection/backtest, entry-watch validation, trade-management, trade-review
- `hooks`
  - lightweight event reactions
  - examples: new watchlist symbol, bundle completed, Deezoh decision written, trigger live, trade closed
- `standing orders`
  - paper-only boundary
  - stale-data freeze
  - max account and portfolio risk
  - no live execution without separate approval

## End-To-End Flow

1. Routine check or watchlist event wakes the system.
2. Screener packet ranks symbols and chooses top candidates.
3. Task Flow creates or updates bundle jobs.
4. `fill-research-bundle.lobster` fills Parts 1-9 from the correct owners.
5. Deezoh fills Part 10 by comparing long, short, and no-trade.
6. Position-sizer and entry-watch fill Part 11 with exact trigger, alert, order, stop, target, leverage, and risk.
7. Strategy fills Part 12 by searching and backtesting matching strategy families.
8. Optional overlays fill Part 14 only as caution or question seeds.
9. Deezoh fills Part 13 and chooses `activate`, `watch`, `wait`, `reject`, or `no_trade`.
10. If `watch` or `wait`, entry-watch monitors the exact Part 11 trigger contract.
11. If trigger confirms, execution opens paper trade only and writes active trade state.
12. Trade-management subflow checks hold/reduce/trail/exit conditions.
13. Trade-review subflow writes outcome and learning.
14. Strategy ledger updates performance by symbol, timeframe, regime, and trigger family.

## Strategy Role

Strategy is a playbook and evidence filter.

It should:

- classify the current market regime by symbol and timeframe
- map the setup candidate to a strategy family
- search available strategies for that family
- backtest by symbol, timeframe, regime, and setup type
- rank by walk-forward first, then profit factor, drawdown, sample size, and regime fit
- advise Deezoh whether the trigger should be trusted, stricter, looser, or rejected

It must not:

- authorize trade entry
- choose exact orders
- set account risk
- override Part 11 or Part 13

Current live strategy weakness:

- `STRATEGY_REPORT.json` is fresh but weak
- `passing_strategies = 0`
- `matching_strategy = false`
- `win_rate = 0`
- `profit_factor = 0`
- `combo_results.json` is missing on VPS
- live alerts are partly proxy-based

## Implementation Phases

### Phase 0 - Contract Cleanup

Goal:

- remove conflicting instructions before building runtime automation

Tasks:

- remove duplicate obsolete final-decision section from bundle template
- fix stale Part 11 names
- fix obvious stale `/home/open-claw` defaults in active owner docs and strategy scripts
- mirror the cleaned template and owner docs to VPS skill/runtime surfaces

Proof:

- template has exactly Parts 1-14
- no active end-state section refers to old `Part 11: Position Management And Risk`
- active owner docs use `/root/openclawtrading`

### Phase 1 - Strategy Evidence Repair

Goal:

- make Part 12 a real evidence source

Tasks:

- restore `strategy_backtest_lab.py`, `backtest_runner_v2.py`, and required strategy files to VPS
- generate `/root/openclawtrading/strategies/backtests/combo_results.json`
- add or repair `REGIMES.json` or equivalent regime input
- split rough watch signals into `STRATEGY_WATCH.json`
- reserve `STRATEGY_ALERTS.json` for regime-matching, backtested, non-locked signals
- upgrade `STRATEGY_REPORT.json` fields:
  - `ranked_strategy_candidates`
  - `best_timeframe_by_strategy`
  - `walk_forward_win_rate`
  - `profit_factor`
  - `sample_size`
  - `max_drawdown`
  - `evidence_quality`
  - `deezoh_trigger_advice`

Proof:

- BTC/ETH/SOL strategy runs for `15m`, `1h`, `4h`, `1d`
- at least one strategy comparison artifact exists
- Part 12 can say supported, weak, unproven, or blocked with evidence

### Phase 2 - Data Source Proof Matrix

Goal:

- prove every section source stack can fill or honestly mark missing fields

Tasks:

- BTC technical structure test across `15m`, `1h`, `4h`, `1d`, `1w`
- chart confirmation using VPS Jackson on port `9333`
- indicator comparison against TradingView for at least one timeframe
- derivatives proof for BTC/ETH/SOL
- liquidation exact heatmap plus maxpain proof
- macro proof including DXY, SPX, gold, oil, yields
- news/catalyst relevance filtering proof
- market intel proof separating exact data from proxy claims
- account/portfolio risk source proof
- optional YouTube/idea overlay refresh proof

Proof:

- one source matrix per section shows primary, fallback, helper-only, missing, and stale behavior
- source failures have fallback branches

### Phase 3 - Bundle Builder

Goal:

- create a repeatable bundle-filling process

Tasks:

- create `fill-research-bundle.lobster`
- create bundle artifact layout:
  - `/root/openclawtrading/reports/bundles/<symbol>/<bundle_id>.json`
  - `/root/openclawtrading/reports/bundles/<symbol>/<bundle_id>.md`
- create file IO manifest:
  - per section reads
  - per section writes
  - freshness owner
  - consumer
- make missing-field checklist explicit
- make Deezoh coordinate missing fields before final decision

Proof:

- one BTC bundle fills every section or marks missing fields honestly
- bundle records exact source files and timestamps

### Phase 4 - Deezoh Consumer Simulation

Goal:

- prove Deezoh uses the document correctly

Tasks:

- run `chimera-bundle-consumer-simulation`
- test BTC full bundle
- test watchlist/new-coin bundle
- test no-trade preservation
- force one missing chart field and one missing indicator field
- prove spawned specialist ids or mark specialist proof missing
- verify Deezoh compares best long, best short, best no-trade

Proof:

- Deezoh returns final posture, exact wait, next owner, provenance, and missing proof
- no-trade stays alive when evidence is incomplete

### Phase 5 - Runtime Task Flow And Lobster Wiring

Goal:

- make the process restart-safe and recurring

Tasks:

- update `taskflow.json` with:
  - `routine_check`
  - `bundle_queue`
  - `entry_watch`
  - `active_trade`
  - `trade_review`
  - `strategy_learning`
- replace old thin `trade-investigation.lobster`
- add:
  - `fill-research-bundle.lobster`
  - `strategy-selection-and-backtest.lobster`
  - `entry-watch.lobster`
  - `trade-management.lobster`
  - `trade-review.lobster`

Proof:

- Task Flow points to the new bundle-aware subflows
- Lobster outputs typed artifacts, not loose prose

### Phase 6 - Alerts, Paper Entry, Management, Exit

Goal:

- complete the lifecycle after Deezoh decides

Tasks:

- make Part 11 trigger contract consumable by entry-watch
- create dry-run chart alert proof
- create active trade state schema
- connect paper execution only after Deezoh and entry-watch agree trigger is live
- implement manage states:
  - hold
  - reduce
  - trail
  - exit
  - invalidate
  - review

Proof:

- entry-watch says `WAIT_TRIGGER`, `READY`, or `CANCEL` without inventing a new thesis
- simulated open trade switches Deezoh to `MANAGE`
- simulated close triggers review and learning

### Phase 7 - Monitoring And Learning

Goal:

- keep the process visible and self-improving

Tasks:

- add monitor output proving read/write/consumer paths
- add hook receipts:
  - `screener_packet_written`
  - `bundle_completed`
  - `deezoh_decision_written`
  - `entry_trigger_live`
  - `trade_closed`
  - `learning_ready`
- keep learning proposed until repeated proof or explicit approval

Proof:

- monitor shows current state for each watched symbol
- stale data is separate from system failure
- learning is captured but not blindly promoted

## First Safe Implementation Slice

Do this first:

1. finish Phase 0 mirror/proof
2. repair the VPS strategy backtest lane enough to produce `combo_results.json`
3. run BTC strategy matrix on `1h` and `4h`
4. update Part 12 example from real runtime evidence
5. run one BTC bundle consumer simulation with the new strategy evidence

Why this first:

- all councils agree strategy evidence is currently the weakest decision-critical lane
- Part 11 cannot choose stronger trigger confidence until Part 12 can say whether the strategy has edge
- Deezoh should not increase conviction from a strategy report that currently says zero passing strategies

## Acceptance Tests Before Calling The Whole Objective Done

The full objective is complete only when all are true:

- every section has owner, goal, questions, source order, freshness, and example
- every source family has a live or local proof result
- strategy produces non-empty evidence or explicitly marks evidence missing
- one BTC full bundle runs from discovery to final decision
- one watchlist/new-symbol path creates or rejects a bundle
- one no-trade case is preserved
- one entry-watch dry run consumes Part 11
- one paper-trade management simulation reaches review
- file IO manifest proves what was read and written
- monitor shows current lifecycle state
- live execution remains disabled unless separately approved

## Current Known Blockers

- strategy backtest artifacts missing on VPS
- account/portfolio risk source not proven
- optional YouTube/idea overlays not live-proven
- some Deezoh historical docs still contain old `/home/open-claw` examples
- old `trade-investigation.lobster` is not bundle-aware
- current `taskflow.json` still points routine market cycle at the old thin investigation flow

## Paper Safety Boundary

This plan is paper-safe.

No live trade may be placed, changed, canceled, or sized from this work unless Sal separately approves live execution.
