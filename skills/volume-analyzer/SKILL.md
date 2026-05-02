---
name: volume-analyzer
description: >
  Analyze volume trends to confirm or deny price moves. Use when user asks about volume,
  whether volume is increasing or decreasing, volume confirmation, volume divergence,
  volume surge, buying/selling climax, capitulation, distribution, accumulation,
  or whether volume supports a trade signal. Volume is the fuel — no volume = no conviction.
---

# Volume Analyzer Skill

## What It Does
Analyzes volume as a **signal layer** — not a zone finder, but a conviction checker.

Four analysis types:
1. **Trend**: Is volume increasing or decreasing over recent candles?
2. **Surge**: Is current volume abnormally high? (>2x or >3x average)
3. **Climax**: Is this a potential exhaustion/reversal event?
4. **Divergence**: Is volume confirming or contradicting the price move?

## Script Location
`trading_system/scripts/indicators/volume_analyzer.py`

## Key Classes & Methods

```python
from trading_system.scripts.indicators.volume_analyzer import VolumeAnalyzer

analyzer = VolumeAnalyzer(df, avg_period=20, surge_threshold=2.0)

# Full analysis (single call for everything)
result = analyzer.get_volume_signal()
# result.trend             → 'increasing' | 'decreasing' | 'flat'
# result.trend_strength    → 0-1
# result.is_surge          → True/False (>2x avg)
# result.is_extreme_surge  → True/False (>3x avg)
# result.surge_multiplier  → exact ratio (e.g. 2.4)
# result.is_climax         → True/False
# result.climax_type       → 'buying_climax' | 'selling_climax' | 'none'
# result.divergence        → 'confirming' | 'distributing' | 'accumulating' | 'weak_pullback' | 'neutral'
# result.divergence_signal → 'bullish' | 'bearish' | 'bullish_warning' | 'bearish_warning' | 'neutral'
# result.overall_signal    → 'strong_bull' | 'bull' | 'neutral' | 'bear' | 'strong_bear'
# result.confidence        → 0-1
# result.description       → Human-readable explanation

# Individual checks
trend = analyzer.analyze_trend(lookback=10)
surge = analyzer.detect_surge()
climax = analyzer.detect_climax(lookback=5)
divergence = analyzer.detect_divergence(lookback=5)

# Volume at a specific price level (is this a high/low volume node?)
node = analyzer.volume_at_price_level(price=50000, tolerance_pct=0.5)
# node['is_high_volume_node'] → True = strong S/R, False = price moves fast here
```

## Volume-Price Divergence Interpretation

| Price | Volume | Signal | Meaning |
|-------|--------|--------|---------|
| ↑ Rising | ↑ Rising | **Confirming** | Healthy uptrend. Hold longs. |
| ↑ Rising | ↓ Falling | **Distributing** ⚠️ | Smart money selling into strength. Caution. |
| ↓ Falling | ↑ Rising | **Accumulating** | Smart money buying dips. Potential bottom. |
| ↓ Falling | ↓ Falling | **Weak pullback** | Low conviction sell-off. Likely to bounce. |

## Volume Climax Signals

**Buying Climax** (at price high + extreme volume):
- Market rushed up, everyone bought at top
- No more buyers → price reversal risk
- Signal: `bearish_reversal_risk`

**Selling Climax / Capitulation** (at price low + extreme volume):
- Market panicked, everyone sold at bottom
- No more sellers → price reversal opportunity
- Signal: `bullish_reversal_risk`

## Volume Rules for Chimera System

1. **Enter only with volume confirmation** — no surge on breakout = false breakout risk
2. **Rising volume in uptrend = add to position** — trend is healthy
3. **Falling volume in uptrend = tighten stops** — trend losing steam
4. **Climax = counter-signal zone** — high risk, consider taking profit
5. **Volume surge on candle pattern** = pattern is 30% more reliable
6. **Low volume at POC or OB** = zone might not hold. High volume = zone is strong.

## Integration in Full Analysis
- **Regime Phase:** Volume trend confirms regime direction
- **Zone Validation:** `volume_at_price_level()` confirms if a zone has historical volume backing
- **Entry Confirmation:** Volume surge on entry candle = higher confidence
- **Risk Management:** Divergence signal = reduce position size or add to stop
- **Exit Signals:** Buying/selling climax = consider partial profit taking
