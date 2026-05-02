---
name: liquidation-vision-analyzer
description: Analyze CoinGlass liquidation heat map screenshots using Claude Vision to extract trading data including liquidation clusters, max pain levels, long/short concentrations, and stop hunt patterns. Use this skill whenever the user mentions liquidation heat maps, CoinGlass screenshots, liquidation data extraction, max pain analysis, stop hunts, or squeeze zones. Also use when working with the Phase 3a-v2 hot zones trading system, or when the user has screenshot files showing liquidation data that need analysis for trading decisions.
compatibility:
  - playwright (for screenshot capture)
  - anthropic SDK (for Claude Vision API)
---

# Liquidation Vision Analyzer

## Overview

This skill analyzes CoinGlass liquidation heat map screenshots using Claude Vision to extract actionable trading data. It identifies liquidation clusters, max pain prices, long/short concentrations, and patterns like stop hunts or squeeze zones. The extracted data feeds directly into the Phase 3a-v2 hot zones trading system for precise entry/exit decisions.

**Why vision analysis?** CoinGlass changes their HTML frequently, making CSS selectors unreliable. Screenshots provide consistent visual data that Claude Vision can reliably analyze.

## Quick Start

When the user wants to analyze liquidation data:

1. **If they provide a screenshot:** Analyze it immediately using Claude Vision
2. **If they want fresh data:** Capture new screenshots from CoinGlass, then analyze
3. **Output:** Always return structured JSON that feeds into `liquidation_scorer.py`

## Core Capabilities

### 1. Screenshot Capture (When Fresh Data Needed)

Use Playwright to capture liquidation heat map screenshots from CoinGlass with proper authentication.

**Cookie Authentication (Required):**
```python
cookie = {
    "name": "obe",
    "value": "s_dee768b945e74d1199f32661aee8f366",
    "domain": ".coinglass.com",
    "path": "/",
    "expires": 1784047115,
    "httpOnly": False,
    "secure": False,
    "sameSite": "Lax"
}
```

**Capture Process:**
```python
# 1. Launch browser headless
browser = await playwright.chromium.launch(headless=True, args=['--no-sandbox'])

# 2. Create context and inject cookie BEFORE navigating
context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
await context.add_cookies([cookie])

# 3. Navigate to heat map
page = await context.new_page()
await page.goto(f"https://www.coinglass.com/pro/futures/LiquidationHeatMap?coin={symbol}")
await page.wait_for_load_state("networkidle")
await asyncio.sleep(3)  # Wait for chart rendering

# 4. Capture screenshot
await page.screenshot(path=f"{symbol}_heatmap.png", full_page=True)
```

**Timeframes to capture:**
- 12h (short-term scalp trades)
- 24h (day trading)
- 48h (swing trades)
- 3d (position trades)
- 1w (macro context)

**Important:** Cookie authentication bypasses the login popup. Without it, screenshots will show a login wall instead of heat maps.

### 2. Vision Analysis (Core Function)

Analyze liquidation heat map screenshots using Claude Vision to extract structured data.

**What to Extract:**

**A) Liquidation Clusters**
- **What:** Price levels where liquidations are concentrated (shown as red/orange/yellow heat zones)
- **How to identify:** Look for bright colors (red, orange, yellow) on the heat map
- **Purple/Blue zones:** Low liquidation concentration
- **Yellow/Orange zones:** Medium concentration
- **Red zones:** High concentration (max pain areas)

**B) Max Pain Price**
- **What:** The price level with the heaviest liquidation concentration (brightest red zone)
- **Why important:** Market makers target max pain to trigger cascading liquidations
- **How to identify:** Find the brightest/reddest zone on the heat map

**C) Long vs Short Positioning**
- **Longs liquidate BELOW current price:** If red zones are below current price, longs are at risk
- **Shorts liquidate ABOVE current price:** If red zones are above current price, shorts are at risk
- **Directional bias:** Whichever side has more liquidations is vulnerable to stop hunts

**D) Current Price vs Liquidations**
- **Proximity:** How far is current price from nearest liquidation cluster?
- **% distance:** Calculate `(cluster_price - current_price) / current_price * 100`
- **Close proximity (<3%):** High probability of sweep/stop hunt
- **Far proximity (>10%):** Low immediate risk

