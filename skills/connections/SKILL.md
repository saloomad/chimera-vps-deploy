---
name: connections
description: Explain and maintain the Chimera, OpenClaw, and OpenCowork access and connection paths across Windows and Linux. Use when the user asks how to reach OpenClaw, Paperclip, dashboards, SSH, Tailscale, Windows Terminal profiles, OpenCowork API settings, or Notion connector setup. Also use when the question involves platform capability comparison — what each platform can enforce, whether OpenClaw enforcement can be imported into Hermes, or how lobster/hooks/cron compare across Hermes/OpenClaw/Codex.
triggers:
  - openclaw into hermes
  - import openclaw into hermes
  - can hermes use lobster
  - what can openclaw do that hermes can't
  - platform comparison
  - capability comparison
  - why doesn't hermes have hooks
  - why doesn't hermes have lobster
  - what enforcement does hermes have
  - hermes vs openclaw enforcement
---

# Connections

Use this skill when the user wants the right access path for:

- **Hermes** (this agent) - runs cron jobs, research, Discord bridge
- **OpenClaw** - runs trading agents, Chimera pipeline
- OpenClaw Linux shell access
- Linux Paperclip access
- Windows Paperclip sandbox access
- Chimera dashboards and monitor portals
- Tailscale versus LAN routing
- Windows Terminal profile creation or cleanup
- OpenCowork desktop app API setup
- Notion connector setup inside OpenCowork

## Platform Truth

| Platform | Hermes Config | OpenClaw Config |
|----------|-------------|-----------------|
| Windows | `C:\Users\becke\.hermes\config.yaml` | `C:\Users\becke\.openclaw\openclaw.json` |
| VPS (100.67.172.114) | `/root/.hermes/config.yaml` | `/root/.openclaw/openclaw.json` |
| Linux PC (100.116.214.127) | `~/.hermes/config.yaml` | `~/.openclaw/openclaw.json` |

**Key distinction:**
- **Hermes** = this agent (me), runs on Windows, VPS, and Linux. Uses MiniMax primary.
- **OpenClaw** = separate system, runs on VPS and Linux. Uses Kimi primary.

## OpenClaw Linux PC (100.116.214.127)

**SSH:** `ssh open-claw@100.116.214.127` (or `ssh open-claw-linux` via SSH config)

**Verified working commands (non-interactive SSH):**
```
openclaw --version   → OpenClaw 2026.5.7
mcporter --version  → 0.7.3
```

**Interactive-only commands** (require login shell, do NOT work via `ssh host "command"`):
- `openclaw-tui` — alias defined in .bashrc
- Any interactive REPL

**OpenClaw global install location:**
- Package: `~/.npm-global/lib/node_modules/openclaw/`
- Binary: `~/.npm-global/bin/openclaw` (symlinked)
- npm global root: `~/.npm-global/lib/node_modules/`

### Linux PC PATH Fix — .bashrc / .bash_profile Layering (2026-05-17)

**Problem:** SSH commands don't source `.bashrc` on Linux PC — they hit `.bash_profile` first.

**Ubuntu shell startup chain for login shells:**
```
~/.bash_profile  →  sources ~/.bashrc  →  sources ~/.bashrc.bak
~/.bashrc       →  has "return" for non-interactive, then exits early
```

**For SSH `ssh host "command"`** → login shell → reads `.bash_profile` → reads `.bashrc` → `.bashrc` exits early for non-interactive → PATH never set.

**For interactive SSH (`ssh host`):** → `.bash_profile` loads → `.bashrc` loads → PATH set correctly.

**The `.bash_profile` already had the PATH fix** from a previous install, but `.bashrc` was exiting early. The fix inserts PATH exports **inside** `.bashrc` before the interactive check, AND ensures `.bash_profile` is correct.

**Verified working PATH for non-interactive SSH:**
```bash
export PATH="$HOME/.npm-global/bin:$PATH"
alias openclaw-tui='openclaw run --profile default'
alias cdp='cd /home/open-claw/openclawtrading'
```

**Test:** `ssh open-claw@100.116.214.127 "openclaw --version"` → `OpenClaw 2026.5.7` ✅

