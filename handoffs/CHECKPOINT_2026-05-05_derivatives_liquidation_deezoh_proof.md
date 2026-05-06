# Derivatives, Liquidation, And Deezoh Proof Checkpoint

Date: 2026-05-05
Owner: Codex
Scope: Part 4 / Part 5 data truth, Deezoh evidence logic, local browser scraping proof

## What changed

- strengthened `scripts/deezoh_question_engine.py`
  - Deezoh now distinguishes:
    - `proxy_only`
    - `exact_liquidation_only`
    - `exact_maxpain_only`
    - `exact_both`
  - added derived reads:
    - `price_vs_oi_24h_read`
    - `price_vs_funding_24h_read`
    - exact liquidation directional bias
    - exact max-pain directional bias
  - exact CoinGlass BTC `24h` heatmap and exact max-pain no longer get flattened into the old proxy-only penalty

- strengthened `scripts/build_deezoh_thoughts.py`
  - now records:
    - `HOMEPAGE_TABLE.json`
    - `HOMEPAGE_SIGNAL.json`
    - `HOMEPAGE_STATS.json`
    - `HOMEPAGE_DERIVATIVES_HISTORY.jsonl`
    - `HOMEPAGE_DERIVATIVES_LATEST.json`
    - `HOMEPAGE_DERIVATIVES_REPLAY.json`
  - so Deezoh provenance shows the CoinGlass homepage lane was actually read
  - now also writes symbol-specific focused bundles even when the main live bundle is still broad `MARKET` mode

- strengthened `scripts/market-maker/run_liquidation_scans.py`
  - now runs the exact `24h` CoinGlass extractor for supported coins
  - now carries exact cluster fields into `LIQUIDATION_SUMMARY.json`
  - no longer treats max-pain screenshots as liquidation screenshot proof
  - no longer reports BTC/ETH/SOL as failed just because CoinAnk login failed when CoinGlass already worked

- strengthened `trading_system/scripts/coinglass_homepage_scraper.py`
  - Windows UTF-8 stdout/stderr fix landed
  - local browser scrape is now working and writes:
    - `trading_system/data/HOMEPAGE_TABLE.json`
    - `trading_system/data/HOMEPAGE_SIGNAL.json`
    - `trading_system/data/HOMEPAGE_STATS.json`
    - `trading_system/data/HOMEPAGE_DERIVATIVES_HISTORY.jsonl`
    - `trading_system/data/HOMEPAGE_DERIVATIVES_LATEST.json`
    - `trading_system/data/HOMEPAGE_DERIVATIVES_REPLAY.json`
  - this is now the small snapshot history loop for future derivatives replay/backtest work

- updated Part 4 draft
  - `chimera-vps-deploy/handoffs/parallel_part4_derivatives_and_positioning.md`
  - now explicitly includes `coinglass_homepage_scraper.py` as the file-backed source for `price_24h_pct`, `oi_1h_pct`, and `oi_24h_pct`

- wrote the durable proof note
  - `research/platforms/2026-05-05_derivatives_liquidation_deezoh_proof.md`

## Fresh proof

Passed:
- `python scripts/market-maker/run_liquidation_scans.py`
- `python scripts/build_deezoh_thoughts.py`
- `python scripts/tests/liquidation_summary_contract_smoke.py`
- `python scripts/tests/deezoh_derivatives_context_smoke.py`
- `python trading_system/scripts/coinglass_homepage_scraper.py`

Fresh outputs:
- `reports/auto/LIQUIDATION_SUMMARY.json`
- `reports/auto/MAXPAIN_SUMMARY.json`
- `reports/auto/DEEZOH_THOUGHTS.json`
- `reports/auto/LIQUIDATION_DATA/BTC_24h.json`
- `reports/auto/DEEZOH_THOUGHTS_FOCUS/INDEX.json`
- `trading_system/data/HOMEPAGE_TABLE.json`
- `trading_system/data/HOMEPAGE_SIGNAL.json`
- `trading_system/data/HOMEPAGE_STATS.json`
- `trading_system/data/HOMEPAGE_DERIVATIVES_HISTORY.jsonl`
- `trading_system/data/HOMEPAGE_DERIVATIVES_LATEST.json`
- `trading_system/data/HOMEPAGE_DERIVATIVES_REPLAY.json`

## Current truth

- exact local liquidation proof is currently working on:
  - `BTC 24h`
  - `ETH 24h`
  - `SOL 24h`
- max-pain fast lane is still `24h`
- homepage scrape now fills the important missing Part 4 fields:
  - `price_24h_pct`
  - `oi_1h_pct`
  - `oi_24h_pct`
  - liquidation table context
- fresh BTC live values now show:
  - `price_24h_pct: 2.26`
  - `oi_1h_pct: 0.89`
  - `oi_24h_pct: 7.65`
  - `funding_rate: -0.0117`
- fresh exact BTC `24h` heatmap now shows:
  - `vulnerable_side: longs`
  - `sweep_bias: down_first`
  - `cluster_count: 8`
  - nearest above cluster at `+1.895%`
  - nearest below cluster at `-0.433%`
- fresh exact BTC max pain now shows:
  - `overall_bias: NEUTRAL`
  - upside target distance `1.17%`
  - downside target distance `1.653%`
- `LIQUIDATION_SUMMARY.json` no longer mixes `coinglass_maxpain` screenshot tags into the heatmap proof rows
- the new focused Deezoh outputs now show:
  - `BTCUSDT -> exact_both`
  - `ETHUSDT -> exact_both`
  - `SOLUSDT -> exact_both`
- the new replay lane is wired, but the fresh file currently has only one snapshot so transition counts are still empty

## Remaining gaps

- local file-backed lane still lacks stable per-symbol:
  - top-trader ratios
  - taker ratio history
  - durable matched-window OI history
- exact heatmap support is still not globally uniform across all coins/timeframes
- the live `DEEZOH_THOUGHTS.json` in this Windows workspace is still a degraded `MARKET` bundle unless the upstream live reports for symbol-specific same-cycle work are present

## Next best follow-up

1. Expand the homepage scrape or another local scrape lane to capture:
   - top-trader account ratio
   - top-trader position ratio
   - per-symbol long/short ratio
2. Add a small history capture loop for homepage-derived OI/funding snapshots so Part 4 can be historically replayed instead of only current-state scored.
3. If live VPS access is restored, mirror and re-prove the same lane on the VPS runtime, not just locally.
