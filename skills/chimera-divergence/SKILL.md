---
name: chimera-divergence
description: >
  Run divergence-only analysis using the Chimera divergence engine — no full report needed.
  Use when Sal asks: "check divergences on BTC", "any divs on ETH", "divergence scan",
  "what are the divergences", "show me divs", "bullish divs", "bearish divs",
  "divergence only", "quick div check", "div scan BTC ETH SOL".
  Runs chimera_data.py and extracts only the divergence table from the report.
---

# CHIMERA DIVERGENCE SKILL

## Purpose
Run a quick divergence-only check on one or more coins using the full Chimera divergence engine (10 indicators × 3 presets × all timeframes). Much faster than full Chimera analysis since we only read the divergence section.

## Trigger Phrases
- "check divergences on BTC" / "any divs on ETH"
- "divergence scan" / "div scan BTC ETH"
- "bullish divs" / "bearish divs"
- "divergence only" / "quick div check"
- "what divs are showing"

## What This Shows
The 3 divergence presets catching different signal tiers:
- **SENSITIVE** (prd=3, maxPP=15, maxBars=200): Early signals, wide scan — more signals, may include weaker ones
- **STANDARD** (prd=5, maxPP=10, maxBars=100): TradingView default settings — balanced
- **STRONG** (prd=8, maxPP=5, maxBars=60): High-conviction reversals only, confirmed macro pivots

10 indicators checked per timeframe: MACD, MACD Histogram, RSI, Stochastic, CCI, Momentum, OBV, VWmacd (volume-weighted MACD), CMF (Chaikin Money Flow), MFI (Money Flow Index)

4 divergence types:
- ▲ REV+↑ (Regular Positive): price lower low + indicator higher low → **BULLISH REVERSAL**
- ▼ REV-↓ (Regular Negative): price higher high + indicator lower high → **BEARISH REVERSAL**
- ▲ CON+↑ (Hidden Positive): price higher low + indicator lower low → **BULLISH CONTINUATION**
- ▼ CON-↓ (Hidden Negative): price lower high + indicator higher high → **BEARISH CONTINUATION**

## Execution Steps

### Step 1: Run chimera_data.py on Windows
```powershell
$py  = "C:\Users\becke\AppData\Local\Programs\Python\Python313\python.exe"
$scr = "C:\Users\becke\claudecowork\trading_system\scripts\chimera_data.py"

Start-Process -FilePath $py `
  -ArgumentList @($scr, "BTC") `
  -WindowStyle Hidden
```

### Step 2: Wait and find the report
```powershell
Start-Sleep -Seconds 45
Get-ChildItem "C:\Users\becke\claudecowork\reports\" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
```

### Step 3: Read and extract only the divergence table
Read the newest report file using the Read tool:
```
/sessions/magical-keen-bardeen/mnt/claudecowork/reports/[filename]
```

Find the section starting with:
```
DIVERGENCE OVERVIEW
```

Read from that section through the `──────` line after the NET BULLISH/BEARISH summary.

### Step 4: Present to Sal
Show ONLY the divergence table and summary. Example format:

```
DIVERGENCE SCAN: BTC  [2026-02-18 10:00 UTC]

TF     1 SENSITIVE(prd3)         2 STANDARD(prd5)       3 STRONG(prd8)
─────  ────────────────────────  ─────────────────────  ─────────────────
1W     ▲3 ★★ MACD/RSI/Hist       ▲2 ★★ MACD/RSI         ○ clean
3D     ○ clean                   ○ clean                ○ clean
1D     ▼1 ★ OBV                  ○ clean                ○ clean
4H     ▲4 ★★ MACD/RSI/CMF/MFI   ▲3 ★★ RSI/CMF/MFI      ▲1 ★ RSI
1H     ▲5 ★★★ [multiple]         ▲3 ★★ MACD/RSI/Stoch   ○ clean
15M    ▲2 ★ RSI/MACD             ○ clean                ○ clean

NET BULLISH  (4 bull TF vs 1 bear TF)
STRONGEST: 1H SENSITIVE ▲BULL ★★★ (5/10 indicators)

→ READ: Strong bullish momentum on 1H/4H — multiple indicators confirming.
  Only 1D OBV bearish. Weekly bulls suggest larger move could be coming.
```

Then give 2-3 lines of interpretation:
- Which TFs have the strongest signal
- Whether it's reversals (REG) or continuations (HID)
- Whether signals are confirmed by multiple presets (more reliable)

## Interpretation Guide

**Multiple presets confirming same TF = HIGH CONFIDENCE**
- If 4H shows ▲ on all 3 presets → very strong signal
- If only SENSITIVE (prd3) catches it → early, may be noise

**Timeframe hierarchy**
- 1W/3D signals = macro (weeks ahead, high impact)
- 1D signals = swing trade (days ahead)
- 4H/2H = medium term setup
- 1H/15M = entry timing

**REV vs CON (shown as REV↑/CON↑ in full report)**
- REV+ bullish = reversal expected (price was falling, now flipping up)
- CON+ bullish = continuation expected (pullback in uptrend, will continue up)

## Windows Shell Command Template

```powershell
# Run divergence scan
$py  = "C:\Users\becke\AppData\Local\Programs\Python\Python313\python.exe"
$scr = "C:\Users\becke\claudecowork\trading_system\scripts\chimera_data.py"

# Single coin
Start-Process -FilePath $py -ArgumentList @($scr, "BTC") -WindowStyle Hidden

# Multi-coin
Start-Process -FilePath $py -ArgumentList @($scr, "BTC", "ETH", "SOL") -WindowStyle Hidden

# Wait, then find newest report
Start-Sleep -Seconds 50
$report = Get-ChildItem "C:\Users\becke\claudecowork\reports\" |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
Write-Output $report.FullName
```

## File Locations
| File | Path |
|------|------|
| Script (Windows) | `C:\Users\becke\claudecowork\trading_system\scripts\chimera_data.py` |
| Script (Linux) | `/sessions/magical-keen-bardeen/mnt/claudecowork/trading_system/scripts/chimera_data.py` |
| Reports (Windows) | `C:\Users\becke\claudecowork\reports\` |
| Reports (Linux) | `/sessions/magical-keen-bardeen/mnt/claudecowork/reports/` |
