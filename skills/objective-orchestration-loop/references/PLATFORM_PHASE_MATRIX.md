# Platform Phase Matrix

Updated: 2026-04-28

## Core Rule

Every non-trivial objective uses:

`plan -> execute -> review -> repeat`

Before the first `plan`, classify the task as:

- `direct task`
- `bounded build`
- `deep research swarm`
- `always-on pipeline`

## Windows Codex

| Phase | Preferred model | Preferred reasoning | Notes |
|---|---|---|---|
| plan | `gpt-5.5` | `high` or `xhigh` | escalation lane, not the default new-session start |
| execute | `gpt-5.4` | `medium` | current verified default |
| review | `gpt-5.5` or `gpt-5.4` | `high` or `medium` | stronger review when ambiguous |

Worker defaults:

- default new session start: `gpt-5.4 medium`
- orchestrator escalation: `gpt-5.5 high` only when the task truly needs the stronger lane
- cheap workers: `gpt-5.3-codex-spark low` or `gpt-5.4-mini low`
- reviewer or verifier: `gpt-5.5 high`

Quota path:

- try `scripts/check_codex_runtime_status.ps1`
- if no verified quota command exists, use `quota=not exposed`

## Claude Code

| Phase | Preferred model | Preferred reasoning | Notes |
|---|---|---|---|
| plan | `gpt-5.5` or strongest available planning model | high | if configured |
| execute | `kimi-for-coding` or `claude-sonnet` | medium | use the currently configured provider |
| review | `gpt-5.5` or `claude-sonnet` | high | use stronger review when needed |

Platform limits:

- no durable native heartbeat after close
- session continuity depends on files

## OpenCode

| Phase | Preferred model | Preferred reasoning | Notes |
|---|---|---|---|
| plan | `kimi-for-coding` | higher reasoning if supported | current verified provider in config |
| execute | `MiniMax-M2.7-highspeed` | provider default | cheaper coding lane |
| review | `kimi-for-coding` | higher reasoning if supported | stronger review lane |

Current verified providers in local config:

- `kimi-for-coding`
- `minimax-coding-plan/MiniMax-M2.7-highspeed`

## Kimi VPS / OpenClaw

| Phase | Preferred model | Preferred reasoning | Notes |
|---|---|---|---|
| plan | `k2.6` | thinking on | strongest VPS reasoning lane |
| execute | `MiniMax-M2.7-highspeed` | provider default | primary live implementation lane |
| review | `k2.6` | thinking on | use when the first result is weak |

Live pipeline guidance:

- routine trading cycle: lean pipeline, not deep swarm
- swarm only for thesis, major event review, or post-trade analysis
- rerun weak slices on `k2.6`, not the whole loop by default

Fallbacks:

- `k2.5`
- `MiniMax-M2.5`

## Hermes VPS

| Phase | Preferred model | Preferred reasoning | Notes |
|---|---|---|---|
| plan | current Hermes configured model | provider-specific | current config is MiniMax-based |
| execute | current Hermes configured model | provider-specific | keep changes conservative |
| review | escalate outside Hermes if needed | provider-specific | Hermes may need external review if multi-model routing is not wired |

Current verified local Hermes config:

- provider: `minimax`
- model: `MiniMax-M2.5-HighSpeed`

## Review Outcomes

- `complete`: stop and close out
- `iterate`: loop again with a better route
- `blocked`: capture blocker, do not fake completion
