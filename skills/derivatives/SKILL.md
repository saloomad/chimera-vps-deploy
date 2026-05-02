---
name: derivatives
description: >
  Fetch real-time derivatives data combining Coinalyze API (free) for OI/funding/L/S/liquidations.
  Use when Sal asks: "derivatives", "check OI", "open interest", "funding rate",
  "long short ratio", "liquidations today", "how leveraged is the market",
  "are shorts or longs dominant", "how much OI", "funding extreme",
  "derivatives BTC ETH", "perp data", "futures data", "coinalyze",
  "OI trend", "is funding positive or negative", "squeeze risk".
  Note: CoinGlass free tier is mostly locked (requires paid plan). Use Coinalyze for all data.
---

# DERIVATIVES SKILL

## Purpose
Fetch professional-grade crypto derivatives data using the Coinalyze API (free, 40 req/min).
Provides what price charts alone can't show: leverage positioning, funding sentiment,
liquidation risk, and long/short crowd positioning.

## What This Tells You
| Metric | What It Means |
|--------|--------------|
| **Open Interest** | Total USD value of open contracts — rising OI = new money entering |
| **OI 24h Change** | OI rising with price = conviction. OI rising against price = squeeze risk |
| **Funding Rate** | Positive = longs paying shorts (longs overleveraged). Negative = shorts paying |
| **Predicted Funding** | What the next funding period will be — trend indicator |
| **Long/Short Ratio** | >1 = more longs. <1 = more shorts. Extreme readings = contrarian signal |
| **Liquidations 24h** | How many longs vs shorts got wiped out — spikes = forced selling |

## Key Interpretations
- **OI ↑ + Price ↑** = Healthy uptrend (real buyers entering)
- **OI ↑ + Price ↓** = Shorts piling in (potential short squeeze)
- **OI ↓ + Price ↑** = Short squeeze in progress
- **OI ↓ + Price ↓** = Deleveraging (can accelerate the dump)
- **Funding >+0.1%** = Longs extremely overleveraged → bearish signal (flush incoming)
- **Funding <-0.05%** = Shorts extremely overleveraged → bullish signal (squeeze incoming)
- **L/S ratio rising** = Retail getting more long → often fades, contrarian bearish
- **Big long liquidations** = Cascading stops hit, potential reversal zone

## API Details
- **Provider**: Coinalyze — https://api.coinalyze.net/v1/
- **API Keys (rotate on 401/429)**:
  - Key 1: `4c6dd80a-e6c6-4716-8db2-e18ab19b9b86`
  - Key 2: `b340a512-9880-406a-adb6-52dac6b466c0`
  - Key 3: `d3aa1989-6450-4136-82a7-0569d0d92ca2`
- **Rate Limit**: 40 calls/minute per key (free forever)
- **Auth**: Header `api_key: [key]`
- **Default exchange**: Binance perpetual (code: `A`) — broadest data

## Symbol Format
`BTCUSDT_PERP.A` where:
- `BTCUSDT` = base/quote pair
- `PERP` = perpetual futures
- `.A` = Binance | `.B` = OKX | `.C` = Bybit | `.E` = Bitget

## Endpoints Used
| Endpoint | Data | Interval |
|----------|------|---------|
| `/open-interest` | Current OI snapshot | — |
| `/open-interest-history` | OI OHLC over 24h | 1hour |
| `/funding-rate` | Current funding rate | — |
| `/predicted-funding-rate` | Next predicted funding | — |
| `/long-short-ratio-history` | L/S ratio over 24h | 1hour |
| `/liquidation-history` | Long + short liquidations | 1hour |

## CoinGlass Status (FYI)
CoinGlass API key `08d148e321d64e85b0283aded27c84c9` is on **free tier**.
Most endpoints return `{"code":"40001","msg":"Upgrade plan"}`.
**Only usable CoinGlass feature is screenshots of liquidation heat maps → use the liquidation-vision-analyzer skill for that.**
Do NOT try to fetch CoinGlass API data programmatically on free tier — it won't work.

## How to Run from Cowork

Option A — **Run via Windows PowerShell (Shell tool)**:
```powershell
$keys = @("4c6dd80a-e6c6-4716-8db2-e18ab19b9b86","b340a512-9880-406a-adb6-52dac6b466c0","d3aa1989-6450-4136-82a7-0569d0d92ca2")
$key  = $keys[0]  # rotates automatically in chimera_data.py
$base = "https://api.coinalyze.net/v1"
$sym  = "BTCUSDT_PERP.A"
$hdrs = @{"api_key" = $key}

# Current OI
$oi = Invoke-RestMethod -Uri "$base/open-interest?symbols=$sym" -Headers $hdrs
$oi | ConvertTo-Json

# Current funding rate
$fr = Invoke-RestMethod -Uri "$base/funding-rate?symbols=$sym" -Headers $hdrs
$fr | ConvertTo-Json

# L/S ratio history (last 24h)
$ts_now = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$ts_24h = $ts_now - 86400
$ls = Invoke-RestMethod -Uri "$base/long-short-ratio-history?symbols=$sym&interval=1hour&from=$ts_24h&to=$ts_now" -Headers $hdrs
$ls | ConvertTo-Json -Depth 5
```

