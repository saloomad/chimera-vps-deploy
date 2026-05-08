# CHECKPOINT - 2026-05-06 Part 12 Strategy Evidence Repair

## What moved in this heartbeat

- resumed the full Chimera bundle lifecycle from the open Part 12 strategy-evidence slice
- verified live VPS truth at `root@100.67.172.114:/root/openclawtrading`
- confirmed the previous blocker:
  - `combo_results.json` was missing
  - `backtest_runner_v2.py` was missing on VPS
  - `strategy_backtest_lab.py` was missing on VPS
  - `ccxt` and `yfinance` were not installed on VPS
- avoided forcing system Python packages after the VPS reported an externally-managed Python environment
- added a built-in Binance REST candle fallback to the strategy runner
- copied the runner and lab to the VPS
- ran a live BTC/USDT 4h strategy matrix
- built Deezoh-readable strategy evidence files
- fixed the strategy engine so unbacktested fired conditions become watch-only instead of entry alerts

## Live proof

Live matrix:

- `/root/openclawtrading/reports/historical_lab/strategy_matrix_live_btc_stoch_4h.json`
- strategy: `stoch_rsi_bounce`
- symbol/timeframe: `BTC/USDT 4h`
- source: Binance REST
- bars fetched: `800`
- full period: `11` trades, `72.73%` win rate, `4.27` profit factor
- walk-forward: `4` trades, `50.0%` win rate, `0.71` profit factor
- verdict: `REJECTED`

Evidence outputs:

- `/root/openclawtrading/strategies/backtests/combo_results.json`
- `/root/openclawtrading/reports/auto/STRATEGY_EVIDENCE.json`
- `/root/openclawtrading/reports/auto/STRATEGY_WATCH.json`
- `/root/openclawtrading/reports/auto/STRATEGY_REPORT.json`

Post-fix strategy runner proof:

- `STRATEGY_ALERTS.active_count = 0`
- `STRATEGY_ALERTS.alerts_len = 0`
- `STRATEGY_WATCH.watch_count = 1`
- `STRATEGY_WATCH.live_watch_count = 14`
- `STRATEGY_REPORT.passing_strategies = 0`
- `STRATEGY_REPORT.matching_strategy = false`
- `STRATEGY_REPORT.walk_forward_win_rate = 50.0`
- `STRATEGY_REPORT.profit_factor = 0.71`
- `STRATEGY_REPORT.sample_size = 4`
- `STRATEGY_REPORT.evidence_quality = no_promoted_strategy_support`

## Files changed locally

- `backtest_runner_v2.py`
- `scripts/strategy_evidence_builder.py`
- `agents/strategy/strategy_engine.py`
- `agents/strategy/run_strategy.sh`
- `agents/strategy/strategy_tracker.py`
- `research/platforms/2026-05-06-part12-strategy-evidence-live-proof.md`
- `chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-06_part12_strategy_evidence_repair.md`

## Files mirrored to VPS

- `/root/openclawtrading/backtest_runner_v2.py`
- `/root/openclawtrading/trading_system/scripts/labs/strategy_backtest_lab.py`
- `/root/openclawtrading/scripts/strategy_evidence_builder.py`
- `/root/openclawtrading/agents/strategy/strategy_engine.py`
- `/root/openclawtrading/agents/strategy/run_strategy.sh`
- `/root/openclawtrading/agents/strategy/strategy_tracker.py`

## Still open

- broader BTC/ETH/SOL strategy matrices are now complete for `15m`, `1h`, `4h`, and `1d`
- merged proof file:
  - `/root/openclawtrading/reports/historical_lab/strategy_matrix_live_btc_eth_sol_15m_1h_4h_1d_merged.json`
- merged result:
  - `69` deduped cases
  - `0` pass
  - `1` marginal
  - `33` rejected
  - `35` insufficient data
- `REGIMES.json` is now repaired from `CANDLES.json`
  - builder: `/root/openclawtrading/scripts/build_regimes_from_candles.py`
  - output: `/root/openclawtrading/reports/auto/REGIMES.json`
  - proof: BTC `4H=BULL_TREND`, ETH `4H=BULL_TREND`, SOL `4H=UNKNOWN`
- normal runner proof after repair:
  - `STRATEGY_ALERTS.active_count = 0`
  - `STRATEGY_WATCH.live_watch_count = 17`
  - `combo_results.summary.total_tested = 69`
  - `combo_results.summary.passing_count = 0`
  - `STRATEGY_REPORT.evidence_quality = no_promoted_strategy_support`
- tracker cleanup decision:
  - no forced cleanup done because oldest open advisory row was about `46.2h`, below the current `48h` expiry rule
  - keep this as a later labeling/semantics improvement, not a blocker for Part 12 proof

## Still open now

- continue Phase 2 data-source proof matrix for the full bundle
