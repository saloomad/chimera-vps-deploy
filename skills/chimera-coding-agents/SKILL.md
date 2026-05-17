---
name: chimera-coding-agents
description: "Spawn Claude Code and OpenClaw from Hermes /goal loops for Chimera trading system development. Claude Code is verified working; Codex requires OAuth re-login."
version: 1.1.0
author: Hermes
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding-agents, claude-code, codex, openclaw, spawning, chimera, autonomous]
    related_skills: [chimera-goal-mode, chimera-trading-consultant]
---

# Chimera Coding Agents

Spawn Claude Code and OpenClaw as sub-agents from Hermes /goal loops.

**Status:**
- Claude Code ✅ (v2.1.113 — verified working)
- Codex ❌ (auth expired — needs `codex auth login` to refresh)
- OpenClaw ✅ (2026.5.7)
- Hermes ✅
nd cross-CLI orchestration patterns."
version: 1.0.0
author: Hermes
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding-agents, claude-code, codex, openclaw, spawning, chimera, autonomous]
    related_skills: [chimera-goal-mode, chimera-trading-consultant]
---

# Chimera Coding Agents

Spawn Claude Code, Codex, and OpenClaw as sub-agents from Hermes /goal loops to build and maintain the Chimera trading system autonomously.

## Architecture

```
Hermes (orchestrator)
├── /goal loop (judge-driven continuation)
│   ├── Spawns Claude Code ──► FVG detector, order blocks
│   ├── Spawns Codex ───────► Backtesting, data pipelines
│   ├── Spawns OpenClaw ───► Workspace management, skills
│   └── Spawns Hermes ──────► Independent analysis lane
└── Cross-CLI relay (future: Issue #413)
```

## Prerequisites

### Linux PC (100.116.214.127)
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code
claude auth login --console

# Install Codex
npm install -g @openai/codex
codex auth login

# Verify
claude --version
codex --version
```

### Hermes on Linux PC
```bash
# Hermes is at:
~/.hermes/hermes-agent/venv/bin/hermes

# Add to PATH:
echo 'export PATH="$HOME/.hermes/hermes-agent/venv/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## Claude Code — Print Mode (Recommended)

Print mode runs one-shot tasks, returns result, exits. No PTY needed.

### From Hermes Terminal Tool
```python
terminal(
    command="claude -p 'Add FVG detection to ~/chimera/trading.py. Use Bitget klines API. Detect 3-candle FVGs on 1H/4H timeframes.' --allowedTools Read,Edit,Bash --max-turns 15",
    workdir="/home/open-claw/openclawtrading",
    timeout=300
)
```

### From /goal Loop
```
/goal Implement FVG detector for BTC/ETH/SOL. Spawn Claude Code in print mode to write the Python module. Monitor output. If it fails, try Codex.
```

### Key Claude Code Flags
| Flag | Use |
|------|-----|
| `-p 'task'` | Print mode — one-shot, no PTY |
| `--allowedTools Read,Edit,Bash` | Restrict tools |
| `--max-turns 15` | Cap turns to control spend |
| `--model sonnet` | Use specific model |
| `--output-format json` | Structured output for parsing |

---

## Codex CLI — Background Mode

Codex needs a git repo. Use for longer tasks with background monitoring.

### From Hermes Terminal Tool
```python
terminal(
    command="codex exec --full-auto 'Refactor chimera_trading_analyst.py to use kline_indicators module'",
    workdir="/home/open-claw/openclawtrading",
    background=True,
    pty=True
)
```

### Monitor with Process Tool
```python
# Poll for completion
process(action="poll", session_id="<session_id>")

# Get output
process(action="log", session_id="<session_id>", limit=50)

# Send input if blocked
process(action="submit", session_id="<session_id>", data="yes")

# Kill if hung
process(action="kill", session_id="<session_id>")
```

### Key Codex Flags
| Flag | Use |
|------|-----|
| `exec 'task'` | Execute one task |
| `--full-auto` | Auto-approve file changes |
| `--yolo` | No sandbox, fastest |
| `--model o4` | Use specific model |

---

## OpenClaw — Workspace Management

```python
terminal(
    command="openclaw run --profile default -- 'Run chimera_trading_analyst.py and post results to Discord'",
    workdir="/home/open-claw/openclawtrading",
    timeout=120
)
```

### OpenClaw Subagent Spawn (native)
```python
delegate_task(
    goal="Analyze BTC/ETH/SOL divergence signals for the last 7 days. Write JSON to ~/trading/divergence_report.json.",
    context="Workspace: /home/open-claw/openclawtrading. Skills: technical-analysis, chimera-divergence.",
    toolsets=['terminal', 'file']
)
```

---

## Wrapper Scripts for Chimera

