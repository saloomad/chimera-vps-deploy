---
name: chimera-tradingview-indicators
description: Use TradingView-backed indicator checks for RSI, MACD, Bollinger Bands, moving averages, and simple pattern confirmation inside Chimera.
metadata:
  short-description: TradingView indicator wrapper for Chimera
---

# Chimera TradingView Indicators

Use this skill when Chimera needs a focused indicator read from TradingView-backed sources.

## Use It For

- RSI state and momentum checks
- MACD crossover and histogram context
- Bollinger Band squeeze or expansion checks
- moving-average alignment
- fast indicator confirmation on a symbol and timeframe
- technical confluence against derivatives, catalysts, or macro context

## Do Not Use It For

- pretending one indicator is enough to take a trade
- replacing multi-timeframe structure analysis
- claiming TradingView indicator output is the same as a full chart review

## Best Source Order

1. `tradingview-mcp` when direct TradingView tooling is callable
2. `tradingview-screener` when a daily snapshot is enough
3. local or live scripts when the MCP is unavailable:
   - `C:\Users\becke\claudecowork\trading_system\scripts\data\tradingview_api.py`
   - `/root/openclawtrading/scripts/data/tradingview_api.py`

## What To Return

Return the result in this shape:

1. symbol and timeframe
2. indicator snapshot
3. what the indicators imply
4. what the indicators do not settle
5. whether they agree with the larger thesis
6. better next question

## Reasoning Rules

- RSI alone is not a signal.
- MACD crossovers matter more when they align with structure and volume.
- A squeeze is a volatility condition, not a directional verdict.
- Moving-average alignment is permission context, not timing by itself.
- Higher timeframe permission beats lower timeframe excitement.

## Escalation

If the question needs more than indicator values, combine this with:

- `tradingview-mcp`
- `historical-market-context`
- `strategy-backtest-lab`
- `chimera-bitget-derivatives-data`
- `coinalyze-derivatives`

## Safe Output Reminder

The skill should help Deezoh challenge or refine a thesis.
It must not become a one-indicator yes-man.
