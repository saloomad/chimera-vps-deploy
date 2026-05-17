---
name: chimera-coding-agents-factory
description: "Spawn Claude Code with Kimi k2.6 or MiniMax M2.7-highspeed from Hermes. Also: OpenCode free fallback (deepseek-v4-free). Codex: blocked (auth expired)."
version: 1.0.0
author: Hermes
platforms: [linux, macos]
metadata:
  hermes:
    tags: [coding-agents, claude-code, kimi, minimax, opencode, chimera, autonomous, spawning]
    related_skills: [chimera-hermes-goal-mode]
---

# Chimera Coding Agents Factory

Spawn Claude Code with different models for Chimera coding tasks.

## Stack (on Linux PC)

| Agent | Version | Status | Models |
|-------|---------|--------|--------|
| Claude Code | 2.1.113 | ✅ Working | **k2.6** (Kimi), **MiniMax-M2.7-highspeed** (MiniMax) |
| OpenCode | 1.14.25 | ✅ Free | deepseek-v4-free |
| Codex | 0.122.0 | ❌ Auth expired | needs `codex auth login` |

## Claude Code — Two Models

Both use the same MiniMax API key via `ANTHROPIC_BASE_URL=https://api.minimax.chat/v1`.

### Kimi Model
```bash
export ANTHROPIC_API_KEY="<key>"
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1"
claude -p "task" --model k2.6 --max-turns 15
```

### MiniMax Model
```bash
export ANTHROPIC_API_KEY="<key>"
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1"
claude -p "task" --model MiniMax-M2.7-highspeed --max-turns 15
```

### From Hermes terminal tool
```python
terminal(
    command="claude -p 'Implement FVG detector for BTC/USDT' --model k2.6 --allowedTools Read,Edit,Bash,Write --max-turns 15",
    workdir="/home/open-claw/openclawtrading",
    timeout=300
)
```

## spawn-claude.sh (updated)

Model is passed as first arg, defaults to k2.6 (Kimi):

```bash
#!/usr/bin/env bash
# Usage: spawn-claude.sh "task" [model] [workdir] [max_turns]
# Models: k2.6 (Kimi), MiniMax-M2.7-highspeed (MiniMax)

set -e
TASK="${1:?Usage: $0 <task> [model] [workdir]}"
MODEL="${2:-k2.6}"
WORKDIR="${3:-/home/open-claw/openclawtrading}"
MAX_TURNS="${4:-15}"
CONFIG="/home/open-claw/.hermes/config.yaml"

KEY=$(python3 -c "import yaml;d=yaml.safe_load(open('$CONFIG'));print(d.get('model',{}).get('api_key',''))")

cd "$WORKDIR"
export ANTHROPIC_API_KEY="$KEY"
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1"

claude -p "$TASK"     --model "$MODEL"     --allowedTools Read,Edit,Bash,Write,Notebook     --max-turns "$MAX_TURNS"     2>&1
```

## spawn-kimi.sh (Kimi model shorthand)

```bash
#!/usr/bin/env bash
~/hermes/skills/chimera-coding-agents-factory/scripts/spawn-claude.sh "task" k2.6 /home/open-claw/openclawtrading 15
```

## spawn-minimax.sh (MiniMax model shorthand)

```bash
#!/usr/bin/env bash
~/hermes/skills/chimera-coding-agents-factory/scripts/spawn-claude.sh "task" MiniMax-M2.7-highspeed /home/open-claw/openclawtrading 15
```

## OpenCode Free Fallback

```bash
# No API key needed
opencode run "task" --model opencode/deepseek-v4-free
```

## Priority Chain

```
1. claude -p "task" --model k2.6                     # Kimi (default)
2. claude -p "task" --model MiniMax-M2.7-highspeed  # MiniMax
3. opencode run "task" --model opencode/deepseek-v4-free  # Free
```

## Codex — Blocked

Codex auth is expired. To fix: run `codex auth login` interactively on Linux PC. After login:
```bash
export ANTHROPIC_API_KEY="<key>"
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1"
codex exec "task" -m k2.6 --skip-git-repo-check < /dev/null
```

## Quick Reference

```bash
# Claude Code Kimi
claude -p "task" --model k2.6 --max-turns 15

# Claude Code MiniMax
claude -p "task" --model MiniMax-M2.7-highspeed --max-turns 15

# OpenCode free
opencode run "task" --model opencode/deepseek-v4-free

# List available models
opencode models 2>&1 | grep -i "minimax\|kimi\|deepseek"
```
