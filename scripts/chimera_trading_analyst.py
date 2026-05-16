#!/usr/bin/env python3
"""
Chimera Trading Analyst v2 — Hermes's market analysis engine
Full multi-timeframe analysis for BTC, ETH, SOL
Generates consultation for Deezoh with SMC-based entry zones

Skills used: technical-analysis, divergence-scanner, fvg-detector, 
             order-block-detector, volume-analyzer, macro-analyst
"""

import json
import urllib.request
import os
from datetime import datetime, timezone
import math

# ==============================================================================
# CONFIG
# ==============================================================================
VPS_API = "http://100.67.172.114:3000"
SPACE_DIR = "/srv/space/customware/L2/user/chimera-data"
CONSULT_DIR = "C:/Users/becke/claudecowork/consultation"

# Trading symbols
SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

# Timeframe definitions (granularity -> Bitget API params)
TIMEFRAMES = {
    "1W":  {"granularity": "1week",  "limit": 52,  "aggregate": 1},
    "3D":  {"granularity": "1day",   "limit": 90,  "aggregate": 3},
    "1D":  {"granularity": "1day",   "limit": 30,  "aggregate": 1},
    "4H":  {"granularity": "4h",     "limit": 168, "aggregate": 4},
    "1H":  {"granularity": "1h",     "limit": 168, "aggregate": 1},
    "15M": {"granularity": "15min",  "limit": 100, "aggregate": 1},
}

# RSI zones
RSI_OVERSOLD  = 35
RSI_OVERBOUGHT = 68
RSI_NEUTRAL_LOW = 45

# ==============================================================================
# DATA FETCHING
# ==============================================================================

def fetch_klines(symbol, granularity, limit=100, aggregate=1):
    """Fetch klines from Bitget API."""
    url = f"https://api.bitget.com/api/v2/spot/market/candles"
    # symbol already includes USDT suffix
    params = f"symbol={symbol}&granularity={granularity}&limit={limit}"
    try:
        raw = json.loads(urllib.request.urlopen(f"{url}?{params}", timeout=10).read())
        if raw.get("code") != "00000" or not raw.get("data"):
            return None
        candles = raw["data"]
        # Data format: [ts, open, high, low, close, volume, turnOver]
        result = []
        for c in candles:
            result.append({
                "ts":    int(c[0]),
                "open":  float(c[1]),
                "high":  float(c[2]),
                "low":   float(c[3]),
                "close": float(c[4]),
                "vol":   float(c[5]),
            })
        return result[::-1]  # oldest first
    except Exception as e:
        return None

# ==============================================================================
# TECHNICAL INDICATORS
# ==============================================================================

def calc_rsi(closes, period=14):
    """Calculate RSI."""
    if len(closes) < period:
        return None
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    if len(deltas) < period:
        return None
    gains = [d if d > 0 else 0 for d in deltas[-period:]]
    losses = [-d if d < 0 else 0 for d in deltas[-period:]]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calc_macd(closes, fast=12, slow=26, signal=9):
    """Calculate MACD histogram."""
    if len(closes) < slow + signal:
        return None, None, None
    def ema(data, n):
        k = 2/(n+1)
        ema_val = sum(data[:n])/n
        for v in data[n:]:
            ema_val = v*k + ema_val*(1-k)
        return ema_val
    ema_fast = ema(closes, fast)
    ema_slow = ema(closes, slow)
    macd_line = ema_fast - ema_slow
    # Signal line (simplified - full would need more data)
    macd_hist = macd_line * 0.8  # approximate signal
    return macd_line, macd_hist, macd_line - macd_hist

def calc_ema(closes, period=20):
    """Calculate EMA."""
    if len(closes) < period:
        return None
    k = 2/(period+1)
    ema_val = sum(closes[:period])/period
    for v in closes[period:]:
        ema_val = v*k + ema_val*(1-k)
    return ema_val

def calc_atr(candles, period=14):
    """Calculate ATR."""
    if len(candles) < period + 1:
        return None
    trs = []
    for i in range(1, len(candles)):
        high = candles[i]["high"]
        low = candles[i]["low"]
        prev_close = candles[i-1]["close"]
        tr = max(high-low, abs(high-prev_close), abs(low-prev_close))
        trs.append(tr)
    return sum(trs[-period:]) / period

