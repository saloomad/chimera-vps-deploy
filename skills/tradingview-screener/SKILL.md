---
name: tradingview-screener
description: Find trading opportunities using TradingView's screener API. Screens 59,000+ cryptocurrencies by current indicators (RSI, MACD, ADX, moving averages, etc.), identifies top gainers/losers, strong buy signals, and high-volume movers. Use when user wants to find trading opportunities, screen for coins meeting specific criteria, or identify top performers. IMPORTANT - Only provides CURRENT snapshot data on DAILY timeframe, NOT historical data or multiple timeframes.
---

# TradingView Screener Skill

## Purpose

This skill uses TradingView's public screener API to find trading opportunities across 59,663+ cryptocurrencies. It provides **current snapshot data** with all major technical indicators, making it ideal for opportunity discovery and initial screening.

## When to Use This Skill

Use this skill when you need to:
- ✅ Find top gainers/losers in the market
- ✅ Screen coins by current indicators (RSI, MACD, ADX, etc.)
- ✅ Identify strong buy/sell signals
- ✅ Filter by volume, recommendation score, or technical criteria
- ✅ Get current prices and indicator values for quality coins

## When NOT to Use This Skill

Do NOT use this skill for:
- ❌ Historical data analysis (only provides current snapshot)
- ❌ Multiple timeframes (1m, 5m, 15m, 1h, 4h) - only DAILY timeframe
- ❌ Chart generation (no OHLCV candles)
- ❌ Divergence detection (needs historical swings)
- ❌ Backtesting (needs historical candles)

**For historical analysis:** Use CCXT library with exchange APIs (Binance, Bybit) instead.

---

## Available Indicators

The TradingView screener provides 40+ technical indicators on the **DAILY timeframe**:

### Oscillators
- **RSI** - Relative Strength Index (current)
- **RSI[1]** - Previous RSI (1 bar ago)
- **Stoch.K, Stoch.D** - Stochastic oscillator
- **CCI20** - Commodity Channel Index
- **W.R** - Williams %R
- **Mom** - Momentum
- **MACD.macd, MACD.signal** - MACD line and signal

### Trend Indicators
- **ADX, ADX+DI, ADX-DI** - Average Directional Index
- **SMA5, SMA10, SMA20, SMA50, SMA100, SMA200** - Simple Moving Averages
- **EMA5, EMA10, EMA20, EMA50, EMA100, EMA200** - Exponential Moving Averages

### Volatility
- **BB.upper, BB.lower** - Bollinger Bands
- **ATR** - Average True Range
- **Volatility.D** - Daily volatility

### Price & Volume
- **close, open, high, low** - OHLC (current candle)
- **volume** - Current volume
- **change, change_abs** - Percentage and absolute change
- **average_volume_10d_calc, average_volume_30d_calc** - Average volumes

### Recommendations
- **Recommend.All** - Overall recommendation (-1 to 1, where 1 = strong buy)
- **Recommend.MA** - Moving average recommendation
- **Recommend.Other** - Oscillator recommendation

### Performance Metrics
- **Perf.W** - 1 week % change
- **Perf.1M** - 1 month % change
- **Perf.3M, Perf.6M, Perf.Y** - Longer-term performance

---

## Usage Instructions

### Step 1: Import the TradingView API

The API client is located at:
```
/sessions/sweet-lucid-fermi/mnt/claudecowork/trading_system/scripts/data/tradingview_api.py
```

### Step 2: Quick Start - Pre-built Functions

Use the pre-built functions for common tasks:

```python
from trading_system.scripts.data.tradingview_api import TradingViewAPI

tv = TradingViewAPI()

# Top 10 gainers
gainers = tv.get_top_gainers(limit=10)

# Top 10 by volume
volume_leaders = tv.get_top_volume(limit=10)

# Strong buy signals (Recommend.All > 0.5)
strong_buys = tv.get_strong_buy_signals(limit=10)
```

