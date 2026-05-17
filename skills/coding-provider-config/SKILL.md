---
name: coding-provider-config
description: Use proactively when entering or diagnosing provider mode, protocol, base URL, model name, or API key for Kimi coding or MiniMax Token Plan / Coding Plan in Space Agent, OpenCowork, OpenCode, OpenClaw, or related tools. Prevents mixing Kimi coding, Kimi OpenAI-compatible, and MiniMax coding-plan endpoints.
---

# Coding Provider Config

Use this skill any time the user asks some version of:

- what do I enter for provider, endpoint, model, or API key
- how do I configure Kimi coding
- how do I configure MiniMax coding plan
- why is this app rejecting my key or endpoint
- can this app use the exact coding endpoint or only an OpenAI-compatible fallback
- how do I enter Kimi coding versus MiniMax coding plan in a specific app

## Read First

- `C:\Users\becke\.codex\skills\model-registry\SKILL.md`
- `C:\Users\becke\.codex\skills\kimi-model-planner\SKILL.md`
- `C:\Users\becke\.codex\skills\minimax-model-planner\SKILL.md`
- `references/provider-config-matrix.md`
- official Kimi docs:
  - `https://www.kimi.com/code/docs/en/kimi-code-for-vscode/configuration.html`
  - `https://www.kimi.com/code/docs/en/third-party-tools/other-coding-agents.html`
- official MiniMax docs:
  - `https://platform.minimax.io/docs/guides/text-ai-coding-tools`
  - `https://platform.minimax.io/docs/guides/mcp-guide`
  - `https://platform.minimax.io/docs/guides/token-plan-mcp-guide`
- Space Agent docs and repo proof:
  - `https://github.com/agent0ai/space-agent`
  - `app/L0/_all/mod/_core/documentation/docs/agent/prompt-and-execution.md`

## Core Rules

1. Keep these three lanes separate:
   - exact `Kimi coding` route
   - exact `MiniMax Token Plan / Coding Plan` route
   - `OpenAI-compatible` fallback route for apps that only speak chat completions
2. Never assume one provider key works for the other provider.
3. Never assume an app that only sends OpenAI-style `chat/completions` can use a raw Anthropic-compatible coding endpoint.
4. If the app supports only one remote protocol, say that plainly before suggesting any endpoint.
5. For MiniMax Token Plan, do not confuse the Token Plan key with a pay-as-you-go key.
6. For Kimi coding, do not confuse the exact coding endpoint with the generic OpenAI-compatible Moonshot endpoint.
7. If the host is Space Agent, read its transport docs before suggesting an endpoint because the remote client is documented as OpenAI-compatible chat completions, not a raw Anthropic coding client.

## Exact Entry Matrix

### Kimi coding exact lane

Use this when the host supports Anthropic-compatible coding providers and the user specifically means the exact coding lane, not the generic OpenAI-compatible lane.

- provider or mode: `custom` or the host's Anthropic-compatible provider slot
- protocol: `anthropic`
- base URL: `https://api.kimi.com/coding/`
- model:
  - `kimi-for-coding` when the host expects the returned server model name
  - `k2.6` when the host already uses the Kimi coding provider abstraction
- API key source: Kimi or Moonshot platform API key from the Kimi platform
- key entry rule: paste the raw key only, not `Bearer ...`
- official source family:
  - Kimi agent-support docs
  - Kimi model list docs
- third-party coding-agent examples:
  - Claude Code: `ANTHROPIC_BASE_URL=https://api.kimi.com/coding/`
  - Roo Code: OpenAI-compatible provider with `https://api.kimi.com/coding/v1` and `kimi-for-coding`

### MiniMax Token Plan / Coding Plan exact lane

Use this when the host supports Anthropic-compatible coding providers and the user specifically means Token Plan / Coding Plan, not a generic OpenAI-style API.

- provider or mode: Anthropic-compatible custom provider or MiniMax Token Plan provider
- protocol: `anthropic`
- base URL:
  - `https://api.minimax.io/anthropic`
  - or `https://api.minimax.io/anthropic/v1` when the host expects the `/v1` form
  - China-hosted alternative from docs: `https://api.minimaxi.com/anthropic`
- model:
  - `MiniMax-M2.7-highspeed` ← use this (user confirmed correct model name)
  - `MiniMax-M2.7` ← wrong, do NOT use
- API key source: MiniMax Token Plan key
- key entry rule: paste the raw Token Plan key only, not `Bearer ...`
- official source family:
  - MiniMax AI coding tools guide
  - MiniMax MCP guide
  - MiniMax Token Plan MCP guide

### Kimi OpenAI-compatible fallback lane

Use this only when the app can send OpenAI-style `chat/completions` but cannot send Anthropic-compatible coding requests.

- protocol: `openai-compatible`
- base URL:
  - `https://api.moonshot.ai/v1`
  - or full endpoint `https://api.moonshot.ai/v1/chat/completions` when the app stores the full path instead of the base URL
- model: `kimi-k2.6`
- API key source: Kimi or Moonshot platform API key
- use this when the host only knows OpenAI-style `chat/completions`

### MiniMax OpenAI-compatible fallback lane

