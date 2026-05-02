---
name: fvg-detector
description: >
  Detect Fair Value Gaps (FVG) and price imbalances. Use when user mentions FVG,
  fair value gap, imbalance, price gap, void, ICT gap, unfilled gap, price magnet,
  or asks where price might return to fill gaps. FVGs act as support/resistance magnets.
  Used in hot zones pipeline for zone identification alongside OBs and Fibonacci.
---

# Fair Value Gap (FVG) Detector Skill

## What Is a Fair Value Gap?
A 3-candle pattern where price moves so fast it **leaves a gap** — an area with no trading.

```
Bullish FVG:  candle[i-1].high  <  candle[i+1].low
              ↑ gap here ↑  (price exploded up, left vacuum below)
              Acts as SUPPORT when price returns

Bearish FVG:  candle[i-1].low   >  candle[i+1].high
              ↓ gap here ↓  (price crashed down, left vacuum above)
              Acts as RESISTANCE when price returns
```

**Why price fills FVGs:** Markets seek efficiency. Gaps represent "missed" trading opportunities that institutions want to fill. Unfilled FVGs are high-probability reversal/reaction zones.

## Script Location
`trading_system/scripts/indicators/fvg_detector.py`

## Key Classes & Methods

```python
from trading_system.scripts.indicators.fvg_detector import FVGDetector

detector = FVGDetector(df, min_gap_pct=0.1)
# min_gap_pct: minimum gap size as % of price to qualify (default 0.1%)

# Detect all FVGs
result = detector.detect_all(lookback=100)
# result['unfilled_bullish'] → list of unfilled bullish FVGs (support zones)
# result['unfilled_bearish'] → list of unfilled bearish FVGs (resistance zones)
# result['summary'] → e.g. "3 unfilled bullish FVGs, 2 unfilled bearish FVGs"

# Each FairValueGap has:
# fvg.top, fvg.bottom, fvg.midpoint → gap boundaries
# fvg.gap_size_pct → size of gap as % of price
# fvg.is_filled → has price completely covered this gap?
# fvg.fill_pct → how much of the gap has been filled (0-1)
# fvg.strength → 0-1 score (gap size + impulse conviction)

# Check if current price is inside an FVG
status = detector.check_if_in_fvg(price=50000)
# status['is_in_fvg'], status['active_fvgs']

# Find nearest FVG above and below price
nearest = detector.get_nearest_fvg(price=50000)
# nearest['nearest_support_fvg']    → unfilled bullish FVG below
# nearest['nearest_resistance_fvg'] → unfilled bearish FVG above
# Both include: top, bottom, strength, distance_pct
```

## FVG Strength Scoring (0-1)

| Factor | Weight | Details |
|--------|--------|---------|
| Gap size | 60% | Larger gap = stronger imbalance magnet |
| Impulse body quality | 40% | Large body on impulse candle = more conviction |

## Trading Rules for FVGs

1. **Unfilled FVG = target** — if price is above a bullish FVG, expect price to revisit it
2. **Entry at midpoint or 50%** — don't wait for full fill. Midpoint = best R:R
3. **FVG + OB alignment** = ultra-high confluence zone
4. **Partially filled FVGs** (>50%) are still valid but weaker
5. **Time decay**: FVGs from several weeks ago matter less than recent ones

## FVG vs Order Block vs Fibonacci

| Tool | What it finds | Priority |
|------|--------------|---------|
| FVG | Price gaps (imbalances) | Acts as magnet |
| Order Block | Institutional candles | Acts as S/R |
| Fibonacci | Mathematical levels | Confluence with price structure |
| POC/VAH/VAL | Volume distribution | Validates zones with volume |

## Integration in Full Analysis
- **Zone Phase:** Unfilled FVGs added as hot zones (support = bullish, resistance = bearish)
- **Entry Phase:** Price entering an FVG = potential entry signal (especially with OB/Fib alignment)
- **Target Phase:** Unfilled FVGs above/below current price = price targets
