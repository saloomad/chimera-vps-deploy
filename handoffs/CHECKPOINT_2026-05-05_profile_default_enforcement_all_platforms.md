# CHECKPOINT — profile default enforcement across platforms

Date: 2026-05-05
Operator: Codex

## Objective

Make the live Chimera/OpenClaw profile the enforced default everywhere it matters:

- host/user: `root@100.67.172.114`
- repo: `/root/openclawtrading`
- runtime workspace: `/root/.openclaw/workspace`
- runtime extra skills: `/root/.openclaw/kimi-skills`

Remove active skill defaults pointing at:

- `open-claw@192.168.1.203`
- `open-claw@100.116.214.127`
- `open-claw@192.168.31.194`
- `/home/open-claw/...`

## What changed

- fixed active profile/path drift in Windows Codex skills
- fixed active profile/path drift in Windows Claude skills
- added `linux-access` to Windows Codex and shared skill mirrors
- replaced the stale Windows Claude `linux-access` body with the live default profile
- mirrored the corrected shared skills into Windows OpenClaw local
- mirrored the corrected shared skills into:
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`

## Skills synced

- `linux-access`
- `openclaw-config-check`
- `macro-calendar`
- `news-reader`
- `openclaw-workspace`
- `tradingview-mcp`
- `divergence-scanner`

## Proof

Windows proof:

- `linux-access` now explicitly says the only default live target is `root@100.67.172.114`
- `openclaw-config-check` now points to:
  - `/root/.openclaw/workspace/OPENCLAW_CONFIG_REFERENCE.md`
  - `/root/openclawtrading/docs/OPENCLAW_CONFIG_REFERENCE.md`
- targeted grep over:
  - `C:\Users\becke\.codex\skills`
  - `C:\Users\becke\.claude\skills`
  - `C:\Users\becke\.openclaw\skills`
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
  returns only intentional guardrails like:
  - `Do not default to ...`
  - `historical only`

VPS proof:

- `/root/openclawtrading/skills/linux-access/SKILL.md`
- `/root/.openclaw/kimi-skills/linux-access/SKILL.md`
- `/root/openclawtrading/skills/openclaw-config-check/SKILL.md`
- `/root/.openclaw/kimi-skills/openclaw-config-check/SKILL.md`
- `/root/openclawtrading/skills/macro-calendar/SKILL.md`
- `/root/.openclaw/kimi-skills/macro-calendar/SKILL.md`
- `/root/openclawtrading/skills/news-reader/SKILL.md`
- `/root/.openclaw/kimi-skills/news-reader/SKILL.md`

All show the live default `root@100.67.172.114` and `/root/openclawtrading`.

Remote grep over the mirrored skill set returns only intentional guardrails:

- `Do not default to /home/open-claw/...`
- `historical only`

## Remaining work

- broader old-path cleanup still exists in non-targeted legacy docs and skills not part of this default-profile enforcement slice
- if needed later, do a second pass just for historical/documentation debt outside the enforced default surfaces
