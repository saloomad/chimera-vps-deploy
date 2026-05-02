---
name: tradingview-mcp-hermes
description: Hermes Lead Agent -- TradingView MCP routing for trade execution. Use tvremix for pre-trade analysis (SMC, multi-TF confluence, screener, fundamentals) and tradingview-jackson for chart confirmation, screenshots, and alert setup. Every tvremix call counts against the 15/day limit -- batch aggressively. Use rank_symbol_setups instead of individual quotes. Use analyze_smc_tool for entry zones. Use analyze_multi_timeframe for directional bias. Never waste tvremix on what jackson can do.triggers:
  - hermes tradingview
  - trade setup analysis
  - entry zone
  - SMC trade
  - order block entry
  - FVG entry
  - liquidity sweep
  - pre-trade check
  - chart confirmation
  - alert setup
  - trade validation
  - setup quality
---

# Hermes TradingView MCP Skill

*For the Hermes Lead Agent -- trade execution focused*

---

## Hermes Decision Flow

```
PRE-TRADE ANALYSIS (tvremix -- budget: 3-4 calls per setup)
  1. Directional bias     -> analyze_multi_timeframe(symbol)
  2. Market structure     -> analyze_smc_tool(symbol, interval, count=300)
  3. [optional] Fundamentals -> get_financials(symbol) + get_forecasts(symbol)
  4. [optional] Correlation  -> calculate_correlation_tool(holdings + candidate)

CHART CONFIRMATION (tradingview-jackson -- unlimited)
  5. Load chart           -> chart_set_symbol(symbol)
  6. Add indicators       -> chart_manage_indicator(add RSI/MACD/Volume)
  7. Read values          -> data_get_study_values
  8. Screenshot           -> capture_screenshot (for trade journal)

EXECUTION
  9. Set alert            -> alert_create (entry zone from SMC analysis)
  10. [optional] Options   -> get_option_chain (if options strategy)

POST-TRADE MONITORING (tvremix -- budget: 2-3 calls daily)
  11. News check          -> get_news(symbol)
  12. Portfolio update    -> get_portfolio
```

---

## Pre-Trade Analysis -- The 4-Call Setup

Hermes should spend **at most 4 tvremix calls** analyzing a trade before deciding. Here's the optimal sequence:

### Call 1: Directional Bias
```bash
mcporter call tvremix.analyze_multi_timeframe --json '{"symbol": "BINANCE:BTCUSDT", "timeframes": ["15m","1h","4h","1D","1W"]}'
```
**What to extract:**
- `confluence.alignment` -- "fully_bullish", "mixed", "fully_bearish"
- `confluence.bullish_count` / `bearish_count` / `neutral_count`
- Per-TF `rating.summary` -- Buy/Sell/Neutral
- Per-TF `oscillators.rsi` -- overbought (>70) / oversold (<30)
- Per-TF `moving_averages` -- price vs EMA20/50

**Decision gate:** If alignment is "mixed" or against your directional bias, STOP. No trade.

### Call 2: Market Structure (SMC)
```bash
mcporter call tvremix.analyze_smc_tool --json '{"symbol": "BINANCE:BTCUSDT", "interval": "4h", "count": 300}'
```
**What to extract:**
- `bias.direction` + `bias.confidence` + `bias.reasoning`
- `market_structure.trend` -- bullish/bearish
- `order_blocks[]` -- untested OBs near price (mitigated=false)
- `fair_value_gaps[]` -- unfilled FVGs (fill_pct < 1.0)
- `key_levels[]` -- strong_low, strong_high, equilibrium
- `premium_discount.zone` -- premium (favor shorts) / discount (favor longs)

**Decision gate:** If bias.direction conflicts with your intended direction, STOP.

### Call 3: Setup Ranking (if comparing multiple candidates)
```bash
mcporter call tvremix.rank_symbol_setups --json '{"symbols": ["BTCUSDT","ETHUSDT","SOLUSDT"], "focus": "momentum", "top_n": 3, "side": "long"}'
```
**What to extract:**
- Top N symbols with score, signal, reason
- Pick the highest-scoring candidate that aligns with your bias

### Call 4: Fundamentals (stocks only)
```bash
mcporter call tvremix.get_financials --json '{"symbol": "NASDAQ:AAPL"}'
mcporter call tvremix.get_forecasts --json '{"symbol": "NASDAQ:AAPL"}'
```
**What to extract:**
- P/E ratio vs sector average
- Revenue growth trend
- Analyst rating distribution (buy/hold/sell)
- Price target vs current price

**Decision gate:** If fundamentals are deteriorating or analyst consensus is "sell", reduce size or skip.

---

## Entry Zone Construction from SMC Data

Given `analyze_smc_tool` output, construct entry zones:

