---
name: chimera-trading-consultant
description: >
  Hermes's trading consultant skill — activated when Deezoh spawns Hermes as a
  consultant subagent. Provides full market analysis, pattern recognition, mistake
  identification, and system improvement suggestions for Deezoh's trading decisions.
---

# Chimera Trading Consultant Skill

## What This Is

When Deezoh spawns Hermes as a consultant, this skill is the brain. It tells
Hermes HOW to analyze what Deezoh did, WHAT to look for, and HOW to deliver
actionable consultation.

## What Hermes Has Available

### Market Analysis Tools

| Tool | What It Does |
|------|-------------|
| **Trading Analyst Script** | `~/.hermes/scripts/chimera_trading_analyst.py` — runs full multi-TF analysis (1W/3D/1D/4H/1H/15M) for BTC, ETH, SOL. RSI, MACD, EMA, ATR, S/R. Writes to `C:/Users/becke/claudecowork/consultation/HERMES_CONSULTATION.md` |
| **21 Trading Skills** | All installed in `~/.hermes/skills/` — technical-analysis, divergence-scanner, fvg-detector, order-block-detector, volume-analyzer, volume-profile, coinalyze-derivatives, chimera-bitget-derivatives-data, macro-analyst, market-intel, sentiment-analyst, news-briefing, tradingview-screener, etc. |
| **Space Agent VPS** | Can read chimera-data files via `http://100.67.172.114:3000/api/file_read` — MACRO.json, WATCHLISTS.json, ACTIVE_TRADES.json |
| **Deezoh Context** | Read from Deezoh's workspace: LESSONS.md, kanban.db, pipeline round files |

### The Consultation Output

Every time the trading analyst cron runs (every 4h), it writes:

```
C:/Users/becke/claudecowork/consultation/HERMES_CONSULTATION.md
C:/Users/becke/claudecowork/consultation/HERMES_CONSULTATION.json
```

This contains:
- **Macro overview** — BTC dominance, Fear & Greed, market bias
- **Per-symbol analysis** — all 6 TFs, RSI/MACD/trend/momentum per TF
- **Cross-symbol summary** — direction, RSI zone, signal strength per symbol
- **Hermes consultation** — overall bias, RSI extremes, divergence watch, actionable notes

## How Deezoh Spawns Hermes

Deezoh can spawn Hermes as a consultant by including this in its prompt:

```
You may spawn Hermes (hermes-consultant) to review your analysis.
Hermes has live market data and 21 trading skills.
Run: ~/.hermes/scripts/chimera_trading_analyst.py
Read: C:/Users/becke/claudecowork/consultation/HERMES_CONSULTATION.md
```

## What To Consult On

### 1. Catalyst Detection
- Did Deezoh identify the key catalysts for the session?
- Are there news/events/DVF/ONET patterns it may have missed?
- Check: news-briefing skill + macro-calendar skill

### 2. Macro Bias
- Did Deezoh read the macro correctly?
- Is the bias (LONG/SHORT/NEUTRAL) consistent with BTC dominance, funding, Fear & Greed?
- Check: MACRO.json from Space Agent VPS + macro-analyst skill

### 3. Signal Detection
- Did Deezoh catch the key divergences, FVGs, order blocks?
- Are there setups on 4H/1H that Deezoh may have missed?
- Check: divergence-scanner + fvg-detector + order-block-detector skills

### 4. Decision Quality
- What did Deezoh decide? Check the LESSONS.md or pipeline round file
- Was the entry/exit timing right given the RSI/MACD state?
- Was position sizing consistent with the signal strength?

### 5. Pattern Recognition (Learning)
- Look at Deezoh's last 5 decisions in the kanban
- Any recurring mistakes? (e.g., always entry too early, wrong TF confirmation)
- Use: codex-lesson-harvester pattern recognition approach

### 6. System Improvements
- Is the lobster pipeline missing anything?
- Are there gaps in the analysis workflow?
- Should a new check/skill be added?

## Consultation Output Format

When Hermes consults for Deezoh, structure the output as:

```
HERMES CONSULTATION
[Symbol/Context Being Reviewed]

## What Deezoh Got Right
- Bullet points of good calls

## What May Be Missing / At Risk
- Catalysts missed
- Signals not confirmed
- Wrong bias given macro

## Suggested Adjustments
- Specific changes to the position/plan
- Additional checks to run

## System Improvements (if any)
- Gaps in workflow or skills
- New patterns to watch for
```

## Key Files To Read

| File | Purpose |
|------|---------|
| `C:/Users/becke/claudecowork/consultation/HERMES_CONSULTATION.md` | Latest market analysis |
| `C:/Users/becke/claudecowork/consultation/HERMES_CONSULTATION.json` | Structured data for programmatic use |
| `http://100.67.172.114:3000/api/file_read` + path `/srv/space/customware/L2/user/chimera-data/MACRO.json` | Live macro |
| `http://100.67.172.114:3000/api/file_read` + path `/srv/space/customware/L2/user/chimera-data/WATCHLISTS.json` | Deezoh's watchlists |
| `C:/Users/becke/.openclaw/deezoh/LESSONS.md` | Deezoh's historical mistakes |

## Skills To Use Per Consultation Type

| Consultation Type | Primary Skills |
|------------------|---------------|
| Catalyst/News | news-briefing, macro-calendar |
| Macro Bias | macro-analyst, market-intel |
| Technical Signals | technical-analysis, divergence-scanner, fvg-detector, order-block-detector |
| Derivatives Context | coinalyze-derivatives, chimera-bitget-derivatives-data |
| Volume Profile | volume-analyzer, volume-profile |
| Screener | tradingview-screener |
| Pattern Learning | chimera-divergence (historian), historical-market-context |

## Trigger Phrases

Deezoh should activate Hermes consultant when:
- "Hermes, review this setup"
- "What's the macro context for [symbol]?"
- "Did I miss any divergences?"
- "Is my bias correct given current conditions?"
- "What did I get wrong in my last trade?"
- "Any patterns I'm repeating?"
- "What does the 4h chart look like?"
