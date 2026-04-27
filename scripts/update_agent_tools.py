#!/usr/bin/env python3
"""
Bulk update agent TOOLS.md files on Kimi VPS.
Generates skill-aware TOOLS.md for each agent based on its role.
"""
import os
import sys

AGENTS_DIR = "/root/.openclaw/workspace/agents"

# Skill catalog
SKILLS = {
    "chimera-derivatives": "OI, funding, L/S ratio, liquidations (Coinalyze/Bitget)",
    "chimera-tradingview-screener": "Screen 59K+ coins by RSI/MACD/ADX",
    "chimera-altfins": "BTC/ETH/SOL RSI, MACD, EMA, patterns",
    "chimera-macro-calendar": "Economic calendar, CPI, FOMC",
    "chimera-news-reader": "Breaking news, narratives",
    "chimera-divergence": "Divergence detection",
    "chimera-fvg-detector": "Fair Value Gaps",
    "chimera-order-block-detector": "Institutional Order Blocks",
    "chimera-volume-profile": "POC, VAH, VAL",
    "chimera-candlestick-classifier": "Pattern recognition",
    "chimera-liquidation-vision-analyzer": "Interpret heatmap screenshots",
    "chimera-indicator-calculator": "Manual RSI/MACD/BB/Stoch/ADX",
    "chimera-volume-analyzer": "Volume confirmation",
    "chimera-full-analysis": "Complete regime-to-entry pipeline",
    "tradingview-mcp": "TradingView Desktop control (jackson/tvremix)",
    "technical-analysis": "Technical analysis with TV data",
    "macro-analyst": "Macro analysis and bias building",
    "stock-analysis": "Stock market analysis",
    "orchestration": "Multi-agent orchestration and pipelines",
    "orchestration-engine": "Run pipeline phases, manage workers",
    "project-management": "Track projects across sessions",
    "project-thread-manager": "Create/update project threads",
    "github-manager": "GitHub repo management and sync",
    "sentiment-analyst": "Market sentiment analysis",
    "market-intel": "Market intelligence aggregation",
    "computer-use": "Browser automation and screenshots",
    "minimax-usage": "MiniMax model routing and usage",
    "model-routing": "Route tasks to optimal models",
    "news-briefing": "News aggregation and briefing",
    "backtesting-simulation": "Backtest strategies",
    "hyperliquid-analyzer": "Hyperliquid exchange analysis",
    "go-trader": "Go-based trading utilities",
    "clawhub-discovery": "Discover and install skills from ClawHub",
    "claude-codex-orchestration": "Claude Code orchestration patterns",
    "state-tracker": "Track system and project state",
    "gateway-ai-repair": "Repair AI gateway issues",
    "windows-ssh-connect": "SSH to Windows from VPS",
    "quality-gate": "Quality assurance gates",
    "skill-vetter": "Vet and validate skills",
    "reasoning-compliance": "Ensure reasoning compliance",
    "market-analysis-collection": "Collect market analysis data",
    "market-analysis-hub": "Hub for market analysis",
    "content-research-writer": "Research and write content",
    "decision-council": "Decision council pattern",
    "openclaw-monitor-and-brief": "Monitor OpenClaw and brief",
    "openclaw-master-skills": "Master skills reference",
    "agent-instruction-optimization": "Optimize agent instructions",
    "prompt-engineer": "Prompt engineering",
    "prompt-upgrade-engineer": "Upgrade prompts",
}