**E) Heat Map Patterns**
- **Stop Hunt Setup:** Large liquidation cluster just below support or above resistance
- **Squeeze Zone:** Red zones on BOTH sides of current price (trapped market)
- **One-Sided Imbalance:** All liquidations on one side (potential reversal target)
- **Thin Zone:** No liquidations nearby (safer zone, less manipulation risk)

**Vision Analysis Prompt Template:**
```
Analyze this CoinGlass liquidation heat map screenshot for [SYMBOL] [TIMEFRAME].

Extract the following data:

1. **Liquidation Clusters:**
   - Identify all price levels with yellow/orange/red heat zones
   - For each cluster, estimate:
     - Price level (read from Y-axis)
     - Intensity (low/medium/high based on color: yellow=medium, orange=high, red=max)
     - Type (long or short - based on position above/below current price)

2. **Max Pain Price:**
   - Find the brightest red zone (heaviest liquidation concentration)
   - Read the price level from the Y-axis

3. **Current Price:**
   - Identify current price marker on the chart
   - Read from Y-axis

4. **Proximity Analysis:**
   - Calculate % distance from current price to each liquidation cluster
   - Flag clusters within 3% as "high risk"

5. **Pattern Recognition:**
   - Identify any stop hunt setups (large clusters near support/resistance)
   - Note if this is a squeeze zone (liquidations on both sides)
   - Check for one-sided imbalance (all liquidations long or short)

Return data as structured JSON (see Output Format section).

Be precise with price levels - read the Y-axis carefully. Heat intensity determines importance.
```

### 3. Output Format

Return a JSON object that feeds directly into `liquidation_scorer.py`:

```json
{
  "symbol": "BTC",
  "timeframe": "24h",
  "timestamp": "2026-02-17T10:15:00Z",
  "current_price": 67234.50,
  "max_pain": {
    "price": 65800.00,
    "intensity": "high",
    "distance_pct": -2.13,
    "type": "long_liquidation"
  },
  "liquidation_clusters": [
    {
      "price": 65800.00,
      "type": "long",
      "intensity": "high",
      "distance_pct": -2.13,
      "risk_level": "high"
    },
    {
      "price": 68500.00,
      "type": "short",
      "intensity": "medium",
      "distance_pct": 1.88,
      "risk_level": "medium"
    },
    {
      "price": 64000.00,
      "type": "long",
      "intensity": "medium",
      "distance_pct": -4.81,
      "risk_level": "medium"
    }
  ],
  "patterns": {
    "stop_hunt_setup": true,
    "squeeze_zone": false,
    "one_sided_imbalance": "long_heavy",
    "description": "Large long liquidation cluster 2.13% below current price - high risk of stop hunt sweep to $65.8K before reversal"
  },
  "directional_bias": {
    "long_liquidations_total": 2,
    "short_liquidations_total": 1,
    "vulnerable_side": "longs",
    "target_direction": "down_first_then_up"
  }
}
```

**Field Definitions:**
- `distance_pct`: Negative = below current price, Positive = above
- `intensity`: "low" (yellow), "medium" (orange), "high" (red)
- `risk_level`: "high" (<3% away), "medium" (3-10%), "low" (>10%)
- `type`: "long" (liquidates below price), "short" (liquidates above price)

### 4. Integration with Hot Zones Scoring

The extracted data feeds into `liquidation_scorer.py` which contributes 15% to the total hot zone score:

**Scoring Logic:**
1. **Proximity Scoring (60% of liquidation score):**
   - If zone price is within 1% of liquidation cluster: +60 points
   - If within 2%: +40 points
   - If within 3%: +20 points

2. **Intensity Multiplier (25% of liquidation score):**
   - High intensity (red): 1.0x
   - Medium intensity (orange): 0.6x
   - Low intensity (yellow): 0.3x

3. **Pattern Bonus (15% of liquidation score):**
   - Stop hunt setup: +15 points
   - Squeeze zone: +10 points
   - One-sided imbalance: +5 points

**Example Integration:**
```python
from liquidation_scorer import score_liquidation_proximity

# Feed vision-extracted data to scorer
liquidation_score = score_liquidation_proximity(
    zone_price=65850.00,
    current_price=67234.50,
    liquidation_clusters=vision_data["liquidation_clusters"],
    patterns=vision_data["patterns"]
)

# Returns score 0-100 (15% weight in final hot zone score)
```

