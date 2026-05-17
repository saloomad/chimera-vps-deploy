# Provider Config Matrix

Use this file for the exact field-entry split.

## Exact Kimi coding route

- protocol: `anthropic`
- base URL: `https://api.kimi.com/coding/`
- model:
  - `kimi-for-coding` for hosts like OpenCowork that read the coding endpoint directly
  - `k2.6` or `k2.5` for hosts that already abstract Kimi coding as a provider
- API key source: Kimi or Moonshot platform key
- do not prepend `Bearer `
- source family:
  - `https://www.kimi.com/code/docs/en/kimi-code-for-vscode/configuration.html`
  - `https://www.kimi.com/code/docs/en/third-party-tools/other-coding-agents.html`

### Kimi coding extras

- Claude Code-style route:
  - `ANTHROPIC_BASE_URL=https://api.kimi.com/coding/`
  - `ANTHROPIC_API_KEY=<Kimi Code API key>`
- Roo Code-style route:
  - provider: OpenAI-compatible
  - entrypoint: `https://api.kimi.com/coding/v1`
  - model: `kimi-for-coding`
  - options from docs:
    - legacy OpenAI API format: enabled
    - streaming: enabled
    - include max output tokens: enabled
    - reasoning effort: `Medium`
    - max output tokens: `32768`
    - context window size: `262144`

### Kimi customization and capabilities

- VS Code settings:
  - `kimi.yoloMode`
  - `kimi.autosave`
  - `kimi.editorContext`
  - `kimi.alwaysExpandThinking`
  - `kimi.executablePath`
  - `kimi.environmentVariables`
- model capability flags:
  - `thinking`
  - `always_thinking`
  - `image_in`
  - `video_in`
- Kimi platform can auto-configure:
  - `SearchWeb`
  - `FetchURL`

## Exact MiniMax Token Plan route

- protocol: `anthropic`
- base URL:
  - `https://api.minimax.io/anthropic`
  - `https://api.minimax.io/anthropic/v1` when the host expects `/v1`
  - China-hosted alternative: `https://api.minimaxi.com/anthropic`
- model:
  - `MiniMax-M2.7`
  - `MiniMax-M2.7-highspeed` when the host and plan support it explicitly
- API key source: MiniMax Token Plan key
- do not use a pay-as-you-go key when the host expects Token Plan
- do not prepend `Bearer `
- source family:
  - `https://platform.minimax.io/docs/guides/text-ai-coding-tools`
  - `https://platform.minimax.io/docs/guides/mcp-guide`
  - `https://platform.minimax.io/docs/guides/token-plan-mcp-guide`

### MiniMax coding-plan notes

- MiniMax docs distinguish Token Plan from Pay-As-You-Go by API key type
- some hosts document `MiniMax-M2.7`; some host flows may separately mention `MiniMax-M2.7-highspeed`
- do not promote `highspeed` unless the target host and plan explicitly support it

## OpenAI-compatible fallback route

Use only when the app cannot speak Anthropic-compatible coding requests.

### Kimi

- base URL: `https://api.moonshot.ai/v1`
- full endpoint when needed: `https://api.moonshot.ai/v1/chat/completions`
- model: `kimi-k2.6`

### MiniMax

- verify the host and current official docs before entering an OpenAI-compatible MiniMax route
- do not assume the Token Plan app lane and the generic OpenAI-compatible lane are interchangeable

### Caching and reasoning

- MiniMax passive prompt caching:
  - automatic on repeated prefixes
  - best practice: put static content first and dynamic content later
- MiniMax explicit prompt caching:
  - Anthropic-compatible only
  - use `cache_control`
- MiniMax OpenAI-compatible reasoning:
  - docs show `reasoning_split: true` support in OpenAI-compatible examples

## MCP and extra tools

### MiniMax MCP

- general MCP server package: `minimax-mcp`
- transport modes discussed in docs:
  - local stdio
  - SSE/server deployment
- useful env vars:
  - `MINIMAX_API_KEY`
  - `MINIMAX_API_HOST`
  - `MINIMAX_MCP_BASE_PATH`
  - `MINIMAX_API_RESOURCE_MODE`

### MiniMax Token Plan MCP

- package: `minimax-coding-plan-mcp`
- primary tools from docs:
  - `web_search`
  - `understand_image`
- `understand_image` accepts:
  - local file paths
  - HTTP/HTTPS image URLs
- supported image formats:
  - JPEG
  - PNG
  - GIF
  - WebP
- verification rule:
  - in hosts like Claude Code, `/mcp` should show the expected tools

### MiniMax vision and image understanding notes

- OpenClaw note from the MiniMax coding-tools guide:
  - when logged in through the MiniMax portal via OAuth, OpenClaw's image tool is automatically backed by MiniMax's image-understanding MCP lane
- for other hosts, prefer explicit MCP setup instead of assuming the base coding endpoint alone provides image understanding

## Platform notes

### OpenCowork

- verified route:
  - provider mode: `custom`
  - protocol: `anthropic`
  - base URL: `https://api.kimi.com/coding/`
  - model: `kimi-for-coding`

### Space Agent

- current packaged app is wired like an OpenAI-style `chat/completions` client
- repo and local docs both describe the remote client as OpenAI-compatible chat completions
- exact Kimi coding and exact MiniMax Token Plan lanes are not yet runtime-proven there without app-level protocol support
