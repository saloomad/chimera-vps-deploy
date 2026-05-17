# Hermes on Linux PC — Setup Reference

**Last verified:** 2026-05-17

## Hermes Installation Path

```
~/.hermes/hermes-agent/venv/bin/hermes    ← Python venv install
~/.hermes/bin/tirith                       ← URL security scanner (separate binary)
```

**NOT** at the npm global `hermes` (that's a different package). The venv is the Nous Research Hermes Agent.

## PATH Entry for Hermes

```bash
export PATH="$HOME/.hermes/hermes-agent/venv/bin:$PATH"
```

Add to `.bashrc` before the interactive check block, or to `.bash_profile`.

## Hermes vs OpenClaw — Separate Installations

| | Hermes | OpenClaw |
|--|--------|----------|
| Install type | Python venv | npm global |
| Binary path | `~/.hermes/hermes-agent/venv/bin/hermes` | `~/.npm-global/bin/openclaw` |
| Config | `~/.hermes/config.yaml` | `~/.openclaw/openclaw.json` |
| Primary model | MiniMax | Kimi |
| Purpose | Orchestration, research, learning | Trading agents, workspace |

They coexist without conflict. `hermes` and `openclaw` are separate CLIs.

## Skills Directory

Hermes skills live at: `~/.hermes/skills/` (NOT `~/.hermes/hermes-agent/skills/`)

The bundled skills in `~/.hermes/hermes-agent/skills/` are read-only defaults; user-installed skills go in `~/.hermes/skills/`.

## Bundled Skills Available on Linux PC

```
autonomous-ai-agents/     ← claude-code, codex, opencode sub-skills
chimera-*                 ← Chimera trading skills
council-pattern/
decision-council/
learning-loop/
technical-analysis/
tradingview-mcp/
... (90+ total)
```

## /goal Command

Available via `hermes` CLI. See `hermes-feature-discovery` skill for full reference.

## Update Hermes

```bash
cd ~/.hermes/hermes-agent && git pull
source venv/bin/activate && pip install -e .
```
