# Dimension 03 - Heartbeat And Automation Policy

## Orchestration Class

- `deep research swarm`

## Why Not Other Classes

- not `direct task` because this needs cross-checks and policy boundaries
- not `bounded build` because this is policy analysis, not implementation
- not `always-on pipeline` because this slice is governing the live loop rather than being the live loop

## Freshness Requirement

- current proof-run context
- current shared skill files
- no stale memory-only assumptions about heartbeat behavior

## Required Artifacts

- `plan.md`
- `research/landscape_brief.md`
- `research/dim03_heartbeat_and_automation_policy.md`
- `research/cross_verification.md`
- `research/insights.md`
- `final/chimera_deep_swarm_deployment_memo.md`

## Required Gates

- time horizon is explicit
- heartbeat is separated from orchestration design
- timers are treated only as wake-up triggers
- hooks are treated as event-driven enforcement points
- no recurring automation is chosen for bounded or routine work
- required outputs exist before synthesis

## Stop Condition

- stop when the policy clearly distinguishes heartbeat, timers, hooks, and no-recurring-automation cases
- stop on blocked if the recommendation would collapse into a generic always-on answer

## Rerun Policy

- rerun only unclear or conflicting slices
- do not restart the whole swarm by default

## Escalation Policy

- raise reasoning first for disputed policy boundaries
- rerun failed slices on a stronger lane only when needed
- preserve uncertainty honestly instead of forcing certainty

## Use Heartbeat When

- the objective needs continuation across wakes in the same thread
- approved work must resume after interruption
- periodic objective re-check or stall detection is needed
- the platform can continue safe approved work and stop cleanly

## Do Not Use Heartbeat When

- the work is a one-pass analysis or report
- the job is a routine trading cycle or normal monitor wake
- the task is bounded enough for normal `plan -> execute -> review`
- the heartbeat would only duplicate a timer, hook, or manual handoff

## Automation Vs Heartbeat Rules

- a heartbeat is a continuation contract, not the orchestration itself
- timers and cron are wake-up triggers only
- hooks are event-driven enforcement points after step or agent events
- use no recurring automation when the work is bounded, cheap, or should end after one review pass
- live trading or monitoring should stay lean and add recurrence only when continuation or stall detection is truly needed
- do not turn every cycle into a swarm or every swarm into an always-on loop

## Practical Stop Rules

- stop on `complete`
- stop on `blocked`
- stop after 3 consecutive wakes with no meaningful visible progress
- stop recurring automation when the objective no longer needs continuation
- require fresh human input after a no-progress stop
