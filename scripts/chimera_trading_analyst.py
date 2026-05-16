#!/usr/bin/env python3
"""
Chimera Trading Analyst - Hermes's market analysis engine
Runs full multi-timeframe analysis for BTC, ETH, SOL
Generates consultation for Deezoh
"""

import sys
import os
import json
import urllib.request
from datetime import datetime, timezone

CONSULT_DIR = "C:/Users/becke/claudecowork/consultation"
VPS_API = "http://100.67.172.114:3000"
SPACE_DIR = "/srv/space/customware/L2/user/chimera-data"

TIMEFRAMES = {
    "1W":  {"granularity": "1day", "limit": 100, "aggregate": 7},  # 7 daily = 1 week
    "3D":  {"granularity": "1day", "limit": 100, "aggregate": 3},  # 3 daily = 3 days
    "1D":  {"granularity": "4h",   "limit": 100, "aggregate": 1},
    "4H":  {"granularity": "1h",   "limit": 200, "aggregate": 1},
    "1H":  {"granularity": "1h",   "limit": 100, "aggregate": 1},
    "15M": {"granularity": "15min","limit": 100, "aggregate": 1},
}

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

def fetch_klines(symbol, granularity, limit, aggregate=1):
    url = f"https://api.bitget.com/api/v2/spot/market/candles?symbol={symbol}&granularity={granularity}&limit={limit}"
    try:
        import pandas as pd
        raw = json.loads(urllib.request.urlopen(url, timeout=10).read())
        df = pd.DataFrame(raw["data"], columns=["timestamp","open","high","low","close","volume","quoteVol","amount"])
        for col in ["open","high","low","close","volume","amount"]:
            df[col] = df[col].astype(float)
        df["timestamp"] = pd.to_datetime(df["timestamp"].astype(float), unit="ms")
        
        # Aggregate if needed (e.g. 7 daily candles = 1 week)
        if aggregate > 1:
            df = df.iloc[::-1]  # reverse so oldest first
            agg_df = df.groupby(df.index // aggregate).agg({
                "timestamp": "first",
                "open": "first",
                "high": "max",
                "low": "min",
                "close": "last",
                "volume": "sum",
            })
            df = agg_df.iloc[::-1]  # reverse back
        
        return df.tail(200)
    except Exception as e:
        print(f"  [!] {symbol} {granularity}: {e}")
        return None

def get_macro():
    try:
        url = f"{VPS_API}/api/file_read"
        data = json.dumps({"path": f"{SPACE_DIR}/MACRO.json"}).encode()
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        resp = json.loads(urllib.request.urlopen(req, timeout=8).read())
        return json.loads(resp.get("content", "{}"))
    except:
        return {}

def calc_rsi(series, period=14):
    import pandas as pd
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / loss.replace(0, 1e-10)
    return float((100 - (100 / (1 + rs))).iloc[-1])

def calc_macd(series, fast=12, slow=26, signal=9):
    ema_fast = series.ewm(span=fast).mean()
    ema_slow = series.ewm(span=slow).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal).mean()
    hist = macd_line - signal_line
    return float(macd_line.iloc[-1]), float(signal_line.iloc[-1]), float(hist.iloc[-1])

