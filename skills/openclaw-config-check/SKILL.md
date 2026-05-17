---
name: openclaw-config-check
description: >
  Read and validate the live OpenClaw config (openclaw.json) on Linux and Windows.
  Checks for invalid keys, bad streaming values, and compares against the known good schema.
  Use when making any channel config change or diagnosing gateway config problems.
triggers:
  - openclaw config
  - check gateway config
  - validate config
  - why is gateway broken
  - deezoh channels
  - openclaw channels
---

# SKILL: openclaw-config-check

Read and validate the current OpenClaw Discord channel configuration. Use this before ANY config modification and to diagnose gateway errors.

## Step 1 - Read the live Linux config

```python
ssh root@100.67.172.114 "python3 -c \"
import json, os
d = json.load(open(os.path.expanduser('~/.openclaw/openclaw.json')))
discord = d['channels']['discord']
print('streaming:', discord.get('streaming'))
guilds = discord.get('guilds', {})
for gid, g in guilds.items():
    print(f'guild {gid} requireMention:', g.get('requireMention', 'NOT SET'))
    for cname, cv in g.get('channels', {}).items():
        rm = cv.get('requireMention', 'NOT SET')
        mode = 'FULL RESPONSE' if rm == False else 'MONITOR' if rm == True else 'DEFAULT'
        print(f'  {cname}: allow={cv.get(\"allow\")} requireMention={rm} [{mode}]')
\""
```

## Step 2 - Validate against known schema

Check each value against `OPENCLAW_CONFIG_REFERENCE.md`:

- `streaming` must be one of: `true`, `false`, `"off"`, `"partial"`, `"block"`, `"progress"`
- Channel keys: only `allow` and `requireMention`
- Guild keys: only `requireMention` and `channels`

## Step 3 - Restart and verify if a change was approved

```bash
ssh root@100.67.172.114 "kill \$(ps aux | grep openclaw-gateway | grep -v grep | awk '{print \$2}'); sleep 3; journalctl --user -n 5 | grep -E 'channels resolved|Config invalid'"
```

## Enforcement

- default live host: `root@100.67.172.114`
- default live repo: `/root/openclawtrading`
- treat `open-claw@...` and `/home/open-claw/...` as historical only
