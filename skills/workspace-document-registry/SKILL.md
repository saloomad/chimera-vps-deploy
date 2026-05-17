---
name: workspace-document-registry
description: Keep the Chimera workspace document registry and full file inventory accurate across platforms whenever durable files are created, deleted, moved, renamed, or newly relied on.
---

# Workspace Document Registry

Use this skill whenever work touches durable files, especially:

- creating a new document
- deleting or archiving an old document
- moving or renaming a file
- adding a new skill
- adding a new workflow
- discovering a file that agents should depend on
- replacing an old script with a new canonical path

## Canonical Surfaces

Human front doors:

- `DOCUMENT_REGISTRY.md`
- `INDEX.md`
- `WORKSPACE_FILE_OPERATING_RULES.md`
- `tracking/WORKSPACE_FILE_REGISTRY.md`

Machine-readable full inventory:

- `tracking/WORKSPACE_FILE_REGISTRY.json`

Updater:

- `scripts/build_workspace_document_registry.py`

## Core Rule

After creating, deleting, moving, renaming, or reclassifying a durable file, rerun:

```powershell
python scripts/build_workspace_document_registry.py
```

If the work is on Linux:

```bash
python3 /root/openclawtrading/scripts/build_workspace_document_registry.py
```

## Durable File Definition

Durable files include:

- root operating docs
- agent instructions
- skills
- workflows
- handoffs
- research notes
- data-source guides
- trading document templates
- scripts that the live bundle or agent flow depends on

Do not treat one-off temp probes, cache files, worktrees, archives, or generated junk as front-door files.

## Category Intent

The registry should make it easy to find files under labels like:

- organization
- guides
- data-sources
- pipeline
- agents
- skills
- research
- tracking
- trading-bundle

## Cleanup Rule

When two files conflict:

1. pick the canonical live path
2. remove dead wrappers or temp indexes if they are clearly obsolete
3. if removal is risky, keep the file but let the registry mark it `needs_review` or historical

Before making a new durable file, also read:

- `WORKSPACE_FILE_OPERATING_RULES.md`

That file explains where new files should go and when to update an existing front door instead of creating a duplicate.

## Platform Mirroring Rule

This skill should exist in:

- `C:\Users\becke\.codex\skills`
- `C:\Users\becke\.claude\skills`
- `C:\Users\becke\.openclaw\skills`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
- `/root/openclawtrading/skills`
- `/root/.openclaw/kimi-skills`

If you update this skill, mirror the tested copy to those real load paths.
