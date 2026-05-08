# CHECKPOINT — 2026-05-05 — VPS Jackson truth and deterministic indicator foundation

## What landed

- Proved the VPS TradingView Jackson lane works through the browser-backed persistent profile.
- Confirmed the old broken lane was the VPS Desktop app path, not Jackson itself.
- Added deterministic local indicator foundations for:
  - anchored VWAP
  - Monday/day/week ranges
  - anchored volume profile
  - explicit-anchor Fibonacci

## Live proof

Host:
- `root@100.67.172.114`

TradingView browser lane:
- service: `tradingview-browser-cdp.service`
- CDP port: `127.0.0.1:9333`
- persistent profile: `/root/.config/google-chrome/chimera-tv-profile`

Verified working in this pass:
- `/json/list` showed real TradingView page targets
- Jackson `quote` returned live BTC data
- Jackson `ohlcv --summary` returned live chart bars
- Jackson `values` returned live study values
- Jackson `data lines` returned line-based study output

## Code touched

- `trading_system/scripts/indicators/anchored_vwap.py`
- `trading_system/scripts/indicators/range_levels.py`
- `trading_system/scripts/indicators/create_anchored_volume_profile.py`
- `trading_system/scripts/indicators/fibonacci_calculator.py`

## Practical owner split

Use local scripts as truth for:
- anchored VWAP
- anchored / fixed-range volume profile
- Monday/day/week range levels
- explicit Fib

Use Jackson on the VPS browser lane for:
- reading the live TradingView chart
- reading study values and line output already on the chart

Use tvremix for:
- secondary opinion
- batch helper work
- not as the only truth owner

## Open work

- add a cleaner alias/wrapper if we want `anchored_volume_profile.py` naming
- build the real market-structure engine next
- rewrite FVG next
- rewrite order blocks next
- collapse duplicated divergence paths into one secondary detector
