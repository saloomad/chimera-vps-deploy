---
name: model-registry
description: Central registry of the models currently used across Windows Codex, Windows Claude, Kimi VPS, and related coding surfaces. Read this BEFORE answering model questions, pricing questions, endpoint questions, or routing questions. Prevents guessed model specs and gives one routing baseline.
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
- Best use: implementation, patching, bounded testing
- Stronger planning/review override when available: `gpt-5.5` with `high` or `xhigh`
- Fast cheap lane when available: `gpt-5.4-mini` with `low`

### Windows Claude

- Use as the planning and synthesis surface when the work is high-ambiguity or cross-platform
- Strong preferred lane: strongest available planning model with high reasoning

### Kimi VPS / OpenClaw

- Primary live model: `MiniMax-M2.7-highspeed`
- Fallback #1: `k2.6`
- Fallback #2: `k2.5`
- Fallback #3: `MiniMax-M2.5`

## Windows Codex Runtime Models

These are the model lanes we currently route against in this Codex environment.

| Model | Best use | Reasoning support | Context | Approx input / 1M | Approx output / 1M | Benchmark signals |
|---|---|---|---|---|---|---|
| `gpt-5.5` | planning, architecture, review, failure analysis | `none`, `low`, `medium`, `high`, `xhigh` | 1M | $5.00 | $30.00 | Terminal-Bench 2.0 `82.7`, SWE-Bench Pro `58.6`, GPQA Diamond `93.6`, HLE w/ tools `52.2` |
| `gpt-5.4` | default execution and coding | `none`, `low`, `medium`, `high`, `xhigh` | 1.05M | $2.50 | $15.00 | Terminal-Bench 2.0 `65.4`, SWE-Bench Pro `57.7`, GPQA Diamond `92.8`, HLE w/ tools `52.1` |
| `gpt-5.4-mini` | formatting, mechanical transforms, low-risk helper work | `none`, `low`, `medium`, `high`, `xhigh` | 400K | $0.75 | $4.50 | no main benchmark rule here; use when cost and speed matter more than top-end judgment |
| `gpt-5.3-codex` | coding-specific fallback | runtime-supported | 400K | $1.75 | $14.00 | use when coding focus matters and explicit override is justified |
| `gpt-5.3-codex-spark` | fastest coding fallback | runtime-supported | runtime-dependent | not verified here | not verified here | use only for speed-sensitive helper work |
| `gpt-5.2` | lower-cost strong fallback | `low`, `medium`, `high`, `xhigh` | runtime-dependent | $1.75 | $14.00 | use when cheaper strong reasoning is enough |

Important:

- spawned agents inherit the parent model by default
- only override a spawned agent model when the subtask clearly benefits from it
- this runtime does not yet expose a verified hidden per-request auto-switch inside one session, so routing is a visible policy, not a fake auto-switch claim

## VPS-Configured Models

Source of truth for the live VPS wiring is `/root/.openclaw/openclaw.json`.

### Provider: `minimax`

| Model ID | Endpoint | Role | Notes |
|---|---|---|---|
| `MiniMax-M2.7-highspeed` | `https://api.minimax.io/anthropic` | Primary | same performance as M2.7 with faster inference |
| `MiniMax-M2.5` | `https://api.minimax.io/anthropic` | Fallback #3 | cheaper fallback |

Known official signals:

- M2 series context: `200K`
- M2 series max output: up to `128K`
- M2.7-highspeed approximate price: `$0.60` input, `$2.40` output per 1M
- M2.5 approximate price: `$0.30` input, `$1.20` output per 1M

### Provider: `kimi-coding`

| Model ID | Endpoint | Role | Notes |
|---|---|---|---|
| `k2.6` | `https://api.kimi.com/coding` | Fallback #1 | strongest VPS reasoning and coding rerun lane |
| `k2.5` | `https://api.kimi.com/coding` | Fallback #2 | older but still strong fallback |

Known official signals:

- K2.6 and K2.5 context: `256K`
- K2.6 supports thinking mode
- K2.5 supports thinking mode
- K2.6 approximate API price: `$0.16` cached input, `$0.95` uncached input, `$4.00` output per 1M
- K2.5 approximate API price: use as cheaper fallback; exact USD sheet not fully standardized in this registry yet

K2.6 benchmark signals from Kimi's technical blog:

- HLE full with tools: `54.0`
- DeepSearchQA accuracy: `83.0`
- Terminal-Bench 2.0: `66.7`
- SWE-Bench Pro: `58.6`

## Default Agent Routing