### Step 3: Custom Screening with Filters

For advanced screening, use the `scan_crypto()` method with custom filters:

```python
# Example: Find coins with bullish setup
results = tv.scan_crypto(
    columns=[
        "name", "close", "volume", "change",
        "RSI", "MACD.macd", "ADX", "Recommend.All"
    ],
    filters=[
        {"left": "volume", "operation": "greater", "right": 5000000},  # >$5M volume
        {"left": "RSI", "operation": "greater", "right": 30},  # Not oversold
        {"left": "RSI", "operation": "less", "right": 70},     # Not overbought
        {"left": "Recommend.All", "operation": "greater", "right": 0.5}  # Strong buy
    ],
    sort_by="Recommend.All",
    sort_order="desc",
    limit=20
)
```

### Step 4: Filter Operators

Available filter operators:
- `"greater"` - Greater than (>)
- `"less"` - Less than (<)
- `"equal"` - Equal to (=)
- `"not_equal"` - Not equal (!=)
- `"greater_or_equal"` - Greater than or equal (>=)
- `"less_or_equal"` - Less than or equal (<=)
- `"match"` - Contains string (for exchange filtering)
- `"nempty"` - Not empty (field has value)

---

## Quality Filtering Best Practices

**Problem:** TradingView returns 59,663 coins, including many low-quality shitcoins with fake volume.

**Solution:** Always apply quality filters:

```python
quality_filters = [
    # Minimum volume (liquid coins only)
    {"left": "volume", "operation": "greater", "right": 5000000},  # >$5M

    # Minimum price (avoid dust tokens)
    {"left": "close", "operation": "greater", "right": 0.01},  # >$0.01

    # Exchange filter (trusted exchanges only)
    {"left": "name", "operation": "match", "right": "BINANCE"}  # Binance only
]
```

### Recommended Exchange Filters

Filter by trusted exchanges to avoid garbage:
- `"BINANCE"` - Binance (most liquid)
- `"BYBIT"` - Bybit
- `"COINBASE"` - Coinbase
- `"KRAKEN"` - Kraken

---

## Common Screening Strategies

### Strategy 1: Oversold Bounce Setup
```python
oversold_bounce = tv.scan_crypto(
    filters=[
        {"left": "volume", "operation": "greater", "right": 5000000},
        {"left": "RSI", "operation": "less", "right": 35},  # Oversold
        {"left": "MACD.macd", "operation": "greater", "right": 0},  # MACD turning up
        {"left": "Recommend.All", "operation": "greater", "right": 0.3}  # Bullish bias
    ],
    sort_by="RSI",
    limit=10
)
```

### Strategy 2: Breakout Candidates
```python
breakout_candidates = tv.scan_crypto(
    filters=[
        {"left": "volume", "operation": "greater", "right": 10000000},  # High volume
        {"left": "change", "operation": "greater", "right": 5},  # Up >5% today
        {"left": "ADX", "operation": "greater", "right": 25},  # Strong trend
        {"left": "RSI", "operation": "less", "right": 75}  # Not overbought yet
    ],
    sort_by="change",
    sort_order="desc",
    limit=10
)
```

### Strategy 3: Mean Reversion Setup
```python
mean_reversion = tv.scan_crypto(
    filters=[
        {"left": "volume", "operation": "greater", "right": 5000000},
        {"left": "close", "operation": "less", "right": "SMA20"},  # Price below 20 SMA
        {"left": "RSI", "operation": "less", "right": 40},  # Oversold
        {"left": "Recommend.All", "operation": "greater", "right": 0}  # Overall bullish
    ],
    sort_by="RSI",
    limit=10
)
```

Note: For field-to-field comparisons (like `close < SMA20`), you need to fetch both values and compare in Python.

---

## Integration with Trading System

### Where This Skill Fits

