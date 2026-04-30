# Orchestration Routing And Swarm Standard

Updated: 2026-04-30

## Goal

Keep one universal orchestration base across platforms while adding one specialized deep research swarm for the jobs that truly need it.

## The Split

### Universal Base

Use `objective-orchestration-loop` for every non-trivial task.

Its permanent contract is:

`plan -> execute -> review -> repeat`

It now also requires an upfront orchestration-class choice:

- `direct task`
- `bounded build`
- `deep research swarm`
- `always-on pipeline`

### Specialized Layer

Use `deep-research-swarm` only for evidence-heavy work.

It adds:

- landscape scan
- dimension decomposition
- parallel deep dive
- cross-verification
- targeted validation
- insight extraction
- writing pipeline

It now also requires:

- a written `plan.md` before worker fan-out
- file-first handoffs
- explicit sub-agent roles
- targeted reruns instead of whole-swarm restarts
- a challenge suite for failure testing

## Model Routing By Role

### Orchestrator

- default: `gpt-5.5 high`
- use for decomposition, gate control, rerun decisions, and final structure

### Worker

- default: `gpt-5.3-codex-spark low` or `gpt-5.4-mini low`
- use for cheap first-pass slices

### Verifier

- default: `gpt-5.5 high`
- use for contradiction handling and confidence grading

### Reviewer

- default: `gpt-5.5 high` when judgment-heavy
- default fallback: `gpt-5.4 medium` when the review is bounded

### VPS Live Worker

- default: `MiniMax-M2.7-highspeed`
- rerun weak or ambiguous slices on `k2.6` with thinking on

## Trading Pipeline Guidance

### What Stays Lean

The routine live loop:

1. monitor inputs
2. detect setup
3. gather only needed specialists
4. validate freshness, conflicts, and risk
5. decide `execute`, `watch`, or `reject`
6. manage the position
7. review and update state

### What Uses The Swarm

- weekly BTC or market theses
- major event reviews
- deep ambiguity cases
- post-trade failure analysis
- large token or sector comparisons

## Deep Swarm Role Set

Use these roles when a platform supports worker fan-out:

- `swarm-orchestrator`
- `landscape-scanner`
- `dimension-researcher`
- `cross-verifier`
- `targeted-validator`
- `insight-synthesizer`
- `chapter-writer`
- `assembly-editor`
- optional `docx-finisher`

## Research Pack

The reusable design notes now live under:

- `research/orchestration/KIMI_ORCHESTRATION_SOURCE_SYNTHESIS_2026-04-30.md`
- `research/orchestration/BITCOIN_SWARM_CASE_STUDY_2026-04-30.md`

The concrete skill references now live under:

- `skills/deep-research-swarm/references/PLAN_AND_STATE_TEMPLATE.md`
- `skills/deep-research-swarm/references/SUBAGENT_ROLE_MAP.md`
- `skills/deep-research-swarm/references/SKILL_COMBINATION_MATRIX.md`
- `skills/deep-research-swarm/references/CHALLENGE_SUITE.md`
- `skills/deep-research-swarm/references/WORKER_VERDICT_SCHEMA.md`
- `skills/openclaw-orchestration-proof-router/references/OPENCLAW_WORKFLOW_AND_VERDICT_TEMPLATES.md`

The Claude/Cowork adapter now lives at:

- `skills/cowork-orchestration-adapter/SKILL.md`

The OpenCowork adapter now lives at:

- `skills/opencowork-orchestration-adapter/SKILL.md`

The OpenClaw feature router now lives at:

- `skills/openclaw-feature-router/SKILL.md`

The latest bounded proof note lives under:

- `research/orchestration/ORCHESTRATION_CHALLENGE_RESULTS_2026-04-30.md`

## Pattern Selector For OpenClaw

- Lobster: deterministic multi-step flow
- Task Flow: durable restartable state
- heartbeat: safe recurring continuation
- hooks: validation and event reactions
- cron or timers: wake-up trigger only

## Example Set

### Example A: BTC Research Swarm

- class: `deep research swarm`
- dimensions: timeframe, on-chain, derivatives, macro, ETF flow, alt rotation
- outputs: dimension notes, cross-verification, insights, final thesis

### Example B: Always-On Setup Watcher

- class: `always-on pipeline`
- trigger: recurring wake or event
- outputs: `execute`, `watch`, or `reject`
- escalation: open a separate deep-swarm objective only if ambiguity is deep enough

### Example C: Post-Trade Review Loop

- class: `deep research swarm`
- dimensions: chart state, specialist advice, freshness, execution timing, risk handling
- rerun only contradictory slices
