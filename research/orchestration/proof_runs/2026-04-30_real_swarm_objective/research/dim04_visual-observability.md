# Dimension 04 - Visual Observability

## Orchestration Class

- `deep research swarm`

## Why Not Other Classes

- not `direct task` because this requires cross-file synthesis about visibility, workflow state, and proof
- not `bounded build` because this slice is about the contract for visibility rather than a UI implementation
- not `always-on pipeline` because this is a design artifact for a one-off swarm proof run

## Freshness Requirement

- same-session design truth only
- use the current proof-run files and current shared swarm standard

## Required Artifacts

- `plan.md`
- `research/landscape_brief.md`
- `research/dim04_visual-observability.md`
- `research/cross_verification.md`
- `research/insights.md`
- `final/visual_workflow.md`

## Required Gates

- human-facing views are distinct from raw worker files
- the diagram or dashboard shows orchestration state, phase, and gate status
- the design separates evidence, confidence, and unresolved conflict
- the observable surface makes rerun and escalation points explicit
- the output is file-first and auditable without reading chat

## Stop Condition

- stop on complete
- stop on blocked if the orchestration still cannot be made legible from the proof artifacts

## Rerun Policy

- rerun only the visual-observability slice or a conflicting slice that changes the human-facing shape
- do not restart the whole swarm by default

## Escalation Policy

- escalate reasoning only for the specific slice that remains ambiguous
- rerun verification on a stronger lane if the view still hides state

## Must-Have Views

- one top-level orchestration status view showing objective, class, phase, owner, and current gate
- one phase timeline view showing landscape scan through writing pipeline
- one worker-fanout view showing roles, assigned dimensions, and verdict status
- one conflict-and-rerun view showing what disagreed and what was rerun
- one final memo or report view separating conclusions from unresolved issues
- one human drill-down path from summary to evidence files

## Must-Have Files

- `plan.md`
- `research/landscape_brief.md`
- `research/dim04_visual-observability.md`
- `research/cross_verification.md`
- `research/insights.md`
- `final/visual_workflow.md`
- `skills/deep-research-swarm/references/WORKER_VERDICT_SCHEMA.md`
- `skills/deep-research-swarm/references/PHASES_AND_GATES.md`

## Best Visual Patterns

- single-page control-room summary with status chips for class, phase, freshness, and gate
- swimlane diagram for phases and ownership
- node-and-edge flow for worker fan-out and merge-back points
- explicit red, amber, and green conflict markers with a separate unresolved box
- layered drill-down from summary to evidence to raw files
- compact matrix mapping dimension, owner, verdict, confidence, and rerun need

## What To Avoid

- burying the human view inside raw research notes
- a generic dashboard that shows activity but not decision state
- confusing heartbeats or automation ticks with orchestration progress
- mixing final conclusions with unresolved disagreement
- showing every worker equally without highlighting gates and rerun points
- using a text dump where a diagram or structured status surface would reduce ambiguity
