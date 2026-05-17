---
name: space-agent-integration
description: Work with the Space Agent visual dashboard layer for Chimera. Use when accessing the dashboard, configuring the LLM, pushing data, creating widgets, or extending the space-agent.ai visual layer with skills.
---

# Space Agent — Chimera Integration

> **VPS URL**: `http://100.67.172.114:3000`
> **Mode**: Single-user (no login required)
> **Customware**: `/srv/space/customware`
> **Full guide**: `docs/SPACE_AGENT_INTEGRATION.md`

---

## Quick Access

From Windows (Tailscale connected):
```
http://100.67.172.114:3000
```

From VPS:
```bash
curl http://127.0.0.1:3000
```

---

## How to Configure LLM

Provider configs are stored as per-agent YAML files. **Desktop app configs** at:
```
C:/Users/becke/AppData/Roaming/space-agent/customware/L2/user/conf/
├── admin-chat.yaml      ← primary agent (Kimi)
└── onscreen-agent.yaml  ← secondary agent (MiniMax)
```

**VPS server config** at `/root/space-agent/params.yaml`.

### MiniMax (onscreen-agent.yaml — confirmed working)
```yaml
api_endpoint: "https://api.minimax.io/anthropic"
model: MiniMax-M2.7-highspeed
api_key: sk-cp-...
```

### Kimi (admin-chat.yaml — confirmed working)
```yaml
api_endpoint: "https://api.kimi.com/coding"
model: kimi-for-coding
api_key: sk-kimi-...
```

**Critical**: `api_endpoint` is the **base URL only** — no `/v1` or `/v1/chat/completions`. The app appends the path internally. Wrong: `https://api.kimi.com/coding/v1/chat/completions` — correct: `https://api.kimi.com/coding`

---

## How Chimera Pushes Data

Pipeline scripts write JSON to:

```
/srv/space/customware/L2/user/chimera-data/
```

| File | What it contains | Written by |
|------|-----------------|------------|
| `MACRO.json` | BTC.D, USDT.D, funding, F&G, bias | `macro_calendar` cron |
| `WATCHLISTS.json` | Scanned symbols, regime, signals | `chimera_scanner_task` |
| `OPPORTUNITIES.json` | Divergence scans, setups | `divergence_scanner` |
| `DERIVATIVES.json` | OI, funding, liquidations | `derivatives_fetcher` |
| `NEWS.json` | Latest headlines | `chimera_news_fetcher` |
| `SCRIPT_HEALTH.json` | Pipeline health | `chimera_heartbeat` |

Widgets read these via `/api/file_read` and auto-refresh every 30s.

---

## How to Create a Widget

Widgets are YAML files in:

```
/srv/space/customware/L2/user/spaces/<space>/widgets/<widget>.yaml
```

Example widget structure:

```yaml
id: my-widget
name: My Widget
cols: 6
rows: 3
metadata:
  title: My Title
renderer: |
  <div style="padding: 16px;">
    <h3>My Widget</h3>
    <div id="content">Loading...</div>
  </div>
  <script>
    async function load() {
      const res = await fetch('/api/file_read', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({path:'L2/user/chimera-data/MACRO.json'})
      });
      const data = await res.json();
      document.getElementById('content').textContent = data.content;
    }
    load();
    setInterval(load, 30000);
  </script>
```

---

## How Agents Extend Space Agent

### 1. Write a SKILL.md

Place in:
```
/srv/space/customware/L1/_admin/mod/chimera/ext/skills/<skill-name>/SKILL.md
```

Space Agent discovers it automatically.

### 2. Call the File API

Any agent with HTTP access can read/write:

```bash
# Read
curl -X POST http://100.67.172.114:3000/api/file_read \
  -H 'Content-Type: application/json' \
  -d '{"path":"L2/user/chimera-data/MACRO.json"}'

# Write
curl -X POST http://100.67.172.114:3000/api/file_write \
  -H 'Content-Type: application/json' \
  -d '{"path":"L2/user/chimera-data/ALERTS.json","content":"{...}"}'
```

### 3. Create Spaces via API

Spaces are just YAML files. Write them directly:

```bash
curl -X POST http://100.67.172.114:3000/api/file_write \
  -H 'Content-Type: application/json' \
  -d '{"path":"L2/user/spaces/my-space/space.yaml","content":"id: my-space\ntitle: My Space\nicon: chart"}'
```

---

## How Space Agent Learns

1. **SKILL.md self-extension** — The agent writes new skills when asked
2. **Git-backed history** — Every change is committed; rollback anytime
3. **Widget evolution** — Agent edits HTML/JS renderers dynamically
4. **Space cloning** — Export spaces as ZIP, share between users

---

## Operational Commands

```bash
# Status
systemctl status space-agent

# Restart
systemctl restart space-agent

# Logs
journalctl -u space-agent -f

# Update from Git
cd /root/space-agent && node space update

# Customware path
cd /root/space-agent && node space get CUSTOMWARE_PATH
```

---

## Z: Drive Deprecation

**OLD**: `Z:\reports\auto\` (Linux PC, DEAD)
**NEW**: `/srv/space/customware/L2/user/chimera-data/` (VPS)

Update all scripts and skills that reference the old path.

---

*space-agent-integration skill v1.0 | 2026-04-29 | VPS: 100.67.172.114:3000*
