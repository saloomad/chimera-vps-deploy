---
name: altfins
description: >
  Fetch live technical analysis data from AltFins API — RSI, MACD, EMA trends,
  support/resistance levels, candlestick patterns, and trend scores for BTC/ETH/SOL.
  Use when Sal asks: "altfins data", "get indicators from altfins", "check trend scores",
  "altfins screener", "RSI from altfins", "EMA trend", "support levels", "resistance levels",
  "candlestick patterns altfins", "altfins BTC", "altfins check", "run altfins".
  Runs altfins_fetcher.py, reads ALTFINS.json, formats output.
---

# ALTFINS SKILL

## Purpose
Pull pre-computed technical analysis from AltFins API for BTC, ETH, SOL.
AltFins does the heavy lifting — calculates 150+ indicators server-side, we just fetch the result.
Covers: RSI, MACD, ADX, Stochastic, EMA/SMA trends, support/resistance, candlestick patterns, trend direction scores.

## API Details
- **Base URL**: `https://altfins.com`
- **Key 1**: `afns_sk_132936.OgJzjX2Qr4V5AiDbn_qQ80-BotC0-Ef_2yHbb4dPOgE` — 1,000 credits/month
- **Key 2**: `afns_sk_137148.OU_GyBEf1D31F4TBlP6uuuuHP3aprrPXRg6ruIdko_M` — 1,000 credits/month
- **Total**: 2,000 credits/month (~500 full runs combined)
- **Rotation**: Auto — on 402 credit exhausted, restarts full fetch with next key
- **State**: `trading_system/config/altfins_key_state.json`
- **Rate Limit**: 30 req/min per key
- **Plan**: Basic (Free) × 2
- **Script**: `trading_system/scripts/altfins_fetcher.py`
- **Output**: `reports/auto/ALTFINS.json`

## Key Endpoint
```
POST https://altfins.com/api/v2/public/screener-data/search-requests
Body: { "symbols": ["BTC"], "timeInterval": "DAILY", "displayType": [...] }
```

## Available displayType Fields
**Momentum:** RSI14, RSI9, RSI25, MACD, ADX, STOCH, STOCH_SLOW, STOCH_RSI, CCI20,
BULL_POWER, BEAR_POWER, ULTIMATE_OSCILLATOR, WILLIAMS, MOM

**Trend:** SHORT_TERM_TREND, MEDIUM_TERM_TREND, LONG_TERM_TREND (format: "Strong Down (0/10)")
SHORT_TERM_TREND_CHANGE, MEDIUM_TERM_TREND_CHANGE, LONG_TERM_TREND_CHANGE
EMA50, EMA100, EMA200, EMA50_TREND, EMA100_TREND, EMA200_TREND
SMA50, SMA100, SMA200, SMA50_TREND, SMA100_TREND, SMA200_TREND
OBV_TREND, VWMA20

**Crossovers (X_ prefix):** X_MACD_CROSS_MACD_SIGNAL_LINE, X_RSI14_CROSS_30/50/70,
X_EMA50_CROSS_EMA200 (golden/death cross), X_ADX_CROSS_20/40, etc.

**Candlestick Patterns (CD_ prefix):** CD_HAMMER, CD_DOJI, CD_ENGULFING_BULLISH/BEARISH,
CD_MORNING_STAR, CD_EVENING_STAR, CD_THREE_WHITE_SOLDIERS, CD_THREE_BLACK_CROWS, etc.

**Levels:** SUPPORT (nested: SUPPORT_1, SUPPORT_2, SUPPORT_3)
RESISTANCE (nested: RESISTANCE_1, RESISTANCE_2, RESISTANCE_3)
ATR, ATH, ATH_PERCENT_DOWN, HIGH_52W, LOW_52W

**Price:** PRICE_CHANGE_1D, PRICE_CHANGE_1W, PRICE_CHANGE_1M, PERFORMANCE, VOLUME

## Timeframes
MINUTES15, HOURLY, HOURS4, HOURS12, DAILY

## How to Run
```python
# In Shell:
C:/Users/becke/AppData/Local/Programs/Python/Python313/python.exe trading_system/scripts/altfins_fetcher.py

# Or read cached data:
import json
with open("reports/auto/ALTFINS.json") as f:
    data = json.load(f)
btc = data["screener"]["BTC"]["DAILY"]
```

## Output Format
```json
{
  "_fetched_at": "2026-02-21 15:00 UTC",
  "screener": {
    "BTC": {
      "DAILY": {
        "price": "68543.44",
        "RSI14": "38.869",
        "MACD": "-3,980.93",
        "ADX": "58.032",
        "SHORT_TERM_TREND": "Strong Down (2/10)",
        "SUPPORT": {"SUPPORT_1": "84,447.08"},
        "RESISTANCE": {"RESISTANCE_1": "97,937.44"}
      },
      "HOURS4": { ... }
    }
  }
}
```

## Instructions

When Sal asks for AltFins data:
1. Run altfins_fetcher.py via Shell (or read ALTFINS.json if fresh < 30 min)
2. Extract DAILY data for requested symbols
3. Format output as a clean summary table — do NOT dump raw JSON
4. Highlight signals: oversold RSI (<30), strong trend direction, golden/death cross detected

### Output Format to Show Sal
```
=== ALTFINS — [DATE] ===

BTC  $68,543 | RSI14: 38.9 [NEAR OVERSOLD] | MACD: -3,981 | ADX: 58 [STRONG TREND]
     Trend: Short=Strong Down | Mid=Strong Down | Long=Strong Down
     EMA50: -14.5% below | EMA200: -8.3% below
     Support: $84,447 | Resistance: $97,937 | ATR: $3,412

ETH  [same format]
SOL  [same format]
```