AGENT_SKILL_MAP = {
    "chart-analyzer": ["chimera-altfins", "chimera-divergence", "chimera-fvg-detector",
                       "chimera-order-block-detector", "chimera-volume-profile",
                       "chimera-candlestick-classifier", "technical-analysis", "tradingview-mcp"],
    "indicator-analyst": ["chimera-indicator-calculator", "chimera-altfins",
                          "chimera-divergence", "technical-analysis"],
    "macro-bias": ["chimera-macro-calendar", "chimera-derivatives", "macro-analyst",
                   "market-intel", "news-briefing"],
    "screener": ["chimera-tradingview-screener", "chimera-altfins", "chimera-derivatives"],
    "strategy": ["chimera-full-analysis", "chimera-fvg-detector",
                 "chimera-order-block-detector", "backtesting-simulation"],
    "execution": ["chimera-derivatives", "go-trader", "hyperliquid-analyzer"],
    "catalyst": ["chimera-news-reader", "chimera-macro-calendar", "news-briefing", "market-intel"],
    "entry-watch": ["chimera-fvg-detector", "chimera-order-block-detector",
                    "chimera-volume-profile", "chimera-divergence"],
    "market-maker": ["chimera-derivatives", "chimera-liquidation-vision-analyzer", "market-intel"],
    "risk-engine": ["chimera-derivatives", "chimera-volume-analyzer", "backtesting-simulation"],
    "trade-judge": ["chimera-full-analysis", "chimera-divergence", "chimera-indicator-calculator"],
    "orchestrator": ["orchestration", "orchestration-engine", "project-management",
                     "project-thread-manager", "model-routing"],
    "project-manager": ["project-management", "project-thread-manager",
                        "orchestration", "state-tracker"],
    "architect": ["orchestration", "project-management", "github-manager",
                  "model-routing", "clawhub-discovery"],
    "architect-codex": ["orchestration", "project-management", "github-manager",
                        "claude-codex-orchestration"],
    "deezoh": ["chimera-full-analysis", "chimera-derivatives", "chimera-news-reader",
               "orchestration", "project-management", "minimax-usage", "tradingview-mcp"],
    "cron-manager": ["orchestration", "project-management", "state-tracker"],
    "system-ops": ["orchestration", "gateway-ai-repair", "windows-ssh-connect"],
    "manager": ["orchestration", "project-management", "decision-council"],
    "youtube-analyst": ["chimera-news-reader", "news-briefing", "sentiment-analyst"],
    "bitget-analyst": ["chimera-derivatives", "market-intel", "technical-analysis"],
    "hermes-lead": ["orchestration", "project-management", "model-routing"],
    "hermes-advisor": ["model-routing", "minimax-usage", "model-intelligence"],
    "news-monitor": ["chimera-news-reader", "news-briefing", "market-intel"],
    "growth-manager": ["orchestration", "project-management", "content-research-writer"],
    "prompt-engineer": ["prompt-engineer", "prompt-upgrade-engineer", "agent-instruction-optimization"],
    "auditor": ["quality-gate", "skill-vetter", "reasoning-compliance"],
    "context-analyst": ["market-analysis-collection", "market-analysis-hub", "market-intel"],
    "pipeline-watchdog": ["orchestration", "orchestration-checker", "state-tracker"],
    "position-sizer": ["chimera-derivatives", "backtesting-simulation"],
    "research-agent": ["chimera-news-reader", "news-briefing", "content-research-writer"],
    "watchdog": ["orchestration", "gateway-ai-repair", "openclaw-monitor-and-brief"],
    "skill-navigator": ["clawhub-discovery", "skill-vetter", "openclaw-master-skills"],
}

SCRIPTS_NO_SKILL = {
    "derivatives_fetcher.py": "Bitget bulk tickers (537 symbols, funding, OI) — free API",
    "liquidation_heatmap.py": "Browser screenshot of CoinGlass heatmaps",
    "coinglass_maxpain_scraper.py": "Browser scrape of CoinGlass max-pain table",
    "macro_bias_builder.py": "Aggregates macro signals into MACRO_BIAS.json verdict",
    "watchlist_generator.py": "Custom watchlist logic",
    "fast_price_check.py": "Quick price monitoring for hot setups",
    "chimera_entry_exit_sim.py": "Entry/exit zone simulation",
    "reset_agent_sessions.py": "Resets OpenFang sessions (1M token limit)",
    "market_scanner.py": "TradingView screener cron → OPPORTUNITIES.json",
    "candle_analyzer.py": "Multi-TF indicator cron → CANDLES.json",
    "economic_calendar_fetcher.py": "Macro calendar cron",
}