**If `.bash_profile` did NOT exist**, the fix would need to create it and source `.bashrc` from there.

### Terminal Tool Limitation

The Hermes `terminal` tool (Git Bash layer) cannot allocate PTY/TTY on Windows:
- `ssh -t host` — hangs
- `ssh host` with PTY via Git Bash — returns `exit_code: 126, "No such file or directory"`
- Interactive shell sessions via PTY — do not work

**Use `execute_code` subprocess for ALL SSH operations from Hermes on Windows.** The SSH config already has `open-claw-linux` and `chimera-vps` entries. Commands like this work reliably:

```python
import subprocess
result = subprocess.run(
    ['ssh', '-o', 'ConnectTimeout=8', '-o', 'StrictHostKeyChecking=no',
     'open-claw@100.116.214.127', 'openclaw --version'],
    capture_output=True, text=True, timeout=20
)
print(result.stdout.strip())  # → OpenClaw 2026.5.7
```

Note: `openclaw-tui` and other aliases only work in a **real login shell** (e.g. `ssh open-claw-linux` from Windows Terminal), not via `subprocess.run()` with `-c "command"`.

## Core Rule

Do not answer connection questions from memory alone when the workspace already carries the current connection guide.

Read the guide first, then verify the live path if the request involves:

- a real host or IP
- a Paperclip mode or URL
- a terminal profile
- a live Linux service
- an away-from-home access question
- an OpenCowork API connection problem
- a Notion connector that exists but still cannot see pages

## Read First

## Companion Artifacts

- `C:\\Users\\becke\\claudecowork\\docs\\CHIMERA_CONNECTIONS_AND_ACCESS_GUIDE_2026-04-21.md`
- `C:\\Users\\becke\\claudecowork\\docs\\CONNECT_TO_LINUX_REMOTE.md`
- `C:\\Users\\becke\\claudecowork\\MODEL_SWITCHING.md`
- `references/PLATFORM_CAPABILITY_COMPARISON.md` — **load this first** when the question involves "import OpenClaw into Hermes," "can Hermes use lobster," or "what can each platform actually enforce." The enforcement comparison is canonical and updated.
- `C:\Users\becke\AppData\Roaming\open-cowork\`

## Decision Order

1. Treat OpenClaw Linux as the real always-on home.
2. Treat Windows as the sandbox and desktop-app lane unless the user explicitly wants local-only work.
3. Prefer Tailscale when the user may be away from home.
4. Use LAN only when the user is clearly on the same network and wants the faster local route.
5. For OpenCowork provider setup, prefer the app's verified working Kimi coding endpoint before inventing a custom route.

## What To Say Clearly

Always make these distinctions plain:

- `OpenClaw Linux shell` versus `Linux Paperclip UI`
- `Linux real runtime` versus `Windows sandbox`
- `direct Tailscale URL` versus `SSH tunnel fallback`
- `OpenCowork desktop app config` versus `OpenClaw live VPS config`
- `Notion token present` versus `Notion page actually shared with the integration`

## If You Need To Change The System

When updating connection paths:

- patch the guide and the terminal profiles together so names stay consistent
- inspect the live Linux config first if the request touches real runtime behavior
- verify the final path with a real SSH or HTTP health check when possible
- for OpenCowork, remember the app config store is encrypted and normal text-file edits are not enough unless the stored values were actually read back

## Closeout

After meaningful connection work:

- update the canonical guide
- record the real hostname, URL, or endpoint truth instead of leaving it only in chat
- mirror shared skill changes into the shared deploy repo when other platforms will need the same truth

## Companion Artifacts

- `C:\\Users\\becke\\claudecowork\\docs\\CHIMERA_CONNECTIONS_AND_ACCESS_GUIDE_2026-04-21.md`
- `C:\\Users\\becke\\claudecowork\\docs\\CONNECT_TO_LINUX_REMOTE.md`
- `C:\\Users\\becke\\claudecowork\\MODEL_SWITCHING.md`
- `references/PLATFORM_CAPABILITY_COMPARISON.md` — **load this first** when the question involves "import OpenClaw into Hermes," "can Hermes use lobster," or "what can each platform actually enforce." The enforcement comparison is canonical and updated.
