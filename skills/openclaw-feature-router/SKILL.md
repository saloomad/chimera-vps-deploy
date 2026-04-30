---
name: openclaw-feature-router
description: Choose the right OpenClaw feature for a Chimera problem, explain what it does in plain English, check what is already implemented locally and live, and point to the official docs when a newer built-in feature may solve the problem better.
triggers:
  - openclaw features
  - lobster
  - task flow
  - hooks
  - cron
  - background tasks
  - standing orders
  - which openclaw feature
---

# OpenClaw Feature Router

Use this skill when the question is:

- which OpenClaw feature should solve this problem
- what Lobster, Task Flow, hooks, cron, heartbeat, or tasks actually are
- what Chimera already implements today
- what is underused and should be promoted
- whether OpenClaw docs or recent features may solve a current Chimera pain point

## Read First

- `references/FEATURE_DECISION_MATRIX.md`
- `references/CURRENT_CHIMERA_IMPLEMENTATION_MAP.md`
- `references/PROBLEM_TO_FEATURE_MAP.md`
- `references/OFFICIAL_OPENCLAW_DOCS.md`
- `openclaw-orchestration-proof-router`

## Core Rule

Do not answer with feature theory alone.

Always separate:

1. what the feature is in OpenClaw
2. when to use it
3. what Chimera already has on disk or live
4. what is still only an opportunity

## Plain-English Feature Roles

- `Skill`
  - reusable instructions and local process knowledge
- `Hook`
  - event-driven automation inside Gateway lifecycle or message events
- `Cron`
  - exact-time isolated wake-up
- `Heartbeat`
  - continuation or periodic check contract, not the main orchestration design
- `Background task`
  - detached work ledger for spawned or scheduled runs
- `Task Flow`
  - durable multi-step state above individual tasks
- `Lobster`
  - deterministic bounded pipeline with explicit structure and approval-friendly checkpoints
- `Standing orders`
  - always-on behavior rules in bootstrap or `AGENTS.md`
- `ACP`
  - external coding harness session

## Mandatory Answer Shape

For any serious feature-routing answer, include:

- problem
- chosen feature
- why it fits
- why the main alternatives do not fit
- local implementation path
- live implementation path when verified
- what is already active
- what is missing or underused
- next safe change

## Chimera-Specific Rule

For the routine trading cycle:

- Task Flow should own durable cadence and restart-safe state
- Lobster should own bounded deterministic subflows
- hooks should own bootstrap, lifecycle, and event reactions
- cron should only wake or schedule isolated jobs
- heartbeat should only continue approved work or detect stalls
- deep swarm should stay outside the routine loop unless ambiguity is unusually deep

## Docs And Updates Rule

When OpenClaw built-ins may have changed:

- check official docs first
- prefer current official docs and official GitHub surfaces
- then compare against Chimera's current implementation map
- if a built-in feature would solve a current Chimera pain point better than the custom path, say that plainly

## Write Targets

If this skill drives a real system change, update:

- `FEATURE_USAGE_REGISTRY.md`
- `HOOK_REGISTRY.md` when hooks changed
- `orchestration/taskflow.json` when Task Flow behavior changed
- `orchestration/lobster/*.lobster` when a Lobster pipeline changed
- shared skill docs under `chimera-vps-deploy/skills/`

## Final Rule

Do not say a feature is "in use" just because a file exists.

Use these labels instead:

- `implemented`
- `verified live`
- `partially wired`
- `documented only`
- `opportunity only`
