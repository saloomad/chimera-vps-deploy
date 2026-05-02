---
name: volume-profile
description: >
  Calculate Volume Profile levels: POC (Point of Control), VAH (Value Area High),
  and VAL (Value Area Low). Use when user asks about volume profile, POC, value area,
  where most volume traded, price distribution by volume, fair value zones from volume.
  Also use in hot zones pipeline — POC/VAH/VAL are strong S/R levels.
---

# Volume Profile Skill (POC, VAH, VAL)

## What It Does
Calculates where the MOST volume has been traded in a price range.

- **POC** = Price level with highest volume. Acts as a magnet — price tends to return here.
- **VAH** = Value Area High — top of the 70% volume zone. Above VAH = buyers in control.
- **VAL** = Value Area Low — bottom of the 70% zone. Below VAL = sellers in control.
- **Value Area** = The 70% of volume traded around the POC.

## When to Use
- Zone identification phase of trade analysis
- Validating support/resistance (is there volume backing this zone?)
- Determining bias: price above VAH (bullish), below VAL (bearish), inside VA (chop)
- Alongside Fibonacci, VWAP, and Order Blocks for hot zones confluence

## Script Location
`trading_system/scripts/indicators/volume_profile.py`

## Key Classes & Methods

```python
from trading_system.scripts.indicators.volume_profile import VolumeProfileCalculator

calc = VolumeProfileCalculator(df, bins=50, value_area_pct=0.70)

# Full calculation
result = calc.calculate(lookback=100)  # lookback=None for all data
# result.poc, result.vah, result.val
# result.current_position: 'above_vah' | 'in_value_area' | 'below_val'
# result.bias: 'bullish' | 'bearish'
# result.poc_strength: 0-1 how dominant the POC is

# Get zones for hot zones pipeline
zones = calc.get_zones(lookback=100)
# Returns list of VolumeProfileZone (poc, vah, val)

# Find nearest level to current price
info = calc.get_nearest_level(price=50000)
# info['nearest_level'], info['distance_pct'], info['is_near']
```

## Trading Interpretation

| Position | Meaning | Bias |
|----------|---------|------|
| Price above VAH | Buyers clearly in control | Bullish |
| Price in value area | Balanced market / chop zone | Neutral |
| Price below VAL | Sellers clearly in control | Bearish |
| Price at POC | Balanced, high liquidity | Wait for break |
| Price far from POC | Mean-reversion risk | Caution on extremes |

## Integration in Full Analysis
- **Zone Phase:** POC, VAH, VAL added as hot zones (medium-high strength 0.65-1.0)
- **Regime Phase:** position relative to VP tells us buyer/seller control
- **Entry Phase:** entering at VAH/VAL (if they align with other zones) = high confluence

## Important Limitations
- We approximate VP from OHLCV (no tick data). Accuracy improves with more candles.
- Use lookback=200+ for meaningful VP. Short lookback = noisy.
- Session VP vs. composite VP: shorter lookback = current session behavior.
