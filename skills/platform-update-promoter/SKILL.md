---
name: platform-update-promoter
description: Push tested skills, workflows, and structure updates across Codex, Claude, OpenClaw, GitHub mirror, and live OpenClaw skill paths without waiting for each platform to update itself.
---

# Platform Update Promoter

Use this when Sal says:

- `update it`
- `push this to the other platforms`
- `mirror this`
- `install this everywhere`

Also use this when a change is both:

- finished
- tested

and the change is a safe skill, workflow, structure, reporting, or instruction update that should not stay local.

## Core Rule

Do not wait for other platforms to discover or recreate the change themselves.

If the update is safe and tested, the agent should perform the platform updates directly and then leave proof.

## What This Skill Updates

- skills
- workflows
- platform structure and docs
- safe reporting and learning utilities
- hook or receipt support files when they are bounded and already expected by config

Do not use this skill to auto-push:

- live trading policy
- execution rules
- order sizing
- credentials
- risky cron mutation

Those still need explicit approval.

## Trigger Gate

Promote only when one of these is true:

1. Sal explicitly asked for the update
2. the change is complete and tested, and mirroring it is low-risk

If proof is weak, stop and finish proof first.

## Platform Targets

### Codex

- primary path:
  - `C:\Users\becke\.codex\skills`
- use for:
  - Codex-discoverable skills
  - local execution helpers

### Claude local

- primary path:
  - `C:\Users\becke\.claude\skills`
- use for:
  - equivalent skill docs when Claude should use the same idea

### OpenClaw local

- primary path:
  - `C:\Users\becke\.openclaw\skills`
- use for:
  - local OpenClaw testing or parity prep

### Shared GitHub mirror

- primary path:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
- use for:
  - durable cross-platform sync truth
  - future GitHub push surface

### Live OpenClaw repo mirror

- primary path:
  - `/root/openclawtrading/skills`
- use for:
  - repo-visible live mirror

### Live OpenClaw runtime extra skills

- primary path:
  - `/root/.openclaw/kimi-skills`
- use for:
  - runtime-usable skill install when the skill should actually be available to live OpenClaw sessions

### Hermes skills (Windows + Kimi VPS + Linux PC)

Hermes's own skills live in three places:

| Platform | Path | Sync Method | Status |
|----------|------|-------------|--------|
| **Hermes Windows** | `C:\Users\becke\.hermes\skills` | Local — Hermes reads directly | ✅ always works |
| **GitHub mirror** | `C:\Users\becke\claudecowork\chimera-vps-deploy\skills` | `git add → commit → push` | ✅ always works |
| **Kimi VPS** | `root@100.67.172.114:/root/.hermes/skills` | Git pull from GitHub when VPS is online | ❌ VPS frequently down |
| **Linux PC** | `open-claw@100.116.214.127:/home/open-claw/.hermes/skills` | Git pull from GitHub when reachable | ❌ SSH times out |

**Primary sync path:** GitHub (`saloomad/chimera-vps-deploy`, branch `codex/github-coordination-hardening-part2`).
- All Hermes skill writes go to `C:\Users\becke\.hermes\skills\` AND `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\`
- From there: `git commit → git push origin codex/github-coordination-hardening-part2`
- VPS pulls via `git clone` or `git pull` when back online

**Secondary (direct SCP) — only when SSH works:**
```bash
scp -r C:\Users\becke\.hermes\skills\SKILL_NAME root@100.67.172.114:/root/.hermes/skills/
scp -r C:\Users\becke\.hermes\skills\SKILL_NAME open-claw@100.116.214.127:/home/open-claw/.hermes/skills/
```
- Test SSH reachability first: `ssh -o ConnectTimeout=5 user@host echo OK`
- If timeout → skip direct SCP, rely on GitHub sync

**SSH reachability is the gate for direct sync:**
- Before attempting `scp` or `ssh` direct sync: test with `ssh -o ConnectTimeout=5 user@host echo OK`
- If timeout → skip direct SCP, rely on GitHub sync ONLY
- Both Kimi VPS (`root@100.67.172.114`) and Linux PC (`open-claw@100.116.214.127`) were UNREACHABLE as of this session (May 16, 2026) — SSH times out on both
- When SSH is down: GitHub push to feature branch is the ONLY viable sync path until VPS/Linux PC recovers

**Current branch:** `codex/github-coordination-hardening-part2` (NOT `main`)
- The `main` branch does NOT have the new trading skills
- All Hermes skills are on the feature branch
- When consolidating, cherry-pick or merge `codex/github-coordination-hardening-part2` into `main`

## Optimization Rule By Platform

Do not force identical payloads everywhere.

- Codex:
  - keep developer-facing skills concise
  - include local proof commands
- Claude:
  - prefer stronger hook and session-lifecycle guidance
- OpenClaw:
  - prefer runtime paths, receipts, and hook-aware language
  - mirror into runtime extra skills when actual runtime use is intended
- GitHub mirror:
  - include the durable shared copy and handoff/update note

## Required Update Loop

1. confirm source of truth
2. confirm proof exists
3. choose target platforms
4. adapt the update to each platform
5. mirror the files
6. verify existence on each target
7. verify runtime path when applicable
8. update handoff or research if the change is durable
9. say what is:
   - local only
   - mirrored locally
   - mirrored live
   - not yet pushed to GitHub
10. if the change can drift in real runtime conditions:
   - register a daily monitor
   - run it once immediately
   - leave the proof path

## Required Proof

At minimum, leave:

- path existence proof on each chosen target
- runtime receipt proof when a live runtime path is involved
- honest GitHub status:
  - not in repo mirror
  - in repo mirror but uncommitted
  - committed locally but not pushed
  - pushed

## Decision Rule

- safe tested update:
  - do it for the platforms
- risky runtime mutation:
  - stop for approval
- weak proof:
  - finish testing first