Option B — **chimera_data.py auto-fetches it** (already integrated):
When you run `chimera_data.py BTC` (real mode, not demo), it automatically calls `fetch_coinalyze()` and shows:
1. SNAPSHOT section: `DERIV OI 79,455 | Fund +0.003% neutral | L/S 0.9876`
2. DERIVATIVES DETAIL section: full breakdown

## Python Template (for scripts)
```python
import requests
from datetime import datetime, timezone

COINALYZE_KEYS = [
    "4c6dd80a-e6c6-4716-8db2-e18ab19b9b86",  # Key 1
    "b340a512-9880-406a-adb6-52dac6b466c0",  # Key 2
    "d3aa1989-6450-4136-82a7-0569d0d92ca2",  # Key 3
]
COINALYZE_BASE = "https://api.coinalyze.net/v1"

def coinalyze_get(endpoint, params=None):
    headers = {"api_key": COINALYZE_KEY}
    r = requests.get(f"{COINALYZE_BASE}/{endpoint}",
                     headers=headers, params=params or {}, timeout=10)
    r.raise_for_status()
    return r.json()

# Quick BTC derivatives snapshot
sym = "BTCUSDT_PERP.A"
oi  = coinalyze_get("open-interest", {"symbols": sym})
fr  = coinalyze_get("funding-rate", {"symbols": sym})
pred = coinalyze_get("predicted-funding-rate", {"symbols": sym})

now_ts  = int(datetime.now(timezone.utc).timestamp())
day_ago = now_ts - 86400
ls  = coinalyze_get("long-short-ratio-history",
                    {"symbols": sym, "interval": "1hour", "from": day_ago, "to": now_ts})
liq = coinalyze_get("liquidation-history",
                    {"symbols": sym, "interval": "1hour", "from": day_ago, "to": now_ts})
```

## Standard Workflow

When Sal asks for derivatives data:

1. **Identify coins**: Default to BTC on Binance (BTCUSDT_PERP.A)
2. **Use Windows Shell** to call Coinalyze endpoints
3. **Parse and analyze**:
   - Is OI rising or falling vs 24h ago?
   - Is funding positive, negative, or extreme?
   - Is L/S ratio rising (more longs) or falling (more shorts)?
   - Any liquidation spikes in last 24h?
4. **Give Sal the verdict** in output format below

## Output Format

```
══════════════════════════════════════════════
  DERIVATIVES — BTC  [BTCUSDT_PERP.A | Binance]
══════════════════════════════════════════════
  Open Interest:    $12.4B  │ 24h change: +3.2% ↑ (OI rising)
  Funding Rate:     +0.018%  (annualized: +19.7%)  longs paying
  Predicted Funding: +0.021%  (rising → longs more overleveraged next period)

  Long/Short Ratio (24h trend):
    Current: 1.42  │  24h ago: 1.28  │  trend: LONGS INCREASING
    → Retail adding long exposure — often contrarian bearish

  Liquidations 24h:
    Longs liquidated:  $45.2M
    Shorts liquidated: $12.8M
    Biggest spike:     $8.2M  (16:00 UTC — longs got flushed)
    Dominant:          LONGS being liquidated

  ⚠ RISK FLAGS:
    Funding extreme (>0.1%): NO
    OI at rising trend: YES (longs building)
    Major liq cascade: NO (no single spike >$20M)

  VERDICT: Market is long-biased with rising OI — watch for squeeze
           if price drops. Funding manageable (not extreme yet).
══════════════════════════════════════════════
```

## Common Symbols Reference
| Coin | Binance | Bybit | Bitget |
|------|---------|-------|--------|
| BTC | BTCUSDT_PERP.A | BTCUSDT_PERP.C | BTCUSDT_PERP.E |
| ETH | ETHUSDT_PERP.A | ETHUSDT_PERP.C | ETHUSDT_PERP.E |
| SOL | SOLUSDT_PERP.A | SOLUSDT_PERP.C | SOLUSDT_PERP.E |
| BNB | BNBUSDT_PERP.A | — | — |
| XRP | XRPUSDT_PERP.A | XRPUSDT_PERP.C | — |

For aggregated across exchanges: comma-separate symbols
`symbols=BTCUSDT_PERP.A,BTCUSDT_PERP.C,BTCUSDT_PERP.E`

## Rate Limit Notes
- 40 calls/minute on free tier
- Batch with comma-separated symbols to save calls
- chimera_data.py makes ~6 calls per coin (stays well within limits)
