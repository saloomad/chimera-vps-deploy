---
name: chimera-coding-agents-factory
description: "Spawn Claude Code (MiniMax/M2.7) and Kimi Code (MiniMax/K2.6) from Hermes /goal loops for Chimera trading. Primary: claude-code print-mode with MiniMax-M2.7-highspeed. Fallback: kimi-code with MiniMax-K2.6. Uses same API keys as Hermes config."
version: 1.0.0
author: Hermes
platforms: [linux, macos]
metadata:
  hermes:
    tags: [coding-agents, claude-code, kimi-code, opencode, chimera, autonomous, spawning, goal-mode]
    related_skills: [chimera-hermes-goal-mode, technical-analysis, chimera-trading-consultant]
---

# Chimera Coding Agents Factory

Spawn Claude Code and Kimi Code as coding agents from Hermes /goal loops, using the same MiniMax credentials as Hermes config.

## Stack (already installed on Linux PC)

| Agent | Version | Status | Model |
|-------|---------|--------|-------|
| Claude Code | 2.1.113 | ✅ Working | MiniMax-M2.7-highspeed (primary) |
| Kimi Code | 1.0.11 | ⚠️ Needs setup | MiniMax-K2.6 (fallback) |
| OpenCode | 1.14.25 | ✅ Free tier | minimax-m2.5-free, deepseek-v4 |
| Claude (standalone) | 2.1.113 | ✅ Working | MiniMax-M2.7-highspeed |

## Agent Priority Chain

```
1. claude -p "task"          → MiniMax-M2.7-highspeed (PRODUCTION - same as Hermes)
2. kimi-code --kimi          → MiniMax-K2.6 (needs MiniMax API setup)
3. opencode run "task"       → minimax-m2.5-free (FREE fallback)
```

---

## 1. Claude Code — Primary (MiniMax-M2.7-highspeed)

### How it works
Claude Code uses Hermes's already-configured MiniMax API key. When invoked via SSH, it reads the same `~/.hermes/config.yaml`.

### Print Mode (one-shot, recommended)
```bash
claude -p "Implement FVG detector for BTC/USDT" \
    --allowedTools Read,Edit,Bash,Write,Notebook \
    --max-turns 15 \
    --model MiniMax-M2.7-highspeed
```

### From Hermes terminal tool
```python
terminal(
    command="claude -p 'Add RSI divergence detection to chimera_trading_analyst.py. Use Bitget klines.' --allowedTools Read,Edit,Bash,Write --max-turns 15",
    workdir="/home/open-claw/openclawtrading",
    timeout=300
)
```

### Wrapper script: ~/chimera/spawn-claude.sh
```bash
#!/usr/bin/env bash
# Claude Code print mode with MiniMax-M2.7-highspeed
# Usage: spawn-claude.sh "task description" [workdir] [max_turns]

set -e
TASK="${1:?Usage: $0 <task> [workdir] [max_turns]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"
MAX_TURNS="${3:-15}"

cd "$WORKDIR"
claude -p "$TASK"     --allowedTools Read,Edit,Bash,Write,Notebook     --max-turns "$MAX_TURNS"     --model MiniMax-M2.7-highspeed     2>&1
```

---

## 2. Kimi Code — Fallback (MiniMax-K2.6)

### How it works
`kimi-code` is a proxy wrapper that: (1) starts an anthropic-proxy, (2) runs Claude Code pointing to it, (3) cleans up on exit.

### Setup: Configure MiniMax API key

MiniMax Cloud Platform requires a custom proxy. Create `~/chimera/minimax-proxy.sh`:

```bash
#!/usr/bin/env bash
# Start a MiniMax-compatible anthropic-proxy for Claude Code
# Usage: ./minimax-proxy.sh <port>

PORT="${1:-3000}"
KEY_FILE="/home/open-claw/.hermes/.mx_key"
CONFIG="/home/open-claw/.hermes/config.yaml"

# Get API key from Hermes config
export MINIMAX_API_KEY=$(python3 -c "import yaml;d=yaml.safe_load(open('$CONFIG'));print(d.get('model',{}).get('api_key',''))")
export MINIMAX_GROUP_ID="${MINIMAX_GROUP_ID:-}"

# MiniMax Cloud Platform proxy (translate Anthropic → MiniMax format)
# Uses the same auth as Hermes/MiniMax-M2.7-highspeed

node -e "
const http = require('http');
const https = require('https');

const API_KEY = process.env.MINIMAX_API_KEY;
const GROUP_ID = process.env.MINIMAX_GROUP_ID || '';

function makeMinimaxRequest(path, body) {
  return new Promise((resolve, reject) => {
    const url = new URL('https://api.minimax.chat' + path);
    const options = {
      hostname: url.hostname,
      port: 443,
      path: url.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_KEY,
        ...(GROUP_ID && { 'GroupId': GROUP_ID }),
      }
    };
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => resolve(JSON.parse(data)));
    });
    req.on('error', reject);
    req.write(JSON.stringify(body));
    req.end();
  });
}

const server = http.createServer(async (req, res) => {
  if (req.method === 'POST' && req.url === '/v1/messages') {
    let body = '';
    req.on('data', d => body += d);
    req.on('end', async () => {
      try {
        const msg = JSON.parse(body);
        // Translate Anthropic format to MiniMax
        const resp = await makeMinimaxRequest('/v1/text/chatcompletion_v2', {
          model: 'MiniMax-Text-01',
          messages: msg.messages || [{role: 'user', content: msg.prompt || ''}],
          max_tokens: msg.max_tokens || 4096,
        });
        res.end(JSON.stringify({
          type: 'message',
          content: [{ type: 'text', text: resp.choices?.[0]?.text || '' }]
        }));
      } catch (e) {
        res.statusCode = 500;
        res.end(JSON.stringify({ error: e.message }));
      }
    });
  } else {
    res.statusCode = 404;
    res.end();
  }
});

server.listen($PORT, () => console.log('Proxy on ' + $PORT));
" &
echo $!
```

