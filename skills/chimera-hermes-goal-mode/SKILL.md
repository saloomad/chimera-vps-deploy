---
name: chimera-hermes-goal-mode
description: "Run Hermes /goal autonomous loops for Chimera trading — persistent judge-driven goals, chain coding agents, 24/7 market monitoring, research pipelines. Spawns Claude Code (MiniMax-M2.7) and Kimi Code (MiniMax-K2.6) as sub-agents."
version: 1.0.0
author: Hermes
platforms: [linux, macos]
metadata:
  hermes:
    tags: [goal-mode, autonomous, chimera, trading, monitoring, research]
    related_skills: [chimera-coding-agents-factory, technical-analysis, chimera-trading-consultant]
---

# Chimera Hermes Goal Mode

Use Hermes `/goal` command to run autonomous, multi-turn Chimera trading workflows.

## What /goal Does

```
/goal <description>     — set a persistent goal (20-turn budget)
/goal status            — show current goal + turns used
/goal pause             — pause the loop
/goal resume            — resume (resets turn counter)
/goal clear             — clear/stop the goal
/subgoal <criterion>    — add completion criteria mid-loop
```

**After each turn**, a judge model evaluates: *"Is the goal satisfied?"*
- **YES** → goal marked done, loop stops
- **NO** → Hermes continues with a continuation prompt
- **20 TURNS** → auto-pause

State persists in SessionDB — close terminal, `/goal resume` picks up where you left off.

---

## Chimera Use Cases

### 1. 24/7 Market Monitor
```
/goal Monitor BTC/ETH/SOL every 4 hours. Run chimera_trading_analyst.py on Bitget klines, detect consensus shifts, alert Discord #hermes-alerts if RSI 1D < 35 across all 3 assets.
```

### 2. Research Pipeline Sprint
```
/goal Analyze Deezoh's last 10 trades. Cross-reference macro calendar, Bitget funding, orderbook data. Output HTML to ~/trading/research/deezoh_analysis.html.
```

### 3. Strategy Backtest Loop
```
/goal Backtest divergence.py signals on 30 days of BTC/USDT klines. Log entry, SL, TP, outcome. Output CSV. If accuracy < 60%, refine entry logic and re-test once.
```

### 4. Multi-Agent Council
```
/goal Run 5-agent council for BTC: macro-analyst, momentum-oscillators, divergence-detector, order-block-detector, volume-analysis. Each produces 1 paragraph. Synthesize into ~/trading/HERMES_CONSULTATION.md.
```

### 5. Coding Sprint (coding agents)
```
/goal Implement FVG detector in ~/chimera/fvg_detector.py.
  Primary: spawn Claude Code print-mode (MiniMax-M2.7-highspeed).
  Fallback: opencode run with deepseek-v4-free.
  Verify: file exists, >50 lines, no syntax errors.
  Push to GitHub on success.
```

---

## Calling Autonomously

### Via Cron (preferred for Chimera)
```python
cronjob(
    action='create',
    prompt='''
    Set /goal: "Analyze BTC/ETH/SOL every 6h. Run chimera_trading_analyst.py, detect consensus shifts, write HERMES_CONSULTATION.md. If all 3 in BEAR_ZONE with RSI<35 on 1D, alert in Discord #hermes-alerts."
    Run analysis, write consultation, /goal clear.
    Deliver to Discord #hermes-feed.
    ''',
    schedule='0 */6 * * *',
    name='Chimera 6H Trading Loop'
)
```

### Via delegate_task (one-shot subagent)
```python
delegate_task(
    goal="Run chimera_trading_analyst.py for BTC/ETH/SOL. Write results to ~/trading/HERMES_CONSULTATION.md.",
    context="Workspace: /home/open-claw/openclawtrading. Python: /home/open-claw/.hermes/scripts/chimera_trading_analyst.py",
    toolsets=['terminal', 'file', 'discord']
)
```

### /goal vs delegate_task

| | `/goal` Agent | `delegate_task` Subagent |
|---|---|---|
| Judge evaluation | ✅ Yes | ❌ No |
| Auto-continues | ✅ Until done/paused | ❌ One-shot |
| Resume across sessions | ✅ Yes | ❌ No |
| Best for | Monitoring loops, research pipelines | Single isolated tasks |

---

## Coding Agents (see chimera-coding-agents-factory)

```python
# Primary: Claude Code (MiniMax-M2.7-highspeed)
terminal(command="claude -p 'Implement FVG detector' --allowedTools Read,Edit,Bash,Write --max-turns 15", workdir="/home/open-claw/openclawtrading", timeout=300)

# Fallback: OpenCode free (no API key)
terminal(command="opencode run 'Implement FVG detector' --model opencode/deepseek-v4-free", workdir="/home/open-claw/openclawtrading", timeout=300)
```

---

## Quick Reference
```
/goal status              — show goal + turns
/goal pause               — pause (state saved)
/goal resume              — resume (counter reset)
/goal clear               — stop
/subgoal <text>           — add criterion
```

## Judge Config (in ~/.hermes/config.yaml)
```yaml
auxiliary:
  goal_judge:
    provider: minimax
    model: MiniMax-M2.7-highspeed

goals:
  max_turns: 20
```
