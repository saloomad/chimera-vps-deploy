---
name: macro-calendar
description: >
  Read MACRO.json for upcoming economic events that move crypto markets.
  Shows FOMC meetings, CPI releases, NFP, GDP, interest rate decisions.
  Calculates days/hours until next event and flags if we're in a high-risk window.
  Use when Sal asks: "any macro events", "when is FOMC", "CPI date", "NFP date",
  "economic calendar", "upcoming events", "any events this week", "macro schedule",
  "interest rate decision", "Fed meeting", "macro risk", "calendar check",
  "any events in 48 hours", "what's coming up macro", "central bank dates",
  "economic events", "GDP release", "macro events this month".
triggers:
  - macro calendar
  - economic calendar
  - when is FOMC
  - CPI date
  - NFP date
  - upcoming events
  - any events this week
  - macro schedule
  - Fed meeting
  - calendar check
  - macro risk
  - any events 48h
  - central bank dates
output_file: Z:\reports\auto\MACRO.json
---

# SKILL: macro-calendar

## What This Skill Does

Reads `MACRO.json` (updated every 6h by `macro_calendar_checker.py`) and tells Sal:
- **What's coming up** — FOMC, CPI, NFP, GDP, earnings
- **How many days/hours until** each event
- **Whether to trade or stand aside** based on proximity to events
- **How each event impacts crypto** — historical pattern and expected volatility

This is a core **Step 1: Macro Bias** input. High-impact events within 48h = elevated risk.

---

## Events Tracked

| Event | Crypto Impact | Pattern |
|-------|---------------|---------|
| **FOMC Meeting** | CRITICAL | 24h before: vol spikes. Rate hold = neutral. Rate cut = BTC pumps. Hike = BTC dumps |
| **CPI Release** | HIGH | High CPI = rate hike fear = crypto sells. Low CPI = rate cut hope = crypto pumps |
| **NFP (Non-Farm Payroll)** | MEDIUM-HIGH | Strong jobs = less rate cuts = bearish. Weak jobs = more cuts = bullish |
| **GDP Release** | MEDIUM | Weak GDP = Fed pivots = bullish for risk assets |
| **ECB Rate Decision** | MEDIUM | Euro weakness from cuts = USD up = crypto pressure |
| **BOJ Rate Decision** | MEDIUM | Yen carry trade implications for risk assets |
| **NVDA Earnings** | HIGH | NVDA miss = tech sells = crypto correlation sell-off |
| **AAPL/MSFT/AMZN Earnings** | MEDIUM | Big tech = sentiment driver for risk |

---

## File Location

```
Z:\reports\auto\MACRO.json          ← primary (Linux, updated every 6h)
```

---

## JSON Structure

```json
{
  "timestamp": "2026-02-22T00:10:32Z",
  "next_event": {
    "date": "2026-03-18",
    "days_until": 24,
    "name": "FOMC Meeting",
    "importance": "CRITICAL",
    "category": "FOMC",
    "impact_on_crypto": "High volatility expected. Rate hold = neutral/positive.",
    "crypto_watch": ["BTC", "ETH"]
  },
  "next_48h": [],                     // Events in next 48h — TRADE WITH CAUTION if populated
  "next_7_days": [],                  // Events this week
  "next_30_days": [...],              // Full month schedule
  "fomc_calendar": [...],             // All 8 FOMC dates for 2026
  "earnings_calendar": [...]          // Tech stock earnings dates
}
```

---

## Analysis Rules

### Step 1 — Is anything in next_48h?
```
next_48h is populated → HIGH RISK WINDOW
  → Widen stops by 1.5x
  → Reduce position size by 50%
  → Prefer sitting out over entering
  → FOMC within 24h = NO NEW TRADES

next_48h is empty → Normal risk environment
```

### Step 2 — FOMC Proximity Rules
```
> 7 days away   → Ignore for now, flag it
3–7 days away   → WATCH. Start reducing overnight exposure
1–3 days away   → HIGH CAUTION. Only scalps, no swing trades
< 24h away      → NO TRADES. Close open positions if possible
Day of FOMC     → HANDS OFF. Sit on cash. Watch for post-decision volatility.
After FOMC      → 30-60 min after = best entry window (dust settles)
```

### Step 3 — CPI/NFP Rules
```
Strong CPI (above estimate) → Bitcoin usually drops (rate hike fear)
Weak CPI (below estimate)   → Bitcoin usually pumps (rate cut hope)
Hot NFP (strong jobs)       → Bearish (no rate cuts needed)
Cold NFP (weak jobs)        → Bullish (rate cuts priced in)
```

### Step 4 — Earnings Rules (NVDA, AAPL, etc.)
```
NVDA earnings within 3 days → Elevated correlation with crypto (AI narrative)
  → NVDA beat = risk-on = crypto often pumps
  → NVDA miss = risk-off = crypto often dumps 5-10%
AAPL/MSFT/AMZN → Lower direct correlation but affect sentiment
```

### Step 5 — "Dead Zone" check
```
No events in next 14 days → Clean macro window
  → Best time for swing trades
  → Macro tail risk is low
```

---

## Output Format

```
📅 MACRO CALENDAR — [timestamp]
════════════════════════════════
⚠️  NEXT 48H: [CLEAR / EVENT NAME - X days away]

NEXT EVENT:
  📌 [EVENT NAME]  — [DATE]  ([N] days away)
     Category: [FOMC/CPI/NFP/GDP/EARNINGS]
     Impact:   [CRITICAL/HIGH/MEDIUM]
     Pattern:  [1-line crypto impact pattern]
     Watch:    [BTC/ETH/specific coins]

THIS WEEK ([dates]):
  [List events with days_until]
  [If empty: "CLEAN WEEK — no high-impact events"]

THIS MONTH:
  [List top 3 events with dates]

💡 MACRO RISK VERDICT:
  [RED / YELLOW / GREEN]
  [1-2 sentence guidance]:
  "Next FOMC is 24 days away — low macro risk window.
   Good time for swing setups. Watch for CPI on [date]."
════════════════════════════════
```

---

## FOMC 2026 Schedule (Quick Reference)

| Date | Days Remaining | Phase |
|------|----------------|-------|
| Mar 18 | 24 | Next |
| May 6 | 73 | — |
| Jun 17 | 115 | — |
| Jul 29 | 157 | — |
| Sep 16 | 205 | — |
| Oct 28 | 247 | — |
| Dec 9 | 289 | — |

---

## Run On-Demand (Refresh Calendar)

```bash
# Windows
C:\Users\becke\AppData\Local\Programs\Python\Python313\python.exe trading_system/scripts/macro_calendar_checker.py

# Linux (via SSH)
ssh open-claw@192.168.31.194 "cd /home/open-claw/chimera && python3 trading_system/scripts/macro_calendar_checker.py"
```

## Agent Rules for OpenClaw

1. **If next_48h is NOT empty → immediately send to TO_ARCHITECT.md** — this is high priority
2. **Check every 6h** — macro_calendar updates every 6h, no need to poll more
3. **FOMC within 7 days → flag in every heartbeat status**
4. **Never flag an event that's already passed** (days_until < 0)
5. **Combine with news-reader**: If news mentions the same event, amplify the alert