def detect_fvg(candles):
    """
    Detect Fair Value Gaps on 15M/1H.
    FVG = 3-candle pattern: candle N has gap between N-2 high and N-1 low (bullish)
    or gap between N-2 low and N-1 high (bearish).
    Returns list of {type, tf, index, range_top, range_bottom, age_bars}.
    """
    fvgs = []
    if len(candles) < 3:
        return fvgs
    for i in range(2, len(candles)):
        c1 = candles[i-2]
        c2 = candles[i-1]
        c3 = candles[i]
        # Bullish FVG: candle 2 low > candle 1 high
        if c2["low"] > c1["high"]:
            fvgs.append({
                "type": "BULLISH",
                "index": i,
                "top": c2["low"],
                "bottom": c1["high"],
                "mid": (c2["low"] + c1["high"]) / 2,
                "filled": c3["low"] < c2["low"] and c3["low"] > c1["high"],
            })
        # Bearish FVG: candle 2 high < candle 1 low
        elif c2["high"] < c1["low"]:
            fvgs.append({
                "type": "BEARISH",
                "index": i,
                "top": c1["low"],
                "bottom": c2["high"],
                "mid": (c1["low"] + c2["high"]) / 2,
                "filled": c3["high"] > c2["high"] and c3["high"] < c1["low"],
            })
    return fvgs[-5:]  # last 5 only

def detect_order_blocks(candles, lookback=20):
    """
    Detect institutional order blocks.
    OB = candle with high volume + directional move (body > 60% of range).
    Returns last 3 untested OBs.
    """
    obs = []
    if len(candles) < lookback + 5:
        return obs
    for i in range(lookback, len(candles)-5):
        c = candles[i]
        body = abs(c["close"] - c["open"])
        range_ = c["high"] - c["low"]
        if range_ == 0:
            continue
        body_pct = body / range_
        if body_pct < 0.6:
            continue
        # Bullish OB: big green candle followed by upward move
        if c["close"] > c["open"]:  # bullish
            # Check next 5 candles have higher closes
            next_moves = [candles[j]["close"] > c["close"] for j in range(i+1, min(i+6, len(candles)))]
            if sum(next_moves) >= 3:
                obs.append({
                    "type": "BULLISH",
                    "index": i,
                    "top": c["high"],
                    "bottom": c["low"],
                    "quality": "HIGH" if body_pct > 0.8 else "MEDIUM",
                })
        else:  # bearish OB
            next_moves = [candles[j]["close"] < c["close"] for j in range(i+1, min(i+6, len(candles)))]
            if sum(next_moves) >= 3:
                obs.append({
                    "type": "BEARISH",
                    "index": i,
                    "top": c["high"],
                    "bottom": c["low"],
                    "quality": "HIGH" if body_pct > 0.8 else "MEDIUM",
                })
    return obs[-3:]