Use this only after verifying the host cannot send Anthropic-compatible coding requests and only if current official MiniMax docs for that host flow support an OpenAI-compatible route.

- protocol: `openai-compatible`
- verify current official MiniMax docs first
- do not assume this lane is the same as Token Plan / Coding Plan

## Customization And Feature Flags

### Kimi Code features worth enabling

From the official Kimi Code docs:

- `thinking`:
  - Kimi Code supports model-level thinking capability
  - in CLI, use `/model`, `--thinking`, or `--no-thinking`
  - in VS Code, `kimi.alwaysExpandThinking` controls whether reasoning is auto-expanded
- `YOLO / auto-approve`:
  - VS Code setting: `kimi.yoloMode`
  - CLI: `kimi --yolo` or `/yolo`
  - use only in safe, controlled environments
- editor and file context:
  - `kimi.autosave`
  - `kimi.editorContext` with `never`, `onConversationStart`, or `onFileChange`
- custom CLI path and env:
  - `kimi.executablePath`
  - `kimi.environmentVariables`
- model capability flags:
  - `thinking`
  - `always_thinking`
  - `image_in`
  - `video_in`
- built-in Kimi platform services:
  - `SearchWeb`
  - `FetchURL`
  - these are automatically configured when using the Kimi Code platform via `/login`

### MiniMax prompt caching and reasoning

From the official MiniMax docs:

- passive prompt caching:
  - works automatically on repeated long prefixes
  - best results come from placing static tool lists, system prompts, and repeated context first
  - dynamic user input should come later
- explicit Anthropic-compatible caching:
  - supported through `cache_control`
  - use this only on Anthropic-compatible MiniMax routes
- OpenAI-compatible reasoning split:
  - MiniMax docs show `extra_body={"reasoning_split": true}` for OpenAI-compatible calls
  - use this only if the host lets you pass extra body parameters
- verification tip:
  - in coding clients that expose status surfaces, verify the active base URL and model after changing reasoning or provider settings

### MiniMax MCP and extra tools

MiniMax has two relevant MCP doc families:

- general MiniMax MCP:
  - `minimax-mcp`
  - supports transport modes described as local stdio and SSE/server deployment options
  - supports resource exposure controls such as `MINIMAX_API_RESOURCE_MODE`
- Token Plan MCP:
  - `minimax-coding-plan-mcp`
  - exposes:
    - `web_search`
    - `understand_image`
  - `understand_image` supports HTTP/HTTPS URLs or local file paths
  - supported image formats include JPEG, PNG, GIF, and WebP
  - in Claude Code, `/mcp` should show those tools after setup

If the user asks for vision or web search under MiniMax Token Plan, point them to Token Plan MCP first instead of pretending the base coding endpoint alone provides those tools.

## Current Platform Guidance

### OpenCowork

Current verified working route from our registry:

- provider mode: `custom`
- protocol: `anthropic`
- base URL: `https://api.kimi.com/coding/`
- model: `kimi-for-coding`

### OpenClaw / live VPS

Current default live route:

- provider: `kimi-coding`
- endpoint: `https://api.kimi.com/coding`
- model: `k2.6`
- fallbacks:
  - `k2.5`
  - `MiniMax-M2.7-highspeed`
  - `MiniMax-M2.5`

### Space Agent / MiniMax Agent local desktop app
### Space Agent Desktop App (Windows)

**Verified working configuration** as of May 2026:

Per-agent YAML configs at:
`C:/Users/becke/AppData/Roaming/space-agent/customware/L2/user/conf/`

`admin-chat.yaml` — Kimi:
```yaml
api_endpoint: "https://api.kimi.com/coding"
model: kimi-for-coding
```

`onscreen-agent.yaml` — MiniMax:
```yaml
api_endpoint: "https://api.minimax.io/anthropic"
model: MiniMax-M2.7-highspeed
```

**Critical notes:**
- `api_endpoint` is base URL only — no `/v1/chat/completions` suffix
- Model name MUST be `MiniMax-M2.7-highspeed` — not `MiniMax-M2.7` (confirmed corrected by user)
- Both configs use `llm_provider: api` (OpenAI-compatible chat completions wire)

## Diagnosis Order

1. Identify the host app.
2. Identify whether it speaks:
   - Anthropic-compatible messages
   - OpenAI-compatible chat completions
3. Match the endpoint to that protocol first.
4. Match the model name expected by that host.
5. Match the API key source to the provider.
6. Check whether the user also expects:
   - reasoning or thinking
   - prompt caching
   - MCP tools like search or image understanding
7. Only then blame the app or account.

## What To Say Clearly

Always say:

- exact route versus compatibility fallback
- provider key source
- whether the app wants a base URL or the full `/chat/completions` path
- whether the app is an Anthropic-compatible host or only an OpenAI-compatible host
- whether advanced features like thinking, caching, or MCP are actually available on that route
- whether the result is only `exists`, `wired`, or `runtime-proven`

## Closeout

After meaningful provider-config work:

- update this skill if the verified entry matrix changes
- update `model-registry` when the live default or verified working route changes
- if a platform-specific app needs the same guidance, mirror this skill to that real skill root