### Running Kimi Code
```bash
# Start proxy in background
PROXY_PID=$(~/chimera/minimax-proxy.sh 3000)

# Run Claude Code with proxy
ANTHROPIC_BASE_URL=http://localhost:3000 claude -p "Write FVG detector" --max-turns 15

# Kill proxy
kill $PROXY_PID
```

### Wrapper: ~/chimera/spawn-kimi.sh
```bash
#!/usr/bin/env bash
# Spawn Claude Code via kimi-code with MiniMax-K2.6
# Usage: spawn-kimi.sh "task" [workdir]

TASK="${1:?Usage: $0 <task> [workdir]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"
PROXY_PORT=3001

# Start MiniMax proxy
~/chimera/minimax-proxy.sh $PROXY_PORT &
PROXY_PID=$!

# Wait for proxy
sleep 2

# Run Claude Code via proxy
cd "$WORKDIR"
ANTHROPIC_BASE_URL=http://localhost:$PROXY_PORT claude -p "$TASK"     --model k2.6     --allowedTools Read,Edit,Bash,Write     --max-turns 15

# Cleanup
kill $PROXY_PID 2>/dev/null
```

---

## 3. OpenCode — Free Tier Fallback

```bash
# minimax-m2.5-free (no API key)
opencode run "Write FVG detector" --model opencode/minimax-m2.5-free

# deepseek-v4-free (no API key)
opencode run "Write FVG detector" --model opencode/deepseek-v4-free
```

---

## Parallel Chimera Workflow

```python
# Spawn all three agents in parallel, use the first one that succeeds
# Agent 1: Claude Code (primary)
terminal(
    command="claude -p 'Refactor fvg_detector.py to use kline_indicators module' --allowedTools Read,Edit,Bash,Write --max-turns 20",
    workdir="/home/open-claw/openclawtrading",
    background=True,
    timeout=300
)

# Agent 2: OpenCode free (fallback if Claude Code fails)
terminal(
    command="opencode run 'Add SMA crossover signals to chimera_trading_analyst.py' --model opencode/deepseek-v4-free",
    workdir="/home/open-claw/openclawtrading",
    background=True,
    timeout=300
)
```

---

## /goal Integration

```
/goal Implement divergence detector for BTC/ETH/SOL.
  Primary: Spawn Claude Code print-mode to write fvg_detector.py (15 turns).
  If Claude Code unavailable after 2 attempts, spawn OpenCode with deepseek-v4-free.
  Verify output: file exists and has >50 lines.
  Push to GitHub on success.
```

---

## Wrapper Scripts (already on Linux PC)

| Script | Path | Purpose |
|--------|------|---------|
| `spawn-claude.sh` | `~/.hermes/skills/chimera-coding-agents-factory/scripts/` | Claude Code print-mode |
| `spawn-kimi.sh` | same | Kimi Code proxy |
| `monitor.sh` | same | Background process monitor |

---

## Quick Reference

```bash
# Primary: Claude Code with MiniMax-M2.7-highspeed
claude -p "task" --model MiniMax-M2.7-highspeed --max-turns 15

# Fallback: OpenCode free
opencode run "task" --model opencode/deepseek-v4-free

# Check Claude Code version
claude --version

# Check OpenCode models
opencode models 2>&1 | head -10

# List background jobs
jobs -l
```

---

## Status & Notes

- **Claude Code**: ✅ Primary — uses same MiniMax-M2.7-highspeed as Hermes
- **Kimi Code**: ⚠️ Needs proxy setup — MiniMax Cloud Platform uses custom sig auth
- **OpenCode free**: ✅ Works immediately — no API key needed
- **Codex**: ❌ Auth expired — needs `codex auth login` refresh