This skill is used by the **Scout Agent** in Project Chimera's trading system:

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: OPPORTUNITY DISCOVERY (TradingView Skill)     │
└─────────────────────────────────────────────────────────┘
                          │
                          ↓
              Scout Agent (Heartbeat 30 min)
                          │
                 Polls TradingView API
                          │
         Finds: Top gainers, strong signals, volume spikes
                          │
                          ↓
         Returns: 10-20 high-potential opportunities
                          │
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: DEEP ANALYSIS (CCXT + pandas-ta)              │
└─────────────────────────────────────────────────────────┘
                          │
                          ↓
              Analyst Agent (Extended Thinking)
                          │
           Pulls historical data via CCXT
                          │
      Calculates: Divergence, confluence, regime
                          │
                          ↓
         If confluence > 70% → Send to Executor
                          │
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: EXECUTION (CCXT Exchange API)                 │
└─────────────────────────────────────────────────────────┘
```

### Limitations in Context

**What TradingView Provides:**
- Initial screening (reduces 59,663 coins → 20 opportunities)
- Current indicator values (for quick assessment)
- Real-time recommendations (momentum/trend signals)

**What TradingView CANNOT Provide:**
- Historical analysis (need CCXT for this)
- Multiple timeframes (need CCXT for this)
- Divergence detection (need CCXT + pandas-ta)
- Precise entry/exit timing (need CCXT for this)

**Therefore:**
- Use TradingView for **discovery** (finding opportunities)
- Use CCXT for **analysis** (deep dive on selected coins)
- Use CCXT for **execution** (actual trading)

---

## Error Handling

### Common Issues

**Issue 1: No results returned**
```python
result = tv.scan_crypto(filters=[...])
if not result.get('data'):
    # Filters too restrictive - loosen criteria
    # Or check if API is down
```

**Issue 2: Timeout errors**
```python
try:
    result = tv.scan_crypto(...)
except requests.exceptions.Timeout:
    # API is slow - retry or skip this scan
```

**Issue 3: None values in indicators**
```python
# Some coins don't have all indicators
rsi = coin.get('rsi')
if rsi is None:
    # Skip this coin or use default value
```

---

## Performance Notes

- **API Speed:** ~500ms per request (fast)
- **Rate Limits:** No rate limits on public screener API
- **Recommended frequency:** Every 30 minutes (Scout Agent heartbeat)
- **Token cost:** ~100 tokens (metadata) + ~5K tokens (when triggered)

---

## Example Output

```python
[
    {
        'symbol': 'BINANCE:BTCUSDT',
        'price': 96234.50,
        'volume': 45234567890.0,
        'change_pct': 2.34,
        'recommendation': 0.72,
        'rsi': 58.2,
        'macd': 1234.5,
        'adx': 32.1
    },
    {
        'symbol': 'BINANCE:ETHUSDT',
        'price': 3456.78,
        'volume': 23456789012.0,
        'change_pct': 1.89,
        'recommendation': 0.65,
        'rsi': 55.4,
        'macd': 45.6,
        'adx': 28.9
    }
]
```

---

## Related Files

- **API Implementation:** `/sessions/sweet-lucid-fermi/mnt/claudecowork/trading_system/scripts/data/tradingview_api.py`
- **Comprehensive Test:** `/sessions/sweet-lucid-fermi/mnt/claudecowork/trading_system/scripts/data/tradingview_explorer.py`
- **Capabilities Doc:** `/sessions/sweet-lucid-fermi/mnt/claudecowork/trading_system/docs/TRADINGVIEW_API_CAPABILITIES.md`

---

## Summary

✅ **Best for:** Opportunity discovery, initial screening, current signals
❌ **Not for:** Historical analysis, backtesting, divergence, multiple timeframes
💡 **Use with:** CCXT (for deep analysis) + pandas-ta (for custom indicators)
⏱️ **Frequency:** Every 30 minutes (Scout Agent)
💰 **Cost:** Free, no API key needed
