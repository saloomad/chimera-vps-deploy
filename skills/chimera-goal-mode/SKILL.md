---
name: chimera-goal-mode
description: "Use Hermes /goal mode for Chimera autonomous trading loops — set persistent goals, chain subagents, spawn Codex/Claude Code, and run 24/7 research pipelines."
version: 1.0.0
author: Hermes
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [goal-mode, autonomous, chimera, trading, codex, claude-code, spawning, cron]
    related_skills: [chimera-trading-consultant, chimera-divergence, technical-analysis]
---

# Chimera Goal Mode

Use Hermes `/goal` command to run autonomous, multi-turn Chimera workflows — research pipelines, trade analysis loops, coding sprints, and 24/7 monitoring with subagent spawning.

## What /goal Does

```
/goal <description>     — set a persistent goal (20-turn budget)
/goal status            — show current goal + turns used
/goal pause             — pause the loop
/goal resume            — resume (resets counter)
/goal clear             — stop the goal
/subgoal <criterion>    — add extra criteria mid-loop
```

**After each turn**, a judge model evaluates if the goal is satisfied. If not, Hermes gets a continuation prompt and keeps working. You can walk away for hours.

**State persists** in SessionDB — close the terminal, come back, `/goal resume` picks up where you left off.

---

## Chimera Use Cases

### 1. Continuous Market Monitoring Loop
```
/goal Monitor BTC/ETH/SOL every 4 hours for 7 days. Run chimera_trading_analyst.py, detect divergences, alert if consensus shifts from previous cycle. Pause if all 3 assets show BEAR_ZONE on 1D RSI below 35.
```
- Runs indefinitely via `/goal resume` resets
- Cron job can `/goal resume` automatically after each pause

### 2. Research Pipeline Sprint
```
/goal Research Deezoh's last 10 trades. Cross-reference with macro calendar, check Bitget funding, identify patterns. Output a HTML report to ~/trading/research/ with buy/sell/hold per asset. Stop when report is written.
```
- Single goal, finite deliverable
- Spawn Claude Code to write the HTML if needed

### 3. Strategy Backtest Loop
```
/goal Backtest the last 30 days of BTC signals from chimera_divergence.py. For each divergence signal, log entry price, stop loss, take profit, and outcome. Output CSV to ~/trading/backtest_results.csv. Run 3 rounds of refinement if accuracy below 60%.
```
- Judge checks if CSV exists and has valid rows
- Spawns Codex for the CSV analysis script

### 4. Parallel Coding Sprint (spawning Codex/Claude Code)
```
/goal Implement FVG detector in Python, write unit tests, push to GitHub. Spawn Claude Code (-p mode) for the implementation, monitor completion, fix failures.
```
- Claude Code in print mode: `claude -p 'task' --allowedTools Read,Edit,Bash --max-turns 20`
- Monitor with process polling

### 5. Multi-Agent Chimera Council
```
/goal Run a 5-agent council: macro-analyst, momentum-oscillators, divergence-detector, order-block-detector, volume-analysis. Each agent produces a 1-paragraph verdict on BTC. Synthesize into a final HERMES_CONSULTATION.md.
```
- Spawn 5 subagents in parallel via delegate_task
- Collect results, synthesize, write consultation

---

## Spawning Codex and Claude Code During Goals

### Claude Code (print mode — preferred for automation)
```python
# In a /goal continuation, call terminal tool:
terminal(command="claude -p 'Implement an FVG detector for BTC/USDT using Bitget klines. Output to ~/chimera/fvg_detector.py'", workdir="/home/open-claw/openclawtrading", timeout=300)
```

### Codex (background mode for long tasks)
```python
terminal(command="codex exec --full-auto 'Refactor chimera_trading_analyst.py to use the kline_indicators module'", workdir="/home/open-claw/openclawtrading", background=true, pty=true)
# Monitor:
process(action="poll", session_id="<id>")
```

### Cross-CLI Orchestration (Issue #413 pattern)
```python
# Spawn Claude Code and Codex in parallel worktrees
# Worktree 1: Claude Code for frontend
terminal(command="git worktree add /tmp/cc-task main && cd /tmp/cc-task && claude -p 'Add RSI dashboard'", background=true, pty=true)

# Worktree 2: Codex for backend
terminal(command="git worktree add /tmp/cx-task main && cd /tmp/cx-task && codex exec 'Add FVG API endpoint'", background=true, pty=true)
```

---

## Calling /goal Autonomously

