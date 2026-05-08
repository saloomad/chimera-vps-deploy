# CHECKPOINT_2026-05-05_workspace_registry_cleanup_loop_pass3

## What landed

- Added a new root front door:
  - `WORKSPACE_FILE_OPERATING_RULES.md`
- Replaced stale/stub root docs with current versions:
  - `FILE_ARCHITECTURE.md`
  - `ARCHITECTURE.md`
  - `AI_SYSTEMS_INVENTORY.md`
  - `CHIMERA_AGENT_ARCHITECTURE.md` is now only a historical redirect
- Updated shared standards so agents are routed to the new file-operating rules:
  - `AGENTS.md`
  - `INDEX.md`
  - `AGENT_STANDARDS.md`
  - `AGENT_REASONING_KERNEL.md`
  - `WORKSPACE_STANDARD.md`
- Improved the workspace registry builder:
  - excludes `_openclaw_live` export snapshots
  - excludes `_tmp_remote_*` export copies
  - stops treating append-only historical ledgers like `ACTION_LOG.md` as live-truth defects just because they mention old paths
  - now includes `WORKSPACE_FILE_OPERATING_RULES.md` as a front door
- Added the bounded review file:
  - `tracking/REDUNDANT_FILE_REVIEW.md`
- Removed obvious local junk/staging files:
  - `_openclaw_live/`
  - `_openclaw_artifacts.txt`
  - `_openclaw_index.txt`
  - `_openclaw_operator_brief.json`
  - `_openclaw_pending_questions.txt`
  - `_tmp_remote_ACTION_LOG.md`
  - `_tmp_remote_AGENT_STANDARDS.md`
  - `_tmp_remote_OPENCLAW_CODEX_AGENTS.md`
  - one garbage root filename that had polluted the registry
- Added the durable wiki source:
  - `research/chimera-knowledge-wiki/wiki/sources/workspace-file-registry-and-operating-rules-2026-05-05.md`
- Fixed the wiki front door so all current source pages are listed in `wiki/index.md`
- Refreshed `wiki/catalog.*`, `graph/graph.*`, and health

## Proof

- Local registry rebuild after cleanup:
  - `Registry updated: 14369 tracked files`
- Live VPS registry rebuild after mirror:
  - `Registry updated: 3675 tracked files`
- Local workspace-document-registry skill hash matches:
  - shared mirror
  - Codex local
  - Claude local
  - OpenClaw local
- Live VPS hashes match for:
  - `/root/openclawtrading/WORKSPACE_FILE_OPERATING_RULES.md`
  - `/root/openclawtrading/skills/workspace-document-registry/SKILL.md`
  - `/root/.openclaw/kimi-skills/workspace-document-registry/SKILL.md`
  - `/root/openclawtrading/tracking/REDUNDANT_FILE_REVIEW.md`
- Wiki health now shows:
  - `in_index_not_on_disk = []`
  - `on_disk_not_in_index = []`

## Remaining open work

- Still review the next active but likely stale large root docs:
  - `OPENCLAW_FILE_MAP.md`
  - `OPENCLAW_BIBLE.md`
  - `OPENCLAW_FEATURES.md`
  - `TASK_REGISTRY.md`
- Decide whether to keep `linuxopenclawtrading/`, `source-code/`, and similar large mirror/import roots in the main registry or demote them further for less noise.
- Consider a second registry script improvement pass that groups “expected duplicates” more explicitly so review queues focus even more on real conflicts.

## Why this matters

The system is now much easier for agents to navigate:
- one clearer file-placement rule set
- fewer junk export surfaces in the inventory
- better separation between active front doors, historical ledgers, and deletable staging files
- wiki memory now captures the file-organization rules so later agents can find them without rediscovering the cleanup
