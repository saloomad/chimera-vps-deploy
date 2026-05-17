---
name: chimera-data-source-router
description: Route Chimera data-source build and integration requests to the right source, owner, and next step, and explain in plain English whether the source is only an idea, built, tested, documented, integrated, or mirrored.
triggers:
  - data source
  - source router
  - integrate a source
  - build a new source
  - data integration
  - source mirror
---

# Chimera Data Source Router

Use this skill when the request is about adding, repairing, comparing, routing, or finishing a data source inside Chimera.

This skill is for deciding the right next move and the right owner path before the work turns into random file edits.

## Current Source Families

Start with this table before choosing a lane:

| Need | Best current owner | Why |
|---|---|---|
| Repeatable anchored VWAP, anchored profile, range levels, explicit Fib | local deterministic scripts | safest truth owner for math that must reproduce |
| Direct derivatives pressure: OI, funding, liquidations, long-short history | `coinalyze-derivatives` | strongest direct derivatives coverage |
| Crypto analyst layer: indicator-series, macro, sentiment, recent news | Bitget skill pack | strongest current analyst layer for crypto |
| Live TradingView chart state or Pine output already on the chart | `tradingview-jackson` on the VPS browser lane | reads the real open chart session |
| Limited-budget deep technical second opinion | `tradingview-mcp` / tvremix | useful one-shot structure and multi-timeframe opinion |

If the user wants "truth math", prefer deterministic local scripts.
If the user wants "what is the live chart showing right now", prefer Jackson.
If the user wants a second opinion, prefer tvremix.

Also prefer these first-class cached or replay owners when the question fits:

- `macro-calendar`
- `historical-market-context`
- `trading_system/scripts/news_fetcher.py`
- `trading_system/scripts/market_context_fetcher.py`
- `trading_system/scripts/economic_calendar_fetcher.py`
- `trading_system/scripts/earnings_calendar_fetcher.py`
- `trading_system/scripts/coinglass_daily_scout.py`

Do not treat every old source as equal. Some lanes are now helper-only or avoid-by-default.

## Current Live TradingView Truth

When the runtime is the live VPS OpenClaw stack:

- host: `root@100.67.172.114`
- browser-backed CDP lane: `127.0.0.1:9333`
- persistent profile: `/root/.config/google-chrome/chimera-tv-profile`
- Jackson server wrapper:
  - `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/run_tv_jackson_browser.sh`
- browser service:
  - `tradingview-browser-cdp.service`

Use this lane for:
- `quote`
- `ohlcv`
- `values`
- `data lines`

Do not confuse the live browser-backed lane with the older broken VPS Desktop lane.

## Use It For

- choosing where a new data source should live
- checking whether a source is already built somewhere else
- deciding whether the next step is build, test, document, integrate, or mirror
- routing a data-source request to the right workflow
- explaining the source state in plain English for Sal or another agent

## Do Not Use It For

- pretending a source is ready because one file exists
- skipping producer or consumer proof
- making live trading changes just because a data feed was added
- replacing a source-specific skill when a dedicated skill already exists and clearly fits better

## Source State Labels

Always describe the source with these labels:

- `idea only`
- `built`
- `tested`
- `documented`
- `integrated`
- `mirrored`
- `blocked`

Do not collapse those states into one vague `done` claim.

## What To Check First

1. What data does the user actually need?
2. Which Chimera consumer needs it?
3. Is there already:
   - a source-specific script
   - a source-specific skill
   - a shared workflow
   - a live repo mirror
4. Which path is the real owner?
5. What is the smallest next safe step?

## Current Deterministic Truth Owners

If the request is about any of these, route to local scripts first:

- market structure
- anchored VWAP
- anchored or fixed-range volume profile
- Monday range
- day range
- week range
- explicit-anchor Fibonacci

Current local owner files:

- `trading_system/scripts/indicators/market_structure.py`
- `trading_system/scripts/indicators/anchored_vwap.py`
- `trading_system/scripts/indicators/anchored_volume_profile.py`
- `trading_system/scripts/indicators/range_levels.py`
- `trading_system/scripts/indicators/fibonacci_calculator.py`
- `trading_system/scripts/indicators/fvg_detector.py`
- `trading_system/scripts/indicators/order_block_detector.py`

## Keep / Demote / Avoid rule

### Keep as first-class owners

- deterministic local indicator scripts
- `coinalyze-derivatives` and `derivatives`
- Bitget skill pack
- `tradingview-jackson` on the VPS browser lane
- `tradingview-mcp` / tvremix
- `macro-calendar`
- `historical-market-context`
- `trading_system/scripts/news_fetcher.py`
- `trading_system/scripts/market_context_fetcher.py`
- `trading_system/scripts/economic_calendar_fetcher.py`
- `trading_system/scripts/earnings_calendar_fetcher.py`
- `trading_system/scripts/coinglass_daily_scout.py`

### Demote to helper or fallback

- `tradingview-screener`
- `news-reader`
- `altfins`
- `chimera-bitget-derivatives-data`
- `trading_system/scripts/coinglass_maxpain_scraper.py`
- `trading_system/scripts/liquidation_heatmap.py`
- `trading_system/scripts/data/ccxt_fetcher.py`
- `trading_system/scripts/data/tradingview_api.py`

### Avoid as current owners unless intentionally repaired

- `earnings-calendar` as a separate lane
- `coingecko_narratives_fetcher.py`
- `trading_system/scripts/data/coinglass_scraper.py`
- `trading_system/scripts/data/liquidation_fetcher.py`
- `trading_system/scripts/data/tradingview_explorer.py`
- `trading_system/scripts/data/tv_simple_test.py`
- `trading_system/scripts/data/test_scraper.py`

If a request matches a demoted lane and a stronger first-class owner exists, route to the stronger owner first and explain why.

## Routing Rule

If the request is about doing the full source lifecycle, route through:

- `workflows/codex/data-source-build-integration-and-mirror-loop.md`

Shared repo mirror of the same contract:

- `chimera-vps-deploy/docs/CHIMERA_DATA_SOURCE_BUILD_AND_INTEGRATION_LOOP_2026-05-05.md`

If the request is mainly about a specific existing source, prefer the source-specific skill first.

If the request is mainly about live runtime wiring, also check:

- `openclaw-feature-router`
- `platform-update-promoter`

## Answer Shape

Return the result in this order:

1. source request in plain English
2. current source state
3. chosen owner path
4. next workflow or skill to use
5. what proof is still missing
6. next safe action

## Proof Rule

Do not treat a source as done because:

- one file exists
- one config entry exists
- one mirror copy exists

Separate these states:

- built
- tested
- documented
- integrated
- mirrored
- blocked

If the request is about OpenClaw runtime use, proof should also separate:

- file exists
- runtime load path exists
- config wired
- real live call worked

## Update Rule

Whenever a new data source or source family becomes important, update all of:

- this skill
- the shared platform catalog under `research/platforms/`
- the wiki source note
- the shared mirror under `chimera-vps-deploy/skills/`
- the live runtime copy if OpenClaw should use it

When source-pruning decisions change, also update:

- `research/platforms/2026-05-05-data-source-keep-demote-avoid-decisions.md`
- shared continuity under `shared_ai_context/`

Do not leave the source knowledge only in chat.

## Final Rule

Do not call a source complete until it is:

- tested
- documented
- integrated
- mirrored when the mirror matters
