---
name: opencowork-orchestration-adapter
description: Small OpenCowork adapter for the shared orchestration rules. Use when OpenCowork should plan, review, or synthesize a swarm-backed objective without forking the shared core.
triggers:
  - opencowork orchestration
  - opencowork
  - opencode orchestration
  - open cowork
---

# OpenCowork Orchestration Adapter

Use this as a small platform adapter for the local OpenCowork or OpenCode environment.

Do not clone the whole swarm here.
Use the shared orchestration core and adapt only the local platform behavior.

## Primary Role

OpenCowork should usually own:

- planning
- review
- prompt shaping
- cross-platform synthesis
- structured handoff writing

## Default Pairing

Before using this adapter, also read:

- `deep-research-swarm`
- `objective-orchestration-loop`
- `codex-runtime-router`

## OpenCowork-Specific Rules

- run the orchestration precheck on every meaningful request, even when the final route stays light
- start by deciding whether the task is really a `deep research swarm` or should stay a lighter loop
- if it is a deep swarm, write or review the `plan.md` first
- use the verdict schema for cheap worker decisions and rerun rules
- let Codex own durable repo edits unless OpenCowork is the confirmed editing owner
- let OpenClaw or Kimi own live runtime truth when operational claims matter
- be honest that the current OpenCowork or OpenCode setup has verified native rules, config, commands, agents, skills, and permission gating
- be honest that a native OpenCowork hook surface is still not separately verified in the current evidence set
- use native commands, native agents, startup docs, workflows, monitors, permission rules, and file-backed `plan.md` as the real enforcement surfaces here until a native hook model is proven

## Output Contract

A good OpenCowork orchestration handoff should say:

- objective
- orchestration class
- why the class fits
- required artifacts
- required gates
- who owns planning, execution, review, and live validation
- whether a heartbeat is actually needed

## Heartbeat Rule

OpenCowork should recommend a heartbeat only when the objective truly needs continuation across wakes.

Do not recommend a heartbeat just because the task is large.

## Final Rule

OpenCowork is a planning and review adapter around the shared orchestration core.
It should make the route clearer, not create a separate operating model.