def detect_divergence(candles, rsi_period=14):
    """
    Detect RSI divergence (regular and hidden).
    Returns {type, strength, bars_since}
    """
    if len(candles) < rsi_period * 3:
        return None
    closes = [c["close"] for c in candles]
    rsi_values = []
    for i in range(rsi_period, len(closes)+1):
        r = calc_rsi(closes[:i], rsi_period)
        rsi_values.append(r)
    if len(rsi_values) < 10:
        return None
    # Find swing highs/lows in price and RSI
    price_swing_highs = []
    rsi_swing_highs = []
    price_swing_lows = []
    rsi_swing_lows = []
    for i in range(2, len(rsi_values)-2):
        # Price swing high
        if closes[i] > closes[i-1] and closes[i] > closes[i-2] and closes[i] > closes[i+1] and closes[i] > closes[i+2]:
            price_swing_highs.append((i, closes[i], rsi_values[i]))
            rsi_swing_highs.append((i, closes[i], rsi_values[i]))
        # Price swing low
        if closes[i] < closes[i-1] and closes[i] < closes[i-2] and closes[i] < closes[i+1] and closes[i] < closes[i+2]:
            price_swing_lows.append((i, closes[i], rsi_values[i]))
            rsi_swing_lows.append((i, closes[i], rsi_values[i]))
    # Regular bullish divergence: price lower low, RSI higher low
    if len(price_swing_lows) >= 2:
        p_low1, p_low2 = price_swing_lows[-2], price_swing_lows[-1]
        r_low1, r_low2 = rsi_swing_lows[-2], rsi_swing_lows[-1] if len(rsi_swing_lows) >= 2 else (None, None, None)
        if p_low2[1] < p_low1[1] and r_low2 and r_low2[2] > r_low1[2]:
            return {"type": "BULLISH", "subtype": "REGULAR", "strength": "STRONG", "bars_ago": len(closes) - p_low2[0]}
        if p_low2[1] < p_low1[1] and r_low2 and r_low2[2] > r_low1[2] * 0.95:
            return {"type": "BULLISH", "subtype": "HIDDEN", "strength": "MODERATE", "bars_ago": len(closes) - p_low2[0]}
    # Regular bearish divergence: price higher high, RSI lower high
    if len(price_swing_highs) >= 2:
        p_high1, p_high2 = price_swing_highs[-2], price_swing_highs[-1]
        r_high1, r_high2 = rsi_swing_highs[-2], rsi_swing_highs[-1] if len(rsi_swing_highs) >= 2 else (None, None, None)
        if p_high2[1] > p_high1[1] and r_high2 and r_high2[2] < r_high1[2]:
            return {"type": "BEARISH", "subtype": "REGULAR", "strength": "STRONG", "bars_ago": len(closes) - p_high2[0]}
    return None

def detect_swing_levels(candles, lookback=50):
    """Detect key support/resistance levels from swing highs/lows."""
    if len(candles) < lookback:
        return None, None
    recent = candles[-lookback:]
    highs = [c["high"] for c in recent]
    lows = [c["low"] for c in recent]
    closes = [c["close"] for c in recent]
    current = closes[-1]
    # Simple S/R: max/min of recent range
    resist = max(highs)
    support = min(lows)
    # Mid range
    mid = (resist + support) / 2
    return {
        "resist": resist,
        "support": support,
        "mid": mid,
        "current": current,
        "dist_to_resist_pct": ((resist - current) / current) * 100 if current > 0 else 0,
        "dist_to_support_pct": ((current - support) / current) * 100 if current > 0 else 0,
    }

# ==============================================================================
# PER-SYMBOL ANALYSIS
# ==============================================================================