def analyze_symbol(symbol):
    import pandas as pd
    result = {"symbol": symbol, "timestamp": datetime.now(timezone.utc).isoformat(), "timeframes": {}, "aggregated": {}}
    
    for tf_name, tf_cfg in TIMEFRAMES.items():
        df = fetch_klines(symbol, tf_cfg["granularity"], tf_cfg["limit"], tf_cfg.get("aggregate", 1))
        if df is None or df.empty:
            result["timeframes"][tf_name] = {"error": "fetch_failed"}
            continue
        
        close = df["close"]
        price = float(close.iloc[-1])
        rsi = calc_rsi(close)
        macd_val, macd_sig, macd_hist = calc_macd(close)
        
        ema20 = float(close.ewm(span=20).mean().iloc[-1])
        ema50 = float(close.ewm(span=50).mean().iloc[-1])
        ema200 = float(close.ewm(span=200).mean().iloc[-1])
        
        if price > ema20 > ema50 > ema200:
            trend = "STRONG_BULL"
        elif price > ema20 and price > ema50:
            trend = "BULL"
        elif price < ema20 < ema50 < ema200:
            trend = "STRONG_BEAR"
        elif price < ema20 and price < ema50:
            trend = "BEAR"
        else:
            trend = "NEUTRAL"
        
        atr = float((df["high"] - df["low"]).tail(14).mean())
        atr_pct = atr / price * 100
        sr_high = float(df["high"].tail(20).max())
        sr_low = float(df["low"].tail(20).min())
        
        recent5 = df.tail(5)
        price_chg5 = float((recent5["close"].iloc[-1] - recent5["open"].iloc[0]) / recent5["open"].iloc[0] * 100)
        
        result["timeframes"][tf_name] = {
            "price": round(price, 4),
            "rsi": round(rsi, 1),
            "macd_hist": round(macd_hist, 4),
            "trend": trend,
            "atr_pct": round(atr_pct, 2),
            "sr_high": round(sr_high, 4),
            "sr_low": round(sr_low, 4),
            "price_change_5": round(price_chg5, 2),
            "momentum": "BULL" if macd_hist > 0 else "BEAR",
        }
    
    rsis = {tf: d["rsi"] for tf, d in result["timeframes"].items() if "rsi" in d}
    avg_rsi = sum(rsis.values()) / len(rsis) if rsis else 50
    bull = sum(1 for d in result["timeframes"].values() if d.get("momentum") == "BULL")
    bear = sum(1 for d in result["timeframes"].values() if d.get("momentum") == "BEAR")
    
    if avg_rsi > 70:   rsi_zone = "OVERBOUGHT"
    elif avg_rsi < 30: rsi_zone = "OVERSOLD"
    elif avg_rsi > 60: rsi_zone = "BULL_ZONE"
    elif avg_rsi < 40: rsi_zone = "BEAR_ZONE"
    else:              rsi_zone = "NEUTRAL"
    
    trends = [d.get("trend","NEUTRAL") for d in result["timeframes"].values() if "trend" in d]
    dom_trend = max(set(trends), key=trends.count) if trends else "NEUTRAL"
    
    result["aggregated"] = {
        "avg_rsi": round(avg_rsi, 1),
        "rsi_zone": rsi_zone,
        "momentum_ratio": f"{bull}/{bear}",
        "dominant_trend": dom_trend,
        "signal_strength": "STRONG" if abs(avg_rsi - 50) > 15 and bull >= 4 else "MODERATE" if abs(avg_rsi - 50) > 8 else "WEAK",
        "direction": "LONG" if avg_rsi > 52 and bull > bear else "SHORT" if avg_rsi < 48 and bear > bull else "NEUTRAL",
    }
    return result

