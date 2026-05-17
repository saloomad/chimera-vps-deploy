---
name: platform-learning-enforcer
description: Audit and enforce the hook-backed learning mechanism across Codex, OpenClaw, and related platform surfaces using receipts instead of assumptions.
---

# Platform Learning Enforcer

Use this when the question is not only "did we build a learning loop" but also "is it actually wired, enabled, and producing proof on this platform?"

## Purpose

This skill gives one shared pattern for platform learning enforcement:

- choose the right enforcement surface per platform
- verify the learning loop is present
- verify it is enabled where config applies
- verify it left receipts
- fail closed when only docs exist but runtime proof does not

## Core Rule

Do not call a learning system "working" from file existence alone.

Check these separately:

1. `exists`
2. `wired`
3. `enabled`
4. `receipt exists`
5. `smoke or runtime proof`

## Platform Mapping

### Codex / local workspace

- primary enforcement: wrapper scripts, local hooks, typed reports
- proof:
  - `scripts/tests/learning_hook_enforcement_smoke.js`
  - `scripts/tests/learning_platform_enforcement_audit_smoke.py`

### OpenClaw / VPS

- primary enforcement: workspace hooks plus runtime reports
- required hooks:
  - `extended-session-memory`
  - `auto-memory-save`
  - `on_session_start`
- proof:
  - `scripts/learning_platform_enforcement_audit.py`
  - bounded hook simulations
  - runtime receipts in `reports/auto/LEARNING_LOOP/` and `memory/`

### Claude-style platforms

- primary enforcement: native hooks
- required equivalent events:
  - session start
  - pre-compact
  - post-failure or repeated-friction capture
- proof:
  - hook receipts
  - durable candidate/review artifacts

## Audit Command

```bash
python scripts/learning_platform_enforcement_audit.py \
  --workspace <workspace> \
  --config <config-if-any> \
  --platform <name> \
  --strict
```

## Output Contract

The audit must say plainly:

- which hooks were checked
- whether they exist
- whether they are enabled
- whether recall exists
- whether hot memory exists
- whether continuity receipts exist

## Guardrails

- if hooks exist but config is disabled, say disabled
- if config is enabled but receipts are missing, say proof incomplete
- if a platform lacks hooks, route to the lightest honest equivalent instead of pretending parity
- do not promote learning-policy changes from raw friction alone