def analyze_symbol(symbol):
    """Full analysis for one symbol across all timeframes."""
    result = {
        "symbol": symbol,
        "timeframes": {},
        "summary": {},
        "signals": [],
        "entry_zones": [],
        "warnings": [],
    }
    
    all_candles = {}
    tf_data = {}
    
    # Fetch all timeframes
    for tf_name, params in TIMEFRAMES.items():
        candles = fetch_klines(symbol, params["granularity"], params["limit"])
        if candles and len(candles) >= 20:
            all_candles[tf_name] = candles
            closes = [c["close"] for c in candles]
            highs = [c["high"] for c in candles]
            lows = [c["low"] for c in candles]
            volumes = [c["vol"] for c in candles]
            
            rsi = calc_rsi(closes)
            macd_line, macd_signal, macd_hist = calc_macd(closes)
            ema20 = calc_ema(closes, 20)
            ema50 = calc_ema(closes, 50) if len(closes) >= 50 else None
            atr = calc_atr(candles)
            current_price = closes[-1]
            
            # Trend: EMA crossover
            if ema20 and ema50:
                trend = "BULL" if ema20 > ema50 else "BEAR"
            elif ema20:
                trend = "BULL" if ema20 > current_price else "BEAR"
            else:
                trend = "NEUTRAL"
            
            # RSI zone
            if rsi:
                if rsi < RSI_OVERSOLD:
                    rsi_zone = "OVERSOLD"
                elif rsi > RSI_OVERBOUGHT:
                    rsi_zone = "OVERBOUGHT"
                elif rsi < RSI_NEUTRAL_LOW:
                    rsi_zone = "BEAR_ZONE"
                else:
                    rsi_zone = "NEUTRAL"
            else:
                rsi_zone = "N/A"
            
            # Momentum score
            momentum_score = 0
            if rsi and rsi > 50: momentum_score += 1
            if macd_hist and macd_hist > 0: momentum_score += 1
            if trend == "BULL": momentum_score += 1
            
            tf_data[tf_name] = {
                "price": current_price,
                "rsi": rsi,
                "macd_hist": macd_hist,
                "ema20": ema20,
                "ema50": ema50,
                "atr": atr,
                "trend": trend,
                "rsi_zone": rsi_zone,
                "momentum": momentum_score,
            }
    
    result["timeframes"] = tf_data
    
    # Multi-TF confluence
    bullish_count = sum(1 for tf, d in tf_data.items() if d["trend"] == "BULL" and tf in ["1W","3D","1D"])
    bearish_count = sum(1 for tf, d in tf_data.items() if d["trend"] == "BEAR" and tf in ["1W","3D","1D"])
    avg_rsi = sum(d["rsi"] for d in tf_data.values() if d["rsi"]) / max(1, sum(1 for d in tf_data.values() if d["rsi"]))
    
    # Overall bias
    if bullish_count >= 2 and avg_rsi < 60:
        overall_bias = "LONG"
        confidence = "MODERATE" if bullish_count == 2 else "HIGH"
    elif bearish_count >= 2 and avg_rsi > 40:
        overall_bias = "SHORT"
        confidence = "MODERATE" if bearish_count == 2 else "HIGH"
    elif avg_rsi < RSI_OVERSOLD:
        overall_bias = "LONG_SETUP"  # oversold but might not have bullish TF confluence yet
        confidence = "LOW"
    elif avg_rsi > RSI_OVERBOUGHT:
        overall_bias = "SHORT_SETUP"
        confidence = "LOW"
    else:
        overall_bias = "NEUTRAL"
        confidence = "LOW"
    
    result["summary"] = {
        "bias": overall_bias,
        "confidence": confidence,
        "avg_rsi": avg_rsi,
        "bullish_tf_count": bullish_count,
        "bearish_tf_count": bearish_count,
    }
    
    # FVG detection on 15M, 1H, 4H
    for tf in ["15M", "1H", "4H"]:
        if tf in all_candles:
            fvgs = detect_fvg(all_candles[tf])
            if fvgs:
                for fvg in fvgs:
                    result["signals"].append({
                        "type": "FVG",
                        "direction": fvg["type"],
                        "tf": tf,
                        "filled": fvg["filled"],
                        "top": fvg["top"],
                        "bottom": fvg["bottom"],
                        "quality": "HIGH" if not fvg["filled"] else "FILLED",
                    })
    
    # Order blocks on 1H, 4H
    for tf in ["1H", "4H"]:
        if tf in all_candles:
            obs = detect_order_blocks(all_candles[tf])
            for ob in obs:
                result["signals"].append({
                    "type": "ORDER_BLOCK",
                    "direction": ob["type"],
                    "tf": tf,
                    "top": ob["top"],
                    "bottom": ob["bottom"],
                    "quality": ob["quality"],
                })
    
    # Divergence on 1H, 4H, 1D
    for tf in ["1H", "4H", "1D"]:
        if tf in all_candles:
            div = detect_divergence(all_candles[tf])
            if div:
                result["signals"].append({
                    "type": "DIVERGENCE",
                    "direction": div["type"],
                    "subtype": div["subtype"],
                    "tf": tf,
                    "strength": div["strength"],
                })
    
    # Entry zones (based on unfilled FVGs + OBs near current price)
    current = tf_data.get("1H", tf_data.get("4H", {})).get("price", 0)
    atr = tf_data.get("4H", tf_data.get("1H", {})).get("atr", 0)
    entry_zones = []
    for sig in result["signals"]:
        if sig.get("filled"):
            continue
        if sig["type"] == "FVG":
            entry_zones.append({
                "type": "FVG_ENTRY",
                "direction": sig["direction"],
                "zone_top": sig["top"],
                "zone_bottom": sig["bottom"],
                "tf": sig["tf"],
                "quality": sig["quality"],
            })
        elif sig["type"] == "ORDER_BLOCK":
            entry_zones.append({
                "type": "OB_ENTRY",
                "direction": sig["direction"],
                "zone_top": sig["top"],
                "zone_bottom": sig["bottom"],
                "tf": sig["tf"],
                "quality": sig["quality"],
            })
    result["entry_zones"] = entry_zones
    
    # Warnings
    if avg_rsi > 70:
        result["warnings"].append("RSI OVERBOUGHT on multiple TFs - caution on longs")
    if all(tf_data.get(t) and tf_data[t]["rsi_zone"] == "OVERSOLD" for t in ["1D","4H","1H"]):
        result["warnings"].append("RSI OVERSOLD on all lower TFs - bounce possible")
    if len([s for s in result["signals"] if s["type"] == "DIVERGENCE" and s["direction"] == "BULLISH"]) > 0:
        result["warnings"].append("BULLISH DIVERGENCE detected - momentum may be shifting")
    
    return result

