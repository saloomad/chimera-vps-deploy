---
name: coinalyze-derivatives
description: >
  Fetch real-time and historical derivatives data from Coinalyze API.
  Use when Sal asks for: open interest, OI history, funding rate, liquidations,
  long/short ratio, predicted funding, derivatives data, perp data, futures data,
  "check OI", "funding rate BTC", "liquidation data", "how leveraged is the market",
  "are there big liquidations", "what's the OI trend", "coinalyze data".
  Uses Coinalyze API (40 req/min, free tier). API key: stored in skill.
---

# COINALYZE DERIVATIVES SKILL

## Purpose
Fetch professional derivatives market data from Coinalyze for any coin.
Provides what CCXT cannot: historical OI, funding history, liquidation events, L/S ratio trends.

## API Details
- **Base URL**: `https://api.coinalyze.net/v1/`
- **API Key**: `4c6dd80a-e6c6-4716-8db2-e18ab19b9b86`
- **Rate Limit**: 40 calls/minute
- **Auth**: Header `api_key: [key]`

## Available Endpoints

| Endpoint | What It Returns | Key Use |
|----------|----------------|---------|
| `/open-interest` | Current OI snapshot | Instant OI level |
| `/open-interest-history` | OHLC OI over time | OI trend analysis |
| `/funding-rate` | Current funding rate | Sentiment check |
| `/funding-rate-history` | Funding OHLC history | Funding trend |
| `/predicted-funding-rate` | Next predicted rate | Upcoming sentiment |
| `/predicted-funding-rate-history` | Predicted rate history | — |
| `/liquidation-history` | Long/short liquidations per period | Cascade risk |
| `/long-short-ratio-history` | L/S ratio over time | Crowd positioning |
| `/future-markets` | List of supported markets | Symbol lookup |

## Symbol Format
Coinalyze uses exchange-specific symbols. Format: `SYMBOL_PERP.EXCHANGE_CODE`

Common exchange codes:
| Exchange | Code |
|----------|------|
| Binance | A |
| OKX | B |
| Bybit | C |
| Bitget | E |
| Bitfinex | D |
| Deribit | F |

**Examples**:
- BTC on Binance: `BTCUSDT_PERP.A`
- ETH on Bybit: `ETHUSDT_PERP.C`
- BTC aggregated (all exchanges): use multiple symbols comma-separated

**To find available symbols for a coin**: call `/future-markets?api_key=KEY` and filter by currency

## Python Implementation Template

```python
import requests

COINALYZE_KEYS = [
    "4c6dd80a-e6c6-4716-8db2-e18ab19b9b86",  # Key 1
    "b340a512-9880-406a-adb6-52dac6b466c0",  # Key 2
    "d3aa1989-6450-4136-82a7-0569d0d92ca2",  # Key 3
]
BASE_URL = "https://api.coinalyze.net/v1"

def coinalyze_get(endpoint, params=None):
    """Generic Coinalyze API call."""
    headers = {"api_key": COINALYZE_KEY}
    url = f"{BASE_URL}/{endpoint}"
    r = requests.get(url, headers=headers, params=params or {}, timeout=15)
    r.raise_for_status()
    return r.json()

def get_oi_history(symbol, interval="1hour", from_ts=None, to_ts=None):
    """
    Open Interest history — OHLC format.
    interval: 1min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 12hour, daily
    Returns list of {t, o, h, l, c} dicts (t=unix timestamp, values in USD)
    """
    params = {"symbols": symbol, "interval": interval}
    if from_ts: params["from"] = from_ts
    if to_ts:   params["to"]   = to_ts
    return coinalyze_get("open-interest-history", params)

def get_funding_history(symbol, interval="1hour"):
    """
    Funding rate history — OHLC format.
    Returns {symbol, history: [{t, o, h, l, c}]} — c = latest rate per period
    """
    return coinalyze_get("funding-rate-history",
                         {"symbols": symbol, "interval": interval})

def get_liquidation_history(symbol, interval="1hour"):
    """
    Liquidation events — {t, l, s} where l=longs liquidated ($), s=shorts liquidated ($)
    Use to detect liquidation cascades and major events.
    """
    return coinalyze_get("liquidation-history",
                         {"symbols": symbol, "interval": interval})

def get_long_short_history(symbol, interval="1hour"):
    """
    Long/Short ratio over time — {t, o, h, l, c} where c = ratio at close of period
    ratio > 1 = more longs. ratio < 1 = more shorts.
    """
    return coinalyze_get("long-short-ratio-history",
                         {"symbols": symbol, "interval": interval})

def get_current_oi(symbol):
    """Current OI snapshot."""
    return coinalyze_get("open-interest", {"symbols": symbol})

def get_current_funding(symbol):
    """Current funding rate."""
    return coinalyze_get("funding-rate", {"symbols": symbol})

def get_predicted_funding(symbol):
    """Next predicted funding rate."""
    return coinalyze_get("predicted-funding-rate", {"symbols": symbol})
```

