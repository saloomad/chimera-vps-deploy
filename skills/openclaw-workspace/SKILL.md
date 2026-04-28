---
name: openclaw-workspace
description: Canonical local skill for creating, auditing, and optimizing OpenClaw agent workspaces and instruction files. Use when creating or optimizing agents, standardizing workspace defaults, deciding what files belong in persistent vs spawned agents, reducing bootstrap bloat, or aligning local work with live `AGENT_OPTIMIZATION.md` and `WORKSPACE_STANDARD.md`.
triggers:
  - create agent
  - optimize agent
  - optimize instructions
  - agent workspace
  - workspace standard
  - what files should this agent have
  - standardize agent files
  - AGENTS.md SOUL.md USER.md
---

# OpenClaw Workspace Skill

This is the **local Codex counterpart** to the live OpenClaw standards in:
- `/home/open-claw/openclawtrading/AGENT_OPTIMIZATION.md`
- `/home/open-claw/openclawtrading/WORKSPACE_STANDARD.md`

Use this skill so agent-creation and agent-optimization work stops living in memory or one-off chat explanations.

## Overview

OpenClaw workspace files form the agent's "soul and memory" — they are injected into the system prompt on every turn (or on relevant turns), giving the agent its identity, behavioral rules, environmental knowledge, and long-term memory. Managing these files well is critical: bloat wastes tokens, redundancy creates confusion, and stale content leads to bad decisions.

**Token budget:** 20,000 chars per file, ~150,000 chars total across all bootstrap files.

## Read First

When the Linux box is reachable, read these first:
- `/home/open-claw/openclawtrading/AGENT_OPTIMIZATION.md`
- `/home/open-claw/openclawtrading/WORKSPACE_STANDARD.md`
- `/home/open-claw/openclawtrading/AGENT_STANDARDS.md`
- `/home/open-claw/openclawtrading/STARTUP_SEQUENCE.md`

If Linux is not reachable, fall back to:
- `docs/OPENCLAW_LIVE_MIRROR_2026-04-17_round8/AGENT_OPTIMIZATION.md`
- `docs/OPENCLAW_LIVE_MIRROR_2026-04-17_round8/WORKSPACE_STANDARD.md`
- repo agent files you are actually changing

If the task reveals a repeated pattern or missing reusable behavior, also read:
- `.claude/skills/codex-skill-opportunity-detector/SKILL.md`
- `.claude/skills/workflow-skill-capture/SKILL.md`

## Default Standard

Treat this as the canonical default unless the live standard proves otherwise.

### Persistent agents

Required:
- `SOUL.md`
- `AGENTS.md`
- `IDENTITY.md`
- `TOOLS.md`
- `USER.md`
- `HEARTBEAT.md`
- `MEMORY.md`
- `KANBAN.md`
- `memory/YYYY-MM-DD.md`

Recommended when justified:
- `SCRATCH_PAD.md`
- `LESSONS.md`
- `CURRENT_BRIEF.md`
- `STATE.json`
- `SPAWN_CONTEXT.md`
- `THOUGHTS.md`
- `CHECKLIST.md`
- `STATUS.md`
- `MONITOR.md`
- `PENDING_QUESTIONS.json`
- `REPORT_FORMAT.md`
- `MODEL_ROUTING.md`
- `YOUTUBE_OVERLAY.md`

### Spawned agents

Required:
- `AGENTS.md`
- `SOUL.md` when role identity matters

Optional only when justified:
- `TOOLS.md`
- `CURRENT_BRIEF.md`
- `CHECKLIST.md`

### Parent-to-child context pattern

For persistent parent agents that feed spawned children, prefer:
- `SPAWN_CONTEXT.md`
- `THOUGHTS.md`
- plus deeper supporting files behind them

Use the short files as the first child read, not the whole bundle every time.

### Startup-load reality

OpenClaw can load extra startup files through the live hook/config layer, but not every useful file should be bootstrapped.

