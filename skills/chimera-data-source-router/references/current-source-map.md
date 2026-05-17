# Current Source Map

Use this note when `chimera-data-source-router` needs the current best owner path.

## Source families

### 1. Deterministic local level math

Best owner for:
- market structure
- anchored VWAP
- anchored or fixed-range volume profile
- Monday/day/week ranges
- explicit-anchor Fibonacci
- first-pass local FVG and order-block structure

Owner files:
- `trading_system/scripts/indicators/market_structure.py`
- `trading_system/scripts/indicators/anchored_vwap.py`
- `trading_system/scripts/indicators/anchored_volume_profile.py`
- `trading_system/scripts/indicators/range_levels.py`
- `trading_system/scripts/indicators/fibonacci_calculator.py`
- `trading_system/scripts/indicators/fvg_detector.py`
- `trading_system/scripts/indicators/order_block_detector.py`

Why:
- same output every run for the same candles
- easiest to test and compare
- safest truth owner for level math

### 2. TradingView live chart lane

Best owner for:
- what the live chart is showing
- study values
- line output from indicators on the chart

Live VPS truth:
- host: `root@100.67.172.114`
- CDP lane: `127.0.0.1:9333`
- persistent profile: `/root/.config/google-chrome/chimera-tv-profile`
- Jackson wrapper:
  - `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/run_tv_jackson_browser.sh`
- browser service:
  - `tradingview-browser-cdp.service`

Best commands:
- `quote`
- `ohlcv`
- `values`
- `data lines`

Why:
- reads the actual live TradingView chart
- good for confirming that layouts and Pine outputs match expectations

### 3. Bitget skill pack

Best owner for:
- crypto analyst-layer context
- indicator series
- macro context
- sentiment context
- recent-news context

Main skills:
- `technical-analysis`
- `sentiment-analyst`
- `macro-analyst`
- `market-intel`
- `news-briefing`

Why:
- strongest current crypto analyst layer
- not the main owner for deterministic desk-state files

### 4. Coinalyze

Best owner for:
- open interest
- funding
- predicted funding
- liquidations
- long-short history

Why:
- strongest direct derivatives source currently in Chimera

### 5. tvremix

Best owner for:
- limited-budget deep technical second opinion
- multi-timeframe one-shot reads
- SMC-style structure checks
- ranking and correlation helpers

Why:
- good second opinion lane
- not the best always-on truth owner

### 6. Cached context owners that still stay first-class

Best owner for:
- cached news file
- cached macro-event timing
- cached earnings-risk timing
- cached cross-asset regime snapshot
- CoinGlass max-pain magnets and category narratives
- historical replay bundles

Owner files and skills:
- `trading_system/scripts/news_fetcher.py`
- `trading_system/scripts/economic_calendar_fetcher.py`
- `trading_system/scripts/earnings_calendar_fetcher.py`
- `trading_system/scripts/market_context_fetcher.py`
- `trading_system/scripts/coinglass_daily_scout.py`
- `historical-market-context`
- `macro-calendar`

Why:
- these still provide saved desk files or replay truth that the new indicator math does not replace

## Demoted lanes

Use only as helper, fallback, or narrow confirmation:

- `tradingview-screener`
- `news-reader`
- `altfins`
- `chimera-bitget-derivatives-data`
- `trading_system/scripts/coinglass_maxpain_scraper.py`
- `trading_system/scripts/liquidation_heatmap.py`
- `trading_system/scripts/data/ccxt_fetcher.py`
- `trading_system/scripts/data/tradingview_api.py`

Why:
- still useful in narrow cases
- no longer good default owners

## Avoid as current owners

Do not route to these by default unless they are intentionally being repaired:

- `earnings-calendar` as a separate skill lane
- `coingecko_narratives_fetcher.py`
- `trading_system/scripts/data/coinglass_scraper.py`
- `trading_system/scripts/data/liquidation_fetcher.py`
- `trading_system/scripts/data/tradingview_explorer.py`
- `trading_system/scripts/data/tv_simple_test.py`
- `trading_system/scripts/data/test_scraper.py`

Why:
- redundant, stale-path, prototype-grade, or smoke-test-only
