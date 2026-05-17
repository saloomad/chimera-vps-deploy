---
name: news-reader
description: >
  Read and analyze the latest news from NEWS.json — crypto, macro, geopolitical.
  Gives a structured verdict on market impact, trending coins, and critical alerts.
  Covers: CryptoPanic, CoinTelegraph, CoinDesk, Decrypt, BeInCrypto (crypto),
  GDELT (geopolitical: wars, tariffs, sanctions), NewsAPI (macro headlines).
  Use when Sal asks: "what's the news", "any news today", "news impact", "check news",
  "what happened in crypto", "any critical news", "macro news", "geopolitical news",
  "crypto news", "news for BTC", "news on ETH", "latest headlines", "market news",
  "what's moving the market", "any important news", "news summary", "news update",
  "tariff news", "war news", "economic news", "check the headlines".
triggers:
  - what's the news
  - any news
  - news impact
  - check news
  - latest headlines
  - market news
  - what happened in crypto
  - any critical news
  - macro news
  - geopolitical news
  - crypto news
  - news summary
  - news update
  - tariff news
output_file: Z:\reports\auto\NEWS.json
---

# SKILL: news-reader

## What This Skill Does

Reads `NEWS.json` (auto-updated every 30 min by `news_fetcher.py`) and gives Sal a
structured verdict on what's happening in the market, what matters, and how it impacts
the trading bias.

This feeds **Step 1: Macro Bias** — news is the first filter before any setup.

---

## Data Sources Covered

| Source | Type | What It Covers |
|--------|------|----------------|
| **CryptoPanic** | Crypto | Community-voted crypto news, coin-tagged, bullish/bearish votes |
| **CoinTelegraph** | Crypto RSS | Industry news, regulation, adoption |
| **CoinDesk** | Crypto RSS | Market analysis, on-chain data |
| **Decrypt** | Crypto RSS | Consumer crypto, DeFi, NFT |
| **BeInCrypto** | Crypto RSS | Altcoin coverage, whale tracking |
| **GDELT** | Geopolitical | Wars, tariffs, sanctions, trade disputes |
| **NewsAPI** | Macro | US economy, Fed commentary, stock market |

---

## File Location

```
Z:\reports\auto\NEWS.json          ← primary (Linux, updated every 30 min)
```

---

## JSON Structure

```json
{
  "timestamp": "2026-02-22T01:31:05Z",
  "total_articles": 6,
  "critical_alerts": 2,
  "market_impact": "CRITICAL",          // CRITICAL | HIGH | MEDIUM | LOW | NEUTRAL
  "market_impact_reason": "tariff",     // reason string
  "trump_mentions": 0,                  // Trump policy mentions (market-moving)
  "trending_coins": ["ETH"],            // coins actively mentioned
  "affected_assets": ["BTC","ETH","STOCKS"],

  "crypto_news": [
    {
      "title": "...",
      "source": "CoinTelegraph",
      "url": "...",
      "published_at": "...",
      "hours_ago": 3.5,
      "coins_mentioned": ["ETH"],
      "votes_positive": 10,             // CryptoPanic only
      "votes_negative": 2,              // CryptoPanic only
      "is_important": true,
      "sentiment_label": "NEUTRAL"      // BULLISH | BEARISH | NEUTRAL
    }
  ],

  "macro_news": [ ... ],                // same structure — macro/econ headlines
  "geopolitical_news": [ ... ]          // same structure — GDELT wars/tariffs
}
```

---

## Analysis Rules

### Step 1 — Check market_impact First
```
"CRITICAL" → HIGH ALERT. Do NOT trade until you understand what's happening.
             Read market_impact_reason. Usually: tariffs, war, major regulation.
"HIGH"      → Elevated risk. Wait for dust to settle before entries.
"MEDIUM"    → Note it. Trade with tighter stops.
"LOW/NEUTRAL" → Normal environment. Proceed.
```

### Step 2 — Check critical_alerts Count
```
> 0 → At least one major event. Read the specific articles.
= 0 → No emergency events today.
```

### Step 3 — Coin-specific impact
```
"trending_coins": ["ETH"] → ETH is the focus coin right now.
"coins_mentioned" in article → Check if your trade coin is named.
```

### Step 4 — Sentiment direction
```
"sentiment_label": "BULLISH"  → Positive coverage → supportive of longs
"sentiment_label": "BEARISH"  → Negative coverage → supportive of shorts
"sentiment_label": "NEUTRAL"  → No directional push
votes_positive >> votes_negative (CryptoPanic) → community is bullish on this
```

### Step 5 — Geopolitical / Macro flags
```
Tariffs       → Crypto often initially sells off, then may recover
War/sanctions → Flight to safety, USD up = crypto pressure
Fed news      → Any mention of rate changes = high volatility incoming
Earnings      → NVDA/AAPL miss = risk-off = crypto sells
```

### Step 6 — Staleness check
```
If timestamp > 60 min ago → news_fetcher.py may have failed → check SCRIPT_HEALTH.json
If total_articles < 3 → API issues, treat data as incomplete
```

---

## Output Format

When Sal asks for news, give this structured response:

```
📰 NEWS SNAPSHOT — [timestamp]
════════════════════════════════
Market Impact: [CRITICAL/HIGH/MEDIUM/LOW]  ← [reason]
Critical Alerts: [N]
Trending Coins: [list]

📌 TOP STORIES:
  1. [title] — [source], [Xh ago]
     → Impact: [your 1-line analysis]
  2. [title] — [source], [Xh ago]
     → Impact: [your 1-line analysis]
  [... top 3-5 only]

🌍 MACRO/GEO FLAGS:
  [Any tariff/war/Fed mentions — if none, say "Clean"]

💡 NEWS BIAS: [BEARISH / BULLISH / MIXED / NEUTRAL]
   [1 sentence verdict: "Tariff news is the dominant risk driver.
    Crypto unfazed so far but watch for escalation."]
════════════════════════════════
```

---

## Where This Fits in the Pipeline

```
Step 1: MACRO BIAS
  ├── NEWS (this skill) → market sentiment, critical events
  ├── MACRO.json → upcoming economic events
  ├── Derivatives → OI/funding/liquidations
  └── ALTFINS trend scores → technical macro
         ↓
Step 2: Setup Identification
Step 3: Trade Execution
```

**Rule:** If news_impact = CRITICAL → flag it **before** any setup discussion.
News can override a perfect technical setup. A clean chart with a war starting = skip.

---

## Run On-Demand (Refresh News)

```bash
# Windows
C:\Users\becke\AppData\Local\Programs\Python\Python313\python.exe trading_system/scripts/news_fetcher.py

# Linux (via SSH)
ssh root@100.67.172.114 "cd /root/openclawtrading && python3 trading_system/scripts/news_fetcher.py"
```

## Key Agent Rules for OpenClaw

1. **Always check market_impact first** — if CRITICAL, escalate to TO_ARCHITECT.md immediately
2. **Don't summarize all articles** — pick top 3 most impactful only
3. **Hours_ago matters** — anything > 12h is background context, < 3h is active
4. **Crypto sentiment ≠ macro sentiment** — separate them in verdict
5. **Trump_mentions > 0** — flag it. Trump tweets move markets unpredictably
6. **Geopolitical + CRITICAL = pause all trades** — message Architect immediately
