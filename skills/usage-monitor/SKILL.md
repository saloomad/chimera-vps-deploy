---
name: usage-monitor
description: "Use proactively for any request about usage, quota, model switching, or efficiency. Checks Claude Code/Kimi session and weekly limits via browser, checks MiniMax quota via CLI, updates ~/.claude/usage_cache.json, and generates model-shift reports. Triggers: 'check usage', 'quota report', 'which model should I use', 'am I near my limit', 'usage snapshot', 'refresh usage', 'minimax quota', 'kimi usage'."
---

# Usage Monitor

Unified usage tracking and model-shift advisor for Claude Code (Kimi), MiniMax, and the claude.ai Pro subscription. Updates a shared cache file that the Stop hook reads to append a live snapshot after every response.

## Architecture

```
~/.claude/usage_cache.json      ← shared cache (read by stop hook)
~/.claude/hooks/usage-footer.sh ← stop hook: reads cache → appends footer
Cron 41a91c6b (*/15 min)        ← browser check → updates claude section
Cron 85a8436d (hourly :07)      ← mmx CLI check → updates minimax section
```

## Platform Detection

Before running any step, detect the platform:

```bash
HAS_CHROME_MCP=false   # set true if mcp__Claude_in_Chrome__* tools respond
HAS_MMX=false          # set true if `mmx --version` exits 0
HAS_BROWSER=false      # set true on Windows Claude Code with Chrome MCP connected
```

- **Claude Code (Windows)**: Chrome MCP available → can run browser check + CLI check
- **Codex (Windows)**: no Chrome MCP → CLI check only
- **Linux VPS**: no Chrome MCP, check if `mmx` installed → CLI only

## Mode 1 — Claude/Kimi Browser Check

**Platform**: Claude Code (Windows) only. Requires Chrome MCP.

**Skip on**: Codex, Linux VPS. Print `[SKIP] Chrome MCP not available on this platform`.

### Steps

1. `mcp__Claude_in_Chrome__tabs_context_mcp` with `createIfEmpty: true` → get `tabId`
2. Navigate to `https://claude.ai/settings/usage`, wait 3 seconds
3. `mcp__Claude_in_Chrome__read_page` with `filter: all`, `depth: 4`
4. Parse from accessibility tree:
   - `"X% used"` near `"Current session"` → `session_pct`
   - `"Resets in X hr Y min"` or `"Resets in X min"` → `session_resets_in`
   - `"X% used"` near `"All models"` under `"Weekly limits"` → `weekly_pct`
   - `"Resets Mon/Tue/..."` → `weekly_resets`
   - `"X% used"` near `"Claude Design"` → `design_pct`
   - `"Pro plan"` or `"Max plan"` → `plan`
5. Read existing cache (preserve `minimax` key), write updated cache:

```json
{
  "updated_at": "<ISO-8601 UTC>",
  "claude": {
    "session_pct": 0,
    "session_resets_in": "4 hr 12 min",
    "weekly_pct": 46,
    "weekly_resets": "Mon 5:00 AM",
    "design_pct": 50,
    "plan": "Pro"
  },
  "minimax": "<preserve existing>"
}
```

## Mode 2 — MiniMax CLI Check

**Platform**: Any platform where `mmx` is installed.

**Skip if**: `mmx --version` fails. Print `[SKIP] mmx not found`.

### Steps

1. Run: `mmx quota show --output json --quiet 2>&1`
2. Parse `model_remains` array. For each entry, compute:
   - `interval_pct = current_interval_usage_count / current_interval_total_count * 100` (skip if total = 0)
   - `weekly_pct = current_weekly_usage_count / current_weekly_total_count * 100` (skip if total = 0)
   - `resets_in_h = remains_time / 3_600_000`
3. Extract key models (see [model-shift-guide.md](references/model-shift-guide.md) for thresholds):
   - `MiniMax-M*` → text interval pct + resets_in_h
   - `speech-hd` → speech weekly pct
   - `music-2.6` → music weekly pct
   - `image-01` → image interval pct
4. Read existing cache (preserve `claude` key), write updated `minimax` section:

```json
{
  "minimax": {
    "text_used": 4185,
    "text_total": 4500,
    "text_pct": 93.0,
    "text_resets_in_h": 3.3,
    "speech_weekly_pct": 90.7,
    "music_weekly_pct": 100.0,
    "image_interval_pct": 100.0,
    "video_available": true
  }
}
```

## Mode 3 — Usage Report + Model-Shift Analysis

Run after updating cache (or on demand). Read `~/.claude/usage_cache.json` and:

1. Print current snapshot table
2. Apply thresholds from [model-shift-guide.md](references/model-shift-guide.md):
   - `[ ]` = OK (< 60%)
   - `[!]` = caution (60–84%)
   - `[!!]` = critical (≥ 85%)
3. Print shift recommendations based on current levels
4. Note time to next reset for any critical quota

### Report Format

```
## Usage Report — [timestamp]

Active: [provider]/[model]  |  Platform: [detected]

| Source      | Metric           | Used  | Status | Resets  |
|-------------|------------------|-------|--------|---------|
| Kimi/CC     | Session          |   3%  |  [ ]   | 3h 57m  |
| Kimi/CC     | Weekly           |  46%  |  [ ]   | Mon 5am |
| Kimi/CC     | Design           |  50%  |  [ ]   | Mon 5am |
| MiniMax     | Text (interval)  |  93%  |  [!!]  | 3.3h    |
| MiniMax     | Speech (weekly)  |  90%  |  [!!]  | 7.3h    |
| MiniMax     | Music (weekly)   | 100%  |  [!!]  | 7.3h    |
| MiniMax     | Image (interval) | 100%  |  [!!]  | 7.3h    |
| MiniMax     | Video            |   0%  |  [ ]   | —       |

### Model Shift Recommendations
[generated from thresholds — see references/model-shift-guide.md]
```

## Mode `all` — Full Run

Run Mode 1 (if Chrome MCP available), then Mode 2 (if mmx available), then Mode 3.

## Invoke Patterns

```
/usage-monitor              → full run (all modes)
/usage-monitor claude       → Mode 1 only (browser check)
/usage-monitor minimax      → Mode 2 only (CLI check)
/usage-monitor report       → Mode 3 only (read cache, no fetch)
```

## Cache File

`~/.claude/usage_cache.json` — always read before writing to preserve the other platform's section.

If file missing: create it with both sections empty, then populate what's available.

## Stop Hook

The footer at `~/.claude/hooks/usage-footer.sh` reads the cache after every response.
To test it: `bash ~/.claude/hooks/usage-footer.sh`
To update it: edit the file directly — it reads `~/.claude/settings.json` for active model.
