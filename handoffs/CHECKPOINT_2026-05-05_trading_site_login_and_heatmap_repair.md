## Objective

Repair the real browser-backed trading-site login and liquidation heatmap capture path across Windows Codex and the live Kimi VPS, then prove which routes now work and what still remains partial.

## What changed

### Shared login/env layer

Added or updated:

- `C:\Users\becke\claudecowork\trading_system\scripts\browser_auth.py`
- `C:\Users\becke\claudecowork\trading_system\config\trading_site_login.env.template`

What it now does:

- loads `.env.trading_sites`
- supports site-specific credentials for:
  - TradingView
  - CoinGlass
  - CoinAnk
- saves browser session state under:
  - `trading_system/data/browser_state/`
- uses a less bot-like Playwright context
- returns clearer failure reasons:
  - missing credentials
  - rejected credentials
  - changed login flow

### Liquidation heatmap capture

Updated:

- `C:\Users\becke\claudecowork\trading_system\scripts\liquidation_heatmap.py`
- `C:\Users\becke\claudecowork\scripts\market-maker\run_liquidation_scans.py`
- `C:\Users\becke\claudecowork\trading_system\scripts\coinglass_heatmap_exact.py`

Main fixes:

- CoinGlass now uses the real heatmap page:
  - `https://www.coinglass.com/pro/futures/LiquidationHeatMap`
- CoinGlass login no longer relies on the dead `/login` route
- timeframe selection is label-based instead of “second combobox”
- screenshot validation is stricter than old “file exists” logic
- screenshot capture uses longer time budgets on the VPS
- the exact 24h extractor now uses the same repaired CoinGlass browser path
- the exact extractor no longer throws away a usable screenshot just because the direct chart element crop was missing
- the exact extractor in `run_liquidation_scans.py` now runs serially so the VPS does not timeout on parallel OCR/browser jobs

### TradingView browser reuse

Updated:

- `C:\Users\becke\claudecowork\trading_system\scripts\chart_viewer.py`

Main fixes:

- TradingView Playwright fallback now uses the shared login/state helper
- the VPS chart route now uses a lighter page-load gate and succeeds where the old route timed out

## Secret/env placement

Local secret file used:

- `C:\Users\becke\claudecowork\.env.trading_sites`

Mirrored to live VPS:

- `/root/openclawtrading/.env.trading_sites`
- `/root/.openclaw/workspace/.env.trading_sites`

Permissions hardened on VPS:

- `chmod 600` on both env files

## Proof

### Local Windows proof

Confirmed:

- CoinGlass heatmap screenshots succeed for:
  - `BTC 24h`
  - `BTC 1w`
  - `ETH 24h`
  - `ETH 1w`
- CoinAnk login attempt reaches the live login endpoint and returns a credential-rejected state with the current credentials
- TradingView Playwright fallback succeeds locally for:
  - `BTCUSDT 4h`

### Live VPS proof

Confirmed:

- TradingView Playwright fallback succeeds on VPS for:
  - `BTCUSDT 4h`
- CoinGlass heatmap screenshots succeed on VPS for:
  - `BTC 24h`
  - `BTC 1w`
  - `ETH 24h`
  - `ETH 1w`
- CoinAnk screenshots now succeed on VPS for:
  - `BTC`
  - `ETH`
  - `SOL`
- Full VPS liquidation summary run completes and writes:
  - `/root/openclawtrading/reports/auto/LIQUIDATION_SUMMARY.json`

Current live summary truth after the repaired run:

- `BTC`
  - `24h`: exact heatmap extracted
  - `1w`: screenshot available, proxy downstream
- `ETH`
  - `24h`: screenshot available, exact extraction still blocked by CoinGlass window/API response path
  - `1w`: screenshot available, proxy downstream
- `SOL`
  - `24h`: exact heatmap extracted
  - `1w`: screenshot available, proxy downstream
- `HYPE`
  - unsupported by the maintained screenshotter, still proxy/no direct browser capture

## What still remains partial

1. `ETH 24h` exact CoinGlass extraction is still not landing on the VPS.
   - browser screenshot path is working
   - exact downstream extraction still returns:
     - `timeframe_locked_or_unavailable`

2. Old legacy screenshot keys still appear in some logs:
   - `coinglass_maxpain`
   - `coinank`
   These are older leftovers and should not be treated as the new owner path.

3. `HYPE` is still unsupported by the maintained screenshotter.

## Recommended next slice

1. tighten `coinglass_heatmap_exact.py` for the `ETH 24h` route specifically
2. clean legacy screenshot-key drift out of `HEATMAP_LOG.json` consumers
3. if HYPE matters, extend the maintained screenshotter with a proven source path instead of pretending it is already covered
