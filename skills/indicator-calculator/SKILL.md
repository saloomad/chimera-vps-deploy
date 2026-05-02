---
name: indicator-calculator
description: Calculate 24+ technical indicators (RSI, MACD, Bollinger Bands, ADX, Stochastic, CCI, Williams %R, OBV, ATR, moving averages) for any cryptocurrency. Use when user asks to calculate indicators, check RSI, analyze MACD, or get technical analysis metrics for a coin.
---

# Indicator Calculator Skill

## Purpose
Calculates 24+ technical indicators on historical price data using the `calculator.py` module.

## When to Use
- User asks: "Calculate RSI for BTC"
- User asks: "What are the indicators for ETH?"
- User asks: "Check MACD on SOL"
- User asks: "Give me technical analysis for this coin"
- User asks: "Is it overbought?" (needs RSI)
- User asks: "Show me the moving averages"

## Indicators Calculated
**Oscillators:**
- RSI (Relative Strength Index)
- Stochastic
- CCI (Commodity Channel Index)
- Williams %R

**Trend:**
- MACD (Moving Average Convergence Divergence)
- ADX (Average Directional Index)
- SMA (Simple Moving Averages: 20, 50, 200)
- EMA (Exponential Moving Averages: 20, 50, 200)

**Volatility:**
- Bollinger Bands (upper, middle, lower)
- ATR (Average True Range)

**Volume:**
- OBV (On-Balance Volume)
- Volume SMA

## How to Use

```python
from trading_system.scripts.indicators.calculator import calculate_all_indicators
import pandas as pd

# Get data first (user should provide symbol)
symbol = "BTC/USDT"  # From user input
timeframe = "1h"     # Default to 1h

# Fetch OHLCV data
from trading_system.scripts.data.ccxt_fetcher import fetch_ohlcv
df = fetch_ohlcv(symbol, timeframe, limit=200)

# Calculate all indicators
indicators = calculate_all_indicators(df)

# Format output
print(f"\n📊 Indicators for {symbol} ({timeframe})")
print(f"RSI: {indicators['rsi']:.2f}")
print(f"MACD: {indicators['macd']:.4f} | Signal: {indicators['macd_signal']:.4f}")
print(f"ADX: {indicators['adx']:.2f}")
print(f"Bollinger Bands: Upper {indicators['bb_upper']:.2f} | Lower {indicators['bb_lower']:.2f}")
```

## Output Format
Returns dictionary with all indicators (values from most recent candle).

## Notes
- Requires minimum 200 candles for accurate calculations
- Uses pandas-ta library under the hood
- All indicators return float values (or NaN if insufficient data)
