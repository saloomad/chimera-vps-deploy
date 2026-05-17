---
name: tradingview-mcp-openclaw
description: OpenClaw Linux agents -- TradingView MCP unified skill. Routes between tradingview-jackson (local on Linux, 81 tools, requires TradingView Desktop running) and tvremix (cloud API, 27 tools, 15/day per key). OpenClaw uses keys TVREMIX_KEY_3 and TVREMIX_KEY_4. Use tradingview-jackson for chart control, Pine Script, alerts, screenshots. Use tvremix for SMC analysis, multi-TF technicals, screener, fundamentals, news. OpenClaw agents should call tvremix through the usage tracker wrapper to auto-switch keys and stay within limits.
triggers:
  - openclaw tradingview
  - tvremix openclaw
  - linux tradingview
  - openclaw screener
  - openclaw SMC
  - openclaw chart
---

# TradingView MCP -- OpenClaw Skill

*For OpenClaw Linux agents -- paths and keys specific to Linux deployment*

---

## OpenClaw Configuration

### API Keys (set in `/root/.chimera.env`)
```bash
TVREMIX_KEY_3="tvr_b_hLS7_ILX8RnNKoBrgyhMLl0QHJBPUlrTZN566"
TVREMIX_KEY_4="tvr_CuI44g_Mv5QkYoW9oxwspLHojENahbiEaKbgXsf"
```

### Usage Tracker
```bash
# Status check
python3 /root/openclawtrading/scripts/tvremix_usage_tracker.py --status --profile openclaw

# Test keys
python3 /root/openclawtrading/scripts/tvremix_usage_tracker.py --test-keys --profile openclaw

# Make a tracked call
python3 /root/openclawtrading/scripts/tvremix_usage_tracker.py \
  --call analyze_smc_tool \
  --json '{"symbol": "BINANCE:BTCUSDT", "interval": "4h"}' \
  --profile openclaw
```

### tradingview-jackson on Linux
```bash
# Start TradingView Desktop with CDP
/opt/tradingview/tradingview --remote-debugging-port=9222 &

# Or via systemd service (if configured)
systemctl start tradingview-cdp

# Health check
curl -s http://localhost:9222/json/version
```

---

## Agent Routing for OpenClaw

| OpenClaw Agent | Primary Server | Tasks |
|----------------|---------------|-------|
| `market-scanner` | tvremix | `run_screener`, `rank_symbol_setups`, `analyze_sector_tool` |
| `technical-analyst` | tvremix + jackson | `analyze_smc_tool`, `analyze_multi_timeframe` (tvremix); chart confirmation (jackson) |
| `macro-analyst` | tvremix | `get_economic_calendar`, `get_news`, `web_search` |
| `alert-engine` | tradingview-jackson | `alert_create`, `alert_list`, `alert_delete` |
| `portfolio-manager` | tvremix | `get_portfolio`, `calculate_correlation_tool` |
| `options-trader` | tvremix | `get_option_chain`, `get_option_expirations` |

---

## OpenClaw Cron Jobs

```bash
# Daily macro check (tvremix: 1 call)
0 6 * * * python3 /root/openclawtrading/scripts/tvremix_usage_tracker.py \
  --call get_economic_calendar \
  --json '{"days_ahead": 3, "importance": ["high"]}' \
  --profile openclaw \
  >> /root/openclawtrading/reports/macro_calendar.json

# Hourly news scan for BTC (tvremix: 1 call)
0 * * * * python3 /root/openclawtrading/scripts/tvremix_usage_tracker.py \
  --call get_news \
  --json '{"symbol": "BTCUSDT", "limit": 5}' \
  --profile openclaw \
  >> /root/openclawtrading/reports/btc_news.json

# Every 4h: SMC analysis for BTC (tvremix: 1 call)
0 */4 * * * python3 /root/openclawtrading/scripts/tvremix_usage_tracker.py \
  --call analyze_smc_tool \
  --json '{"symbol": "BINANCE:BTCUSDT", "interval": "4h", "count": 300}' \
  --profile openclaw \
  > /root/openclawtrading/reports/btc_smc.json
```

---

## File Paths

| File | Linux Path |
|------|-----------|
| Usage tracker | `/root/openclawtrading/scripts/tvremix_usage_tracker.py` |
| Usage state | `/root/.tvremix_usage.json` |
| tradingview-jackson tools | `/root/openclawtrading/agents/spawned/tradingview-chart/TOOLS.md` |
| Main skill | `/root/openclawtrading/skills/tradingview-mcp/SKILL.md` |
| Hermes skill | `/root/openclawtrading/skills/tradingview-mcp/SKILL-hermes.md` |
| Prompt guide | `/root/openclawtrading/skills/tradingview-mcp/TVREMIX_PROMPT_GUIDE.md` |

---

*OpenClaw TradingView MCP Skill -- v1.0 | 2026-04-26*
