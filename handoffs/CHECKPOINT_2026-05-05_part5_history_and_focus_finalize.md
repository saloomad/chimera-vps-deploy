# Part 5, History, And Focused Deezoh Finalize Checkpoint

Date: 2026-05-05
Owner: Codex
Scope: finish the remaining derivatives/liquidity follow-up after the first proof slice

## What changed

- tightened `parallel_part5_liquidation_heat_map.md`
  - now matches the real local truth:
    - exact structured heatmap proof is currently strongest on `BTC 24h`
    - `ETH 24h` is currently locked/unavailable in the unauthenticated exact route
    - `SOL 24h` currently fails to render the chart in the unauthenticated exact route
  - now separates:
    - `exact_heatmap_structured`
    - `screenshot_only_needs_vision`
    - `derivatives_proxy_only`

- strengthened `scripts/market-maker/run_liquidation_scans.py`
  - exact-run success now means actual `exact_heatmap_extracted`, not just subprocess exit `0`
  - this removed the false `OK exact ETH/SOL` console result

- strengthened `trading_system/scripts/coinglass_homepage_scraper.py`
  - now appends:
    - `trading_system/data/HOMEPAGE_DERIVATIVES_HISTORY.jsonl`
  - now writes:
    - `trading_system/data/HOMEPAGE_DERIVATIVES_LATEST.json`
    - `trading_system/data/HOMEPAGE_DERIVATIVES_REPLAY.json`
  - this is the new small snapshot-history lane for future replay/backtest work

- strengthened `scripts/build_deezoh_thoughts.py`
  - now exposes the new history/replay files in source metadata
  - now writes:
    - `reports/auto/DEEZOH_THOUGHTS_FOCUS/INDEX.json`
    - `reports/auto/DEEZOH_THOUGHTS_FOCUS/BTC_DEEZOH_THOUGHTS.json`
    - `reports/auto/DEEZOH_THOUGHTS_FOCUS/ETH_DEEZOH_THOUGHTS.json`
    - `reports/auto/DEEZOH_THOUGHTS_FOCUS/SOL_DEEZOH_THOUGHTS.json`
  - this is the focused live path so `MARKET` mode does not hide symbol-specific derivatives/liquidity truth

## Fresh proof

Passed:
- `python trading_system/scripts/coinglass_homepage_scraper.py`
- `python scripts/market-maker/run_liquidation_scans.py`
- `python scripts/build_deezoh_thoughts.py`
- `python scripts/tests/deezoh_derivatives_context_smoke.py`
- `python scripts/tests/liquidation_summary_contract_smoke.py`

## Current truth

- exact structured heatmap:
  - `BTC 24h` -> works
  - `ETH 24h` -> `timeframe_locked_or_unavailable`
  - `SOL 24h` -> `chart_not_rendered`
- exact max-pain browser scrape:
  - working
- focused bundle precision:
  - `BTCUSDT -> exact_both`
  - `ETHUSDT -> exact_maxpain_only`
  - `SOLUSDT -> exact_maxpain_only`
- history/replay lane:
  - wired and writing files
  - fresh replay only has one snapshot so transition counts are still empty today

## Remaining gaps

- stable per-symbol top-trader ratios are still not present in the local homepage-derived file-backed lane
- stable taker-ratio history is still not present in the local homepage-derived file-backed lane
- real historical replay quality will improve only after more scheduled homepage snapshots accumulate