Good startup additions are short indexes and standards such as:
- `skills/agent-handbook/SKILL.md`
- `OPENCLAW_BIBLE.md`
- `WORKSPACE_STANDARD.md`
- short registries and role maps

Do not auto-load large research dumps, logs, or bulky strategy notes. Those should be referenced on demand or summarized into `SPAWN_CONTEXT.md`, `CURRENT_BRIEF.md`, or `THOUGHTS.md`.

### Skill-trigger reality

Skills are not magical background daemons.

If you want a skill to "auto-trigger," one of these must be true:
- the agent instructions explicitly route that task class through the skill
- a startup/bootstrap file makes the skill the default first stop
- a hook/router/runtime rule enforces it

If none of those are true, the skill is only available, not guaranteed.

## File Inventory

| File | Purpose | Loaded When | Sub-agents? |
|------|---------|-------------|-------------|
| `AGENTS.md` | Boot sequence, checklists, behavioral rules | Every turn (all agents) | Yes |
| `SOUL.md` | Persona, tone, values, continuity philosophy | Every turn (all agents) | Yes |
| `TOOLS.md` | Env-specific notes (SSH, TTS, cameras, devices) | On-demand reference (part of bootstrap set) | Yes |
| `USER.md` | Human profile, preferences, relationship context | Every turn (all agents) | Yes |
| `IDENTITY.md` | Name, emoji, avatar, self-description | Every turn | Yes |
| `HEARTBEAT.md` | Periodic check tasks and health routines | Every heartbeat turn | Depends |
| `BOOT.md` | Startup actions (requires `hooks.internal.enabled`) | On gateway startup | No |
| `BOOTSTRAP.md` | First-time onboarding script — delete after use | New workspaces only | No |
| `MEMORY.md` | Long-term curated facts and iron-law rules | Main sessions only | No |
| `memory/YYYY-MM-DD.md` | Daily session logs | Loaded per AGENTS.md boot sequence | No |
| `checklists/*.md` | Step-by-step ops guides | Referenced in AGENTS.md, loaded on demand | No |

**Security rule:** MEMORY.md must NEVER be loaded in group chats or sub-agent sessions — it contains private context that should not leak.

For full details on each file's design, anti-patterns, and section structure, see [references/workspace-files.md](references/workspace-files.md).

## Workspace Paths

| Path | Purpose |
|------|---------|
| `~/.openclaw/workspace/` | Default workspace for main agent |
| `~/.openclaw/workspace-<profile>/` | Per-profile workspace (multiple agents) |
| `~/.openclaw/workspace/vendor/OpenClaw-Memory/` | Vendor-managed base files (synced from upstream) |
| `~/.openclaw/workspace/checklists/` | Checklist files referenced from AGENTS.md |
| `~/.openclaw/workspace/memory/` | Daily session logs |
| `~/.openclaw/workspace/docs/` | On-demand documentation (NOT auto-loaded) |

Config key: `agents.defaults.workspace` or per-agent `agents.list[].workspace`.

## Workflow: Audit Existing Workspace

Use when workspace files may be bloated, stale, or redundant.

1. **Read all active files** — AGENTS.md, SOUL.md, TOOLS.md, USER.md, IDENTITY.md, HEARTBEAT.md, BOOT.md, MEMORY.md
2. **Check character counts:**
   ```bash
   wc -c ~/.openclaw/workspace/AGENTS.md
   wc -c ~/.openclaw/workspace/SOUL.md
   wc -c ~/.openclaw/workspace/TOOLS.md
   wc -c ~/.openclaw/workspace/USER.md
   wc -c ~/.openclaw/workspace/IDENTITY.md
   wc -c ~/.openclaw/workspace/MEMORY.md
   # Or all at once:
   wc -c ~/.openclaw/workspace/*.md
   ```
