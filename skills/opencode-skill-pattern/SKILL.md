---
name: opencode-skill-pattern
description: "How to create reusable prompt packs and wrappers for OpenCode CLI and Desktop App. Use when Sal wants OpenCode to run structured tasks, repeat prompts, integrate with the Chimera pipeline, or configure MiniMax/Kimi providers. Triggers: opencode skill, opencode prompt, opencode wrapper, opencode automation, opencode template, run opencode with skill, opencode config, configure opencode, opencode model not working, opencode 404, minimax opencode, kimi opencode."
---

# OpenCode Skill Pattern

> **Platform**: OpenCode CLI v1.14.25 + OpenCode Desktop App (Windows)
> **CLI Config**: `C:\Users\becke\.config\opencode\opencode.jsonc`
> **Desktop Config**: Same file — both CLI and Desktop read the same config
> **Auth**: `C:\Users\becke\.local\share\opencode\auth.json`
> **Discovery**: Manual — OpenCode has NO auto-skill detection. Skills = shell scripts + prompt templates.

---

## CRITICAL: Working Provider Config (Copy-Paste Ready)

This is the ONLY config that works. Save this to `C:\Users\becke\.config\opencode\opencode.jsonc`:

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

**After editing the config, CLOSE and REOPEN OpenCode completely** (including system tray) for it to take effect.

---

## Common Mistakes (Read This Before Guessing)

These are the EXACT mistakes that were made before. Do NOT repeat them:

| Mistake | Wrong Value | Right Value | Why It Breaks |
|---------|-------------|-------------|---------------|
| **Kimi baseURL** | `https://api.moonshot.ai/v1` | `https://api.kimi.com/coding/v1` | Moonshot is the old domain. Kimi API is on `api.kimi.com`. |
| **Kimi baseURL missing /v1** | `https://api.kimi.com/coding` | `https://api.kimi.com/coding/v1` | OpenCode's ai-sdk appends `/chat/completions`. Without `/v1` it calls the wrong endpoint. |
| **Kimi model ID** | `kimi-k2-6`, `k2.6`, `k2p6` | `kimi-for-coding` | The API only accepts `kimi-for-coding` as the model ID. |
| **MiniMax baseURL** | `https://api.minimax.chat/v1` | `https://api.minimax.io/v1` | `.chat` is wrong. Must be `.io`. |
| **MiniMax model ID** | `MiniMax-M2.7-High-Speed` | `MiniMax-M2.7-highspeed` | Case-sensitive. Lowercase `h`, no space, no hyphens around `highspeed`. |

**If you see "404 Page not found"**: Check baseURL first.
**If you see "invalid params, unknown model"**: Check model ID case/spelling.
**If you see "Not Found / 没找到对象"**: Wrong baseURL or model ID for Kimi.

---

## How to Verify Config is Working

```bash
# Test Kimi
opencode run -m kimi-for-coding/kimi-for-coding "Say hello in 5 words"

# Test MiniMax
opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed "Say hello in 5 words"
```

Both should respond without 404 errors.

---

## The Problem (Original)

OpenCode is a CLI tool, not an agent platform. It has:
- ✅ Providers (MiniMax, Kimi)
- ✅ Models per provider
- ✅ `run` command for one-shot prompts
- ❌ NO native skill system
- ❌ NO auto-discovery
- ❌ NO session memory between runs

**Solution**: Create a convention where "skills" for OpenCode = **shell script wrappers** + **prompt template files** stored in `.opencode/skills/`.

---

## OpenCode Skill Anatomy

```
C:\Users\becke\.opencode\skills\           ← Windows convention
└── my-skill/
    ├── SKILL.md          ← Documentation (this file)
    ├── prompt.md         ← The prompt template
    └── run.bat           ← Wrapper script (optional)
```

**Only `prompt.md` is required.** `run.bat` is optional but recommended for complex workflows.

---

## Prompt Template Format (`prompt.md`)

```markdown
# Prompt: [Skill Name]

## Role
You are a [role].

## Task
[Specific task description]

## Input
{{INPUT}}

## Output Format
[Expected format]

## Constraints
- [Constraint 1]
- [Constraint 2]
```

**Usage:**
```powershell
# Replace {{INPUT}} and pipe to OpenCode
(Get-Content C:\Users\becke\.opencode\skills\my-skill\prompt.md).replace('{{INPUT}}', 'BTC funding rate') | opencode run
```

---

## Wrapper Script Format (`run.bat`)

```batch
@echo off
set SKILL_DIR=C:\Users\becke\.opencode\skills\my-skill
set INPUT=%1

powershell -Command "(Get-Content '%SKILL_DIR%\prompt.md').replace('{{INPUT}}', '%INPUT%') | opencode run"
```

---

## Working Model Reference

| Provider | Model | Command | Status |
|----------|-------|---------|--------|
| Kimi | K2.6 | `opencode run -m kimi-for-coding/kimi-for-coding` | ✅ Working |
| MiniMax | M2.7-HighSpeed | `opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed` | ✅ Working |
| MiniMax | M2.5 (built-in free) | `opencode run -m opencode/minimax-m2.5-free` | ✅ Working |

---

## Integration with Chimera Pipeline

OpenCode can be called from PowerShell scripts or Task Scheduler:

```powershell
# Example: Daily market summary via OpenCode
$MARKET_DATA = Get-Content Z:\reports\auto\MACRO.json | ConvertFrom-Json
$Summary = opencode run -m minimax-coding-plan/MiniMax-M2.7-highspeed "Summarize this in 3 bullets: $($MARKET_DATA.summary)"
$Summary | Out-File Z:\reports\auto\DAILY_SUMMARY.txt
```

---

## OpenCode vs. OpenClaw vs. Claude Code vs. Codex

| Feature | OpenCode | OpenClaw | Claude Code | Codex |
|---------|----------|----------|-------------|-------|
| Type | CLI tool | Agent platform | Agent platform | Agent platform |
| Skills | Shell scripts + prompts | SKILL.md auto-detect | SKILL.md auto-detect | SKILL.md auto-detect |
| Memory | None per run | Session-based | Session-based | Session-based |
| Models | MiniMax, Kimi | MiniMax, Kimi | Claude | GPT-5.4/5.5 |
| Best for | One-shot tasks, cron jobs | Multi-step agent workflows | Interactive dev work | Interactive dev work |
| Config file | `opencode.jsonc` | `openclaw.json` | `settings.json` | `config.toml` |

---

## Best Practices

1. **Keep prompts under 2000 tokens** — OpenCode has no cache optimization
2. **Use wrapper scripts for repeated tasks** — Don't retype long prompts
3. **Pipe JSON data carefully** — Escape quotes when passing JSON to opencode run
4. **Log outputs** — OpenCode has no built-in history; redirect to files
5. **ALWAYS use the exact baseURLs and model IDs from this skill** — Do NOT guess

---

*opencode-skill-pattern v2.0 | 2026-04-28 | OpenCode CLI + Desktop App*
