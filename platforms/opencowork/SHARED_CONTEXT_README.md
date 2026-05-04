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

## Stronger Proof We Have Now

- the local OpenCowork plugin registry contains `chimera-enforcement-bundle`
- `enabled = true`
- `componentsEnabled.commands = true`
- `componentsEnabled.hooks = true`
- runtime path points at:
  - `C:\Users\becke\AppData\Roaming\open-cowork\claude\plugins\runtime\chimera-enforcement-bundle`
- direct local smoke proved these scripts can run and write receipts:
  - `InstructionsLoaded`
  - `FileChanged`
  - `PreCompact`
  - `PostCompact`

## Current Limitation

This repo mirror plus the registry check prove the bundle is installed and enabled, but a real app reload is still the stronger proof that OpenCowork picked the bundle up and fired the hooks through a live UI session.

Extra proof from the latest pass:

- restarting `CoworkVMService` did not create new OpenCowork receipts
- launching `claude.exe` created app processes but still did not create new OpenCowork receipts

That means the remaining proof gap is specifically a real in-app session or prompt trigger, not just app/service startup.
