---
name: strategy-backtest-lab
description: Run professional-style historical strategy testing for Chimera using multi-timeframe matrices, walk-forward checks, regime context, and A/B comparisons. Use when the task is to test strategy logic on previous price data, compare indicator combinations, compare timeframes, or validate whether a strategy change improved edge.
---

# Strategy Backtest Lab

Use this skill for strategy testing only.

This is for:
- which strategy had edge
- which timeframe worked better
- which regime it worked in
- whether a change improved the strategy

## Not The Same As Pipeline Simulation

This skill tests trading logic.

It does **not** prove that Deezoh or the whole desk asked the right questions.
For that, use `pipeline-simulation-lab`.

## Main Script

`C:\Users\becke\claudecowork\trading_system\scripts\labs\strategy_backtest_lab.py`

## Modes

Read [references/MODES.md](references/MODES.md) when selecting how deep to go.

## Common Commands

Quick matrix:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\strategy_backtest_lab.py `
  --strategies all `
  --symbols "BTC/USDT,ETH/USDT" `
  --timeframes "1h,4h,1d" `
  --top-n 10
```

A/B on selected strategies:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\strategy_backtest_lab.py `
  --strategies "stoch_rsi_bounce,ema_ichimoku_rsi,bb_squeeze" `
  --symbols "BTC/USDT,SOL/USDT" `
  --timeframes "1h,4h"
```

If you are using PowerShell, quote comma-separated lists.

## Rules

1. Always report symbol, timeframe, matching regimes, full-period result, and walk-forward result.
2. Do not call a strategy strong just because the full-history result looks good.
3. Give more weight to unseen-data and walk-forward behavior.
4. Keep strategy testing separate from desk-process testing.
