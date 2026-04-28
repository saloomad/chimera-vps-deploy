# OpenCode Desktop App — MiniMax + Kimi Fix

> **Problem**: You configured MiniMax and Kimi in OpenCode desktop app but get 404 errors when trying to use them.
> **Root cause**: Wrong base URLs. OpenCode is calling `/v1/messages` (Anthropic path) on the wrong endpoints.
> **Fix**: Use the Anthropic-compatible base URLs below.

---

## What Went Wrong (Simple Explanation)

OpenCode desktop app speaks **Anthropic API language** (`/v1/messages`) to custom providers.

You probably entered:
- MiniMax base URL: `https://api.minimax.chat` or `https://api.minimax.io` ❌
- Kimi base URL: `https://api.moonshot.ai` or `https://api.moonshot.cn` ❌

These are **OpenAI-compatible** endpoints. They expect `/v1/chat/completions`, not `/v1/messages`.

**The fix**: Add `/anthropic` (MiniMax) or `/coding` (Kimi) to the base URL so OpenCode talks to the right endpoint.

---

## Correct OpenCode Desktop Config

### MiniMax

| Setting | Wrong (what you probably have) | Right (fix this) |
|---------|-------------------------------|------------------|
| **Base URL** | `https://api.minimax.chat` or `https://api.minimax.io` | `https://api.minimax.io/anthropic` |
| **API Key** | `sk-cp-R9KqNRCZ8fM9xGEYEwz8_K3dcJ1bXTTyBLaWCStWU1rxKKujuJYUpceNJ-PbLdzdix4aCmv4AnnrD3CfQsAXJGpieYqHbT1PCHcBTgdptmJ-lnPWB5lhCck` | Same |
| **Model ID** | `MiniMax-M2.5-HighSpeed` or `MiniMax-M2.7-highspeed` | Same |

### Kimi (Moonshot)

| Setting | Wrong (what you probably have) | Right (fix this) |
|---------|-------------------------------|------------------|
| **Base URL** | `https://api.moonshot.ai` or `https://api.moonshot.cn` | `https://api.kimi.com/coding` |
| **API Key** | `sk-kimi-zbLEAyaxC1vAcBdbSPklDLBgXlbg6H6sMdaH8hrKcPAXf5BTMu6IEEUmCb63fK9S` | Same |
| **Model ID** | `k2.6` or `k2.5` | Same |

---

## How to Apply the Fix in OpenCode Desktop

1. **Open OpenCode desktop app**
2. **Go to Settings** (gear icon or `Ctrl+,`)
3. **Find Providers section**
4. **Edit MiniMax provider**:
   - Change Base URL to: `https://api.minimax.io/anthropic`
   - Keep API key and model names the same
   - Save
5. **Edit Kimi provider**:
   - Change Base URL to: `https://api.kimi.com/coding`
   - Keep API key and model names the same
   - Save
6. **Start a new chat** and select the fixed model
7. **Test**: Ask "Say hello in 5 words"

---

## Why This Happens

| Platform | API Format | MiniMax Endpoint | Kimi Endpoint |
|----------|-----------|------------------|---------------|
| **OpenClaw (VPS)** | Anthropic SDK | `https://api.minimax.io/anthropic` | `https://api.kimi.com/coding` |
| **OpenCode CLI/Desktop** | Anthropic SDK | `https://api.minimax.io/anthropic` | `https://api.kimi.com/coding` |
| **Generic OpenAI tools** | OpenAI-compatible | `https://api.minimax.io/v1` | `https://api.moonshot.cn/v1` |

OpenCode uses **Anthropic format** for custom providers. That's why the `/anthropic` and `/coding` suffixes are required.

---

## OpenCode Desktop App + Skills

OpenCode desktop app **does NOT have a native skill system** like Claude Code or Codex.

But you can still use skills with it:

### Method 1: Prompt Templates (Recommended)
Store reusable prompts as text files and paste them into OpenCode:

```
C:\Users\becke\.opencode\skills\          ← Create this folder
└── market-analysis\
    └── prompt.txt
```

**prompt.txt**:
```
You are a crypto market analyst. Analyze this data:

{{PASTE_DATA_HERE}}

Give me:
1. Macro bias (LONG/SHORT/MIXED)
2. Key levels
3. Risk assessment
```

**Usage**: Copy-paste the prompt into OpenCode, replace `{{PASTE_DATA_HERE}}` with actual data.

### Method 2: Windows Shortcut Scripts
Create `.bat` files that pipe prompts to OpenCode CLI:

```bat
@echo off
set PROMPT_FILE=C:\Users\becke\.opencode\skills\market-analysis\prompt.txt
set /p DATA="Paste data: "
type %PROMPT_FILE% | findstr /V "{{PASTE_DATA_HERE}}" > %TEMP%\prompt.txt
echo %DATA% >> %TEMP%\prompt.txt
opencode-cli run --file %TEMP%\prompt.txt
```

---

## Test Results from Your System

I checked your OpenCode desktop app logs. Here's what I found:

| Model | What OpenCode Called | Result |
|-------|---------------------|--------|
| MiniMax | `https://api.minimax.chat/v1/messages` | ❌ 404 — wrong domain + wrong path |
| Kimi | `https://api.moonshot.ai/v1/messages` | ❌ 404 — wrong domain + wrong path |

After applying the fix above, both should return ✅ 200 OK.

---

*OpenCode Desktop Fix v1.0 | 2026-04-28*