def skill_path(skill_name):
    if skill_name.startswith("chimera-"):
        return f"/root/.openclaw/skills/{skill_name}/SKILL.md"
    return f"/root/.openclaw/workspace/skills/{skill_name}/SKILL.md"


def generate_tools_md(agent_name):
    skills = AGENT_SKILL_MAP.get(agent_name, [])
    lines = [
        f"# TOOLS.md — {agent_name.upper()} Agent",
        "",
        "> **SKILL-FIRST RULE**: Always use skills first. Scripts are fallback ONLY.",
        "> **VPS Path**: All skills in `/root/.openclaw/skills/` (chimera) and `/root/.openclaw/workspace/skills/` (Bitget Hub + custom).",
        "> **Scripts Path**: `/root/openclawtrading/scripts/` — use only when no skill exists.",
        "",
        "## My Skills (Use These FIRST)",
        "",
    ]

    if skills:
        lines.append("| Skill | Path | Use For |")
        lines.append("|-------|------|---------|")
        for sk in skills:
            desc = SKILLS.get(sk, "Custom skill")
            path = skill_path(sk)
            lines.append(f"| `{sk}` | `{path}` | {desc} |")
    else:
        lines.append("_No specific skills mapped. Use clawhub-discovery or ask the architect._")

    lines.extend([
        "",
        "## Scripts (Fallback ONLY)",
        "",
        "These scripts run via cron. Use them ONLY if no skill covers the need:",
        "",
    ])
    for script, desc in SCRIPTS_NO_SKILL.items():
        lines.append(f"- `{script}` — {desc}")

    lines.extend([
        "",
        "## How to Invoke Skills",
        "",
        "```bash",
        "# From any agent or shell",
        'openclaw agent --agent <agent-name> --message "<task>" --channel discord --deliver',
        "",
        "# Or read skill directly",
        "cat /root/.openclaw/skills/<skill-name>/SKILL.md",
        "cat /root/.openclaw/workspace/skills/<skill-name>/SKILL.md",
        "```",
        "",
        "## Model Routing (if applicable)",
        "",
        "- **MiniMax (free)**: `MiniMax-M2.5-HighSpeed` — fast, cheap, good for coding",
        "- **Kimi K2.6**: `kimi-k2-6` — 262k context, best for complex analysis",
        '**Claude Code**: Use `claude -p "<prompt>"` for local tasks',
        "",
        "## VPS Quick Reference",
        "",
        "- Gateway: `systemctl status openclaw-gateway`",
        "- Logs: `/root/.openclaw/logs/openclaw.log`",
        "- Config: `/root/.openclaw/openclaw.json`",
        "- TradingView Desktop: `systemctl status tradingview-desktop` (port 9222)",
        "- OpenCode: `opencode run <message>` (MiniMax + Kimi)",
        "- Hermes: `hermes chat` (MiniMax)",
        "",
        "---",
        "*Generated by update_agent_tools.py | Kimi VPS | OpenClaw 2026.3.13*",
    ])
    return "\n".join(lines) + "\n"


def main():
    if not os.path.isdir(AGENTS_DIR):
        print(f"ERROR: {AGENTS_DIR} does not exist")
        sys.exit(1)

    updated = 0
    skipped = 0

    for agent in sorted(os.listdir(AGENTS_DIR)):
        agent_dir = os.path.join(AGENTS_DIR, agent)
        if not os.path.isdir(agent_dir):
            continue

        # Only update agents that have an IDENTITY.md (registered agents)
        identity_path = os.path.join(agent_dir, "IDENTITY.md")
        if not os.path.exists(identity_path):
            skipped += 1
            continue

        tools_path = os.path.join(agent_dir, "TOOLS.md")
        content = generate_tools_md(agent)

        with open(tools_path, "w", encoding="utf-8") as f:
            f.write(content)

        updated += 1
        print(f"Updated: {agent}")

    print(f"\nDone: {updated} agents updated, {skipped} skipped (no IDENTITY.md)")


if __name__ == "__main__":
    main()
