---
name: model-registry
description: Central registry of the models currently used across Windows Codex, Windows Claude, Kimi VPS, OpenCowork, and related coding surfaces. Read this BEFORE answering model questions, pricing questions, endpoint questions, or routing questions. Prevents guessed model specs and gives one routing baseline.
---

# Model Registry - Chimera Ecosystem

Read this before answering questions about:

- model names
- endpoints
- fallback order
- context windows
- approximate cost
- benchmark signals
- which model should handle planning, execution, or review

If a fact is not in this registry or in the cited official source, say that plainly instead of guessing.

## Current Routing Summary

### Windows Codex

- Current verified default: `gpt-5.4`
- Current verified reasoning default: `medium`
- New-session default: start there unless Sal explicitly wants a stronger lane
- Best use: implementation, patching, bounded testing
- Stronger planning or review override when available: `gpt-5.5` with `high` or `xhigh`
- Fast cheap lane when available: `gpt-5.4-mini` with `low`

### Windows Claude

- Use as the planning and synthesis surface when the work is high-ambiguity or cross-platform
- Strong preferred lane: strongest available planning model with high reasoning

### Kimi VPS / OpenClaw

- Primary live model: `k2.6`
- Fallback #1: `k2.5`
- Fallback #2: `MiniMax-M2.7-highspeed`
- Fallback #3: `MiniMax-M2.5`

### OpenCowork On Windows

- Verified working provider mode: `custom`
- Verified working protocol: `anthropic`
- Verified working base URL: `https://api.kimi.com/coding/`
- Verified working model: `kimi-for-coding`

## Windows Codex Runtime Models

These are the model lanes we currently route against in this Codex environment.

| Model | Best use | Reasoning support | Context | Approx input / 1M | Approx output / 1M | Benchmark signals |
|---|---|---|---|---|---|---|
| `gpt-5.5` | planning, architecture, review, failure analysis | `none`, `low`, `medium`, `high`, `xhigh` | 1M | $5.00 | $30.00 | Terminal-Bench 2.0 `82.7`, SWE-Bench Pro `58.6`, GPQA Diamond `93.6`, HLE w/ tools `52.2` |
| `gpt-5.4` | default execution and coding | `none`, `low`, `medium`, `high`, `xhigh` | 1.05M | $2.50 | $15.00 | Terminal-Bench 2.0 `65.4`, SWE-Bench Pro `57.7`, GPQA Diamond `92.8`, HLE w/ tools `52.1` |
| `gpt-5.4-mini` | formatting, mechanical transforms, low-risk helper work | `none`, `low`, `medium`, `high`, `xhigh` | 400K | $0.75 | $4.50 | use when cost and speed matter more than top-end judgment |
| `gpt-5.3-codex` | coding-specific fallback | runtime-supported | 400K | $1.75 | $14.00 | use when coding focus matters and explicit override is justified |

Important:

- spawned agents inherit the parent model by default
- only override a spawned agent model when the subtask clearly benefits from it
- this runtime does not yet expose a verified hidden per-request auto-switch inside one session, so routing is a visible policy, not a fake auto-switch claim

## VPS-Configured Models

Source of truth for the live VPS wiring is `/root/.openclaw/openclaw.json`.

### Provider: `minimax`

| Model ID | Endpoint | Role | Notes |
|---|---|---|---|
| `MiniMax-M2.7-highspeed` | `https://api.minimaxi.com/anthropic` or `https://api.minimaxi.com/anthropic/v1` | Fallback #2 | cheap fast fallback, not main OpenClaw default |
| `MiniMax-M2.5` | `https://api.minimaxi.com/anthropic` or `https://api.minimaxi.com/anthropic/v1` | Fallback #3 | cheaper fallback |

Known official signals:

- M2 series context: around `200K`
- MiniMax coding-plan docs show Anthropic-compatible setup

### Provider: `kimi-coding`

| Model ID | Endpoint | Role | Notes |
|---|---|---|---|
| `k2.6` | `https://api.kimi.com/coding` | Primary | current live OpenClaw default |
| `k2.5` | `https://api.kimi.com/coding` | Fallback #1 | older but still strong fallback |

