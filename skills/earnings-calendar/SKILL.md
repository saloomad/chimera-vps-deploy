---
name: earnings-calendar
description: >
  Track tech stock earnings dates that drive crypto correlation moves.
  NVDA, AAPL, MSFT, AMZN, GOOGL, META, TSLA earnings directly impact crypto sentiment.
  Reads MACRO.json earnings_calendar section. Shows days until next earnings, expected impact.
  Use when Sal asks: "when is NVDA earnings", "earnings dates", "any earnings this week",
  "NVDA report date", "tech earnings", "earnings calendar", "when does Apple report",
  "Microsoft earnings", "TSLA earnings", "stock earnings crypto impact", "AAPL report",
  "GOOGL earnings", "META earnings", "earnings risk", "big tech earnings",
  "is there an earnings event", "stock earnings", "when is the next earnings".
triggers:
  - earnings calendar
  - earnings dates
  - NVDA earnings
  - tech earnings
  - AAPL earnings
  - MSFT earnings
  - TSLA earnings
  - GOOGL earnings
  - META earnings
  - when does Apple report
  - Microsoft earnings
  - stock earnings crypto
output_file: Z:\reports\auto\MACRO.json
---

# SKILL: earnings-calendar

## What This Skill Does

Reads the `earnings_calendar` section of `MACRO.json` to show upcoming tech stock earnings.

**Why this matters for crypto:**
Big tech earnings (especially NVDA, AAPL) are sentiment drivers for all risk assets.
When NVDA beats, AI narrative pumps, crypto often follows. When NVDA misses, crypto typically
sells 5-15% within hours. This is an often-overlooked but critical macro input.

---

## The 7 Stocks That Move Crypto

| Ticker | Crypto Correlation | Why |
|--------|-------------------|-----|
| **NVDA** | VERY HIGH | AI narrative, risk appetite. Beat = BTC pumps. Miss = BTC dumps. |
| **AAPL** | HIGH | Biggest stock. Risk-on/off barometer. Miss = sell crypto. |
| **MSFT** | HIGH | Azure AI, BTC treasury exposure. Tech sentiment. |
| **AMZN** | MEDIUM-HIGH | AWS revenue = cloud/AI sentiment. |
| **GOOGL** | MEDIUM | Ad revenue = economy health. AI model competition. |
| **META** | MEDIUM | AI spending = positive for tech narrative. |
| **TSLA** | HIGH | Musk effect. Tesla misses = sentiment dampens across risk assets. |

---

## File Location

```
Z:\reports\auto\MACRO.json  →  .earnings_calendar[]
```

---

## JSON Structure (earnings section)

```json
"earnings_calendar": [
  {
    "ticker": "NVDA",
    "company": "NVIDIA Corporation",
    "date": "2026-02-26",
    "days_until": 4,
    "importance": "HIGH",
    "crypto_correlation": "very high",
    "expected_impact": "AI narrative play. Beat = crypto pumps. Miss = 5-15% crypto drop.",
    "watch_coins": ["BTC", "ETH", "SOL"]
  }
]
```

---

## Analysis Rules

### NVDA Earnings (most important for crypto)
```
> 7 days away   → Note it, monitor sentiment
3-7 days away   → Start watching pre-earnings drift on BTC
1-3 days away   → HIGH ALERT. Reduce swing position size.
Day of earnings → NO NEW SWING TRADES. Scalps only.
After report:
  NVDA BEAT (EPS above estimate) → AI narrative buy signal for crypto
    → Look for BTC/ETH long entry 30-60 min after market digest
  NVDA MISS (EPS below estimate) → Risk-off event
    → Close any crypto longs. Watch for cascading sell-off.
```

### Pattern Recognition
```
NVDA pre-earnings pump (days -7 to -1):
  → Crypto often follows tech sentiment up
  → Be long-biased but set tight stops

NVDA post-earnings sell-the-news:
  → Even on beats, stock sometimes dips first
  → Wait 1-2h for direction to confirm before trading crypto
```

### General Earnings Rules
```
Any earnings within 48h → treat as MEDIUM risk event
NVDA within 24h → treat as HIGH risk event (close swings)
NVDA same day → NO TRADES. Cash is a position.
```

---

## Output Format

```
📊 EARNINGS CALENDAR — [timestamp]
════════════════════════════════
NEXT EARNINGS EVENT:
  🎯 [TICKER] — [COMPANY]
     Date:    [DATE] ([N] days away)
     Impact:  [HIGH/MEDIUM/LOW]
     Crypto:  [expected pattern — 1 line]
     Watch:   [BTC/ETH/relevant coins]

UPCOMING (30 days):
  [TICKER] — [DATE] — [N days] — [HIGH/MEDIUM]
  ...

💡 EARNINGS VERDICT:
  [GREEN / YELLOW / RED]
  "NVDA reports in 4 days. This is the most important earnings for crypto.
   Reduce swing exposure from [date]. Watch for AI narrative move after print."
════════════════════════════════
```

---

## Refresh Calendar

```bash
C:\Users\becke\AppData\Local\Programs\Python\Python313\python.exe trading_system/scripts/macro_calendar_checker.py
```

Note: earnings dates are fetched via `yfinance` (free). May be approximate — verify on
earnings.com or finviz.com for exact time (pre/post market matters).

## Agent Rules for OpenClaw

1. **NVDA within 48h → send to TO_ARCHITECT.md** — critical for position sizing
2. **Any earnings within 7 days → include in daily heartbeat report**
3. **Check earnings_calendar every 6h** (updates with macro_calendar_checker.py)
4. **Always note PRE-MARKET vs POST-MARKET timing** — post-market on Wednesday =
   crypto reaction Thursday morning
