# Insights

## Insight 1 - The Verdict Schema Made Cheap Workers Useful

Derived from:

- use-case routing
- platform routing
- heartbeat policy
- visual observability

Rationale:

The earlier proof only showed that cheap workers could classify work correctly.
This run showed that once the verdict schema was enforced, cheap workers could return the actual orchestration contract: freshness, artifacts, gates, stop condition, rerun policy, and escalation policy.

Implication:

Cheap workers can be used earlier and more safely because they now produce actionable routing artifacts, not just labels.

## Insight 2 - Heartbeats Belong To Continuation, Not To Identity

Derived from:

- heartbeat policy
- use-case routing
- visual observability

Rationale:

The real question is not "does this system have a heartbeat," but "does this objective need continuation across wakes."

Implication:

We should stop treating heartbeats as proof of sophistication.
A bounded objective should often finish without one.

## Insight 3 - The Swarm Is Best Thought Of As A Memo Engine, Not A Live Loop

Derived from:

- use-case routing
- platform routing

Rationale:

All dimensions agreed that the deep swarm is strongest when the outcome is a thesis, memo, postmortem, or large comparison.

Implication:

The live trading loop should stay lean and only escalate into the swarm when ambiguity or scope becomes materially larger than a normal cycle.

## Insight 4 - Platform Equality Is The Wrong Goal; Platform Logic Parity Is The Right Goal

Derived from:

- platform routing
- visual observability

Rationale:

The same orchestration logic should exist everywhere, but the actual work surface should differ by platform.

Implication:

We should use small platform adapters and templates, not giant cloned skills.

## Insight 5 - Visual Proof Should Center Phase And Gate State

Derived from:

- visual observability
- heartbeat policy

Rationale:

A human needs to see:

- objective
- class
- phase
- gate
- conflict
- rerun status

not just "agents are active."

Implication:

Any future dashboard or workflow view should make phase and gate state first-class.
