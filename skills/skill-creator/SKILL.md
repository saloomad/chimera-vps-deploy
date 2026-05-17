---
name: skill-creator
description: Create, repair, diagnose, validate, sync, or mirror agent skills across Codex, Claude Code, Kimi Code, OpenClaw, OpenCowork or OpenCode, and Hermes-facing workflows. Use when a skill needs better discoverability, parser safety, platform fit, or cross-platform sync.
---

# Cross-Platform Skill Creator

Use this skill proactively for any request about creating, fixing, optimizing, mirroring, validating, or troubleshooting skills.

## Goal

Ship skills that:

- load cleanly
- trigger from natural descriptions
- stay small enough to be discoverable
- keep deep details in references or scripts
- match the real skill roots and precedence rules of the platform they serve
- stay synced across the platforms that actually need them

## Done Contract

Do not call a skill done until all of these are true:

1. the source `SKILL.md` validates
2. the description clearly says what the skill does and when to use it
3. the right mirror copies were updated
4. the host runtime or startup path was smoke-tested
5. the result is classified honestly as `exists`, `wired`, `used`, or `scheduler-owned proof`
6. **Windows file creation verified** — on Windows, confirm files actually exist on disk after write (see Pitfalls)

## Windows File Creation — Critical Pitfall

`write_file` tool silently succeeds at the tool-call level but files may NOT actually land on disk for Windows paths like `C:\Users\becke\...`.

**Symptoms:**
- Tool returns `{"status": "ok"}` but `os.path.exists()` returns False
- Workers report success but the files are not there
- `terminal` tool cannot `cd` into `C:\` paths either

**How to write files on Windows:**
- Use Python `execute_code` with `open(path, 'w').write(content)` — this works correctly
- For spawned workers: do NOT delegate file creation to workers on Windows paths. Do it in the orchestrator directly via execute_code.
- After any write_file call on Windows, always verify with a separate read/exists check

**Verification pattern after Windows file write:**
```python
import os
path = r'C:\Users\becke\.hermes\skills\hermes-continuity-enforcer\SKILL.md'
if os.path.exists(path):
    print(f"OK: {path} ({os.path.getsize(path)}b)")
else:
    print(f"MISSING: {path}")
