---
name: tvremix-prompt-guide
description: How to craft one-shot tvremix prompts that maximize data per call. tvremix has a 15 request/day limit -- every prompt must be designed to get everything needed in a single call. This guide shows compound tool usage, batching strategies, and example prompts for common trading workflows.
triggers:
  - tvremix prompt
  - one shot prompt
  - tvremix guide
  - prompt strategy
  - batch tvremix
  - compound call
---

# tvremix One-Shot Prompt Guide

*Maximize every call. 15/day = 15 chances to get it right.*

---

## The Golden Rule

**One compound tool call > multiple atomic tool calls**

| Workflow | Bad (N calls) | Good (1 call) | Savings |
|----------|--------------|---------------|---------|
| Check BTC bias | get_quote + get_technicals(1D) + get_technicals(4h) + get_technicals(1h) | analyze_multi_timeframe | 3 calls |
| Analyze structure | Manual OB scan + FVG scan + BOS check + liquidity check | analyze_smc_tool | 3+ calls |
| Compare ETH vs SOL | get_quote(ETH) + get_quote(SOL) + get_technicals(ETH) + get_technicals(SOL) | compare_symbols_tool | 3 calls |
| Watchlist scan | get_quote(BTC) + get_quote(ETH) + get_quote(SOL) + ... | rank_symbol_setups | N-1 calls |
| Full stock DD | get_quote + get_technicals + get_financials + get_forecasts | compare_symbols_tool or custom script | 3 calls |

---

## Compound Tool Reference

### `analyze_multi_timeframe` -- The Bias Call
**Replaces:** `get_quote` + `get_technicals` x 5 timeframes

**Returns:** Price + OHLC + volume + RSI + Stoch + CCI + ADX + AO + Momentum + MACD + EMA10/20/50 + SMA50/100/200 + Bollinger Bands + ATR + 52-week range + market cap -- for EACH timeframe + confluence score.

**Best for:** Determining directional bias before ANY trade.

**Example prompt:**
```bash
mcporter call tvremix.analyze_multi_timeframe --json '{
  "symbol": "BINANCE:BTCUSDT",
  "timeframes": ["15m","1h","4h","1D","1W"]
}'
```

**What to look for:**
- `confluence.alignment` = "fully_bullish" or "fully_bearish" = strong directional signal
- Mixed alignment = stay out or reduce size
- Weekly RSI > 70 = overbought on higher TF = caution on longs
- 4h MACD crossing above signal = momentum building

---

### `analyze_smc_tool` -- The Structure Call
**Replaces:** Manual OB detection + FVG detection + BOS/CHoCH identification + liquidity mapping + bias assessment

**Returns:** Swing points (HH/HL/LL/LH), market structure events, order blocks (with mitigated status), fair value gaps (with fill percentage), equal levels, strong/weak highs/lows, premium/discount zone, equilibrium, bias direction + confidence + reasoning, consolidated key levels.

**Best for:** Finding precise entry zones, stops, and targets.

**Example prompt:**
```bash
mcporter call tvremix.analyze_smc_tool --json '{
  "symbol": "BINANCE:BTCUSDT",
  "interval": "4h",
  "count": 300,
  "swing_lookback": 5
}'
```

**What to look for:**
- Untested bullish OBs (mitigated=false) = long entry zones
- Unfilled FVGs (fill_pct < 1.0) = price magnets
- BOS in direction of trade = structure confirmation
- CHoCH against trade direction = warning sign
- Premium zone + bullish bias = consider waiting for discount retest
- EQL below price = liquidity target for longs

---

### `rank_symbol_setups` -- The Batch Call
**Replaces:** Individual get_quote + get_technicals for N symbols

**Returns:** Ranked list with price, change, volume, RSI, MACD, rating, signal, and reason for EACH symbol.

**Best for:** Scanning a watchlist to find the best setup.

**Example prompt:**
```bash
mcporter call tvremix.rank_symbol_setups --json '{
  "symbols": ["BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","DOGEUSDT"],
  "focus": "momentum",
  "side": "long",
  "top_n": 3,
  "exclude_earnings_within_days": 2
}'
```

**Focus profiles:**
- `balanced` -- general setup quality
- `momentum` -- strong directional moves, best for trending markets
- `mean_reversion` -- oversold bounces, best for ranging markets
- `breakout` -- range breaks, best for consolidation exits

---

### `compare_symbols_tool` -- The Side-by-Side Call
**Replaces:** Multiple individual symbol queries

