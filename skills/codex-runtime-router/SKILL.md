---
name: codex-runtime-router
description: Decide where a task should run, which model lane it belongs to, what reasoning level to use, how spawned agents should inherit or override models, how to self-grade results, how to sync created skills and durable artifacts, and how to announce runtime status at the top of each reply. Use for platform routing, model routing, session closeout sync, and response-header discipline.
---

# Codex Runtime Router

Use this skill when the work needs a routing decision across:

- Windows Codex
- Windows Claude
- Kimi VPS / OpenClaw
- GitHub handoff and sync

Also use it when deciding:

- which model lane fits the task
- which reasoning level fits the task
- whether to split work into planning, execution, and review
- whether a weak result should be rerun on a stronger model or higher reasoning effort
- what model spawned agents should use
- whether a new skill should stay local or be shared through GitHub
- what the response header should say

Read `references/MODEL_ROUTING_SPEC.md` for the benchmark, pricing, quota, and platform-routing reference sheet.

## Response Header Contract

Start the reply with one compact line:

`Runtime: model=<name> | reasoning=<effort> | quota=<value-or-not-exposed> | phase=<plan|execute|review|mixed> | why=<short reason>`

Rules:

- Use the real active model and reasoning level for this session.
- If live quota is not exposed in the runtime, say `quota=not exposed`.
- Do not invent percentages or remaining tokens.
- Keep the reason short and plain English.

## Quota And Usage Check

Before claiming usage or quota:

1. try the local Codex CLI first
2. if it only exposes login state and not usage, say `quota=not exposed`
3. do not guess remaining messages, tokens, credits, or subscription percentages

Current verified truth on this Windows Codex machine:

- `codex login status` works
- a verified quota command has not been found yet
- the honest header value is still `quota=not exposed`
- shared helper script: `scripts/check_codex_runtime_status.ps1`

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
- stronger prompt shaping before implementation

### Use Kimi VPS / OpenClaw for

- live Chimera runtime work
- gateway, agent, cron, and Linux service checks
- live repo truth at `/root/openclawtrading/`
- production-like scripts and deploy validation
- model routing for live agent tasks on the VPS

### Use GitHub for

- cross-platform handoffs
- shared skills
- deploy scripts
- durable notes other platforms must pull

## Model Routing

This runtime does not currently expose a verified automatic per-request model switch for the same session. Treat model routing as an enforced decision rule, not a guaranteed hidden switch.

Current local default on Windows Codex:

- model: `gpt-5.4`
- reasoning: `medium`

Supported model overrides for spawned agents in this runtime:

- `gpt-5.5`
- `gpt-5.4`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5.3-codex-spark`
- `gpt-5.2`

Rule:

- the main thread should stay on the inherited runtime unless there is a strong reason to change
- spawned agents inherit the parent model by default
- only override a spawned agent model when the subtask clearly benefits from it and the user wants the stronger routing behavior

## Work Split

### Planning

Use for:

- architecture
- tradeoff selection
- policy and workflow design
- ambiguous or failure-sensitive tasks
- evaluation of whether the task should be broken apart

Preferred routing:

- Windows Claude or a strong planning-capable lead
- `gpt-5.5`
- reasoning `high` or `xhigh`

### Planning lane

- Use this label in the response header when the current turn is mostly planning.

### Execution

Use for:

- coding
- patching
- deterministic implementation loops
- test repair
- bounded file edits

Preferred routing:

- Windows Codex for local work
- Kimi VPS for live runtime work
- `gpt-5.4`
- reasoning `medium`

### Execution lane

- Use this label in the response header when the current turn is mostly implementation.

### Review

Use for:

- code review
- failure analysis
- final quality checks
- comparing whether a stronger rerun is justified

Preferred routing:

- `gpt-5.5` with `high` when the review needs judgment
- `gpt-5.4` with `medium` when the review is bounded and code-focused

### Research

Use for:

- doc lookups
- benchmark lookups
- product capability checks
- pricing or changelog verification

Preferred routing:

- strongest available model is optional
- accuracy and source quality matter more than raw model size
- official docs first

### Fast mechanical lane

Preferred model when selectable: `gpt-5.4-mini`
Preferred reasoning: `low`
Use for:
- simple formatting
- bulk mechanical edits
- low-judgment transforms

## Routing Heuristic

### Choose `gpt-5.5`

When the task is:

- high ambiguity
- architecture-heavy
- review-heavy
- likely to fail expensively if the first plan is weak
- worth paying more to reduce retries

### Choose `gpt-5.4`

When the task is:

- mostly implementation
- medium ambiguity
- bounded enough that a stronger planner is optional
- best served by good quality at lower cost than `gpt-5.5`

### Choose `gpt-5.4-mini`

When the task is:

- repetitive
- low-risk
- formatting-heavy
- primarily mechanical rather than judgment-heavy

### Escalate reasoning before escalating models

When possible, escalate in this order:

1. `low` -> `medium`
2. `medium` -> `high`
3. `high` -> `xhigh`
4. then move from `gpt-5.4` to `gpt-5.5`

If the task is already clearly planning-heavy or review-heavy, skip straight to the stronger lane.

## Rerun Rule

If the result is weak, incomplete, or uncertain:

1. say the first lane was not good enough
2. reroute to a stronger reasoning level or stronger model if that option is truly available
3. note the rerun reason in the closeout
4. record what lane would be better next time

Do not pretend the first lane was sufficient if the result quality says otherwise.

## Result Self-Grade

At closeout, grade the route internally in plain English. Capture at least:

- `task_type`
- `platform_used`
- `model_used`
- `reasoning_used`
- `result_quality` = strong / acceptable / weak
- `rerun_needed` = yes / no
- `next_time_better_route`

Example:

`execution coding | Windows Codex | gpt-5.4 medium | result_quality=strong | rerun_needed=no | next_time_better_route=same`

## Spawned Agent Rule

Spawned agents inherit the parent model by default.

Only override when there is a clear bounded need:

- planner or reviewer child: prefer `gpt-5.5` + `high`
- execution worker child: prefer inherited model, usually `gpt-5.4`
- fast explorer or mechanical worker child: consider `gpt-5.4-mini`

If you override, say why in one short line.

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

Also capture:

- model lane used
- reasoning level used
- phase used
- whether a rerun happened
- whether the route should change next time

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
- what reasoning level was used
- whether the result would have benefited from a stronger lane
- what could not be verified