3. **Flag files over 10,000 chars** — prime candidates for trimming or offloading to `docs/`
4. **Check for redundancy** — same fact in SOUL.md and AGENTS.md? Same tool note in TOOLS.md and MEMORY.md?
5. **Check for staleness** — outdated SSH hosts, old tool names, deprecated rules, historical context that's no longer needed
6. **Check MEMORY.md discipline** — should contain curated facts, lessons learned, decisions, and critical rules — not raw session summaries or task-specific notes
7. **Propose targeted edits** — trim, move to docs/, or restructure
8. **Check startup breadcrumbs** — confirm the workspace points to real shared standards, registries, checklists, or supporting files instead of copying them badly
9. **Check child handoff design** — if the agent acts as a persistent parent, decide whether it needs `SPAWN_CONTEXT.md`, `THOUGHTS.md`, `CURRENT_BRIEF.md`, or `STATE.json`

See [references/optimization-guide.md](references/optimization-guide.md) for specific optimization strategies.

## Workflow: Set Up New Workspace

Use when creating a workspace for a new agent from scratch.

**File creation order** (matters for boot sequence to work):

1. `SOUL.md` — persona and values first; everything else follows from identity
2. `AGENTS.md` — boot sequence, safety rules, checklist table
3. `IDENTITY.md` — name, emoji, avatar
4. `USER.md` — human profile and preferences (main agent only)
5. `TOOLS.md` — environment-specific notes (add as you discover env details)
6. `MEMORY.md` — start minimal; only truly universal iron laws
7. `HEARTBEAT.md` — periodic health checks (optional, add when needed)
8. `BOOT.md` — startup hooks (optional, only if `hooks.internal.enabled = true`)
9. `BOOTSTRAP.md` — first-run onboarding (optional; delete after first successful startup)

**Minimal viable workspace:** AGENTS.md + SOUL.md + TOOLS.md. Everything else is optional.

If the new agent is a **persistent parent** for spawned children:
1. add `CURRENT_BRIEF.md`
2. add `STATE.json` if machine-readable state helps
3. add `SPAWN_CONTEXT.md`
4. add `THOUGHTS.md`
5. tell child workers in `AGENTS.md` what to read first and when fresh reports still override parent judgment

**BOOTSTRAP.md note:** If creating a BOOTSTRAP.md, include a self-deletion instruction at the end:
```
## Final Step
Delete this file: exec `rm ~/.openclaw/workspace/BOOTSTRAP.md`
```

## Workflow: Memory Distillation

Use periodically (weekly or monthly) to keep MEMORY.md lean.

1. **Read all recent daily logs:** `memory/YYYY-MM-DD.md` files from the past period
2. **Identify candidates for promotion to MEMORY.md:**
   - Rules violated more than once (recurring mistakes)
   - Hard-won discoveries that aren't in skills docs
   - Env-specific facts that should always be in context (not left to memory_search recall)
3. **Check what's already in MEMORY.md** — avoid duplicates
4. **Draft additions** — use iron-law format: concise, action-oriented, unambiguous
5. **Archive old daily logs** — move files older than 30 days to `memory/archive/` or delete
6. **Check MEMORY.md total size** — keep under 10,000 chars; if larger, review for rules that are now stable enough to move to a skill's SKILL.md instead

**Do NOT put in MEMORY.md:**
- Long narratives or session summaries
- Things already covered in skill docs
- Anything specific to a single past task
- Episodic or task-specific memories (store those via memory_search/SQLite instead)

## Workflow: Add or Update a Checklist

Use when adding a new high-risk operation type or updating an existing checklist.

1. **Create or edit** `checklists/<operation-name>.md`
2. **Structure:**
   ```markdown
   # Checklist: <Operation Name>

   ## Pre-flight
   - [ ] Step 1
   - [ ] Step 2

   ## Execution
   - [ ] Step 3

   ## Verification
   - [ ] Confirm outcome
   - [ ] Log result in memory
   ```
3. **Register in AGENTS.md** — add a row to the checklists table:
   ```markdown
   | <Operation description> | `checklists/<filename>.md` |
   ```