# ==============================================================================
# MACRO DATA
# ==============================================================================

def get_macro():
    """Get macro context from Space Agent VPS."""
    macro = {}
    try:
        url = f"{VPS_API}/api/file_read"
        data = json.dumps({"path": f"{SPACE_DIR}/MACRO.json"}).encode()
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        resp = json.loads(urllib.request.urlopen(req, timeout=8).read())
        macro = json.loads(resp.get("content", "{}"))
    except:
        pass
    return macro

# ==============================================================================
# FORMAT CONSULTATION FOR DEEZOH
# ==============================================================================

def format_consultation(results, macro):
    """Format full consultation document for Deezoh."""
    lines = []
    lines.append("=" * 78)
    lines.append("HERMES TRADING CONSULTATION — CHIMERA ANALYSIS")
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("=" * 78)
    
    # MACRO
    lines.append("\n## MACRO OVERVIEW")
    btc_dom = macro.get("BTC_Dominance", "N/A")
    fng = macro.get("Fear_Greed_Index", "N/A")
    bias = macro.get("Market_Bias", "N/A")
    lines.append(f"  BTC Dominance: {btc_dom}  |  Fear & Greed: {fng}  |  Bias: {bias}")
    lines.append(f"  Source: {'VPS live' if macro else 'FALLBACK - VPS down'}")
    
    # Per-symbol analysis
    lines.append("\n" + "=" * 78)
    lines.append("## PER-SYMBOL ANALYSIS")
    
    for symbol, data in results.items():
        summary = data["summary"]
        tf_data = data["timeframes"]
        signals = data["signals"]
        entry_zones = data["entry_zones"]
        warnings = data["warnings"]
        
        lines.append(f"\n### {symbol}")
        
        # Bias summary
        bias = summary["bias"]
        conf = summary["confidence"]
        avg_rsi = summary["avg_rsi"]
        bull_tfs = summary["bullish_tf_count"]
        bear_tfs = summary["bearish_tf_count"]
        
        bias_icon = {"LONG":"🟢","SHORT":"🔴","LONG_SETUP":"🟡","SHORT_SETUP":"🟠","NEUTRAL":"⚪"}.get(bias,"⚪")
        lines.append(f"  BIAS: {bias_icon} {bias} ({conf}) | Avg RSI: {avg_rsi:.1f} | TFs: {bull_tfs}🟢/ {bear_tfs}🔴")
        
        # Warnings
        if warnings:
            for w in warnings:
                lines.append(f"  ⚠️  {w}")
        
        # Multi-TF table
        lines.append(f"\n  {'TF':<6} {'Price':>12} {'RSI':>6} {'MACD':>10} {'Trend':<10} {'RSI Zone':<12}")
        lines.append(f"  {'--':<6} {'-----':>12} {'---':>6} {'----':>10} {'-----':<10} {'-------':<12}")
        for tf_name in ["1W","3D","1D","4H","1H","15M"]:
            if tf_name not in tf_data:
                continue
            d = tf_data[tf_name]
            price_str = f"${d['price']:,.2f}" if d['price'] else "N/A"
            rsi_str = f"{d['rsi']:.1f}" if d['rsi'] else "N/A"
            macd_str = f"{d['macd_hist']:+.4f}" if d['macd_hist'] else "N/A"
            lines.append(f"  {tf_name:<6} {price_str:>12} {rsi_str:>6} {macd_str:>10} {d['trend']:<10} {d['rsi_zone']:<12}")
        
        # Signals summary
        fvgs = [s for s in signals if s["type"] == "FVG"]
        obs = [s for s in signals if s["type"] == "ORDER_BLOCK"]
        divs = [s for s in signals if s["type"] == "DIVERGENCE"]
        unfilled_fvgs = [f for f in fvgs if not f.get("filled")]
        
        lines.append(f"\n  Signals: {len(fvgs)} FVGs ({len([f for f in fvgs if not f.get('filled')])} unfilled) | {len(obs)} OBs | {len(divs)} divergences")
        
        # Unfilled FVGs as entry zones
        if unfilled_fvgs:
            lines.append(f"\n  UNFILLED FVGs (active entry zones):")
            for fvg in unfilled_fvgs[:3]:
                dir_icon = "🟢" if fvg["direction"] == "BULLISH" else "🔴"
                lines.append(f"    {dir_icon} {fvg['direction']} FVG on {fvg['tf']}: "
                           f"${fvg['bottom']:,.2f} → ${fvg['top']:,.2f} [{fvg['quality']}]")
        
        # Active divergences
        if divs:
            lines.append(f"\n  DIVERGENCES:")
            for d in divs:
                dir_icon = "🟢" if d["direction"] == "BULLISH" else "🔴"
                lines.append(f"    {dir_icon} {d['direction']} {d['subtype']} on {d['tf']} [{d['strength']}]")
        
        # Best entry zones
        if entry_zones:
            zones_15m_1h = [z for z in entry_zones if z["tf"] in ["15M","1H"]]
            if zones_15m_1h:
                lines.append(f"\n  LOWER TF ENTRY ZONES (15M/1H):")
                for z in zones_15m_1h[:2]:
                    dir_icon = "🟢" if z["direction"] == "BULLISH" else "🔴"
                    lines.append(f"    {dir_icon} {z['type']} {z['direction']}: "
                               f"${z['zone_bottom']:,.4f} → ${z['zone_top']:,.4f} [{z['quality']}]")
        
        lines.append("")
    
    # CROSS-SYMBOL SUMMARY
    lines.append("=" * 78)
    lines.append("## CROSS-SYMBOL SUMMARY")
    
    biases = [r["summary"]["bias"] for r in results.values()]
    long_count = sum(1 for b in biases if b in ["LONG", "LONG_SETUP"])
    short_count = sum(1 for b in biases if b in ["SHORT", "SHORT_SETUP"])
    neutral_count = sum(1 for b in biases if b == "NEUTRAL")
    
    # Consensus
    if long_count >= 2:
        consensus = "🟢 CONSENSUS LONG"
    elif short_count >= 2:
        consensus = "🔴 CONSENSUS SHORT"
    elif long_count == 1 and short_count == 1:
        consensus = "⚪ MIXED - wait for clarity"
    else:
        consensus = "⚪ NEUTRAL"
    
    lines.append(f"  Overall: {consensus} ({long_count}🟢 / {short_count}🔴 / {neutral_count}⚪)")
    
    # Best setup
    setups = []
    for symbol, data in results.items():
        if data["summary"]["confidence"] == "HIGH":
            setups.append((symbol, data["summary"]["bias"], data["summary"]["avg_rsi"]))
    if setups:
        lines.append(f"  Highest confidence setups:")
        for sym, bias, rsi in sorted(setups):
            dir_icon = "🟢" if bias in ["LONG","LONG_SETUP"] else "🔴" if bias in ["SHORT","SHORT_SETUP"] else "⚪"
            lines.append(f"    {dir_icon} {sym}: {bias} (RSI {rsi:.1f})")
    
    # ==============================================================================
    # DEEZOH CONSULTATION
    # ==============================================================================
    lines.append("\n" + "=" * 78)
    lines.append("## HERMES CONSULTATION FOR DEEZOH")
    lines.append("=" * 78)
    
    # Actionable advice
    lines.append("\n### MARKET STATE")
    if all(r["summary"]["avg_rsi"] < RSI_OVERSOLD + 5 for r in results.values()):
        lines.append("  🔵 ALL SYMBOLS IN BEAR ZONE (RSI < 40) — momentum is weak")
        lines.append("  → Deezoh should await confirmation before entries")
        lines.append("  → If bias is LONG, wait for bullish divergence + TF confluence")
        lines.append("  → If bias is SHORT, trailing stop recommended")
    
    # Check for divergences
    all_divs = []
    for sym, data in results.items():
        for s in data["signals"]:
            if s["type"] == "DIVERGENCE":
                all_divs.append((sym, s))
    
    if all_divs:
        lines.append("\n### DIVERGENCE ALERT")
        for sym, d in all_divs:
            dir_icon = "🟢" if d["direction"] == "BULLISH" else "🔴"
            lines.append(f"  {dir_icon} {sym}: {d['direction']} {d['subtype']} divergence on {d['tf']} [{d['strength']}]")
        lines.append("  → Use as early warning, not standalone entry signal")
    
    # Best entry quality
    best_zones = []
    for sym, data in results.items():
        for z in data["entry_zones"]:
            if z["tf"] in ["15M","1H"] and z["quality"] == "HIGH":
                best_zones.append((sym, z))
    
    if best_zones:
        lines.append("\n### HIGH-QUALITY ENTRY ZONES")
        for sym, z in best_zones:
            dir_icon = "🟢" if z["direction"] == "BULLISH" else "🔴"
            lines.append(f"  {dir_icon} {sym} {z['type']} {z['direction']} on {z['tf']}: "
                        f"${z['zone_bottom']:,.4f} → ${z['zone_top']:,.4f}")
    
    # Macro alignment check
    macro_bias = macro.get("Market_Bias", "N/A")
    if macro_bias != "N/A":
        lines.append(f"\n### MACRO ALIGNMENT")
        for sym, data in results.items():
            tf_bias = data["summary"]["bias"]
            if (macro_bias == "LONG" and tf_bias in ["LONG","LONG_SETUP"]) or                (macro_bias == "SHORT" and tf_bias in ["SHORT","SHORT_SETUP"]):
                align = "✅ ALIGNED"
            elif (macro_bias == "LONG" and tf_bias in ["SHORT","SHORT_SETUP"]) or                  (macro_bias == "SHORT" and tf_bias in ["LONG","LONG_SETUP"]):
                align = "❌ CONFLICT"
            else:
                align = "⚪ NEUTRAL"
            lines.append(f"  {sym}: {align} (macro={macro_bias}, TF={tf_bias})")
    
    lines.append("\n" + "=" * 78)
    lines.append(f"END — Hermes Trading Analyst v2")
    lines.append("=" * 78)
    
    return "\n".join(lines)

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    os.makedirs(CONSULT_DIR, exist_ok=True)
    print(f"[Hermes Trading Analyst v2] {datetime.now(timezone.utc).isoformat()}")
    
    results = {}
    macro = get_macro()
    
    for symbol in SYMBOLS:
        print(f"  Analyzing {symbol}...")
        try:
            results[symbol] = analyze_symbol(symbol)
            summary = results[symbol]["summary"]
            warnings = results[symbol]["warnings"]
            tf = results[symbol]["timeframes"]
            rsi_1h = tf.get("1H",{}).get("rsi","N/A")
            rsi_1d = tf.get("1D",{}).get("rsi","N/A")
            print(f"    {symbol}: {summary['bias']} | RSI 1H={rsi_1h} | RSI 1D={rsi_1d} | ⚠️ {len(warnings)}")
        except Exception as e:
            print(f"    ERROR analyzing {symbol}: {e}")
            results[symbol] = {"symbol": symbol, "error": str(e), "summary": {}, "timeframes": {}}
    
    consultation = format_consultation(results, macro)
    
    md_path = os.path.join(CONSULT_DIR, "HERMES_CONSULTATION.md")
    json_path = os.path.join(CONSULT_DIR, "HERMES_CONSULTATION.json")
    
    with open(md_path, "w") as f:
        f.write(consultation)
    print(f"\n  Saved: {md_path}")
    
    # Save structured JSON
    json_data = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "macro": macro,
        "results": results,
    }
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2, default=str)
    print(f"  Saved: {json_path}")
    
    # Print to stdout for cron delivery
    print("\n" + consultation)
    return consultation

if __name__ == "__main__":
    main()
