# Current Chimera Implementation Map

Updated: 2026-04-30

## Important Path Truth

- local workspace orchestration examples:
  - `C:\Users\becke\claudecowork\orchestration\`
- live OpenClaw orchestration home on the VPS:
  - `/root/.openclaw/workspace/orchestration/`
- live OpenClaw hooks home on the VPS:
  - `/root/.openclaw/workspace/hooks/`

Do not assume the live VPS orchestration files live under `/root/openclawtrading/orchestration/`.

## What Is Implemented In Chimera

### Lobster

- local files:
  - `orchestration/lobster/trading-pipeline.lobster`
  - `orchestration/lobster/trade-investigation.lobster`
  - `orchestration/lobster/trade-review.lobster`
  - `orchestration/lobster/council-review.lobster`
  - `orchestration/lobster/project-creation.lobster`
- live VPS path:
  - `/root/.openclaw/workspace/orchestration/lobster/`
- current role:
  - deterministic bounded pipelines
- current status:
  - implemented
  - partially wired
  - verify live runtime execution separately when the exact workflow matters
  - verify allowlist or tool exposure separately from file existence

### Task Flow

- local file:
  - `orchestration/taskflow.json`
- live VPS path:
  - `/root/.openclaw/workspace/orchestration/taskflow.json`
- current role:
  - durable flow cadence and restart-safe state
- current status:
  - implemented
  - verified live
  - should own the routine market-cycle state more clearly than it did before

### Hooks

- local paths:
  - `hooks/on_session_start/HOOK.md`
  - `hooks/on_agent_spawn/HOOK.md`
  - `hooks/on_compact_before/HOOK.md`
  - `hooks/on_compact_after/HOOK.md`
  - `hooks/on_gateway_restart/HOOK.md`
  - `hooks/mandatory-bootstrap/HOOK.md`
  - `hooks/message-router/HOOK.md`
  - `hooks/auto-memory-save/HOOK.md`
  - `hooks/extended-session-memory/HOOK.md`
- live VPS path:
  - `/root/.openclaw/workspace/hooks/`
- current role:
  - startup, lifecycle, memory, and message routing
- current status:
  - implemented
  - partially wired
  - event-driven layer is real, but workspace hooks still need explicit enablement to be live

### Cron

- live registry path:
  - `/root/.openclaw/cron/jobs.json`
- current role:
  - exact-time isolated wake-up
- current status:
  - implemented
  - opportunity only until real jobs are active

### Heartbeat

- current role:
  - continuation or stall detection
- current status:
  - documented only or route-specific
  - should not be confused with the whole orchestration design

### Standing Orders

- current role:
  - durable authority and recurring operating boundaries
- current status:
  - implemented in instructions
  - partially wired live because some OpenClaw instruction surfaces still need freshness cleanup

## Underused Or Worth Promoting

- stronger Task Flow ownership for durable trading-cycle state
- more intentional Lobster use for deterministic bounded subflows
- hooks for more specific post-phase or completion reactions where an event is known
- background task and flow inspection during audits instead of only file existence checks
