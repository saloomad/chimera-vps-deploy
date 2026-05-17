---
name: linux-access
description: Access the Chimera Linux machines over SSH. Use by default for the live Kimi VPS at root@100.67.172.114, and use the Linux-home draft/test machine at open-claw@100.116.214.127 only when the user explicitly wants the old Linux-home lane.
---

# linux-access

## Purpose

Use this skill for SSH access, Linux file checks, remote commands, log checks, and file copy operations on Chimera Linux machines.

## Default Live Profile

Unless the user explicitly asks for Linux home, default to the live VPS:

```bash
ssh root@100.67.172.114
```

Live VPS path defaults:

- repo: `/root/openclawtrading`
- runtime workspace: `/root/.openclaw/workspace`
- extra runtime skills: `/root/.openclaw/kimi-skills`

## Linux Home Profile

Use Linux home only when the user explicitly wants the old Linux-home lane, draft/test work, or historical Linux-home state:

```bash
ssh open-claw@100.116.214.127
```

Linux-home path defaults:

- draft repo: `/home/open-claw/openclawtrading`
- clean staging gate: `/home/open-claw/openclawtrading-staging`

## Enforcement

- Do not confuse Linux home with the live VPS.
- Do not default to `192.168.1.203` while `100.116.214.127` is the verified reachable path.
- Do not default to `/home/open-claw/...` for current VPS work.
- If the user says `linux`, check whether they mean:
  - live VPS
  - Linux home draft/test lane

## Linux Home PATH Fix

**Symptom:** `openclaw`, `mcporter`, `claude` return "command not found" on Linux PC even though the binaries exist at `~/.npm-global/bin/`.

**Root cause:** Linux PC's `.bashrc` has an early exit for non-interactive shells (`case $- in *i*) ;; *) return;; esac`). The PATH export must be inserted **before** that block, not after it.

**Symptoms of wrong fix attempts:**
- Adding PATH to `.bash_profile` alone does NOT help — `.bashrc` exits before reading it for non-interactive SSH
- Appending PATH after the `return` line means it never executes for SSH sessions

**Correct fix — insert BEFORE the interactive check:**

```bash
# In ~/.bashrc, find this line:
# If not running interactively, don't do anything
# Then insert BEFORE the "case $-" block:

export PATH="$HOME/.npm-global/bin:$PATH"
alias openclaw-tui='openclaw run --profile default'
alias cdp='cd /home/open-claw/openclawtrading'
```

**Automated fix — use Python patch script on the remote:**

```python
# Run on the Linux PC to patch .bashrc correctly
import os
bashrc = os.path.expanduser("~/.bashrc")
with open(bashrc, 'r') as f:
    content = f.read()

marker = "# If not running interactively, don't do anything"
insert = '''export PATH="$HOME/.npm-global/bin:$PATH"
alias openclaw-tui='openclaw run --profile default'
alias cdp='cd /home/open-claw/openclawtrading'

'''

if marker in content and "NPM_GLOBAL" not in content:
    content = content.replace(marker, insert + marker)
    with open(bashrc, 'w') as f:
        f.write(content)
    print("Patched OK")
```

**Verified working on Linux PC (May 16, 2026):**
```
openclaw --version  →  OpenClaw 2026.5.7 ✅
mcporter --version   →  0.7.3 ✅
openclaw-tui         →  alias set ✅
```

## Useful Checks

### VPS identity

```bash
ssh root@100.67.172.114 "echo OK && whoami && pwd"
```

> **Status (May 17, 2026):** VPS SSH times out. Tailscale shows `linux -` (not peer). VPS is likely down or Tailscale client died. Do not assume it is up. Try `ssh root@100.67.172.114` but expect timeout. GitHub push remains the sync path when VPS is down.

### Linux-home identity

```bash
ssh open-claw@100.116.214.127 "echo OK && whoami && pwd"
```

> **Status (May 17, 2026):** Linux PC IS reachable via Tailscale SSH at `100.116.214.127`. User was physically at the machine when commands returned "command not found" — this was a PATH issue, not a connectivity issue. `ssh open-claw@100.116.214.127 "openclaw --version"` works and returns `OpenClaw 2026.5.7`. See "Linux Home PATH Fix" below.

> **VPS Status (May 17, 2026):** `root@100.67.172.114` SSH times out. Tailscale shows `linux -` (not peer). VPS is likely down or Tailscale client died. GitHub push remains the sync path. Do not assume VPS is up — probe first.

### VPS logs

```bash
ssh root@100.67.172.114 "journalctl -u openclaw-gateway --since '10 min ago' --no-pager | tail -50"
```

### Linux-home repo status

```bash
ssh open-claw@100.116.214.127 "cd /home/open-claw/openclawtrading && git status --short"
```

## Related Skills

- `platform-access-and-sync-guide` for deciding which platform should own the work
- `github-manager` for Git and GitHub flow after the right Linux target is chosen