**Returns:** Price, fundamentals, and technicals for multiple symbols with per-metric rankings.

**Best for:** Choosing between 2-5 candidates.

**Example prompt:**
```bash
mcporter call tvremix.compare_symbols_tool --json '{
  "symbols": ["BTCUSDT","ETHUSDT"],
  "metrics": ["price","change","volume","rsi","macd","market_cap","pe_ratio"]
}'
```

---

### `get_full_technicals` -- The Comprehensive Single-Symbol Call
**Replaces:** get_quote + get_technicals

**Returns:** Price, OHLC, volume, RSI, MACD (macd/signal/hist), Stochastic K/D, CCI, ADX, AO, Momentum, EMA10/20/50, SMA50/100/200, Bollinger Bands, ATR, 52-week high/low, market cap, volume/market_cap ratio.

**Best for:** When you need EVERYTHING for one symbol and don't need multi-TF.

**Example prompt:**
```bash
mcporter call tvremix.get_full_technicals --json '{
  "symbol": "BINANCE:BTCUSDT"
}'
```

---

### `calculate_correlation_tool` -- The Portfolio Call
**Replaces:** Manual correlation analysis

**Returns:** NxN Pearson correlation matrix from REAL OHLCV bars + top 5 most correlated pairs.

**Best for:** Portfolio diversification check, pairs trading setup.

**Example prompt:**
```bash
mcporter call tvremix.calculate_correlation_tool --json '{
  "symbols": ["BTCUSDT","ETHUSDT","SOLUSDT","SPY","QQQ"],
  "period": 30,
  "interval": "1D"
}'
```

---

## Workflow Prompts

### Workflow 1: Complete Trade Setup (2 calls)

**Call 1 -- Directional Bias + Structure:**
```bash
mcporter call tvremix.analyze_multi_timeframe --json '{"symbol": "BINANCE:BTCUSDT", "timeframes": ["1h","4h","1D","1W"]}'
```

**Call 2 -- Entry Zone:**
```bash
mcporter call tvremix.analyze_smc_tool --json '{"symbol": "BINANCE:BTCUSDT", "interval": "4h", "count": 300}'
```

**Then use tradingview-jackson for:**
- Chart load + screenshot
- Alert setup at SMC-derived levels

**Total tvremix calls: 2**

---

### Workflow 2: Watchlist Scan + Best Pick (1-2 calls)

**Call 1 -- Rank all candidates:**
```bash
mcporter call tvremix.rank_symbol_setups --json '{
  "symbols": ["BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","ADAUSDT","AVAXUSDT","LINKUSDT"],
  "focus": "breakout",
  "top_n": 3
}'
```

**Call 2 -- Deep dive on winner (optional):**
```bash
mcporter call tvremix.analyze_smc_tool --json '{
  "symbol": "BINANCE:ETHUSDT",
  "interval": "4h",
  "count": 300
}'
```

**Total tvremix calls: 1-2**

---

### Workflow 3: Stock Due Diligence (2-3 calls)

**Call 1 -- Fundamentals + Forecasts:**
```bash
mcporter call tvremix.get_financials --json '{"symbol": "NASDAQ:AAPL"}'
mcporter call tvremix.get_forecasts --json '{"symbol": "NASDAQ:AAPL"}'
```

**Call 2 -- Technicals + Structure:**
```bash
mcporter call tvremix.get_full_technicals --json '{"symbol": "NASDAQ:AAPL"}'
mcporter call tvremix.analyze_swing_tool --json '{"symbol": "NASDAQ:AAPL", "interval": "1D", "count": 300}'
```

**Call 3 -- News + Filings (optional):**
```bash
mcporter call tvremix.get_news --json '{"symbol": "AAPL", "limit": 5}'
mcporter call tvremix.get_documents --json '{"symbol": "AAPL", "limit": 5}'
```

**Total tvremix calls: 2-6 (use judgment)**

---

### Workflow 4: Macro Risk Check (1 call)

```bash
mcporter call tvremix.get_economic_calendar --json '{
  "days_ahead": 7,
  "importance": ["high", "medium"],
  "countries": ["United States", "Euro Area"]
}'
```

**Total tvremix calls: 1**

---

### Workflow 5: Sector Rotation (1-2 calls)

**Call 1 -- Scan sector:**
```bash
mcporter call tvremix.analyze_sector_tool --json '{
  "sector_name": "Technology",
  "metric": "perf_1m",
  "limit": 20
}'
```