```text
Primary:   minimax/MiniMax-M2.7-highspeed
Fallbacks:
  1. kimi-coding/k2.6
  2. kimi-coding/k2.5
  3. minimax/MiniMax-M2.5
```

## Planning / Execution / Review Routing

| Work type | Preferred platform | Preferred model | Preferred reasoning |
|---|---|---|---|
| planning | Windows Claude or strong Codex override | `gpt-5.5` | `high` or `xhigh` |
| execution | Windows Codex for local, Kimi VPS for live | `gpt-5.4` locally, `MiniMax-M2.7-highspeed` on VPS | `medium` locally |
| review | Windows Codex or Windows Claude | `gpt-5.5` for judgment-heavy review, `gpt-5.4` for bounded code review | `high` or `medium` |
| fast mechanical | Windows Codex | `gpt-5.4-mini` | `low` |

## Rerun And Escalation Rule

If the result quality is weak:

1. raise reasoning first
2. split planning from execution if the task was mixed
3. rerun review on a stronger model
4. record the better route for next time

Do not pretend a cheap or weak lane was sufficient if the output quality says otherwise.

## Quota And Usage Rule

Verified current truth on this Windows Codex machine:

- `codex login status` works
- a reliable quota or remaining-usage command has not been found yet
- header value should stay `quota=not exposed` until a real supported command exists

## Connection Methods Summary

### MiniMax on VPS

```bash
base_url: https://api.minimax.io/anthropic
model: MiniMax-M2.7-highspeed
protocol: Anthropic Messages API
```

### Kimi on VPS

```bash
base_url: https://api.kimi.com/coding
model: k2.6
protocol: Anthropic Messages API
```

### OpenAI models in Codex

The local runtime is not configured through this file with raw API credentials.
Instead, use the Codex runtime's selected model and the routing policy in `codex-runtime-router`.

### Space Agent (Visual Dashboard Layer)

```bash
url: http://100.67.172.114:3000
mode: single-user (no login)
customware: /srv/space/customware
purpose: browser-first AI dashboard for Chimera trading data
```

Space Agent can be configured with any OpenAI-compatible endpoint:

| Provider | API Endpoint | Model | Max Tokens |
|----------|-------------|-------|------------|
| MiniMax | `https://api.minimax.io/v1/chat/completions` | `MiniMax-M2.7-highspeed` | 200K |
| Kimi | `https://api.kimi.com/coding/v1/chat/completions` | `kimi-for-coding` | 256K |

Set these in the Space Agent UI → Agent Panel → Settings → API tab.

## Routing Notes That Matter In Practice

- Use `gpt-5.5` when the cost of a weak plan is higher than the extra tokens
- Use `gpt-5.4` for most implementation work
- Use `gpt-5.4-mini` only when the task is clearly mechanical
- Use `k2.6` on the VPS when MiniMax output is not good enough for a hard coding or reasoning task
- Keep `MiniMax-M2.7-highspeed` as the main live default because it is much cheaper and fast enough for most runtime work
- Use **Space Agent** (`100.67.172.114:3000`) for visual dashboards, dynamic widgets, and browser-based agent interactions
- Space Agent reads Chimera data from `/srv/space/customware/L2/user/chimera-data/` — pipeline scripts should write JSON there
- Space Agent skills are plain `SKILL.md` files — any agent can write new skills that Space Agent immediately discovers

## Sources

- OpenAI GPT-5.5: https://openai.com/index/introducing-gpt-5-5/
- OpenAI GPT-5.4 docs: https://developers.openai.com/api/docs/models/gpt-5.4/
- OpenAI pricing: https://platform.openai.com/docs/pricing/
- MiniMax pricing: https://platform.minimax.io/docs/guides/pricing-paygo
- MiniMax models intro: https://platform.minimax.io/docs/guides/models-intro
- Kimi K2.6 benchmark blog: https://www.kimi.com/blog/kimi-k2-6
- Kimi K2.6 quickstart: https://platform.kimi.com/docs/guide/kimi-k2-6-quickstart
- Kimi K2.6 pricing: https://www.kimi.com/resources/kimi-k2-6-pricing

## Update Rule

When models, prices, or routes change:

1. verify with official docs first
2. update this registry
3. update `codex-runtime-router` if routing behavior changes
4. mirror shared skill changes into `chimera-vps-deploy`
5. mention the sync state in the current handoff

*model-registry skill v2.1 | Last updated: 2026-04-29 | Sources: official OpenAI, MiniMax, and Kimi docs linked above*
