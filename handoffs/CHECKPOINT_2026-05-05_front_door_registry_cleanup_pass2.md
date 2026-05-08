# CHECKPOINT_2026-05-05_front_door_registry_cleanup_pass2

## What landed

- Replaced stale root front-door docs that still pointed agents at dead `/home/open-claw/...` paths:
  - `AGENT_REGISTRY.md`
  - `SKILL_INDEX.md`
  - `HEARTBEAT_REGISTRY.md`
  - `SYSTEM_INDEX.md`
- Kept those files concise and tied to the current live truth:
  - `root@100.67.172.114`
  - `/root/openclawtrading`
  - `/root/.openclaw/workspace`
  - `/root/.openclaw/kimi-skills`
- Rebuilt the local workspace registry after the cleanup.
- Mirrored the rewritten root docs to the live VPS repo.
- Rebuilt the live VPS registry and resynced the runtime tracking copies under `/root/.openclaw/workspace/tracking`.

## Proof

- Local registry rebuild:
  - `Registry updated: 14380 tracked files`
- VPS registry rebuild:
  - `Registry updated: 3667 tracked files`
- Targeted stale-reference scan on the rewritten front-door docs now only returns intentional warning lines telling agents not to use old paths.

## Remaining open work

- The registry still shows a broad `needs_review` backlog across older root and historical docs.
- Highest-value remaining active front doors to review next:
  - `ACTION_LOG.md`
  - `AGENT_OPTIMIZATION.md`
  - `AGENT_REASONING_KERNEL.md`
  - `AGENT_STANDARDS.md`
  - `AI_SYSTEMS_INVENTORY.md`
  - `ARCHITECTURE.md`
- That next pass should stay bounded to active front doors, not archive/historical sprawl.

## Why this matters

Agents now have a much cleaner top-level map:
- current agent ownership
- current skill-load truth
- current heartbeat ownership
- current system/front-door file locations

That reduces the chance that new work keeps reintroducing old path assumptions while the registry enforcement skill is live across platforms.