## How to Run from Cowork

Use Bash tool to execute Python directly in the VM:

```python
# Save as /sessions/.../mnt/claudecowork/trading_system/scripts/coinalyze_fetch.py
# Then run via Bash: python3 coinalyze_fetch.py BTC Binance
```

**Note**: This script CAN run in the VM (uses requests over HTTPS, not pip install needed — requests is built in).

Actually, use WebFetch tool for simple calls:
```
WebFetch("https://api.coinalyze.net/v1/open-interest?symbols=BTCUSDT_PERP.A",
         prompt="...",
         headers={"api_key": "4c6dd80a-e6c6-4716-8db2-e18ab19b9b86"})
```

Or run on Windows via Shell:
```powershell
$headers = @{"api_key" = "4c6dd80a-e6c6-4716-8db2-e18ab19b9b86"}
$r = Invoke-RestMethod -Uri "https://api.coinalyze.net/v1/open-interest?symbols=BTCUSDT_PERP.A" -Headers $headers
$r | ConvertTo-Json
```

## Standard Workflow

When Sal asks for derivatives data:

1. **Identify symbol**: Convert `BTC` → `BTCUSDT_PERP.A` (Binance) or ask which exchange
2. **Fetch 3 key metrics in parallel**:
   - OI history (last 24h, 1hour intervals)
   - Funding history (last 24h, 1hour intervals)
   - Liquidation history (last 24h, 1hour intervals)
3. **Analyze trends**:
   - OI rising + price rising = healthy uptrend (real buyers)
   - OI rising + price falling = leveraged shorts piling in (squeeze risk)
   - OI falling + price rising = short squeeze in progress
   - OI falling + price falling = deleveraging (can accelerate down)
   - Funding >0.1% = longs overleveraged, bearish signal
   - Funding <-0.05% = shorts overleveraged, bullish signal
4. **Report to Sal**: Current OI, 24h change, funding trend, any liquidation spikes

## Output Format Template

```
══════════════════════════════════════════════
  COINALYZE DERIVATIVES — BTC [BTCUSDT_PERP.A]
══════════════════════════════════════════════
  Open Interest:   $12.4B  (24h change: +3.2% ↑ OI rising)
  Funding Rate:    +0.018%  (longs paying | annualized: +19.7%)
  Predicted Fund:  +0.021%  (expected to rise → longs more overleveraged)

  24h Liquidations:
    Longs: $45.2M  | Shorts: $12.8M
    Biggest spike: 14:00 UTC — $8.2M longs wiped

  L/S Ratio (24h trend):
    Current: 1.42 (more longs)  | 24h ago: 1.28
    Trend: INCREASING LONGS — retail adding long exposure on decline

  Derivative Divergence vs Price:
    ↑ Price, ↑ OI = conviction rally — real buyers
    ↑ Funding trend = longs at risk if price reverses

  ⚠ RISK FLAGS:
    - Funding extreme (>0.1%): NO
    - OI at ATH: NO
    - Major liq cascade: NO
══════════════════════════════════════════════
```

## Common Symbol Lookup

| Coin | Binance | Bybit | Bitget |
|------|---------|-------|--------|
| BTC | BTCUSDT_PERP.A | BTCUSDT_PERP.C | BTCUSDT_PERP.E |
| ETH | ETHUSDT_PERP.A | ETHUSDT_PERP.C | ETHUSDT_PERP.E |
| SOL | SOLUSDT_PERP.A | SOLUSDT_PERP.C | SOLUSDT_PERP.E |
| BNB | BNBUSDT_PERP.A | — | — |
| XRP | XRPUSDT_PERP.A | XRPUSDT_PERP.C | — |

For aggregated (all exchanges): comma-separate multiple symbols.
Example: `symbols=BTCUSDT_PERP.A,BTCUSDT_PERP.B,BTCUSDT_PERP.C`

## Rate Limit
40 calls/minute. For multi-coin, batch symbols: `symbols=BTCUSDT_PERP.A,ETHUSDT_PERP.A`
