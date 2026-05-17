---
name: tradingview-mcp
description: "Route TradingView work to the right lane: direct TradingView MCP when callable, TradingView screener for daily snapshots, or the synced TradingView helper script when MCP access is unavailable."
metadata:
  short-description: TradingView routing wrapper for Chimera
---

# TradingView MCP

Use this skill when the request is about TradingView-backed chart work, indicators, screening, or multi-timeframe technical confirmation.

## Route Selection

Use these lanes in order:

1. direct TradingView MCP or Jackson route when the runtime exposes it
2. `tradingview-screener` when a daily snapshot is enough
3. `chimera-tradingview-indicators` for indicator-focused checks
4. the synced helper script when MCP is not callable:
   - `C:\Users\becke\claudecowork\trading_system\scripts\data\tradingview_api.py`
   - `/root/openclawtrading/scripts/data/tradingview_api.py`

## Use It For

- chart-backed symbol review
- indicator confirmation
- daily screener snapshots
- multi-timeframe sanity checks
- validating whether a trade thesis matches the chart
- confirming the public macro board `https://www.tradingview.com/chart/81pv7c9g/` for Section 6 context

## Do Not Use It For

- treating the screener as historical proof
- acting like one TradingView snapshot settles execution risk
- hiding whether the runtime used MCP, screener, or script fallback

## Output Contract

The answer should say:

1. which TradingView lane actually ran
2. timeframe and symbol
3. what the chart or indicators support
4. what remains unproven
5. the better next question

For the macro board, prefer:

1. `1W`
2. `1D`
3. `4H`
4. `1H`

and explain what each lane means for:

- BTC quality versus alt breadth
- SPX risk appetite
- DXY pressure
- gold or oil defensiveness
- USDT.D and OTHERS/TOTAL3 participation

## Important Limits

- `tradingview-screener` is daily snapshot only.
- If direct TradingView MCP is not callable in the current runtime, say that plainly.
- Higher timeframe permission still beats lower timeframe excitement.

## Best Companions

- `chimera-bitget-derivatives-data`
- `coinalyze-derivatives`
- `derivatives`
- `historical-market-context`
- `strategy-backtest-lab`
