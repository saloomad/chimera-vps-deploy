---
name: openclaw-orchestration-proof-router
description: Use when a task involves OpenClaw orchestration choices, core-agent spawning, Task Flow, Lobster, heartbeat continuation, external ACP sessions, peer review or council patterns, or proof that orchestration really happened.
triggers:
  - orchestration
  - task flow
  - taskflow
  - lobster
  - heartbeat
  - peer to peer
  - p2p review
  - council
  - acp
  - codex session
  - claude session
  - core agents
  - objective checker
  - prompt engineer
  - prove orchestration
---

# OpenClaw Orchestration Proof Router

Use this skill when the job is not just "do the work," but "choose the right OpenClaw orchestration structure and prove it."

## Read First

- `tasks/TASK_REGISTRY.md`
- `tasks/JOB_BOARD.md`
- `trace/ACTION_LOG.md`
- `docs/OPENCLAW_LIVE_MIRROR_2026-04-16/orchestration/ORCHESTRATION_DECISION_MODEL.md`
- `docs/OPENCLAW_LIVE_MIRROR_2026-04-16/orchestration/ORCHESTRATION_HANDOFF_CONTRACT.md`
- `tmp_openclaw_patch_20260416_round3/OPENCLAW_BIBLE.md`
- `tmp_openclaw_patch_20260416_round3/OPENCLAW_FEATURES.md`
- `docs/OPENCLAW_LIVE_MIRROR_2026-04-17_round8/AGENT_REGISTRY.md`
- `workflows/openclaw/orchestration-proof-loop.md`

## Decision Order

1. If the request is really coding-harness work, prefer ACP.
2. If deterministic multi-step flow matters, prefer Lobster.
3. If durable restartable state across restarts matters, prefer Task Flow.
4. If safe recurring continuation matters, prefer heartbeat.
5. If the trigger is event-driven, prefer hooks.
6. If the timing must only wake work, prefer cron or timers as the wake-up trigger.
7. If the work is internal, bounded, and parallel, prefer native subagents or fan-out.
8. If multiple peers must challenge the same proposal, prefer P2P review or council.
9. If one worker plus a quality gate is enough, use the simpler review loop.
10. Otherwise, do not fake orchestration. Say the direct path is the right choice.

## Pattern Selector

### Lobster

Choose for:

- deterministic multi-step flows
- parallel branches with clear dependencies
- explicit gates and conditional reruns
- a visible workflow contract

### Task Flow

Choose for:

- durable restartable state
- workflows that must recover after interruption
- explicit phase or state-machine ownership

### Heartbeat

Choose for:

- continuation of approved work
- periodic objective re-checks
- stall detection and stop rules

### Hooks

Choose for:

- validation after an agent or step finishes
- event-driven reactions
- quality gates tied to specific lifecycle events

### Cron Or Timers

Choose only as:

- wake-up triggers
- cadence drivers

Do not confuse a timer with the orchestration logic itself.

## Live Trading Pipeline Rule

Do not route every trading cycle into the deep research swarm.

The default live trading loop should stay lean:

1. monitor inputs
2. detect setup
3. gather only the needed specialists
4. validate freshness, conflicts, and risk
5. decide `execute`, `watch`, or `reject`
6. manage the position
7. review and update state

Use the deep research swarm only when the task is materially bigger than the normal live loop, such as:

- weekly thesis generation
- major event review
- deep ambiguity requiring cross-verification
- post-trade failure analysis

## Discovery Rules

Before claiming the "right agent" was chosen, check both:

- the configured agent inventory or runtime config when available
- the documented agent registry or role descriptions

If those disagree, do not hide it. Record the contradiction and route through the safest verified surface.

## Core Support Rules

For non-trivial work, consider at minimum:

- `orchestrator`
- `project-manager`
- `reviewer`

For complex or ambiguous work, also evaluate:

- `planner`
- `critic`
- `objective`
- `objective-checker`
- `prompt-engineer`
- `tester`
- `workflow` or tracker owner

Use one execution-facing worker per real task unit when parallelism is justified.

## Heartbeat Completion Contract

When a heartbeat is the chosen pattern, completion should mean:

- objective complete
- required tests or proof passed
- unresolved blockers zero
- blocking improvement backlog zero
- required council agrees when the task needed one
- council evidence references exist when a council was part of done criteria

Manual cleanup is not proof of self-stop.

Require explicit runtime stop outcomes such as:

- `stop_complete`
- `stop_loop_guard`
- `stop_max_wakes`

## Transparency Fields

For major orchestration decisions, report:

- chosen pattern
- chosen runtime
- chosen lead
- selected workers or core roles
- cadence when heartbeat is involved
- stop contract when heartbeat is involved
- why the other main patterns were not chosen
- docs proof
- config proof
- runtime proof
- remaining risk

## Write Targets

- `tasks/TASK_REGISTRY.md`
- `tasks/JOB_BOARD.md` when routing or ownership changes
- `trace/ACTION_LOG.md`
- `docs/` for the audit or proof report
- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/KANBAN.md`
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/memory/MEMORY.md`
- `harnesses/codex/chimera/memory/LESSONS.md`

## Expected Output

Leave behind:

1. the chosen orchestration pattern
2. the proof matrix by evidence type
3. any contradictions or discovery gaps
4. any new task needed for blocked live proof
5. the next safe step
