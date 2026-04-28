# Space Agent — Chimera Integration Guide

> **Status**: INSTALLED ✅ | **VPS**: `100.67.172.114:3000` | **Mode**: Single-user (no login required)
> **Server**: systemd service `space-agent` | **Customware**: `/srv/space/customware`

---

## What Is Space Agent

Space Agent is a **browser-first AI agent runtime** by Agent Zero. Unlike Claude Code or Codex (terminal-based), Space Agent runs entirely in the browser with a thin Node.js server for:

- **Dynamic UI generation** — the agent creates spaces, widgets, and tools on demand
- **SKILL.md extensibility** — new capabilities via plain text skill files
- **Git-backed history** — every change is versioned, rollback is one click
- **File API** — agents read/write files through a REST API
- **Hierarchical layers** — L0 (system), L1 (group), L2 (user) for clean separation

**Best fit for Chimera**: Visual dashboard layer, dynamic trading workspaces, agent-built tools.

---

## How to Access It

### From Windows (Tailscale)

Open Chrome and go to:

```
http://100.67.172.114:3000
```

No login required — single-user mode is enabled.

### From VPS local

```bash
curl http://127.0.0.1:3000
```

---

## How to Configure LLM (MiniMax or Kimi)

Space Agent defaults to **OpenRouter** (`anthropic/claude-sonnet-4.6`). To use MiniMax or Kimi:

1. Open Space Agent in browser
2. Click the **agent panel** (bottom-right corner)
3. Click **Settings** (gear icon)
4. Switch to the **API** tab
5. Fill in:

### MiniMax M2.7-HighSpeed

| Field | Value |
|-------|-------|
| API Endpoint | `https://api.minimax.io/v1/chat/completions` |
| Model | `MiniMax-M2.7-highspeed` |
| API Key | Your MiniMax key (`sk-cp-...`) |
| Max Tokens | `200000` |

### Kimi K2.6

| Field | Value |
|-------|-------|
| API Endpoint | `https://api.kimi.com/coding/v1/chat/completions` |
| Model | `kimi-for-coding` |
| API Key | Your Kimi key (`sk-kimi-...`) |
| Max Tokens | `256000` |

**Note**: These settings are browser-local (stored in localStorage). Set them once per browser.

---

## How Chimera Agents Use Space Agent

### 1. File-Based Data Bridge

Chimera pipeline scripts write JSON to:

```
/srv/space/customware/L2/user/chimera-data/
```

Files:
- `MACRO.json` — macro bias, BTC.D, funding, F&G
- `WATCHLISTS.json` — scanned symbols and regimes
- `OPPORTUNITIES.json` — divergence scans and setups
- `DERIVATIVES.json` — OI, funding, liquidations
- `NEWS.json` — latest market news
- `SCRIPT_HEALTH.json` — pipeline health status

Space Agent widgets read these via the `/api/file_read` endpoint and auto-refresh every 30 seconds.

### 2. SKILL.md Extension

Chimera-specific skills live in:

```
/srv/space/customware/L1/_admin/mod/chimera/ext/skills/chimera-dashboard/SKILL.md
```

This skill teaches the Space Agent how to:
- Read Chimera JSON data files
- Create dashboard widgets
- Format trading summaries

**To add a new skill**: Write a `SKILL.md` file in any `ext/skills/<skill-name>/` directory. Space Agent discovers it automatically.

### 3. Spaces and Widgets

A **Space** = a dashboard page (YAML file)
A **Widget** = a visual panel inside a space (YAML + HTML/JS renderer)

Current Chimera space: `chimera-dashboard`
- Widget `macro` — 4-card macro overview (BTC.D, F&G, Funding, Bias)
- Widget `watchlist` — sortable watchlist table

**To create new widgets**: Write YAML files to `L2/user/spaces/<space>/widgets/<widget>.yaml`

### 4. API for External Agents

Any agent with HTTP access can:

