---
name: codex-runtime-router
description: Decide where a task should run, which model lane it belongs to, how to sync created skills and durable artifacts, and how to announce runtime status at the top of each reply. Use for platform routing, model routing, session closeout sync, and response-header discipline.
---

# Codex Runtime Router

Use this skill when the work needs a routing decision across:

- Windows Codex
- Windows Claude
- Kimi VPS / OpenClaw
- GitHub handoff and sync

Also use it when deciding:

- which model lane fits the task
- whether a new skill should stay local or be shared through GitHub
- what the response header should say

## Response Header Contract

Start the reply with one compact line:

`Runtime: model=<name> | reasoning=<effort> | quota=<value-or-not-exposed> | lane=<planning|execution|research|mixed> | why=<short reason>`

Rules:

- If live quota is not exposed in the runtime, say `quota=not exposed`.
- Do not invent percentages or remaining tokens.
- Keep the reason short and plain English.

## Platform Routing

### Use Windows Codex for

- local implementation
- local file edits
- Codex continuity
- shared instruction updates
- skill creation or migration in `C:\Users\becke\.codex\skills\`
- turning chat lessons into durable files

### Use Windows Claude for

- planning
- architecture tradeoffs
- human-facing synthesis
- coordination across tools, repos, and agents

### Use Kimi VPS / OpenClaw for

- live Chimera runtime work
- gateway, agent, cron, and Linux service checks
- live repo truth at `/root/openclawtrading/`
- production-like scripts and deploy validation

### Use GitHub for

- cross-platform handoffs
- shared skills
- deploy scripts
- durable notes other platforms must pull

## Model Routing

This runtime does not currently expose a verified automatic per-request model switch for the same session. Treat model routing as an enforced decision rule, not a guaranteed hidden switch.

### Planning lane

- Preferred model when selectable: `gpt-5.5`
- Preferred reasoning: `high` or `xhigh`
- Use for:
  - architecture
  - strategy
  - large system design
  - policy and workflow design
  - "why this and not that?" decisions

### Execution lane

- Preferred model when selectable: `gpt-5.4`
- Preferred reasoning: `medium`
- Use for:
  - coding
  - patching
  - testing
  - file edits
  - bounded implementation loops

### Fast mechanical lane

- Preferred model when selectable: `gpt-5.4-mini`
- Preferred reasoning: `low`
- Use for:
  - simple formatting
  - bulk mechanical edits
  - low-judgment transforms

## Session Sync Contract

If the session creates or updates any durable artifact, capture it in the closeout:

- skills created
- skills updated
- startup or routing files changed
- handoffs created
- docs created
- scripts created
- important reports or dashboards created

For each item, say whether it is:

- `local only`
- `shared in GitHub repo but not pushed yet`
- `pushed and available to other platforms`

## Shared Skill Rule

If a skill should be available on more than one platform:

1. update the local Codex skill copy in `C:\Users\becke\.codex\skills\`
2. mirror it into `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\`
3. mention it in the latest checkpoint handoff
4. do not call it cross-platform synced unless the GitHub repo is actually up to date

## Closeout Minimum

When ending meaningful work, make sure the latest handoff or continuity note states:

- what was created
- what was updated
- what platform should use it
- what still needs push or pull
- what model lane was used
- what could not be verified
