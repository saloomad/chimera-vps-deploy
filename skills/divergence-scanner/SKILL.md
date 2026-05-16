---
name: divergence-scanner
description: >
  Scan top 50 Binance coins (by 24h volume) for divergences across multiple timeframes.
  Uses threading â€” 50 coins in ~30 seconds. Only outputs coins WITH active signals.
  Uses v2 scoring: 3 independent categories (Volume/Trend/Momentum) with TF weighting.
  Output is ONE entry per coin with plain-English explanation and tier rating.
  Use when Sal asks: "scan for divs", "any divergences in the market", "scan 50 coins",
  "market scan", "which coins have divergences", "find divergence setups",
  "divergence scan", "scan for crossovers", "find rsi signals", "what's setting up",
  "scan the market", "which coins are setting up", "find opportunities".
  Runs divergence_scanner.py, reads DIVERGENCES.json, formats the best hits.
triggers:
  - scan for divs
  - market scan
  - any divergences
  - scan 50 coins
  - which coins have divergences
  - find divergence setups
  - divergence scan
  - scan for crossovers
  - what's setting up
  - find opportunities
  - scan the market
output_file: reports/auto/DIVERGENCES.json
---

# SKILL: divergence-scanner (v2)

## What This Skill Does

Scans the **top 50 Binance USDT pairs by 24h volume** for divergences across multiple timeframes.

**Key v2 improvements:**
- ONE entry per coin (not one per coin-per-timeframe â€” no duplicates)
- Tier output (CRITICAL / STRONG / MODERATE / WEAK / MIXED) â€” instantly actionable
- 3 independent scoring categories (Volume, Trend, Momentum) â€” no false amplification from correlated oscillators
- Higher timeframe divergences weighted exponentially higher (1w = 5Ã— more than 1h)
- Multi-timeframe alignment bonus (+50% for 3+ TFs, +20% for 2 TFs)
- Plain English explanation per coin: what happened, what it means, what to watch for

---

## Prerequisites

**Set Binance API key first** (higher rate limits):
Edit `trading_system/config/binance_config.json`:
```json
{
  "api_key": "your_actual_binance_api_key_here",
  "api_secret": ""
}
```
- Without key: 1,200 req/min (still works)
- With key: 6,000 req/min (5Ã— more headroom, recommended)

---

## How to Run

```bash
# Default: top 50 coins, 1w + 1d + 4h + 1h
python trading_system/scripts/divergence_scanner.py

# Custom timeframes
python trading_system/scripts/divergence_scanner.py --timeframes 1d 4h 1h

# Fewer coins (faster)
python trading_system/scripts/divergence_scanner.py --top 30

# Specific coins only
python trading_system/scripts/divergence_scanner.py --symbols BTCUSDT ETHUSDT SOLUSDT

# More workers (needs API key)
python trading_system/scripts/divergence_scanner.py --workers 16
```

**Linux path:**
```bash
cd /root/openclawtrading && python3 trading_system/scripts/divergence_scanner.py
```

---

## Scoring System (v2)

### 3 Independent Categories

| Category | Indicators | Min to confirm | Base score |
|----------|-----------|----------------|------------|
| **Volume** | OBV | 1 signal | 2.0 |
| **Trend** | MACD, MACD_Hist | 1 signal | 1.5 |
| **Momentum** | RSI, Stoch, CCI, Williams %R | 2 signals | 1.0 |

**Why 2 signals for Momentum?** RSI, Stoch, CCI, Williams %R are all correlated oscillators. One of them showing divergence is not independent from the others. We require at least 2 to count it as a genuine confirmation.

### Timeframe Weights

| Timeframe | Weight | Reason |
|-----------|--------|--------|
| 1w | 5.0Ã— | Structural â€” months of data |
| 1d | 3.0Ã— | Swing â€” weekly rhythm |
| 12h | 2.0Ã— | Medium |
| 4h | 1.5Ã— | Swing entry timing |
| 1h | 1.0Ã— | Baseline |

### Multi-Timeframe Bonus

| Alignment | Bonus |
|-----------|-------|
| 3+ TFs aligned | Ã—1.5 |
| 2 TFs aligned | Ã—1.2 |
| 1 TF only | no bonus |

### Tier Thresholds

| Tier | Score | Meaning |
|------|-------|---------|
| **CRITICAL** | â‰¥12 | Major structural signal. Rare. High conviction. |
| **STRONG** | â‰¥7 | High-conviction setup. Watch for entry trigger. |
| **MODERATE** | â‰¥3 | Signal present. Needs more confirmation. |
| **WEAK** | â‰¥1 | Too early. Monitor only. |
| **MIXED** | any | Conflicting signals. Skip. |

---

## Output File: DIVERGENCES.json (v2)

Location: `reports/auto/DIVERGENCES.json`

### Top-Level Structure
```json
{
  "version": "2.0",
  "generated_at": "2026-02-22T10:00:00+00:00",
  "scan_duration_s": 28.4,
  "coins_scanned": 50,
  "timeframes": ["1w", "1d", "4h", "1h"],
  "scoring_rules": { ... },
  "summary": {
    "critical": 1,
    "strong": 3,
    "moderate": 8,
    "mixed": 4,
    "weak": 12,
    "total_hits": 28
  },
  "divergence_hits": [ ... ]
}
```

