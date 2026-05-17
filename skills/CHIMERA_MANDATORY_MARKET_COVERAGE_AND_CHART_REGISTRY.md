# Chimera Mandatory Market Coverage And Chart Registry

Purpose: keep a small mandatory market board alive even when the screener changes focus, and preserve user-shared TradingView chart links as durable reference surfaces.

Important:

- TradingView shared links are human-reference boards first.
- Actual machine analysis should prefer the live TradingView chart lane, current chart studies, and fresh source reports.
- Do not treat a saved link alone as proof that Deezoh actually checked that board this cycle.

## Coverage Rule

Every meaningful Deezoh market cycle should cover:

1. Crypto majors:
   - `BTCUSDT`
   - `ETHUSDT`
   - `SOLUSDT`
2. Macro board:
   - `SPX` or `SPY`
   - `NDX` or `QQQ`
   - `DXY`
   - `gold`
   - `oil`
   - `BTC.D`
   - `USDT.D`
   - `TOTAL3`
3. Stock leaders:
   - `NVDA`
   - `AAPL`
   - `GOOGL`
   - `MSFT`
   - `AMZN`
   - `TSLA`
   - `PLTR`
   - `MSTR`
   - `COIN`
4. Screener-selected names:
   - top current long candidates
   - top current short candidates
   - watch-only names that may become next focus

The mandatory board should always exist even when the active trade focus is only one symbol.

## Priority Rule

Technical structure has the highest weight.

Default weighting:

1. technical map and zones
2. indicator interpretation by timeframe
3. derivatives / liquidation / participation routing
4. macro and catalyst alignment or restraint

Macro and catalyst should adjust or veto a technical idea.
They should not replace the technical map.

## What Deezoh Must Carry

For every mandatory symbol or promoted watchlist symbol, Deezoh should keep:

- `higher_timeframe_bias`
- `main_zones`
- `active_trade_ideas`
- `best_long_case`
- `best_short_case`
- `best_no_trade_case`
- `missing_confirmation`
- `entry_trigger_lower_tf`
- `invalidation`
- `next_best_question`

Rule:

- an `idea` is not a `trade`
- a `zone` is not a `trigger`
- a lower-timeframe trigger cannot override a broken higher-timeframe thesis

## Required Idea Ledger Shape

Each symbol should support multiple ideas at once:

- continuation long
- reset / pullback long
- reaction short
- failed-breakout or failed-breakdown reversal
- explicit no-trade

Each idea should record:

- `strategy_family`
- `timeframe_owner`
- `zone_owner`
- `thesis`
- `what_supports_it_now`
- `what_is_missing`
- `entry_trigger`
- `invalidation`
- `target_path`
- `counter_case`
- `status: watching / forming / armed / invalid / completed`

## Chart Lane Capabilities

When the direct TradingView lane is callable, it can currently help with:

- symbol and timeframe switching
- current visible study inspection
- current study input inspection
- current indicator value reads for visible studies
- chart screenshots
- Pine line / label / box / table extraction when the study exposes them

It is useful for:

- moving averages
- RSI
- MACD
- stochastic
- anchored VWAP when the chart has a real anchored VWAP study loaded
- visible range or anchored volume profile when the study exposes usable outputs
- chart-backed confirmation of support, resistance, and structure

Limits:

- arbitrary hand-drawn zones are not always machine-readable
- some custom studies only expose partial numeric output
- support / fib / POC detection is strongest when the chart already contains those studies or when a dedicated script/source report computes them

## Source Order For Zone Work

When Deezoh needs support, resistance, fib, POC, anchored VWAP, or reaction zones:

1. live TradingView chart with the real studies already loaded
2. TradingView chart screenshot plus chart-analyzer interpretation
3. dedicated source reports or scripts
4. screener snapshot only as discovery, not execution proof

## Saved TradingView Boards

These links should be preserved as durable reference boards for Deezoh and OpenClaw:

- `https://www.tradingview.com/chart/oJfoRwdK/`
- `https://www.tradingview.com/chart/81pv7c9g/`
- `https://www.tradingview.com/chart/YMJkkVnX/`
- `https://www.tradingview.com/chart/wtPsofqi/`

Registry:

```json
{
  "saved_chart_boards": [
    {
      "board_id": "user-shared-chart-1",
      "url": "https://www.tradingview.com/chart/oJfoRwdK/",
      "board_role": "user_shared_reference",
      "linked_symbol_or_scope": "confirm_in_live_tradingview_session",
      "notes": "Use as a human-reference board until live chart session confirms exact symbol and study stack."
    },
    {
      "board_id": "macro-board",
      "url": "https://www.tradingview.com/chart/81pv7c9g/",
      "board_role": "macro_reference",
      "linked_symbol_or_scope": "macro_board",
      "notes": "Known shared macro board reference. Use with live chart lane for current-direction confirmation."
    },
    {
      "board_id": "user-shared-chart-3",
      "url": "https://www.tradingview.com/chart/YMJkkVnX/",
      "board_role": "user_shared_reference",
      "linked_symbol_or_scope": "confirm_in_live_tradingview_session",
      "notes": "Use as a human-reference board until live chart session confirms exact symbol and study stack."
    },
    {
      "board_id": "user-shared-chart-4",
      "url": "https://www.tradingview.com/chart/wtPsofqi/",
      "board_role": "user_shared_reference",
      "linked_symbol_or_scope": "confirm_in_live_tradingview_session",
      "notes": "Use as a human-reference board until live chart session confirms exact symbol and study stack."
    }
  ]
}
```

## Daily Mandatory Review Loop

Every day, the desk should:

1. refresh the macro board
2. refresh `BTCUSDT`, `ETHUSDT`, and `SOLUSDT`
3. refresh stock leaders
4. compare screener-selected names against the mandatory board
5. keep a living watchlist and idea ledger
6. record what Deezoh still needs to know
7. route the next sharp question to the right specialist

## Feedback Path

If Deezoh finds a recurring logic gap, missing source, weak workflow, or bad agent behavior, it should write a feedback item to:

- `reports/auto/DEEZOH_ARCHITECT_FEEDBACK.json`

Each item should include:

- `issue`
- `symptom`
- `why_it_hurt_the_decision`
- `owner`
- `suggested_fix`
- `evidence_paths`
- `priority`

## Good Outcome

A good cycle leaves:

- one mandatory board view
- one active watchlist
- one idea ledger per focus symbol
- one explicit long vs short vs no-trade comparison
- one typed wait or next promotion
- one next best question
- one architect feedback item when the workflow itself is weak