## Common Use Cases

### Use Case 1: Real-Time Trading Decision
```
User: "Show me BTC liquidation levels for the next 24 hours"

You should:
1. Capture fresh BTC 24h heat map screenshot
2. Analyze with Claude Vision
3. Extract liquidation clusters + max pain
4. Highlight stop hunt risks
5. Return JSON + human summary
```

### Use Case 2: Multi-Timeframe Analysis
```
User: "Analyze ETH liquidations across multiple timeframes"

You should:
1. Capture 12h, 24h, 48h, 3d screenshots
2. Analyze each with vision
3. Compare patterns across timeframes
4. Identify aligned liquidation zones (all timeframes agree)
5. Return JSON array + confluence analysis
```

### Use Case 3: Hot Zones Integration
```
User: "Generate hot zones for SOL"

You should:
1. Capture SOL liquidation screenshot
2. Extract liquidation data via vision
3. Pass to liquidation_scorer.py
4. Combine with technical indicators
5. Output final scored hot zones
```

## Error Handling

**Common Issues:**

**1. Login Popup Visible**
- **Symptom:** Screenshot shows "Continue with Google" instead of heat map
- **Cause:** Cookie not injected or expired
- **Fix:** Verify cookie is added BEFORE navigation, check expiration date

**2. Price Levels Unclear**
- **Symptom:** Vision can't read Y-axis prices accurately
- **Cause:** Low resolution, small font, overlapping elements
- **Fix:** Use 1920x1080 viewport, capture full page, zoom if needed

**3. No Liquidation Clusters Detected**
- **Symptom:** Vision sees chart but no heat zones
- **Cause:** Chart not fully loaded, low liquidation volume
- **Fix:** Wait 3-5 seconds after page load, try different timeframe

**4. Cookie Expired**
- **Symptom:** Screenshots show login popup again
- **Cause:** Cookie expiration (expires: 1784047115 = ~June 2026)
- **Fix:** User needs to provide fresh cookie from browser DevTools

## Best Practices

1. **Always capture fresh screenshots** before major trading decisions (data can be stale in 15-30 min)

2. **Multi-timeframe confluence** is stronger signal than single timeframe
   - If 24h, 48h, and 3d all show liquidations at $65.8K = very strong level

3. **Combine with technical analysis** - liquidation zones near Fib levels = highest probability

4. **Don't trade INTO liquidation clusters** - wait for sweep, then reversal

5. **Max pain price** is NOT always hit - but it's where most damage would occur

6. **Pattern context matters:**
   - Stop hunt setup in downtrend = likely sweep lower
   - Squeeze zone = volatile move incoming (direction unclear)
   - One-sided imbalance = potential fuel for opposite move

## Technical Notes

**Why Claude Vision?**
- CoinGlass uses dynamic JavaScript rendering
- HTML structure changes frequently
- CSS selectors break constantly
- Vision analysis works regardless of HTML changes
- Human traders look at charts visually anyway - we replicate that

**Performance:**
- Screenshot capture: ~3-5 seconds per timeframe
- Vision analysis: ~5-10 seconds per screenshot
- Total pipeline: ~10-15 seconds per coin per timeframe
- Batch processing: Parallelize captures, analyze sequentially

**Cost Estimation:**
- Claude Vision API: ~$0.01-0.02 per screenshot analysis (Sonnet)
- Analyzing 5 timeframes = $0.05-0.10 per coin
- Daily usage (3 coins, 3x per day) = $0.45-0.90/day = ~$15/month

**Alternative (cheaper):**
- Use Haiku for less critical analysis: ~$0.001 per screenshot
- Monthly cost: ~$1.50 instead of $15

## Resources

This skill includes:
- **scripts/coinglass_scraper.py**: Playwright-based screenshot capture with cookie auth
- **references/api_reference.md**: Claude Vision API documentation and examples
- No assets needed (heat maps are fetched remotely)

For implementation details, see:
- Phase 3a-v2 documentation: `trading_system/docs/HOT_ZONES_SYSTEM_COMPLETE.md`
- Liquidation scorer: `trading_system/scripts/indicators/liquidation_scorer.py`
- Test screenshots: `/sessions/vigilant-fervent-ride/test_cookie_screenshot.png`
