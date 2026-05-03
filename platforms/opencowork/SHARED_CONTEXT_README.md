# OpenCowork Shared Context Mirror

This platform folder is the durable mirror for the local OpenCowork enforcement bundle.

## What It Mirrors

- the local Chimera OpenCowork plugin bundle
- prompt-start enforcement
- risky-tool guardrails
- control-layer change guardrails
- compaction continuity guardrails
- stop gating
- local enforcement commands

## Local Source Of Truth

Live local plugin source on this Windows machine:

- `C:\Users\becke\AppData\Roaming\open-cowork\claude\plugins\source\chimera-enforcement-bundle`

Live local plugin runtime on this Windows machine:

- `C:\Users\becke\AppData\Roaming\open-cowork\claude\plugins\runtime\chimera-enforcement-bundle`

## Durable Repo Mirror

The shared mirror lives here:

- `platforms/opencowork/local-bundle/chimera-enforcement-bundle`

Use this when:

- rebuilding the local OpenCowork plugin bundle
- reviewing the hook set without reading AppData directly
- syncing the OpenCowork enforcement logic to another machine

## Current Hook Events

- `UserPromptSubmit`
- `InstructionsLoaded`
- `ConfigChange`
- `FileChanged`
- `PreToolUse`
- `PostToolUse`
- `Stop`
- `PreCompact`
- `PostCompact`

## Current Limitation

This repo mirror proves the bundle contents, but a real app reload is still the stronger proof that OpenCowork picked the bundle up in a live session.
