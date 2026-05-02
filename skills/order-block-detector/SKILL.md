---
name: order-block-detector
description: >
  Detect institutional Order Blocks (OB) — the last opposing candle before a strong impulse move.
  Use when user asks about order blocks, OBs, supply zones, demand zones, institutional levels,
  ICT concepts, smart money, last bearish candle before bullish move, or market structure zones.
  Used in hot zones pipeline for zone identification.
---

# Order Block Detector Skill

## What Is an Order Block?
The **last opposing candle before a strong impulse move**.

- **Bullish OB**: Last BEARISH candle before a strong UP move → becomes a demand/support zone
- **Bearish OB**: Last BULLISH candle before a strong DOWN move → becomes a supply/resistance zone

Why? Institutions place large orders here. When price returns, those orders get filled.

**Fresh OB** = Not yet revisited by price → High probability reaction zone
**Mitigated OB** = Price already traded through it → No longer valid

## Script Location
`trading_system/scripts/indicators/order_block_detector.py`

## Key Classes & Methods

```python
from trading_system.scripts.indicators.order_block_detector import OrderBlockDetector

detector = OrderBlockDetector(df, min_impulse_pct=0.5, mitigation_method='body')
# min_impulse_pct: minimum % move after OB to qualify it (default 0.5%)
# mitigation_method: 'body' (conservative) or 'wick' (aggressive)

# Detect all OBs
result = detector.detect_all(lookback=100)
# result['fresh_bullish'] → list of unmitigated bullish OBs
# result['fresh_bearish'] → list of unmitigated bearish OBs
# result['summary'] → e.g. "3 fresh bullish OBs, 2 fresh bearish OBs"

# Each OrderBlock has:
# ob.high, ob.low           → full candle range
# ob.body_high, ob.body_low → candle body (more precise S/R)
# ob.strength               → 0-1 score (volume + impulse + body quality)
# ob.is_mitigated           → True if price already came back through it
# ob.impulse_strength       → % of impulse move that followed

# Find nearest OBs to current price
nearest = detector.get_nearest_ob(current_price=50000)
# nearest['nearest_support_ob']    → closest unmitigated bullish OB below price
# nearest['nearest_resistance_ob'] → closest unmitigated bearish OB above price
# Both include: high, low, body_high, body_low, strength, distance_pct
```

## OB Strength Scoring (0-1)

| Factor | Weight | Details |
|--------|--------|---------|
| Impulse strength | 40% | Larger move after = stronger OB |
| Volume | 30% | Higher vol on OB candle = more institutional |
| Body quality | 30% | Larger body relative to range = more conviction |

## Trading Rules for OBs

1. **Enter at body_high (bullish OB)** — not at the wick low
2. **Stop below OB low** — if price takes the full wick out, OB is void
3. **Only trade fresh OBs** — mitigated ones are unreliable
4. **Higher timeframe OBs > lower timeframe OBs** — always
5. **OB + other confluence** — OB alone is not enough. Layer with Fib, FVG, VP

## Integration in Full Analysis
- **Zone Phase:** Fresh OBs added as hot zones (strength from OB score)
- **Entry Phase:** When price approaches a fresh OB from higher timeframe → potential entry
- **Risk Phase:** OB low/high defines the invalidation point → used for stop placement