Known official signals:

- `kimi-k2.6` and `kimi-k2.5` have 256K context in Kimi docs
- K2.6 supports strong coding and agent tasks
- Kimi API also supports an official OpenAI-compatible path at `https://api.moonshot.ai/v1`

## Default Agent Routing

```text
Primary:   kimi-coding/k2.6
Fallbacks:
  1. kimi-coding/k2.5
  2. minimax/MiniMax-M2.7-highspeed
  3. minimax/MiniMax-M2.5
```

## Planning / Execution / Review Routing

| Work type | Preferred platform | Preferred model | Preferred reasoning |
|---|---|---|---|
| planning | Windows Claude or strong Codex override | `gpt-5.5` | `high` or `xhigh` |
| execution | Windows Codex for local, Kimi VPS for live | `gpt-5.4` locally, `k2.6` on VPS | `medium` locally |
| review | Windows Codex or Windows Claude | `gpt-5.5` for judgment-heavy review, `gpt-5.4` for bounded code review | `high` or `medium` |
| fast mechanical | Windows Codex | `gpt-5.4-mini` | `low` |

## Connection Methods Summary

### MiniMax on VPS

```bash
base_url: https://api.minimaxi.com/anthropic
model: MiniMax-M2.7-highspeed
protocol: Anthropic Messages API
```

### Kimi on VPS

```bash
base_url: https://api.kimi.com/coding
model: kimi-for-coding or kimi-k2.6
protocol: Anthropic Messages API
```

### Kimi Official OpenAI-Compatible API

```bash
base_url: https://api.moonshot.ai/v1
model: kimi-k2.6
protocol: OpenAI Chat Completions API
```

### OpenCowork On Windows

```bash
provider: custom
protocol: anthropic
base_url: https://api.kimi.com/coding/
model: kimi-for-coding
verified: 2026-04-29
```

Important:

- this was read back from the encrypted OpenCowork config store after repair
- the Kimi coding endpoint returned HTTP `200` in a live test
- the returned server model name was `kimi-for-coding`

### OpenAI models in Codex

The local runtime is not configured through this file with raw API credentials.
Instead, use the Codex runtime's selected model and the routing policy in `codex-runtime-router`.

## Routing Notes That Matter In Practice

- Use `gpt-5.5` when the cost of a weak plan is higher than the extra tokens
- Use `gpt-5.4` for most implementation work
- Use `gpt-5.4-mini` only when the task is clearly mechanical
- Keep `k2.6` as the main live OpenClaw default unless the user explicitly asks for a cheaper MiniMax-first lane
- Use `MiniMax-M2.7-highspeed` as the cheap fallback lane, not the default OpenClaw route

## Sources

- OpenCowork README: https://github.com/OpenCoworkAI/open-cowork
- OpenAI GPT-5.5: https://openai.com/index/introducing-gpt-5-5/
- OpenAI GPT-5.4 docs: https://developers.openai.com/api/docs/models/gpt-5.4/
- OpenAI pricing: https://platform.openai.com/docs/pricing/
- Kimi API overview: https://platform.kimi.ai/docs/api/overview
- Kimi model list: https://platform.kimi.ai/docs/models
- Kimi K2.6 quickstart: https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart
- Kimi Claude Code support: https://platform.kimi.ai/docs/guide/agent-support
- MiniMax coding quickstart: https://platform.minimaxi.com/docs/coding-plan/quickstart
- MiniMax OpenCode setup: https://platform.minimaxi.com/docs/coding-plan/opencode

## Update Rule

When models, prices, or routes change:

1. verify with official docs first
2. update this registry
3. update `codex-runtime-router` if routing behavior changes
4. mirror shared skill changes into `chimera-vps-deploy`
5. mention the sync state in the current handoff

*model-registry skill v2.2 | Last updated: 2026-04-29 | Sources: official OpenAI, OpenCowork, MiniMax, and Kimi docs linked above*
