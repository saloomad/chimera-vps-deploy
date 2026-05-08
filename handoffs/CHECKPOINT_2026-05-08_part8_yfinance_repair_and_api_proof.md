# CHECKPOINT - 2026-05-08 Part 8 YFinance Repair And API Proof

## What changed

- repaired the earlier Part 8 shortcut where `yfinance` was removed instead of fixed
- found the real VPS root cause:
  - `/root/.pip/pip.conf` pointed at a dead Aliyun mirror
- fixed the live VPS pip config to use:
  - `https://pypi.org/simple`
- installed `yfinance` on the VPS and proved import success
- updated:
  - `scripts/cross_market_leadership_snapshot.py`
- added:
  - `scripts/tests/cross_market_leadership_snapshot_smoke.py`
- updated durable source notes:
  - `research/platforms/2026-05-05-structural-market-intel-source-matrix.md`
  - `research/platforms/2026-05-06-part8-leadership-news-earnings-and-flow-helper-audit.md`
  - `research/platforms/2026-05-08-part8-yfinance-repair-and-api-proof.md`
- updated agent source guidance:
  - `agents/market-intel/TOOLS.md`

## Script behavior now

For `scripts/cross_market_leadership_snapshot.py`:

- stocks and commodities:
  - `yfinance` preferred
  - direct Yahoo chart fallback if `yfinance` is unavailable or fails
- crypto:
  - CoinGecko markets endpoint

The output now exposes:

- `source_strategy`
- `source_summary.symbol_source_map`
- `source_summary.fallback_reasons`
- `source_summary.failed_symbols`

## Proof

### Local Windows

- `python scripts/tests/cross_market_leadership_snapshot_smoke.py`
  - result: `ok=true`
- `python scripts/cross_market_leadership_snapshot.py`
  - wrote:
    - `reports/auto/CROSS_MARKET_LEADERSHIP_SNAPSHOT.json`
- stock sources:
  - `yfinance`
- commodity sources:
  - `yfinance`
- stock fallbacks:
  - `0`
- commodity fallbacks:
  - `0`

### Live VPS

- `python3 /root/openclawtrading/scripts/tests/cross_market_leadership_snapshot_smoke.py`
  - result: `ok=true`
- `python3 /root/openclawtrading/scripts/cross_market_leadership_snapshot.py`
  - wrote:
    - `/root/openclawtrading/reports/auto/CROSS_MARKET_LEADERSHIP_SNAPSHOT.json`
- `python3 -m pip show yfinance`
  - version: `1.3.0`
- stock sources:
  - `yfinance`
- commodity sources:
  - `yfinance`
- stock fallbacks:
  - `0`
- commodity fallbacks:
  - `0`

### Cross-check probes

`yfinance` matched direct Yahoo closes on both local and VPS for:

- `NVDA`
- `AMD`
- `GC=F`
- `CL=F`

Additional tested working helper lanes in this pass:

- `mcp__market_data__.crypto_market(action="markets")`
- `mcp__market_data__.global_assets(action="ohlcv")`
- `mcp__market_data__.tradfi_news(action="earnings")`
- `mcp__market_data__.derivatives_sentiment(action="top_position")`

## Git status note

- current repo branch before publish:
  - `add-remaining-files`
- this is still branch-strategy drift from the preferred `main` rule
- if this bounded fix is pushed on the current branch, GitHub visibility on `main` is still not satisfied yet

## Still open

- publish the bounded fix set cleanly to GitHub
- decide later whether `main` should get this directly or whether the current branch drift should be cleaned first
