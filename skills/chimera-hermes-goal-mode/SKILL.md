---
name: chimera-hermes-goal-mode
description: "Run Hermes /goal autonomous loops for Chimera trading. Judge-driven persistent goals that survive session boundaries. Spawn Claude Code with Kimi k2.6 or MiniMax M2.7-highspeed as coding agents. 24/7 monitoring, research pipelines, backtest loops."
version: 1.0.0
author: Hermes
platforms: [linux, macos]
metadata:
  hermes:
    tags: [goal-mode, autonomous, chimera, trading, monitoring, research]
    related_skills: [chimera-coding-agents-factory]
---

# Chimera Hermes Goal Mode

Use Hermes `/goal` for autonomous, multi-turn Chimera workflows. Judge evaluates after every turn.

## /goal Commands

```
/goal <text>          — set goal (20-turn budget)
/goal status          — show current goal + turns used
/goal pause           — pause loop
/goal resume          — resume (resets counter)
/goal clear           — stop
/subgoal <text>       — add completion criterion
```

## Chimera Use Cases

### 1. Market Monitor
```
/goal Monitor BTC/ETH/SOL every 4h. Run chimera_trading_analyst.py on Bitget klines. If RSI 1D < 35 on all 3 and macro ZONE=BEAR, alert Discord #hermes-alerts.
```

### 2. Research Pipeline
```
/goal Analyze Deezoh's last 10 trades. Cross-reference macro calendar, Bitget funding, orderbook. Output HTML to ~/trading/research/deezoh_analysis.html.
```

### 3. Strategy Backtest
```
/goal Backtest divergence.py on 30 days BTC/USDT klines. Log entry/SL/TP/outcome to CSV. If accuracy < 60%, refine entry logic and re-test once.
```

### 4. Coding Sprint
```
/goal Implement FVG detector in ~/chimera/fvg_detector.py.
  Spawn Claude Code with Kimi k2.6 model. Verify file >50 lines, no syntax errors. Push to GitHub.
```

### 5. Multi-Agent Council
```
/goal Run 5-agent council for BTC: macro-analyst, momentum-oscillators, divergence-detector, order-block-detector, volume-analysis. Each produces 1 paragraph. Synthesize into ~/trading/HERMES_CONSULTATION.md.
```

## Coding Agents (see chimera-coding-agents-factory)

```
Primary:   claude -p "task" --model k2.6              # Kimi model
Secondary: claude -p "task" --model MiniMax-M2.7-highspeed  # MiniMax model
Free:      opencode run "task" --model opencode/deepseek-v4-free
```

## Cron Integration

```python
cronjob(
    action='create',
    prompt='Set /goal: "Analyze BTC/ETH/SOL every 6h. Run chimera_trading_analyst.py, write HERMES_CONSULTATION.md. If consensus shift, alert Discord #hermes-alerts." /goal clear. Deliver to Discord.',
    schedule='0 */6 * * *',
    name='Chimera 6H Trading Loop'
)
```

## /goal vs delegate_task

| | /goal | delegate_task |
|--|-------|---------------|
| Judge evaluation | ✅ | ❌ |
| Auto-continue | ✅ Until done | ❌ One-shot |
| Resume across sessions | ✅ | ❌ |
| Best for | Monitoring, research | Isolated tasks |
