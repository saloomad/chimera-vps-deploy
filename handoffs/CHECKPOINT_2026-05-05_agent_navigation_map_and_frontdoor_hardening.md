# CHECKPOINT_2026-05-05_agent_navigation_map_and_frontdoor_hardening

## What landed

- Added `AGENT_NAVIGATION_MAP.md` as the fast front door for:
  - what to read first
  - which registry owns what
  - where to find workflows, skills, architecture, and file rules
  - how to route different situations without guessing
- Updated:
  - `AGENTS.md`
  - `INDEX.md`
  - `scripts/build_workspace_document_registry.py`
  - wiki `index.md`
- Added wiki source:
  - `agent-navigation-map-and-file-discovery-2026-05-05.md`
- Rebuilt local registry and wiki catalog/health
- Mirrored the new navigation layer and refreshed registry outputs on the live VPS

## Proof

- Local registry:
  - `Registry updated: 14393 tracked files`
- Live VPS registry:
  - `Registry updated: 3681 tracked files`
- Wiki health:
  - `in_index_not_on_disk = []`
  - `on_disk_not_in_index = []`
- Live VPS grep shows:
  - `AGENT_NAVIGATION_MAP.md` and `WORKSPACE_FILE_OPERATING_RULES.md` now appear in the active front-door outputs

## Current best front-door stack

- `AGENTS.md`
- `AGENT_NAVIGATION_MAP.md`
- `DOCUMENT_REGISTRY.md`
- `WORKSPACE_FILE_OPERATING_RULES.md`
- `AGENT_REGISTRY.md`
- `SKILL_INDEX.md`
- `FEATURE_USAGE_REGISTRY.md`
- `ARCHITECTURE.md`
- `AI_SYSTEMS_INVENTORY.md`
- `tracking/WORKSPACE_FILE_REGISTRY.md`
- `tracking/REDUNDANT_FILE_REVIEW.md`

## Remaining open work

- Review and modernize the remaining older big root guidance docs:
  - `OPENCLAW_FILE_MAP.md`
  - `OPENCLAW_BIBLE.md`
  - `OPENCLAW_FEATURES.md`
  - `TASK_REGISTRY.md`
- Consider another registry-noise pass for large mirror/import roots like:
  - `linuxopenclawtrading/`
  - `source-code/`
- If desired, add one more front door later:
  - a dedicated situation-router / decision-router with even shorter “if X then read Y” flows

## Why this matters

Agents now have a clearer way to:
- know their rules
- know their abilities
- know where architecture and workflows live
- know when to create vs update vs delete files
- know which registries to consult first
