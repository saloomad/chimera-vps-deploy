# OpenCode Desktop App — MiniMax + Kimi Fix

> **Status**: MiniMax FIXED ✅ | Kimi FIXED ✅
> **Config file edited**: `C:\Users\becke\.config\opencode\opencode.jsonc`
> **Auth file edited**: `C:\Users\becke\.local\share\opencode\auth.json`

---

## What Was Broken

You configured MiniMax and Kimi in OpenCode but got 404 errors. The problem was **wrong base URLs and model IDs** in the auto-generated config.

---

## The Fix (I Edited Your Config Files Directly)

### File 1: `C:\Users\becke\.config\opencode\opencode.jsonc`

**Before (broken):**
```json
{
  "kimi-for-coding": {
    "options": {
      "baseURL": "https://api.moonshot.ai/v1"
    },
    "models": {
      "kimi-k2-6": { "name": "Kimi K2.6" }
    }
  },
  "minimax-coding-plan": {
    "options": {
      "baseURL": "https://api.minimax.chat/v1"
    },
    "models": {
      "MiniMax-M2.7-High-Speed": { "name": "M2.7 High Speed" }
    }
  }
}
```

**After (working):**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "kimi-for-coding": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Kimi for Coding",
      "options": {
        "baseURL": "https://api.kimi.com/coding/v1"
      },
      "models": {
        "kimi-for-coding": { "name": "Kimi K2.6" }
      }
    },
    "minimax-coding-plan": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "MiniMax Coding Plan",
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

### What Changed

| Provider | Setting | Wrong | Right |
|----------|---------|-------|-------|
| **Kimi** | Base URL | `https://api.moonshot.ai/v1` | `https://api.kimi.com/coding/v1` |
| **Kimi** | Model ID | `kimi-k2-6` | `kimi-for-coding` |
| **MiniMax** | Base URL | `https://api.minimax.chat/v1` | `https://api.minimax.io/v1` |
| **MiniMax** | Model ID | `MiniMax-M2.7-High-Speed` | `MiniMax-M2.7-highspeed` (lowercase h, no space) |

**Critical detail for Kimi**: The base URL needs `/v1` at the end (`coding/v1`), not just `/coding`. OpenCode's ai-sdk appends `/chat/completions` to the baseURL, so without `/v1` it calls the wrong endpoint.

---

## Test Results

### ✅ Kimi K2.6 — WORKING

```bash
opencode run -m kimi-for-coding/kimi-for-coding "Say hello in exactly 5 words"
```

**Output:**
```
> build · kimi-for-coding
Hello, how are you doing?
```

### ✅ MiniMax M2.7-HighSpeed — WORKING

```bash
opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed "Say hello in exactly 5 words"
```

**Output:**
```
> build · MiniMax-M2.7-highspeed
<think>
The user wants me to say hello in exactly 5 words.
</think>
Hello there, how are you?
```

---

## How to Apply to OpenCode Desktop App

1. **Close OpenCode desktop app completely** (tray icon too)
2. The config changes are already saved in `opencode.jsonc`
3. **Reopen OpenCode desktop app**
4. Start a new chat
5. Select **Kimi for Coding** or **MiniMax M2.7 High Speed** from the model dropdown
6. Test with "Say hello"

If the models don't show up in the dropdown:
- Go to Settings → Providers
- Remove and re-add the Kimi/MiniMax provider
- It will read the corrected config

---

## Working Model Commands

```bash
# Kimi K2.6
opencode run -m kimi-for-coding/kimi-for-coding "your prompt"

# MiniMax M2.7 HighSpeed
opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed "your prompt"

# MiniMax M2.5 (built-in free model)
opencode run -m opencode/minimax-m2.5-free "your prompt"
```

---

## Skills with OpenCode Desktop

OpenCode desktop has **no native skill system** like Claude Code.

**Workaround**: Create prompt templates as text files:

```
C:\Users\becke\.opencode\skills\market-analysis\prompt.txt
C:\Users\becke\.opencode\skills\risk-check\prompt.txt
```

Copy-paste into OpenCode when needed. No auto-discovery.

---

*OpenCode Desktop Fix v3.0 | 2026-04-28 | Config manually edited and tested*