### For LONG entries:
1. **Premium discount zone** = "discount_zone" or "equilibrium"?
2. **Nearest untested bullish OB** (mitigated=false) -- use the low of the OB as entry
3. **Nearest unfilled bullish FVG** (fill_pct < 1.0) -- use the bottom of the FVG as entry
4. **Strong_low** -- use as stop loss
5. **Equal low (EQL)** below price -- target for liquidity sweep entry

### For SHORT entries:
1. **Premium discount zone** = "premium_zone"?
2. **Nearest untested bearish OB** (mitigated=false) -- use the high of the OB as entry
3. **Nearest unfilled bearish FVG** (fill_pct < 1.0) -- use the top of the FVG as entry
4. **Weak_high / strong_high** -- use as stop loss
5. **Equal high (EQH)** above price -- target for liquidity sweep entry

### Risk:Reward Calculation
```
Entry = OB low (long) or OB high (short)
Stop = strong_low - 1 ATR (long) or strong_high + 1 ATR (short)
Target = recent swing high (long) or recent swing low (short)
R:R = (Target - Entry) / (Entry - Stop)
```
**Hermes rule:** Minimum 2:1 R:R. If SMC-derived R:R < 2, skip the trade.

---

## Chart Confirmation Checklist (tradingview-jackson)

After tvremix analysis, confirm on chart BEFORE entering:

```bash
# 1. Load symbol
mcporter call tradingview-jackson.chart_set_symbol --symbol BINANCE:BTCUSDT

# 2. Set timeframe to match SMC analysis
mcporter call tradingview-jackson.chart_set_timeframe --resolution 240

# 3. Add key indicators
mcporter call 'tradingview-jackson.chart_manage_indicator(action: "add", indicator: "RSI")'
mcporter call 'tradingview-jackson.chart_manage_indicator(action: "add", indicator: "MACD")'
mcporter call 'tradingview-jackson.chart_manage_indicator(action: "add", indicator: "Volume")'

# 4. Read values
mcporter call tradingview-jackson.data_get_study_values

# 5. Screenshot for journal
mcporter call tradingview-jackson.capture_screenshot
```

**Confirmation checklist:**
- [ ] Price is near SMC-derived entry zone (within 2%)
- [ ] RSI on chart confirms tvremix reading (within 5 points)
- [ ] MACD direction aligns with intended trade direction
- [ ] Volume supports the move (above 20-period average)
- [ ] Screenshot captured for trade journal

---

## Alert Setup (tradingview-jackson)

Use SMC-derived levels for alerts:

```bash
# Entry zone alert
mcporter call tradingview-jackson.alert_create --json '{
  "condition": "crossing",
  "symbol": "BINANCE:BTCUSDT",
  "price": 74235,
  "message": "BTC at bullish OB entry zone"
}'

# Stop loss alert
mcporter call tradingview-jackson.alert_create --json '{
  "condition": "crossing",
  "symbol": "BINANCE:BTCUSDT",
  "price": 73309,
  "message": "BTC stop loss hit"
}'

# Target alert
mcporter call tradingview-jackson.alert_create --json '{
  "condition": "crossing",
  "symbol": "BINANCE:BTCUSDT",
  "price": 79472,
  "message": "BTC target reached"
}'
```

---

## Post-Trade Monitoring (tvremix -- 2 calls/day)

### Daily check (2 calls)
```bash
# 1. News scan for all holdings
mcporter call tvremix.get_news --json '{"symbol": "BTCUSDT", "limit": 5}'

# 2. Portfolio status
mcporter call tvremix.get_portfolio
```

### If news contains negative catalyst:
- Re-run `analyze_multi_timeframe` for affected holding (1 call)
- If confluence turns bearish, consider early exit

---

## tvremix Call Budget Per Trade

| Phase | Calls | Tools |
|-------|-------|-------|
| Pre-trade analysis | 2-4 | analyze_multi_timeframe, analyze_smc_tool, [rank_symbol_setups], [get_financials] |
| Chart confirmation | 0 | tradingview-jackson only |
| Execution | 0-1 | [get_option_chain] |
| Post-trade monitoring | 2/day | get_news, get_portfolio |
| **Total per setup** | **2-5** | |

**With 15 calls/day:** Hermes can analyze 3-7 setups per day + daily monitoring.
**With 30 calls/day (backup key):** 6-15 setups per day + monitoring.

---

## Anti-Patterns (DO NOT DO)

1. **DON'T** call `get_quote` then `get_technicals` separately -- use `get_full_technicals`
2. **DON'T** call `get_technicals` for multiple TFs -- use `analyze_multi_timeframe`
3. **DON'T** manually scan for OBs/FVGs -- use `analyze_smc_tool`
4. **DON'T** check each watchlist symbol individually -- use `rank_symbol_setups`
5. **DON'T** use tvremix for chart screenshots -- use tradingview-jackson.capture_screenshot
6. **DON'T** use tvremix for alerts -- use tradingview-jackson.alert_create
7. **DON'T** call `get_ohlcv` with full bars if you only need summary -- set `summary=true`

---

*Hermes TradingView MCP Skill -- v1.0 | 2026-04-26*