```bash
# Read a file
curl -X POST http://100.67.172.114:3000/api/file_read \
  -H 'Content-Type: application/json' \
  -d '{"path":"L2/user/chimera-data/MACRO.json"}'

# Write a file
curl -X POST http://100.67.172.114:3000/api/file_write \
  -H 'Content-Type: application/json' \
  -d '{"path":"L2/user/chimera-data/ALERTS.json","content":"{...}"}'

# List spaces
curl -X POST http://100.67.172.114:3000/api/file_list \
  -H 'Content-Type: application/json' \
  -d '{"path":"L2/user/spaces/"}'
```

---

## How Space Agent Learns and Improves

### 1. SKILL.md Self-Extension

The agent can write new SKILL.md files and modify existing ones. When you ask it:

> "Create a skill that shows liquidation heatmaps"

It writes a new `SKILL.md` + helper JS. The skill is immediately available.

### 2. Git-Backed History

Every user's L2 directory is a Git repo. All changes are committed automatically.

- **Time travel**: Roll back any change via the admin panel
- **Diff view**: See exactly what the agent changed
- **Branching**: Experiment safely, revert if broken

### 3. Widget Evolution

Widgets are plain HTML/JS. The agent can:
- Edit widget renderers to add new visualizations
- Create new widgets from scratch
- Copy and modify existing widgets

### 4. Space Cloning

Spaces can be exported as ZIP and imported elsewhere. This means:
- Share dashboard templates between team members
- Backup trading workspaces
- Clone a "master" setup for new users

---

## Architecture: How It Fits Chimera

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Windows Claude │     │  Windows Codex  │     │  Linux OpenClaw │
│   (Planning)    │     │  (Execution)    │     │  (27 Agents)    │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │   Chimera Pipeline Scripts │
                    │   (derivatives_fetcher,    │
                    │    macro_calendar, etc.)    │
                    └─────────────┬─────────────┘
                                  │ writes JSON
                    ┌─────────────▼─────────────┐
                    │  /srv/space/customware/   │
                    │  L2/user/chimera-data/    │
                    └─────────────┬─────────────┘
                                  │ reads via API
                    ┌─────────────▼─────────────┐
                    │      Space Agent          │
                    │   (Browser Dashboard)     │
                    │  100.67.172.114:3000      │
                    └───────────────────────────┘
```

**Key principle**: Space Agent is the **visual layer**, not the computation layer. All heavy lifting (data fetching, analysis, scanning) stays in the Chimera pipeline. Space Agent reads the outputs and displays them.

---

## Operational Commands

```bash
# Check status
ssh root@100.67.172.114 "systemctl status space-agent"

# Restart
ssh root@100.67.172.114 "systemctl restart space-agent"

# View logs
ssh root@100.67.172.114 "journalctl -u space-agent -f"

# Update space-agent from Git
ssh root@100.67.172.114 "cd /root/space-agent && node space update"

# Create admin user (if disabling single-user mode)
ssh root@100.67.172.114 "cd /root/space-agent && node space user create admin --password '...' --groups _admin"
```

---

## Z: Drive Deprecation Note

**CRITICAL**: The old `Z:\reports\auto\` path no longer exists. All Chimera JSON outputs now go to:

- **VPS local**: `/srv/space/customware/L2/user/chimera-data/` (Space Agent reads from here)
- **Linux OpenClaw**: `/home/open-claw/openclawtrading/reports/auto/` (pipeline writes here)
- **Windows**: `C:\Users\becke\claudecowork\reports\auto\` (fallback mirror)

Update any scripts or skills that reference `Z:\reports\auto\`.

---

## Next Steps

1. **Open Space Agent** in browser: `http://100.67.172.114:3000`
2. **Configure LLM** with MiniMax or Kimi API key
3. **Open the Chimera Dashboard** space (it should appear in spaces list)
4. **Ask the agent**: "Create a widget that shows funding rates for BTC, ETH, SOL"
5. **Watch it build** the widget in real time

---

*Space Agent Integration v1.0 | 2026-04-29 | VPS: 100.67.172.114*
