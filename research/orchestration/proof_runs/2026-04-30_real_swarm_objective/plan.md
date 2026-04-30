# Plan: Chimera Deep Swarm Deployment Memo

## Objective
Produce a real internal memo that decides how Chimera should use the deep swarm in trading and orchestration work, including platform routing, heartbeat policy, visual observability, and the exact places where the swarm should and should not be used.

## User Intent Classification
- Research required: YES
- Writing required: YES
- Code/building required: NO
- Orchestration class: `deep research swarm`
- Expected deliverable: recommendation memo with visual workflow

## Current Reality
- Date checked: 2026-04-30
- Freshness window: same-session internal design truth with current shared skill files
- Known tensions:
  - The swarm logic is much stronger now, but it still needs one real end-to-end run.
  - Heartbeats are useful for continuation, but they should not be confused with the orchestration itself.
  - Platform behavior differs enough that one giant copy-paste skill is the wrong answer.

## Stage 1 - Landscape Scan
- Owner: `swarm-orchestrator`
- Output: `research/landscape_brief.md`
- Gate: the reusable patterns, platform differences, and unresolved questions are explicit

## Stage 2 - Dimension Decomposition
- Owner: `swarm-orchestrator`
- Output: dimension list below
- Gate: dimensions are distinct and still overlap enough to cross-check each other

## Dimensions
1. `use-case-routing` - when deep swarm should and should not be used in Chimera trading and build work
2. `platform-routing` - how Codex, Claude/Cowork, OpenClaw/Kimi, and Hermes should apply the same logic differently
3. `heartbeat-and-automation-policy` - when to use heartbeats, timers, hooks, or no recurring automation at all
4. `visual-observability` - how a human should see the orchestration and what artifacts or diagrams should exist

## Stage 3 - Parallel Deep Dive
- Owner: `dimension-researcher`
- Output: `research/dim01_use-case-routing.md` through `research/dim04_visual-observability.md`
- Gate: all four outputs exist and each includes verdict-schema fields plus the real reasoning for that slice

## Stage 4 - Cross-Verification
- Owner: `cross-verifier`
- Output: `research/cross_verification.md`
- Gate: conflicts, overlaps, and shared recommendations are explicit

## Stage 5 - Targeted Validation
- Owner: `targeted-validator`
- Trigger: only if one or more dimensions conflict on a recommendation that changes the final memo
- Output: `research/targeted_validation.md`
- Gate: unresolved disagreement is either resolved or preserved honestly

## Stage 6 - Insight Extraction
- Owner: `insight-synthesizer`
- Output: `research/insights.md`
- Gate: the memo-level rules are explicit and actionable

## Stage 7 - Writing Pipeline
- Owner: `assembly-editor`
- Outputs:
  - `writing/outline.md`
  - `final/chimera_deep_swarm_deployment_memo.md`
  - `final/visual_workflow.md`

## Done Criteria
- all dimension outputs exist
- cross-verification is complete
- the memo answers where deep swarm belongs, where it does not, and what heartbeat/automation role is appropriate
- at least one visual workflow artifact exists
- if the run stays clean, the verdict schema is promoted deeper into platform-specific templates

## Stop Condition
- `complete` when artifacts and gates pass
- `blocked` if the proof run cannot produce a coherent recommendation
- `iterate` if only one or more slices need rerun