```

**Exception:** `write_file` works fine for Unix/Linux paths (`/root/...`, `/home/...`) and for paths within the git-bash/MSYS environment. The failure is specifically for Windows-native `C:\\` paths routed through the CLI tool layer.

## Pitfall: Authored Skill ≠ Enforced Skill

A skill can be "complete" (rich SKILL.md, good triggers, clear logic) but still **unenforceable** if the platform lacks the runtime to fire it.

**Examples from the field:**

| Skill | Says it does | Actually does |
|-------|-------------|---------------|
| `objective-orchestration-loop` | "create a heartbeat" | Nothing runs it — no heartbeat mechanism existed |
| `hermes-continuity-enforcer` | "update files after every meaningful action" | Nothing triggers it automatically |
| Lobster workflow definitions | "bounded step gates" | No runner exists on Hermes to execute them |
| Hook definitions | "event-driven enforcement" | No event system exists on Hermes to fire them |

**The failure mode:** A skill describes the correct behavior, the agent follows the description during the session, but nothing enforces it after the session ends. Future sessions start from scratch because the enforcement was session-local, not platform-native.

**How to avoid it — ask before calling a skill "done":**
1. Does the platform have a runtime that fires this skill automatically?
2. If not, is there a cron job, heartbeat, or daemon that enforces the behavior?
3. If neither — the skill is **documentation**, not **enforcement**. Be honest about this.
4. If enforcement is needed but missing — build the cron/guard mechanism, not just the skill.

**Three enforcement tiers:**
- **Tier 1 — Native runtime** (lobster runner, hook system, gateway lifecycle): skill fires automatically on every relevant event. Best.
- **Tier 2 — Cron/heartbeat guard** (scheduled script checks state): enforces continuation on a schedule. Good for continuation, not for real-time events.
- **Tier 3 — Skill only** (just the SKILL.md): describes behavior but enforces nothing. Only works during an active session.

Always be honest about which tier your skill is in. Don't claim Tier 1 enforcement when you only have Tier 3.

## First Pass

1. Choose the source-of-truth copy.
   - Default local source: `C:\Users\becke\.codex\skills\<skill-name>`
2. Choose the real consumers.
   - Codex, Claude Code, Kimi Code, OpenClaw, OpenCowork or OpenCode, shared repo mirror, Hermes-facing workflow packs.
3. Choose one primary job.
   - Avoid kitchen-sink skills.
4. Decide whether the skill needs:
   - `references/` for deeper guidance
   - `scripts/` for deterministic validation or sync help
   - `assets/` only when output files need them
5. Validate before mirroring.

## Platform Rules

### OpenAI / Codex

- Keep `SKILL.md` metadata concise and explicit.
- Prefer small reusable playbooks over one giant end-to-end skill.
- Put the real trigger in the description.
- Do not hide trigger words inside brittle YAML text patterns.
- When the skill is meant for the OpenAI skill UI, keep `agents/openai.yaml` aligned.

### Claude Code

- Claude delegates based on the `description`, so make it action-oriented.
- If the skill must be used aggressively, say so plainly in the description with phrases like `use proactively` or `must be used`.
- Keep the skill focused and version-controlled when it is project-level.

### Kimi Code

- Kimi auto-discovers skills from brand and generic directories, with brand paths winning by priority.
- Keep `SKILL.md` under about 500 lines when possible and move deep details to `references/`.
- Use relative links inside the skill body for supporting files.
- If multiple brand skill roots must merge, account for the `merge_all_available_skills` behavior.

### OpenClaw

- OpenClaw uses Agent Skills-compatible folders and applies precedence across workspace, project-agent, personal-agent, managed, bundled, and extra directories.
- Treat location and allowlisting as separate concerns.
- Do not call a skill live just because one copy exists; prove the relevant OpenClaw path or allowlist sees it.

### OpenCowork / OpenCode

- Prefer the native shared agent-skill roots the host already understands, especially `.claude/skills`, `.codex/skills`, `.agents/skills`, and platform-specific config roots.
- Keep descriptions tuned for auto-discovery instead of chat-only wording.
- Mirror durable shared skills into the shared repo when more than one platform needs the same behavior.

### Hermes-Facing Workflows

- Hermes should consume skills as optional playbooks, not as authority over fresher market or runtime truth.
- Skills that feed Hermes should mark evidence priority and freshness rules explicitly.

## Discoverability Rules

- The description must answer both `what this skill does` and `when to use it`.
- Mention 3 to 8 natural trigger phrases inside readable prose.
- Keep the description under the platform limits.
- Avoid inline `Triggers:` labels inside a single-line YAML value.
- Quote the description if punctuation could confuse YAML.
- Keep the body workflow-oriented and move variant-heavy details into `references/`.

## Diagnosis Workflow

1. Validate one skill.
   - Use [quick_validate.py](C:/Users/becke/.codex/skills/.system/skill-creator/scripts/quick_validate.py)
2. Validate a whole tree.
   - Use [validate_skill_tree.py](C:/Users/becke/.codex/skills/.system/skill-creator/scripts/validate_skill_tree.py)
3. Fix parser problems first.
   - frontmatter
   - control characters
   - overlong descriptions
   - bad name format
4. Check mirror drift.
   - compare the source copy against the real platform skill roots
5. Smoke test the host runtime.
   - startup path, skill list, or a real invocation surface

## Sync Workflow

1. Validate the source copy first.
2. Sync only from the chosen source-of-truth copy.
3. Mirror to the real roots that matter:
   - `C:\Users\becke\.codex\skills`
   - `C:\Users\becke\.claude\skills`
   - `C:\Users\becke\.openclaw\skills`
   - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
4. Use [sync_skill_to_platforms.ps1](C:/Users/becke/.codex/skills/.system/skill-creator/scripts/sync_skill_to_platforms.ps1) for local Windows mirroring.
5. After sync, revalidate and smoke test.

## Resources

- Read [platform-skill-patterns.md](C:/Users/becke/.codex/skills/skill-creator/references/platform-skill-patterns.md) for the current source-backed platform notes.
- Use the scaffolder in [init_skill.py](C:/Users/becke/.codex/skills/.system/skill-creator/scripts/init_skill.py) when starting from scratch.
- Capture new parser, discoverability, or precedence failures as durable rules instead of fixing them only once.
