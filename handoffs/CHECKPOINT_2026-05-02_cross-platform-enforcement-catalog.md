# Checkpoint: Cross-Platform Enforcement Catalog And OpenCowork Bundle

Date: 2026-05-02

## What Finished

- Added shared detector skills:
  - `hook-opportunity-detector`
  - `pipeline-enforcement-detector`
- Added workflow:
  - `platform-enforcement-selection-and-receipt-loop.md`
- Added shared catalog:
  - `docs/PLATFORM_WORKFLOW_AND_SKILL_ENFORCEMENT_CATALOG_2026-05-02.md`
- Added shared receipt helper:
  - `scripts/log_activation_receipt.py`
- Added receipt verifier:
  - `scripts/verify_platform_activation_receipts.ps1`

## Platform Work Completed

### Claude Code

- local hook scripts now write activation receipts into `trace/platform_activation_receipts.jsonl`
- shared mirror updated under:
  - `platforms/claude-code/project-bundle/.claude/hooks/`

### OpenCode

- native `.opencode/skills/` now includes:
  - `hook-opportunity-detector`
  - `pipeline-enforcement-detector`
- prompts and commands now mention receipt paths and enforcement review
- shared mirror updated under:
  - `platforms/opencode/project-bundle/.opencode/`

### OpenCowork

- local AppData skills added:
  - `%AppData%\open-cowork\claude\skills\hook-opportunity-detector`
  - `%AppData%\open-cowork\claude\skills\pipeline-enforcement-detector`
- local AppData plugin added and enabled:
  - `%AppData%\open-cowork\claude\plugins\source\chimera-enforcement-bundle`
  - `%AppData%\open-cowork\claude\plugins\runtime\chimera-enforcement-bundle`
- plugin-registry entry now has:
  - `enabled = true`
  - `componentsEnabled.commands = true`
  - `componentsEnabled.hooks = true`

### OpenClaw / Kimi VPS

- synced live hook receipt logger:
  - `/root/.openclaw/workspace/hooks/_shared/receipt_logger.js`
- synced live handlers:
  - `/root/.openclaw/workspace/hooks/message-router/handler.js`
  - `/root/.openclaw/workspace/hooks/mandatory-bootstrap/handler.js`
- live smoke proved:
  - `message-router` wrote a receipt
  - `mandatory-bootstrap` wrote a receipt
- missing bootstrap source docs were synced into `/root/openclawtrading`
- fresh bootstrap smoke now injects `13` files into a clean workspace

### Hermes

- synced live:
  - `/root/openclawtrading/scripts/hermes_runtime_bridge.py`
  - `/root/openclawtrading/agents/hermes-lead/AGENTS.md`
- Hermes runtime bridge now has receipt logging support
- smoke wrote a Hermes receipt line

## Proof Snapshot

- `scripts/verify_platform_enforcement_surfaces.ps1`
  - shows Claude hook events
  - shows OpenCode agents, commands, prompts, native skills
  - shows OpenCowork bundle enabled with hooks
  - shows live OpenClaw enabled hooks and no stale old-path hits in key Lobster files
- `scripts/verify_platform_activation_receipts.ps1`
  - summarizes current local receipt lines

## Local-Only Items

These are real on this Windows machine but are not stored in GitHub the same way as repo files:

- `%AppData%\open-cowork\claude\skills\...`
- `%AppData%\open-cowork\claude\plugins\...`
- `%AppData%\open-cowork\plugin-registry.json`
- local `.claude/settings.json`
- local `trace/platform_activation_receipts.jsonl`

## Remaining Next Pass

1. restart or refresh OpenCowork and verify the local plugin hooks fire during a real app session
2. run a real Claude Code session pass that hits `Stop` and `SubagentStop`
3. decide whether more OpenClaw hooks should move from on-disk to enabled
4. decide whether the receipt log should stay runtime-only or become a curated summarized artifact