### Via Cron Job
```python
# Cron job that sets a goal and delivers the result
cronjob(action='create',
    prompt='''
    Set /goal to: "Analyze BTC/ETH/SOL every 6 hours. Run chimera_trading_analyst.py, detect consensus shifts, write HERMES_CONSULTATION.md. If all 3 assets in BEAR_ZONE with RSI<35, alert @Deezo with market crash warning."
    
    Run the analysis, write the output, then /goal clear.
    Deliver the consultation to Discord #hermes-feed.
    ''',
    schedule='0 */6 * * *',
    name='Chimera 6H Trading Loop'
)
```

### Via delegate_task (spawning subagents)
```python
delegate_task(
    goal="Run chimera_trading_analyst.py for BTC/ETH/SOL. Write results to ~/trading/HERMES_CONSULTATION.md. Post summary to Discord #hermes-feed.",
    context="Trading workspace: /home/open-claw/openclawtrading. Python: ~/.hermes/scripts/chimera_trading_analyst.py",
    toolsets=['terminal', 'file', 'discord']
)
```

### Spawning a Goal Agent vs Regular Subagent

| | `/goal` Agent | `delegate_task` Subagent |
|---|---|---|
| Judge evaluation | ✅ Yes | ❌ No |
| Auto-continues | ✅ Until done/paused | ❌ One-shot |
| Resume across sessions | ✅ Yes | ❌ No |
| Best for | Research pipelines, monitoring loops | Single tasks, isolated work |
| Spawns other agents | ✅ Yes | ✅ Yes |

---

## Spawning Coding Agents in Goals

### Pattern 1: Goal sets task, coding agent does the work
```
/goal Build a trading dashboard. Spawn Claude Code (-p mode) to create the HTML. Monitor completion. If Claude Code fails, spawn Codex. If both fail, report error.
```

### Pattern 2: Coding agent IS the goal worker
```
/goal Have Claude Code implement the FVG detector. Monitor 3 turns. If incomplete, continue with Codex.
```

### Pattern 3: Parallel coding agents
```
/goal Parallel implementation: Claude Code implements FVG detector, Codex writes tests, OpenClaw reviews. All run simultaneously. Collect results in 20 minutes.
```

---

## Configuration

### Judge Model
```yaml
# ~/.hermes/config.yaml
auxiliary:
  goal_judge:
    provider: minimax
    model: MiniMax-M2.7-highspeed

goals:
  max_turns: 20
```

### Cross-CLI Spawn Config
```yaml
# ~/.hermes/config.yaml  
coding_agents:
  claude_code:
    path: ~/.npm-global/bin/claude   # or claude if in PATH
    default_mode: print             # print | interactive
    print_mode:
      allowedTools: [Read,Edit,Bash]
      max_turns: 20
  codex:
    path: ~/.npm-global/bin/codex
    default_mode: exec
    exec_mode:
      full_auto: true
```

---

## Chimera-Specific Tips

1. **/goal works across sessions** — set a 7-day monitoring loop, close laptop, resume next day
2. **/subgoal for criteria** — add "RSI must be below 40" or "alert Discord if consensus changes"
3. **Spawn in worktrees** — Codex needs a git repo; use worktrees for isolation
4. **Judge is fail-open** — if judge fails to parse JSON, goal auto-pauses after 3 tries
5. **/goal resume resets turns** — run in measured chunks of 20 turns at a time
6. **Combine with cron** — cron sets `/goal`, goal runs, pauses when done, next cron resumes

---

## Limitations & Gotchas

- **Judge model quality matters** — weak models return prose instead of JSON, triggering auto-pause. Use MiniMax-M2.7 or better.
- **Context limit** — long conversations compress; goal state survives but context may reset
- **One goal at a time per session** — use multiple sessions for parallel goals
- **Codex must run in git repo** — use worktrees for scratch work
- **Claude Code print mode** — skips all interactive prompts, auto-approves tools
- **Cross-CLI orchestration** — Hermes cannot natively control Codex/Claude Code stdin after startup; use background=true + process polling

---

## Quick Reference

```
/goal status            — show goal state
/goal pause             — pause (save state)
/goal resume           — resume (reset counter)
/goal clear            — stop
/subgoal <text>         — add criterion
/subgoal remove 1       — remove criterion 1
/delegate_task          — spawn one-shot subagent
```

**Judge verdict format expected:**
```json
{"done": true, "reason": "CSV written with 47 valid rows"}
```
