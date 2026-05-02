---
name: historical-market-context
description: Build point-in-time historical market bundles for crypto trading tests. Use when the task needs previous price data across multiple timeframes in parallel, indicators at a historical cutoff, optional derivatives context, optional recent historical news/catalyst context, or a reusable bundle for strategy backtests and pipeline simulations.
---

# Historical Market Context

Use this skill when the job is to build the historical truth bundle first.

That means:
- previous price candles
- multiple timeframes at once
- indicators at that exact time
- optional derivatives context
- optional recent news/catalyst context
- optional economic-calendar snapshot context when a matching archive exists

## What This Skill Is For

This is the shared data layer.

It is for:
1. strategy backtests
2. pipeline simulations
3. Deezoh reasoning replays
4. A/B tests between two implementations
5. checking whether instruction or enforcement changes actually improved decisions

## Important Distinction

- `backtesting` means testing a trading rule or strategy on historical data and scoring the outcome
- `simulation` means replaying a broader system behavior over time, including questions, routing, and decisions

Backtesting is one kind of simulation, but simulation is broader.

## Modes

Read [references/MODES.md](references/MODES.md) when choosing the mode.

Fast rule:
- use `bundle` for one historical checkpoint
- use `range` for a sequence of checkpoints
- include news only when catalyst context matters
- include economic only when you have a truthful archived snapshot close to that anchor

## Main Script

Use:

`C:\Users\becke\claudecowork\trading_system\scripts\labs\historical_market_context_lab.py`

## Common Commands

Single bundle:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\historical_market_context_lab.py `
  --mode bundle `
  --symbol BTC/USDT `
  --anchor 2026-04-20T12:00:00Z `
  --timeframes "15m,1h,4h,1d" `
  --limit 400 `
  --include-derivatives
```

Range of checkpoints:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\historical_market_context_lab.py `
  --mode range `
  --symbol ETH/USDT `
  --start 2026-04-18T00:00:00Z `
  --end 2026-04-20T00:00:00Z `
  --step 4h `
  --timeframes "15m,1h,4h,1d"
```

Recent catalyst context:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\historical_market_context_lab.py `
  --mode bundle `
  --symbol BTC/USDT `
  --anchor 2026-04-20T12:00:00Z `
  --timeframes "1h,4h,1d" `
  --include-news `
  --catalyst-lookback-hours 24
```

If you are using PowerShell, quote comma-separated lists like `"1h,4h,1d"`.

## Rules

1. Do not invent historical news or calendar context.
2. If the provider cannot truthfully supply the requested historical depth, say that plainly in the output.
3. Keep the bundle as data, not judgment.
4. Use this bundle as the source of truth for later strategy or pipeline tests.
5. Prefer the fastest truthful mode first, then deepen only when needed.
