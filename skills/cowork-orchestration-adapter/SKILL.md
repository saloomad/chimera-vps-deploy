---
name: cowork-orchestration-adapter
description: Small Windows Claude/Cowork adapter for the shared orchestration rules. Use when Claude/Cowork should plan, shape, or synthesize a swarm-backed objective without duplicating the core deep-swarm skill.
triggers:
  - cowork orchestration
  - claude cowork
  - claude planning
  - orchestration adapter
---

# Cowork Orchestration Adapter

Use this as a small platform adapter for the Windows Claude/Cowork environment.

Do not duplicate the whole deep swarm here.
Use the shared core and adapt only the platform behavior.

## Primary Role

Claude/Cowork should usually own:

- planning
- architecture tradeoffs
- prompt shaping
- human-facing synthesis
- cross-platform coordination

## Default Pairing

Before using this adapter, also read:

- `deep-research-swarm`
- `objective-orchestration-loop`
- `codex-runtime-router`

## Cowork-Specific Rules

- run the orchestration precheck on every meaningful request, even when the final route stays light
- start by deciding whether the task is really a deep swarm or should stay a lighter loop
- if the task is a deep swarm, write or review the `plan.md` first
- use the verdict schema for cheap worker decisions
- let Codex own durable local file implementation when real repo edits are needed
- let OpenClaw/Kimi own live runtime truth when operational claims matter
- prefer Claude Code hooks and slash commands for enforcement when the local Cowork surface supports them

## Output Contract

A good Cowork orchestration handoff should say:

- objective
- orchestration class
- why the class fits
- required artifacts
- required gates
- who should own planning, execution, review, and live validation
- whether a heartbeat is actually needed

## Heartbeat Rule

Cowork should recommend a heartbeat only when the objective truly needs continuation across wakes.

Do not recommend a heartbeat just because the work is large.

## Final Rule

Cowork is the planning and synthesis adapter around the shared orchestration core.
It should shape the work clearly, not fork the logic into a separate operating model.
