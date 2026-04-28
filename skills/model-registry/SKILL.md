---
name: model-registry
description: Central registry of ALL AI models used across the Chimera ecosystem. Read this BEFORE answering questions about model capabilities, endpoints, pricing, or connection methods. Prevents hallucinated model specs. Triggers: model info, which model, model capabilities, endpoint URL, API base, model pricing, connection method, what model to use.
---

# Model Registry — Chimera Ecosystem

> **READ THIS FIRST** before answering any question about models, endpoints, capabilities, or pricing. Do NOT guess. If info is missing here, say "I don't have that in the registry" rather than making it up.

---

## VPS-Configured Models (source: `/root/.openclaw/openclaw.json`)

These are the models actually wired into the OpenClaw gateway. If it's not in this list, the VPS cannot use it without config changes.

### Provider: `minimax`

| Model ID (config) | Display Name | Endpoint | Status |
|-------------------|--------------|----------|--------|
| `MiniMax-M2.7-highspeed` | MiniMax M2.7 High Speed | `https://api.minimax.io/anthropic` | DEFAULT |
| `MiniMax-M2.5` | MiniMax M2.5 | `https://api.minimax.io/anthropic` | Fallback #3 |

**API Key**: `sk-cp-R9KqNRCZ8fM9xGEYEwz8_K3dcJ1bXTTyBLaWCStWU1rxKKujuJYUpceNJ-PbLdzdix4aCmv4AnnrD3CfQsAXJGpieYqHbT1PCHcBTgdptmJ-lnPWB5lhCck`

**Protocol**: Anthropic Messages API (`/v1/messages`)

**Docs**: https://platform.minimax.io/docs/guides/models-intro

**What the architect got wrong before**:
- Claimed `MiniMax-Text-01` was available — it is NOT in the VPS config
- Claimed endpoint was `https://api.minimax.io/v1/chat/completions` — actual VPS uses `https://api.minimax.io/anthropic` (Claude SDK compatible)
- Did not know M2.7-highspeed was configured but only as fallback

**Known specs** (from official docs + web research):
- M2.5: Optimized for code, fast inference
- M2.7-highspeed: Same performance as M2.7, significantly faster inference
- Context window for M2 series: **200k tokens**
- Max output for M2 series: **128k tokens** (including CoT) (not documented)
- MiniMax-Text-01 (NOT in config): 4M context, ~$0.20/1M in, ~$1.10/1M out

---

### Provider: `kimi-coding`

| Model ID (config) | Display Name | Endpoint | Status |
|-------------------|--------------|----------|--------|
| `k2.6` | Kimi K2.6 | `https://api.kimi.com/coding` | Fallback #1 |
| `k2.5` | Kimi K2.5 | `https://api.kimi.com/coding` | Fallback #2 |

**API Key**: `sk-kimi-zbLEAyaxC1vAcBdbSPklDLBgXlbg6H6sMdaH8hrKcPAXf5BTMu6IEEUmCb63fK9S`

**Protocol**: Anthropic Messages API (`/v1/messages`)

**Docs**: https://platform.kimi.com/docs/api/chat (Moonshot) + https://www.kimi.com/code/docs/en/ (Kimi Code)

**What the architect got wrong before**:
- Claimed endpoint was `https://api.moonshot.cn/v1/chat/completions` — actual VPS uses `https://api.kimi.com/coding` (Anthropic-compatible)
- Claimed model ID was `kimi-k2-6` — actual config ID is just `k2.6`
- Claimed 262k context / 65k output without verifying — these numbers are NOT in the official docs

**Known specs** (from official Moonshot docs):
- k2.6: Supports `thinking` parameter with `type` and `keep` options ("Preserved Thinking")
- k2.5: Supports `thinking` parameter with `type` only
- Function calling: Supported (max 128 tools)
- Vision: Supported via `image_url` and `video_url`
- JSON mode: Supported via `response_format`
- Context window and pricing: **NOT documented** in the API reference

---

## Default Agent Routing

```javascript
Primary:   minimax/MiniMax-M2.7-highspeed
Fallbacks:
  1. kimi-coding/k2.6
  2. kimi-coding/k2.5
  3. minimax/MiniMax-M2.5
```

**How to read this**: `minimax/MiniMax-M2.5` means provider `minimax`, model ID `MiniMax-M2.5`.

---

## Windows-Only Models

These are used on the Windows machine (this interactive session), NOT on the VPS.

| Model | Provider | Endpoint | Where Used |
|-------|----------|----------|------------|
| `claude-sonnet-4` | Anthropic | `https://api.anthropic.com` | Windows Claude Code |
| `claude-opus-4` | Anthropic | `https://api.anthropic.com` | Windows Claude Code (expensive) |
| `claude-haiku-3.5` | Anthropic | `https://api.anthropic.com` | Windows Claude Code (fast) |
| `anthropic/claude-sonnet-4.6` | OpenRouter | `https://openrouter.ai/api/v1` | User's local settings UI |