### ~/chimera/spawn-claude.sh
```bash
#!/usr/bin/env bash
# Spawn Claude Code for a Chimera task
# Usage: ./spawn-claude.sh "task description" [workdir] [max_turns]

TASK="${1:?Usage: $0 <task> [workdir] [max_turns]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"
MAX_TURNS="${3:-15}"

cd "$WORKDIR"
claude -p "$TASK"     --allowedTools Read,Edit,Bash,Write,Notebook     --max-turns "$MAX_TURNS"     --model sonnet     2>&1
```

### ~/chimera/spawn-codex.sh
```bash
#!/usr/bin/env bash
# Spawn Codex for a Chimera task
# Usage: ./spawn-codex.sh "task description" [workdir]

TASK="${1:?Usage: $0 <task> [workdir]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"

cd "$WORKDIR"
codex exec --full-auto "$TASK" 2>&1
```

### ~/chimera/monitor-goal.sh
```bash
#!/usr/bin/env bash
# Monitor a background process, alert on completion
# Usage: ./monitor-goal.sh <session_id> <alert_command>

SESSION="${1:?Usage: $0 <session_id> [alert_cmd]}"
ALERT="${2:-echo 'DONE'}"

while true; do
    STATUS=$(hermes process poll "$SESSION" 2>/dev/null | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
    if [ "$STATUS" = "done" ] || [ "$STATUS" = "exited" ]; then
        echo "[$(date)] Process completed"
        eval "$ALERT"
        break
    fi
    echo "[$(date)] Still running... ($STATUS)"
    sleep 60
done
```

---

## Parallel Chimera Workflow

```python
# In a /goal loop — spawn 3 coding agents in parallel

# Agent 1: Claude Code — FVG detector
t1 = terminal(
    command="claude -p 'Write ~/chimera/fvg_detector.py. Detect 3-candle FVGs on Bitget 1H/4H klines. Output bullish/bearish signals with entry zones.' --allowedTools Read,Edit,Bash,Write --max-turns 20",
    workdir="/home/open-claw/openclawtrading",
    background=True,
    timeout=300
)

# Agent 2: Codex — Backtesting engine
t2 = terminal(
    command="codex exec --full-auto 'Write ~/chimera/backtest_engine.py. Backtest FVG signals on 30 days of BTC/USDT klines. Output win rate, avg profit, max drawdown.'",
    workdir="/home/open-claw/openclawtrading",
    background=True,
    timeout=300
)

# Agent 3: OpenClaw — Discord report
t3 = terminal(
    command="openclaw run --profile default -- 'Run ~/hermes/scripts/chimera_trading_analyst.py && post summary to Discord #hermes-feed'",
    workdir="/home/open-claw/openclawtrading",
    background=True,
    timeout=120
)

# Monitor all three
for sid in $t1 $t2 $t3; do
    process(action="poll", session_id=sid)
    process(action="log", session_id=sid)
done
```

---

## Cross-CLI Orchestration (Issue #413 Pattern)

**Current limitation:** Hermes cannot natively control Codex/Claude Code stdin after spawning. The workaround is background=true + polling.

**Future (Issue #413):** Native `relay` tool that wraps external CLIs in PTY, injects messages as stdin, captures stdout, and treats them as first-class subagents.

### Implementation Plan for Native Support

```yaml
# Future ~/.hermes/config.yaml
relay:
  enabled: true
  agents:
    claude_code:
      command: claude
      args: ["-p", "{prompt}", "--allowedTools", "Read,Edit,Bash", "--max-turns", "20"]
      workdir: "{workspace}"
      parse_mode: json
    codex:
      command: codex
      args: ["exec", "--full-auto", "{prompt}"]
      workdir: "{workspace}"
      parse_mode: stdout
```

```python
# Future Hermes tool
relay(
    agent="claude_code",
    prompt="Implement FVG detector for BTC/USDT",
    workspace="/home/open-claw/openclawtrading",
    max_turns=20,
    parse_mode="json"
)
```

---

## Chimera Production Patterns

### Pattern 1: Research → Code → Test → Deploy
```
/goal Build and deploy FVG detector. 
  1. Claude Code writes fvg_detector.py (5 turns)
  2. Codex writes tests (3 turns)
  3. Hermes runs backtest (5 turns)
  4. If win rate > 55%, push to GitHub
  5. Post results to Discord
```

### Pattern 2: 24/7 Market Monitor
```
/goal Keep monitoring BTC/ETH/SOL every 4 hours. 
  Run chimera_trading_analyst.py.
  If consensus SHIFT detected, spawn Claude Code to generate alert.
  Claude Code posts to Discord #alerts.
  Continue until manually cleared.
```

### Pattern 3: Learning Loop
```
/goal Review last 10 Deezoh trades. 
  Spawn OpenClaw subagent to analyze.
  Spawn Claude Code to suggest strategy improvements.
  Hermes synthesizes into HERMES_ADVISOR_REVIEW.json.
  Post to Discord #hermes-feed.
```