def format_consultation(analyses, macro):
    lines = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    lines.append("=" * 70)
    lines.append("HERMES TRADING CONSULTATION")
    lines.append(f"Generated: {now}")
    lines.append("=" * 70)
    
    lines.append("\n## MACRO OVERVIEW")
    if macro:
        lines.append(f"  BTC Dominance: {macro.get('BTC_Dominance','N/A')}  |  Fear & Greed: {macro.get('Fear_Greed_Index','N/A')}  |  Bias: {macro.get('Market_Bias','N/A')}")
    else:
        lines.append("  [Macro data unavailable - VPS may be down]")
    
    lines.append("\n" + "=" * 70)
    lines.append("## PER-SYMBOL ANALYSIS")
    
    for a in analyses:
        sym = a["symbol"]
        agg = a["aggregated"]
        lines.append(f"\n### {sym}")
        lines.append(f"  Direction: {agg['direction']}  |  Trend: {agg['dominant_trend']}  |  RSI Zone: {agg['rsi_zone']} (avg {agg['avg_rsi']})")
        lines.append(f"  Momentum: {agg['momentum_ratio']} bull/bear  |  Signal: {agg['signal_strength']}")
        lines.append(f"\n  {'TF':<6} {'Price':<14} {'RSI':<6} {'MACD Hist':<12} {'Trend':<12} Momentum")
        lines.append(f"  {'-'*6} {'-'*14} {'-'*6} {'-'*12} {'-'*12} {'-'*8}")
        
        for tf in ["1W","3D","1D","4H","1H","15M"]:
            if tf in a["timeframes"]:
                d = a["timeframes"][tf]
                if "error" in d:
                    lines.append(f"  {tf:<6} ERROR")
                    continue
                sign = "+" if d["macd_hist"] > 0 else ""
                lines.append(f"  {tf:<6} {d['price']:<14.4f} {d['rsi']:<6.1f} {sign}{d['macd_hist']:<11.4f} {d['trend']:<12} {d['momentum']}")
        
        if "1D" in a["timeframes"] and "error" not in a["timeframes"]["1D"]:
            d = a["timeframes"]["1D"]
            lines.append(f"\n  Key Levels:  Resist {d['sr_high']:.4f}  |  Support {d['sr_low']:.4f}  |  ATR {d['atr_pct']:.2f}%")
    
    lines.append("\n" + "=" * 70)
    lines.append("## CROSS-SYMBOL SUMMARY")
    for a in analyses:
        agg = a["aggregated"]
        lines.append(f"  {a['symbol']}: {agg['direction']} | RSI {agg['rsi_zone']} | {agg['signal_strength']} signal")
    
    lines.append("\n" + "=" * 70)
    lines.append("## HERMES CONSULTATION FOR DEEZOH\n")
    
    longs = sum(1 for a in analyses if a["aggregated"]["direction"] == "LONG")
    shorts = sum(1 for a in analyses if a["aggregated"]["direction"] == "SHORT")
    neutrals = sum(1 for a in analyses if a["aggregated"]["direction"] == "NEUTRAL")
    
    if longs >= 2:
        lines.append("  OVERALL BIAS: BULLISH")
        lines.append("  - Multiple symbols showing LONG setup with momentum confirmation")
        lines.append("  - Favor long entries on pullbacks to key support zones")
        lines.append("  - Watch for continuation patterns on 4H/1H frames")
    elif shorts >= 2:
        lines.append("  OVERALL BIAS: BEARISH")
        lines.append("  - Multiple symbols in SHORT territory")
        lines.append("  - Be cautious with long positions; look for shorts on rallies")
        lines.append("  - Support levels likely to break - prefer shorting rallies")
    elif neutrals >= 2:
        lines.append("  OVERALL BIAS: NEUTRAL")
        lines.append("  - No clear directional bias - range-bound environment")
        lines.append("  - Wait for confirmed breakouts before sizing up")
        lines.append("  - Focus on scalp setups at key S/R levels")
    else:
        lines.append("  OVERALL BIAS: MIXED - see per-symbol above")
    
    overbought = [a["symbol"] for a in analyses if a["aggregated"]["rsi_zone"] == "OVERBOUGHT"]
    oversold = [a["symbol"] for a in analyses if a["aggregated"]["rsi_zone"] == "OVERSOLD"]
    if overbought:
        lines.append(f"\n  OVERBOUGHT: {', '.join(overbought)} - Momentum stretched. Watch for reversal signals.")
    if oversold:
        lines.append(f"\n  OVERSOLD: {', '.join(oversold)} - Potential bounce candidates. Look for divergence.")
    
    lines.append("\n  DIVERGENCE WATCH:")
    div_found = False
    for a in analyses:
        for tf, d in a["timeframes"].items():
            if "error" in d:
                continue
            pc5 = d.get("price_change_5", 0)
            mh = d.get("macd_hist", 0)
            if pc5 > 2 and mh < -0.5:
                lines.append(f"    {a['symbol']} {tf}: Price +{pc5:.1f}% but MACD hist {mh:.4f} - HIDDEN BULL (momentum div)")
                div_found = True
            elif pc5 < -2 and mh > 0.5:
                lines.append(f"    {a['symbol']} {tf}: Price {pc5:.1f}% but MACD hist +{mh:.4f} - HIDDEN BEAR (momentum div)")
                div_found = True
    if not div_found:
        lines.append("    No strong divergences detected in current frame.")
    
    lines.append("\n" + "=" * 70)
    lines.append("Hermes Trading Analyst | For Deezoh consultation only")
    lines.append("=" * 70)
    return "\n".join(lines)

def main():
    import os
    os.makedirs(CONSULT_DIR, exist_ok=True)
    
    print(f"[Hermes Trading Analyst] {datetime.now(timezone.utc).isoformat()}")
    print(f"  Symbols: {SYMBOLS}")
    
    macro = get_macro()
    analyses = []
    for sym in SYMBOLS:
        print(f"  Analyzing {sym}...")
        a = analyze_symbol(sym)
        analyses.append(a)
        print(f"    {sym}: {a['aggregated']['direction']} | RSI {a['aggregated']['avg_rsi']} | {a['aggregated']['rsi_zone']}")
    
    consultation = format_consultation(analyses, macro)
    
    md_file = os.path.join(CONSULT_DIR, "HERMES_CONSULTATION.md")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(consultation)
    print(f"\n  Saved: {md_file}")
    
    json_file = os.path.join(CONSULT_DIR, "HERMES_CONSULTATION.json")
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump({"timestamp": datetime.now(timezone.utc).isoformat(), "symbols": SYMBOLS, "analyses": analyses, "macro": macro}, f, indent=2, default=str)
    print(f"  Saved: {json_file}")
    
    print("\n" + consultation)
    return 0

if __name__ == "__main__":
    sys.exit(main())
