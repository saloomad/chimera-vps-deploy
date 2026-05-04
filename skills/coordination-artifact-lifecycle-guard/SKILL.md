---
name: coordination-artifact-lifecycle-guard
description: Use when creating or changing durable coordination files, guides, registries, workflows, handoff surfaces, or verification surfaces so they do not become dead ends. It forces every coordination artifact to have a purpose, reader, trigger, and proof surface.
---

# Coordination Artifact Lifecycle Guard

Use this skill when the work creates or changes durable coordination artifacts such as:

- guides
- workflows
- registries
- state files
- handoff surfaces
- verification scripts
- platform instructions

## Core Rule

Do not create a durable coordination file unless you can answer all four:

1. What is this file for?
2. Who reads or owns it automatically?
3. When is it supposed to be used?
4. How do we prove it is wired?

## Required Follow-Through

If you create or materially change a durable coordination artifact, do all of these in the same pass:

1. update the human-facing guide if the operator needs to understand it
2. update the workflow if the task order changed
3. update the file usage registry
4. update verification so dead-end files fail review
5. update platform instructions or runtime hooks if the artifact should be consumed automatically

## File Usage Registry

Register durable coordination artifacts in:

- `docs/GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md`

That registry must say:

- purpose
- automatic reader or owner
- trigger
- proof surface

## Review Test

Before calling the coordination change complete, ask:

- If this file disappeared tomorrow, who would notice?
- If the answer is "nobody," this is probably a dead-end artifact.

## Proof Surfaces

Use:

- `scripts/github_coordination_guard.py`
- `scripts/verify_github_coordination_system.py`

The change is not done when the file merely exists.
It is done when the file has a reader, a trigger, and a passing proof path.