### Per-Coin Structure
```json
{
  "symbol": "AXSUSDT",
  "price": 1.39,
  "tier": "STRONG",
  "tier_icon": "RED",
  "tier_desc": "High-conviction. Watch for entry trigger.",
  "bias": "BEARISH",
  "score": 8.1,
  "aligned_timeframes": ["1d", "4h"],
  "multi_tf_count": 2,
  "has_conflict": false,
  "timeframes": {
    "1d": {
      "bias": "BEARISH",
      "score": 4.5,
      "categories": {
        "momentum": "BEARISH",
        "trend": "BEARISH",
        "volume": "NONE"
      },
      "confirmed": ["momentum", "trend"],
      "div_count": 4
    },
    "4h": {
      "bias": "BEARISH",
      "score": 3.2,
      "categories": { ... },
      "confirmed": ["momentum"],
      "div_count": 2
    }
  },
  "crossovers": ["macd_cross_below_signal", "rsi_cross_50_below"],
  "indicators": {
    "price": 1.39,
    "rsi": 41.2,
    "stoch_k": 28.4,
    "adx": 31.5,
    "macd_state": "bearish"
  },
  "plain_english": {
    "what_happened": "AXS price pushed up (or held), but momentum indicators peaked earlier and are now declining. Buyers are running out of fuel.",
    "what_it_means": "The move is losing conviction. Reversal or continued drop likely.",
    "timeframe_context": "Signal on 1d + 4h â€” moderate confirmation.",
    "rsi_note": "RSI 41.2 â€” bearish zone.",
    "adx_note": "ADX 31.5 â€” moderate trend strength.",
    "watch_for_entry": "RSI crossing below 50, or Stochastic K crossing below D. A rejection candle at resistance confirms the short setup.",
    "crossover_context": "Bear crossovers: MACD-bearcross, RSI<50(bear)."
  }
}
```

---

## How to Read Results as an Agent

### Priority: Read by Tier
```
CRITICAL â†’ immediate attention
STRONG â†’ investigate, look for entry trigger
MODERATE â†’ monitor, not yet actionable
MIXED â†’ skip
WEAK â†’ ignore unless nothing else
```

### Step 1: Filter by Macro Bias
```python
if macro_bias == "SHORT":
    candidates = [r for r in data["divergence_hits"] if r["bias"] == "BEARISH"]
elif macro_bias == "LONG":
    candidates = [r for r in data["divergence_hits"] if r["bias"] == "BULLISH"]
```

### Step 2: Read the Plain English
For each candidate, read `plain_english.what_happened` and `plain_english.what_it_means`.
This tells you in plain words what the signal is saying.

### Step 3: Check Timeframe Alignment
`aligned_timeframes` shows which TFs are pointing in the same direction.
- 1w + 1d aligned = structural signal, very strong
- 1d + 4h aligned = swing trade setup
- 4h only = timing signal, lower conviction

### Step 4: Check the TF Grid
`timeframes[tf].categories` shows which category confirmed per TF:
- `volume: "BEARISH"` = OBV divergence (strong, independent)
- `trend: "BEARISH"` = MACD divergence (solid)
- `momentum: "BEARISH"` = 2+ oscillators (RSI/Stoch/CCI/WR)

### Step 5: Top STRONG+ hits â†’ run candle-analyzer
For any CRITICAL or STRONG coin, run `candle-analyzer` to get:
- AVWAP levels
- Sweep detection
- Candlestick confirmation patterns

---

## Divergence Quick Reference

| Type | Price | Indicator | Meaning | Action |
|------|-------|-----------|---------|--------|
| `bullish_regular` | Lower Low | Higher Low | Bears losing strength | Look for long |
| `bearish_regular` | Higher High | Lower High | Bulls losing strength | Look for short |
| `bullish_hidden` | Higher Low | Lower Low | Uptrend intact | Buy dip |
| `bearish_hidden` | Lower High | Higher High | Downtrend intact | Sell rally |

---

## Console Output Format (v2)

```
==============================================================
  [RED] AXS -- $1.39  |  STRONG  (score: 8.1)
  Bias: BEARISH  |  High-conviction. Watch for entry trigger.
--------------------------------------------------------------
  TF    | Bias      | Volume | Trend  | Momentum
  --------------------------------------------------
  1d    | BEARISH   | [ ]    | [S]    | [S]     <--
  4h    | BEARISH   | [ ]    | [ ]    | [S]     <--
  1h    | NONE      | [ ]    | [ ]    | [ ]
--------------------------------------------------------------
  WHAT'S HAPPENING:
    AXS price pushed up (or held), but momentum indicators
    peaked earlier and are now declining.
  WHAT IT MEANS:  The move is losing conviction.
  TF ALIGNMENT:   Signal on 1d + 4h -- moderate confirmation.
  RSI STATE:      RSI 41.2 -- bearish zone.
  WATCH FOR:      RSI crossing below 50, or Stoch K below D.
==============================================================
```

`[B]` = BULLISH, `[S]` = BEARISH, `[M]` = MIXED, `[ ]` = no signal
`<--` marks timeframes that align with the coin's overall bias

---

## Scheduling

Linux cron (already configured):
```
*/30 * * * * cd /root/openclawtrading && python3 trading_system/scripts/divergence_scanner.py >> logs/div_scanner.log 2>&1
```

Or run on demand:
```bash
python3 trading_system/scripts/divergence_scanner.py --top 50 --timeframes 1w 1d 4h 1h
```

---

## Workflow Integration

```
Every 30 min (cron on Linux):
  divergence_scanner.py â†’ DIVERGENCES.json

Screener Agent reads DIVERGENCES.json:
  â†’ Filter by MACRO_BIAS direction
  â†’ Only STRONG+ tiers considered
  â†’ Score 75+ â†’ alert_sal: true â†’ Discord alert to Sal

When Sal reviews manually:
  â†’ Read DIVERGENCES.json, show CRITICAL + STRONG tiers
  â†’ Filter by macro bias
  â†’ For top hits â†’ run candle-analyzer for entry confirmation
```
