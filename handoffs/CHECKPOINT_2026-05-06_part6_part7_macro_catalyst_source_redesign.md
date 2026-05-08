# Part 6 / Part 7 Macro-Catalyst Source Redesign Checkpoint

Date: 2026-05-06
Owner: Codex
Scope: redo the macro/catalyst boundary from actual Deezoh decision needs and real available source lanes

## What changed

- rebuilt `Part 6: Macro And Cross-Asset` around:
  - event timing
  - rates / yields
  - cross-asset relationship context
  - current directional state when available
  - crypto-internal breadth and dominance
  - broad earnings-week helper context
- clarified that `Part 6` is recommendation-based, not lock-based
- clarified that:
  - economic calendar belongs primarily in `Part 6`
  - earnings belong mainly in `Part 7`
  - broad earnings-week context can still help `Part 6` for index-sensitive setups
- added the missing distinction between:
  - relationship context
  - current directional state

- updated:
  - `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
  - `agents/macro-bias/AGENTS.md`
  - `agents/macro-bias/TOOLS.md`
  - `agents/news-monitor/AGENTS.md`
  - `agents/news-monitor/TOOLS.md`
  - `research/platforms/2026-05-05-macro-and-cross-asset-source-matrix.md`
  - `research/platforms/2026-05-05-btc-part6-deezoh-example.md`
  - `research/platforms/2026-05-05-part6-macro-deezoh-simulation-and-improvement.md`
  - `research/platforms/2026-05-05-news-and-catalysts-source-matrix.md`

- corrected skill truth for:
  - `macro-calendar`
  - `earnings-calendar`
  in both local Codex and shared mirror copies
- added a proved public TradingView macro board workflow note:
  - `research/platforms/2026-05-06-tradingview-macro-board-workflow.md`
- tightened the section contract so labels are no longer enough by themselves:
  - `macro_recommendation_explanation`
  - `deezoh_context_now`
  - `plain_english_macro_take`
  - `what_this_means_for_btc`
  - `what_this_means_for_alts`

## Best current source stack for Part 6

1. `ECONOMIC_CALENDAR.json`
2. `mcp__market_data__.rates_yields`
3. `mcp__market_data__.cross_asset`
4. `mcp__market_data__.crypto_market` global
5. `MARKET_CONTEXT.json`
6. TradingView chart confirmation when alive
7. `tradfi_news(earnings)` helper context
8. `news_feed` helper context
9. `MACRO_BIAS.json` compatibility / workflow lane
10. `CROSS_ASSET.json` helper only

## Best current source stack for Part 7

1. `CATALYST_REPORT.json`
2. `NEWS.json`
3. persistent catalyst bundle files
4. `tradfi_news(earnings)` when earnings matter
5. `EARNINGS_CALENDAR.json` only when it is present and fresh
6. `ECONOMIC_CALENDAR.json` only when a macro event is acting like a live catalyst headline

## Important live proof from this run

- live VPS report freshness:
  - `ECONOMIC_CALENDAR.json` fresh
  - `NEWS.json` fresh
  - `MACRO_BIAS.json` fresh
  - `CROSS_ASSET.json` fresh
  - `CATALYST_REPORT.json` fresh
  - `EARNINGS_CALENDAR.json` missing
- live `CROSS_ASSET.json` is still too thin:
  - `equities`, `dollar`, `volatility`, and `commodities` were empty
- live `MACRO_BIAS.json` still had blank new recommendation fields in this run:
  - `macro_recommendation_state`
  - `how_deezoh_should_use_macro_now`
  - `recommendation_weight`
- direct tool proof:
  - `rates_yields` worked
  - `cross_asset` worked
  - `crypto_market global` worked
  - `tradfi_news(earnings)` worked
  - `news_feed` worked
- public web TradingView board proof:
  - `https://www.tradingview.com/chart/81pv7c9g/` loaded through the browser lane
  - proved visible board members included:
    - `CRYPTOCAP:OTHERS`
    - `BINANCE:BTCUSDT.P`
    - `CRYPTOCAP:USDT.D`
    - `BITGET:PAXGUSDT.P`
    - `NSE:OIL1!`
    - `BLACKBULL:US500.F`
    - `TVC:DXY`
- local Windows TradingView Desktop lane was not available because TradingView Desktop is not installed on this machine

## Mirrors and sync

- synced to live VPS:
  - bundle template
  - macro-bias agent docs
  - news-monitor agent docs
  - macro/catalyst source notes
  - BTC Part 6 example
  - Part 6 simulation note
  - shared `macro-calendar` skill
  - shared `earnings-calendar` skill

- mirrored local skill truth to:
  - `C:\Users\becke\.claude\skills`
  - `C:\Users\becke\.openclaw\skills` where the skill existed

## Remaining gaps

1. direct current directional state for `SPX`, `DXY`, `gold`, and `oil` still needs a reliable live chart or equivalent direct lane
2. `MACRO_BIAS.json` producer still needs to populate the newer recommendation fields instead of leaving them blank
3. live `EARNINGS_CALENDAR.json` is still missing, so direct earnings tools remain the better owner today
4. the public TradingView macro board is proved as a visual lane, but not yet as a fully automated recurring multi-timeframe extractor

## Best next follow-up

1. promote or repair one live chart-based current-direction lane for:
   - `SPX`
   - `DXY`
   - `gold`
   - `oil`
   - `BTC.D`
   - `USDT.D`
   - `TOTAL3`
2. decide whether to patch the live macro producer so `MACRO_BIAS.json` emits the new recommendation fields directly
3. turn the public TradingView board into a recurring 4-hour multi-timeframe macro-board sweep if the browser/chart automation lane is promoted
4. run a full Deezoh consumption test that uses the rebuilt Part 6 plus the existing Part 7 boundary