4. **Keep checklists short** — if a checklist exceeds ~50 lines, it's probably trying to be documentation; move narrative content to `docs/` and keep only the actionable steps

## Workflow: Optimize Agent Instructions

Use this when changing `AGENTS.md`, `SOUL.md`, `USER.md`, or related files.

1. Decide what belongs in each file instead of writing everything into `AGENTS.md`
2. Convert vague values into trigger -> action rules
3. Move long references and examples out of bootstrap files
4. Keep shared rules in shared standards when possible
5. Put durable facts in `MEMORY.md`, repeated failures in `LESSONS.md`, and current mutable state in brief/state files
6. If the same optimization advice keeps getting repeated, create or update a skill instead of repeating yourself in chat

## Output Expectations

When using this skill, leave behind:
- the chosen workspace type: persistent or spawned
- the file package used
- why any non-standard file was added
- what shared references the agent should read instead of duplicating
- what child agents should read first, if parent context is relevant
- any contradictions, token-bloat risks, or stale-file risks you found

## Workflow: Update TOOLS.md

Use when adding a new tool, device, or environment capability.

**TOOLS.md = environment-specific cheat sheet.** It should contain:
- SSH hosts and common commands for this specific machine
- TTS provider, voice IDs, and any quirks
- Camera IDs or device names for this setup
- Node device IDs or names
- Any local aliases or shortcuts that aren't obvious

**Do NOT put in TOOLS.md:**
- General skill documentation (use skill SKILL.md files)
- Things that are the same across all environments
- Installation instructions (use docs/)

**Format conventions:**
```markdown
# TOOLS.md - Local Notes

## SSH
- Main server: `ssh user@hostname`

## TTS
- Provider: Edge
- Voice: zh-CN-XiaoxiaoNeural

## Cameras
- Living room: node-id `abc123`, device `camera-0`
```

## Common Issues

### File exceeds token limit
**Symptom:** File is over 20,000 chars; OpenClaw may truncate it.
**Fix:** Audit for content that belongs in `docs/` (loaded on demand) instead of the bootstrap file. Move detailed references, historical context, and long examples out. Keep only what needs to be on every turn.

### MEMORY.md leaking to groups
**Symptom:** Agent shares private context in group chats or Discord.
**Fix:** Ensure MEMORY.md boot step in AGENTS.md is gated: "Main session only: Read MEMORY.md". Verify the agent's boot sequence explicitly checks session type before loading.

### Boot sequence not loading files
**Symptom:** Agent doesn't know about content in SOUL.md, USER.md, or MEMORY.md at session start.
**Fix:** Check that AGENTS.md boot sequence explicitly names each file to read. The agent won't auto-load files — it follows the boot sequence instructions in AGENTS.md. Verify `hooks.internal.enabled = true` in config if using BOOT.md.

### MEMORY.md growing too large
**Symptom:** File approaches or exceeds 10,000 chars; reading it on every turn wastes significant context.
**Fix:** Run memory distillation workflow. Move stable rules that have been incident-free for months into relevant skill SKILL.md files. Delete rules that are no longer relevant.

### Workspace changes not taking effect
**Symptom:** Agent still uses old content after editing a workspace file.
**Fix:** Workspace files are read at session start per the boot sequence. Restart the gateway or start a new session for changes to take effect.

### Agent optimization knowledge keeps living in chat instead of a skill
**Symptom:** The same agent-file advice keeps being re-explained manually.
**Fix:** Use this skill as the first stop, update it when live standards improve, and capture new repeated patterns through the skill/workflow detector skills instead of relying on memory.

## Reference Files

| Reference | Coverage |
|-----------|---------|
| [workspace-files.md](references/workspace-files.md) | Deep-dive on each file: purpose, design principles, anti-patterns, section structure |
| [optimization-guide.md](references/optimization-guide.md) | Token efficiency strategies, audit commands, distillation process |
