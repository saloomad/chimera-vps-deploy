---
name: codex-workflow-detector
description: Detect when a process should become a named workflow, create the workflow artifact, and link the workflow back into skills or docs so it is reused.
triggers:
  - create a workflow
  - this needs a workflow
  - repeated process
  - standard procedure
  - checklist
---

# Codex Workflow Detector

Use this skill when a repeatable step sequence should become an explicit workflow.

## Auto Trigger Rules

Create or update a workflow when:

1. a process has multiple steps and order matters
2. a task crosses build, test, review, and documentation boundaries
3. a procedure should be repeatable by future sessions
4. a risky fix needs the same checklist every time
5. a skill needs a step-by-step companion
6. the same conversation pattern keeps producing the same friction
7. a workflow now matters enough to be promoted across platforms

## Read First

- `docs/WORKFLOW_AND_SKILL_CAPTURE_POLICY.md`
- `workflows/codex/`
- `workflows/openclaw/`
- `C:\Users\becke\.codex\skills\workflow-skill-capture\SKILL.md`
- `C:\Users\becke\claudecowork\workflows\codex\WORKFLOW_CATALOG.md`

## Write Targets

- `workflows/codex/`
- `workflows/openclaw/`
- `.claude/skills/<related-skill>/SKILL.md` when the workflow should be referenced by a skill
- `docs/` when the workflow needs a broader explanation
- `chimera-vps-deploy/skills/` when the resulting skill or workflow should be shared across platforms

## Minimum Workflow Standard

Each workflow should define:

1. trigger
2. required inputs
3. ordered steps
4. expected outputs
5. when to stop or escalate
6. whether it is one-pass or loop-until-done
7. which existing skill or workflow should call it

## Promotion Rule

Score each candidate on:

- importance
- recurrence
- dependency complexity
- cross-platform use

Promote:

- to `workflow` when order matters
- to `skill` when behavior should be automatically reused
- to shared mirrors and AGENTS references when the pattern is important on more than one platform