**Call 2 -- Compare top 3 (optional):**
```bash
mcporter call tvremix.compare_symbols_tool --json '{
  "symbols": ["AAPL","MSFT","NVDA"],
  "metrics": ["price","rsi","pe_ratio","market_cap"]
}'
```

**Total tvremix calls: 1-2**

---

## Prompt Anti-Patterns

### DON'T: Chain small calls
```bash
# WASTE -- 4 calls
get_quote BTC
get_technicals BTC 1D
get_technicals BTC 4h
get_ohlcv BTC 4h

# BETTER -- 1 call
analyze_multi_timeframe BTC
```

### DON'T: Analyze symbols one by one
```bash
# WASTE -- 6 calls
analyze_smc_tool BTC
analyze_smc_tool ETH
analyze_smc_tool SOL

# BETTER -- 1-2 calls
rank_symbol_setups [BTC,ETH,SOL]  # 1 call
# Then deep-dive only the winner   # +1 call
```

### DON'T: Use get_ohlcv with full bars when summary suffices
```bash
# WASTE -- returns 5000 bars you won't read
get_ohlcv BTC 1D count=5000

# BETTER
get_ohlcv BTC 1D count=300 summary=true  # Only returns stats
```

### DON'T: Call get_quote for price checks when doing analysis
```bash
# WASTE -- get_quote only returns price
get_quote BTC  # 1 call wasted

# BETTER -- get_full_technicals includes price + everything else
get_full_technicals BTC  # 1 call, 20x more data
```

---

## Call Budget Planning

### Daily Budget: 15 Calls

| Activity | Calls | Tools |
|----------|-------|-------|
| Morning macro check | 1 | get_economic_calendar |
| BTC bias scan | 1 | analyze_multi_timeframe |
| BTC structure | 1 | analyze_smc_tool |
| Watchlist ranking | 1 | rank_symbol_setups |
| Top 2-3 deep dives | 2-3 | analyze_smc_tool each |
| News scan | 1 | get_news |
| Portfolio check | 1 | get_portfolio |
| **Total** | **8-9** | **7-8 setups analyzed** |

### With Backup Key: 30 Calls
Double everything -- 14-18 setups analyzed per day.

---

## Symbol Format Reference

| Market | Prefix | Example |
|--------|--------|---------|
| Crypto (Binance) | `BINANCE:` | `BINANCE:BTCUSDT` |
| US Stocks | `NASDAQ:` or `NYSE:` | `NASDAQ:AAPL`, `NYSE:JPM` |
| Forex | `FX:` | `FX:EURUSD` |
| Futures | `CME:` or `COMEX:` | `CME:ES1!` |

**Always use the exchange prefix** -- tvremix resolves symbols faster and more accurately with prefixes.

---

## Response Parsing Quick Reference

### analyze_multi_timeframe
```python
alignment = data["confluence"]["alignment"]  # "fully_bullish", "mixed", "fully_bearish"
bullish_count = data["confluence"]["bullish_count"]
for tf, vals in data["timeframes"].items():
    rsi = vals["oscillators"]["rsi"]
    macd = vals["oscillators"]["macd"]
    signal = vals["oscillators"]["macd_signal"]
    rating = vals["rating"]["summary"]  # "Buy", "Sell", "Neutral"
```

### analyze_smc_tool
```python
bias = data["bias"]["direction"]           # "bullish" or "bearish"
confidence = data["bias"]["confidence"]    # "high", "medium", "low"
reasoning = data["bias"]["reasoning"]

# Untested bullish order blocks (entry zones)
untested_obs = [ob for ob in data["order_blocks"]
                if ob["bias"] == "bullish" and not ob["mitigated"]]

# Unfilled FVGs (price magnets)
unfilled_fvgs = [fvg for fvg in data["fair_value_gaps"]
                 if fvg["fill_pct"] < 1.0]

# Key levels
for level in data["key_levels"]:
    if level["type"] == "strong_low":
        stop_loss = level["price"]
```

### rank_symbol_setups
```python
for item in data["ranked"]:
    symbol = item["symbol"]
    score = item["score"]
    signal = item["signal"]      # "strong_buy", "buy", "neutral", etc.
    reason = item["reason"]
```

---

*tvremix One-Shot Prompt Guide -- v1.0 | 2026-04-26*
*Tested with live BTCUSDT data*
