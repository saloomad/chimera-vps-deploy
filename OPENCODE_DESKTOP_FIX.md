# OpenCode Desktop App — MiniMax + Kimi Fix

> **Status**: MiniMax FIXED ✅ | Kimi BLOCKED by provider ❌
> **Config file edited**: `C:\Users\becke\.config\opencode\opencode.jsonc`
> **Auth file edited**: `C:\Users\becke\.local\share\opencode\auth.json`

---

## What I Fixed Manually

You were right — the OpenCode desktop UI doesn't let you edit base URLs. I edited the config files directly.

### File 1: `C:\Users\becke\.config\opencode\opencode.jsonc`

Changed MiniMax base URL from `https://api.minimax.chat/v1` → `https://api.minimax.io/v1`

**Before (broken):**
```json
{
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
  "minimax-coding-plan": {
    "options": {
      "baseURL": "https://api.minimax.io/v1"
    },
    "models": {
      "MiniMax-M2.7-highspeed": { "name": "M2.7 High Speed" }
    }
  }
}
```

**Two changes:**
1. Domain: `api.minimax.chat` → `api.minimax.io` (`.chat` was wrong)
2. Model ID: `MiniMax-M2.7-High-Speed` → `MiniMax-M2.7-highspeed` (lowercase 'h', no space — this is what MiniMax API accepts)

### File 2: `C:\Users\becke\.local\share\opencode\auth.json`

Updated the Kimi API key to the working one from the VPS.

---

## Test Results

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

### ❌ Kimi K2.6 — NOT WORKING (Provider Restriction)

I tested every combination. Kimi's API returns this error:

```json
{"error":{"message":"Kimi For Coding is currently only available for Coding Agents such as Kimi CLI, Claude Code, Roo Code, Kilo Code, etc.","type":"access_terminated_error"}}
```

**This means:** Kimi intentionally blocks OpenCode. They only allow their API through specific coding agent platforms. OpenCode is NOT on their allowlist.

**You CAN use Kimi through:**
- Claude Code (which you already have)
- Kimi's own CLI
- Roo Code, Kilo Code, etc.

**You CANNOT use Kimi through:**
- OpenCode desktop app
- OpenCode CLI
- Generic API calls

---

## How to Apply to Desktop App

1. **Close OpenCode desktop app completely** (tray icon too)
2. The config changes are already saved
3. **Reopen OpenCode desktop app**
4. Start a new chat
5. Select **MiniMax M2.7 High Speed** from the model dropdown
6. Test with "Say hello"

If the desktop app doesn't pick up the new model name, you may need to:
- Go to Settings → Providers
- Remove the old MiniMax provider
- Re-add it (it will read the corrected config from `opencode.jsonc`)

---

## Working Models in OpenCode

| Model | Command | Status |
|-------|---------|--------|
| `minimax-coding-plan/MiniMax-M2.7-highspeed` | `opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed "prompt"` | ✅ Working |
| `opencode/minimax-m2.5-free` | Built-in free model | ✅ Working |
| `kimi-for-coding/k2p6` | Kimi K2.6 | ❌ Blocked by Kimi |
| `kimi-for-coding/kimi-for-coding` | Kimi for Coding | ❌ Blocked by Kimi |

---

## What About Skills?

OpenCode desktop app has **no native skill system**.

**Workaround**: Create prompt templates in:
```
C:\Users\becke\.opencode\skills\
```

Example:
```
.opencode\skills\market-analysis\prompt.txt
```

Copy-paste the prompt into OpenCode when you need it. No auto-discovery.

---

*OpenCode Desktop Fix v2.0 | 2026-04-28 | Config manually edited and tested*