---

## Connection Methods Summary

### MiniMax (VPS — Anthropic SDK)
```bash
base_url: https://api.minimax.io/anthropic
api_key: sk-cp-...
model: MiniMax-M2.5
```

### Kimi (VPS — Anthropic SDK)
```bash
base_url: https://api.kimi.com/coding
api_key: sk-kimi-...
model: k2.6
```

### MiniMax (OpenCode Desktop/CLI — OpenAI-compatible)
```json
{
  "provider": {
    "minimax-coding-plan": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "https://api.minimax.io/v1"
      },
      "models": {
        "MiniMax-M2.7-highspeed": { "name": "M2.7 High Speed" }
      }
    }
  }
}
```
**Config file**: `C:\Users\becke\.config\opencode\opencode.jsonc`
**Command**: `opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed "prompt"`
**Common mistakes**: Using `api.minimax.chat` (wrong domain), using `MiniMax-M2.7-High-Speed` (wrong case/spacing).

### Kimi (OpenCode Desktop/CLI — OpenAI-compatible)
```json
{
  "provider": {
    "kimi-for-coding": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "https://api.kimi.com/coding/v1"
      },
      "models": {
        "kimi-for-coding": { "name": "Kimi K2.6" }
      }
    }
  }
}
```
**Config file**: `C:\Users\becke\.config\opencode\opencode.jsonc`
**Command**: `opencode run -m kimi-for-coding/kimi-for-coding "prompt"`
**Critical**: Base URL MUST include `/v1` at the end (`coding/v1`, not just `/coding`).
**Common mistakes**: Using `api.moonshot.ai` (old domain), using `kimi-k2-6` or `k2.6` as model ID (must be `kimi-for-coding`).

### Anthropic (Windows)
```bash
base_url: https://api.anthropic.com/v1
api_key: sk-ant-...
model: claude-sonnet-4-20250514
```

---

## When to Use What (VPS)

| Task | Recommended Model | Why |
|------|-------------------|-----|
| Default agent responses | `minimax/MiniMax-M2.7-highspeed` | Free, fastest inference |
| Complex analysis | `kimi-coding/k2.6` | Better reasoning, longer thinking |
| Code generation | `minimax/MiniMax-M2.7-highspeed` | Optimized for code, fast |
| Fallback if primary fails | `kimi-coding/k2.6` | Reliable backup |
| Fallback if Kimi fails | `minimax/MiniMax-M2.5` | Stable workhorse |

---

## Why M2.7-highspeed is Now Default

The config was changed on 2026-04-28:
```json
"default": {
  "primary": "minimax/MiniMax-M2.7-highspeed",
  "fallbacks": ["kimi-coding/k2.6", "kimi-coding/k2.5", "minimax/MiniMax-M2.5"]
}
```

**Rationale**: M2.7-highspeed offers same performance as M2.7 with significantly faster inference. Since it's free via our key and faster, it makes sense as primary.

**Previous config** (before 2026-04-28): M2.5 was primary, M2.7-highspeed was fallback #3.

**To revert to M2.5 as default**:
```bash
python3 -c "
import json
with open('/root/.openclaw/openclaw.json') as f:
    d = json.load(f)
d['agents']['defaults']['model']['primary'] = 'minimax/MiniMax-M2.5'
with open('/root/.openclaw/openclaw.json', 'w') as f:
    json.dump(d, f, indent=2)
"
systemctl restart openclaw-gateway
```

---

## Known Knowledge Gaps (Do NOT Guess)

These are NOT in any official doc I have read. If asked, say "I don't have that information":

1. **Exact context window** for MiniMax M2.5 and M2.7-highspeed
2. **Exact pricing** for MiniMax M2.5 and M2.7-highspeed (they're free for us via the current key, but public pricing is unknown)
3. **Exact context window** for Kimi k2.6 and k2.5
4. **Exact pricing** for Kimi k2.6 and k2.5
5. **Whether MiniMax-Text-01** can be added to the VPS config (likely yes, but not currently configured)
6. **Vision support** on MiniMax models (unknown)

---

## How to Update This Registry

When new models are added to the VPS:
```bash
# 1. Read the actual config
python3 -m json.tool /root/.openclaw/openclaw.json | grep -A20 'providers'

# 2. Update this SKILL.md with the real values

# 3. Update the Notion page
```

---

*model-registry skill v1.1 | Last updated: 2026-04-28 | Source of truth: `/root/.openclaw/openclaw.json`*
