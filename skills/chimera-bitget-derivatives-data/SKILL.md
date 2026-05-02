---
name: chimera-bitget-derivatives-data
description: Fetch Bitget derivatives context for funding, open interest, long-short ratios, and liquidation pressure when Chimera needs venue-specific perp evidence.
metadata:
  short-description: Bitget derivatives wrapper for Chimera
---

# Chimera Bitget Derivatives Data

Use this skill when the question is about Bitget-specific derivatives context, not generic market commentary.

## Use It For

- current funding on Bitget perps
- open interest and open-interest trend checks
- long-short ratio imbalance
- liquidation pressure or squeeze risk
- venue-specific confirmation for a setup already found elsewhere
- comparing Bitget evidence against TradingView, Coinalyze, Binance futures, or AltFins

## Do Not Use It For

- placing or changing live trades
- replacing multi-source confirmation with one venue snapshot
- pretending Bitget alone proves the trade

## What This Skill Should Produce

Return the answer in this shape:

1. venue snapshot
2. what the data suggests
3. what it does not prove
4. whether it agrees or conflicts with the rest of the desk
5. what question should be asked next

## Primary Data

Preferred scripts:

- `C:\Users\becke\claudecowork\derivatives_fetcher_bitget.py`
- `C:\Users\becke\claudecowork\openclawtrading\scripts\bitget_fetcher.py`
- `C:\Users\becke\claudecowork\openclawtrading\scripts\bitget_ws_monitor.py`
- live OpenClaw mirrors under `/root/openclawtrading/scripts/`

Relevant Bitget fields:

- funding rate
- next funding time
- open interest
- long-short account ratio
- long-short position ratio
- liquidation clusters or liquidation flow if available

## Reasoning Rules

- Funding extremes are context, not entries.
- Rising open interest plus direction matters more than OI alone.
- Long-short crowding is useful mostly as contrarian risk when it gets one-sided.
- If Bitget disagrees with the broader derivatives stack, say so plainly.

## Escalation

If the task needs broader derivatives confirmation, combine this with:

- `coinalyze-derivatives`
- `derivatives`
- `tradingview-screener`
- `tradingview-mcp`

## Safe Output Reminder

The result must help Deezoh decide whether the venue data strengthens, weakens, or blocks a thesis.
It must not silently jump from data collection to trade instruction.
