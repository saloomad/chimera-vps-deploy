---
name: candlestick-classifier
description: >
  Classify major candlestick patterns for reversals and continuations. Use when user asks about
  candlestick patterns, candle classification, hammer, shooting star, doji, engulfing, pinbar,
  morning star, evening star, reversal candles, tweezer tops/bottoms, three soldiers, three crows,
  marubozu, harami, or wants to identify significant candle formations for trade entries.
---

# Candlestick Classifier Skill

## What It Does
Identifies **high-signal candlestick patterns** from OHLCV data with:
- Strict criteria (no false signals from weak patterns)
- Volume confirmation flag (high volume = stronger signal)
- Direction + strength + actionable trade guidance

## Script Location
`trading_system/scripts/indicators/candlestick_classifier.py`

## Patterns Detected

### 🕯️ Single-Candle Patterns
| Pattern | Direction | Signal |
|---------|-----------|--------|
| **Hammer** | Bullish reversal | Long lower wick (2x+ body), small body at top. At support = buy signal. |
| **Shooting Star** | Bearish reversal | Long upper wick (2x+ body), small body at bottom. At resistance = sell signal. |
| **Bullish Pinbar** | Bullish reversal | Lower wick = 60%+ of total range. Strong rejection of lows. |
| **Bearish Pinbar** | Bearish reversal | Upper wick = 60%+ of total range. Strong rejection of highs. |
| **Bullish Marubozu** | Bullish continuation | Full body candle, tiny/no wicks. Institutional conviction. |
| **Bearish Marubozu** | Bearish continuation | Full body candle, tiny/no wicks. |
| **Doji** | Indecision | Body ≤ 10% of range. Wait for next candle. |
| **Gravestone Doji** | Bearish reversal | Doji with long upper wick at tops. |
| **Dragonfly Doji** | Bullish reversal | Doji with long lower wick at bottoms. |
| **Spinning Top** | Indecision | Small body, wicks both sides. No signal. |

### 🕯️🕯️ Two-Candle Patterns
| Pattern | Direction | Signal |
|---------|-----------|--------|
| **Bullish Engulfing** | Bullish reversal | Bullish candle fully engulfs prior bearish. HIGH probability. |
| **Bearish Engulfing** | Bearish reversal | Bearish candle fully engulfs prior bullish. HIGH probability. |
| **Tweezer Bottoms** | Bullish reversal | Same low tested twice. Support confirmed. |
| **Tweezer Tops** | Bearish reversal | Same high tested twice. Resistance confirmed. |
| **Bullish Harami** | Bullish reversal | Small bullish inside large bearish. Weak — needs confirmation. |
| **Bearish Harami** | Bearish reversal | Small bearish inside large bullish. Weak — needs confirmation. |

### 🕯️🕯️🕯️ Three-Candle Patterns (Strongest)
| Pattern | Direction | Signal |
|---------|-----------|--------|
| **Morning Star** | Bullish reversal | Bearish → small/doji → bullish. Very reliable at bottoms. |
| **Evening Star** | Bearish reversal | Bullish → small/doji → bearish. Very reliable at tops. |
| **Three White Soldiers** | Bullish continuation | 3 ascending bullish bodies. Strong trend confirmation. |
| **Three Black Crows** | Bearish continuation | 3 descending bearish bodies. Strong trend confirmation. |

## Key Classes & Methods

```python
from trading_system.scripts.indicators.candlestick_classifier import CandlestickClassifier

clf = CandlestickClassifier(df, wick_ratio=2.0, body_pct_threshold=0.1)

# Classify single candle at index
pattern = clf.classify_candle(idx=-1)  # Last candle
# pattern.pattern     → 'hammer', 'bullish_engulfing', etc.
# pattern.direction   → 'bullish_reversal', 'bearish_reversal', 'continuation', 'indecision'
# pattern.strength    → 0-1 confidence score
# pattern.volume_confirmed → True if above-average volume
# pattern.action      → "Long entry signal. Stop below hammer low."

# Get all patterns in recent candles
patterns = clf.get_recent_patterns(lookback=20)

# Get only HIGH-QUALITY reversal signals
signals = clf.get_reversal_signals(lookback=20, min_strength=0.55)
# signals['bullish_reversals'] → list
# signals['bearish_reversals'] → list
# signals['latest_signal']     → most recent reversal pattern
# signals['signal_bias']       → 'bullish' | 'bearish' | 'neutral'
```

## Key Rules When Using Patterns

1. **Context matters** — a hammer at support is powerful; a hammer mid-trend is noise
2. **Volume confirmation** — `volume_confirmed=True` adds 1 grade to the signal
3. **Higher timeframe patterns >> lower TF patterns** — 4H hammer > 15min hammer
4. **3-candle > 2-candle > 1-candle** — pattern hierarchy applies
5. **Engulfing + OB/FVG zone** = extremely high confluence entry
6. **Doji alone = wait** — never enter on doji without confirmation candle

## Pattern Priority (Most to Least Reliable)
1. Morning/Evening Star (3-candle, strict criteria)
2. Bullish/Bearish Engulfing (2-candle, large body)
3. Pinbar / Hammer / Shooting Star (1-candle with strong wick rejection)
4. Marubozu (continuation confirmation)
5. Tweezer Tops/Bottoms
6. Harami (weak — needs confirmation)
7. Doji / Spinning Top (indecision only)

## Integration in Full Analysis
- **Confirmation Phase:** After zone is identified (Fib, OB, FVG, VP), check if current or last candle forms a reversal pattern
- **Entry Timing:** Pattern + zone confluence = entry trigger
- **Strength Boost:** volume_confirmed patterns get +0.1 to confluence score
- **Avoid:** Entering on indecision patterns (doji/spinning top) without next-candle confirmation
