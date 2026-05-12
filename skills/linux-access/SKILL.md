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

## Useful Checks

### VPS identity

```bash
ssh root@100.67.172.114 "echo OK && whoami && pwd"
```

### Linux-home identity

```bash
ssh open-claw@100.116.214.127 "echo OK && whoami && pwd"
```

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
