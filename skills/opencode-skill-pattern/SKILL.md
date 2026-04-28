---
name: opencode-skill-pattern
description: "How to create reusable prompt packs and wrappers for OpenCode CLI (v1.14.25) since it has no native skill system. Use when Sal wants OpenCode to run structured tasks, repeat prompts, or integrate with the Chimera pipeline. Triggers: opencode skill, opencode prompt, opencode wrapper, opencode automation, opencode template, run opencode with skill."
---

# OpenCode Skill Pattern

> **Platform**: OpenCode CLI v1.14.25 (VPS Linux)
> **Location**: `/root/.opencode/skills/` (convention we created)
> **Config**: `/root/.config/opencode/config.yaml`
> **Discovery**: Manual — OpenCode has NO auto-skill detection. Skills = shell scripts + prompt templates.

---

## The Problem

OpenCode is a CLI tool, not an agent platform. It has:
- ✅ Providers (MiniMax, Kimi)
- ✅ Models per provider
- ✅ `run` command for one-shot prompts
- ❌ NO skill system
- ❌ NO auto-discovery
- ❌ NO session memory between runs

**Solution**: Create a convention where "skills" for OpenCode = **shell script wrappers** + **prompt template files** stored in `/root/.opencode/skills/`.

---

## OpenCode Skill Anatomy

```
/root/.opencode/skills/
└── my-skill/
    ├── SKILL.md          ← Documentation (this file)
    ├── prompt.md         ← The prompt template
    └── run.sh            ← Wrapper script (optional)
```

**Only `prompt.md` is required.** `run.sh` is optional but recommended for complex workflows.

---

## Prompt Template Format (`prompt.md`)

A reusable OpenCode prompt template:

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
```bash
# Replace {{INPUT}} and pipe to OpenCode
sed 's/{{INPUT}}/BTC funding rate/' /root/.opencode/skills/my-skill/prompt.md | opencode run
```

---

## Wrapper Script Format (`run.sh`)

For skills that need pre-processing or post-processing:

```bash
#!/bin/bash
# OpenCode Skill Wrapper: my-skill
# Usage: ./run.sh "[input]"

SKILL_DIR="/root/.opencode/skills/my-skill"
INPUT="${1:-default input}"

# Build prompt from template
PROMPT=$(sed "s/{{INPUT}}/${INPUT}/g" "${SKILL_DIR}/prompt.md")

# Run via OpenCode with appropriate model
opencode run -m minimax/MiniMax-M2.5-HighSpeed "${PROMPT}"
```

---

## OpenCode Model Reference

| Model | Command | Status |
|-------|---------|--------|
| MiniMax M2.5-HighSpeed | `opencode run` (default) | ✅ Working |
| MiniMax M2.5-HighSpeed | `opencode run -m minimax/MiniMax-M2.5-HighSpeed` | ✅ Working |
| Kimi K2.6 | `opencode run -m kimi/kimi-k2-6` | ❌ Model resolution bug |
| Kimi for Coding | `opencode run -m kimi/kimi-for-coding` | ❌ Model resolution bug |

**Known issue**: Kimi models fail with "Model not found" even when configured. Use MiniMax as default. Track issue in OpenCode repo.

---

## Integration with Chimera Pipeline

OpenCode can be called from cron scripts or agent wrappers:

```bash
# Example: Daily market summary via OpenCode
#!/bin/bash
source /root/.chimera.env
MARKET_DATA=$(cat /root/reports/auto/MACRO.json | jq -r '.summary')

opencode run "Summarize this market data in 3 bullets: ${MARKET_DATA}" > /root/reports/auto/DAILY_SUMMARY.txt
```

---

## Creating a New OpenCode "Skill"

### Step 1: Create directory
```bash
mkdir -p /root/.opencode/skills/my-skill
```

### Step 2: Write prompt.md
```bash
cat > /root/.opencode/skills/my-skill/prompt.md <<'EOF'
# Prompt: My Skill

## Task
[What to do]

## Input
{{INPUT}}

## Output
[Expected output]
EOF
```

### Step 3: (Optional) Write run.sh
```bash
cat > /root/.opencode/skills/my-skill/run.sh <<'EOF'
#!/bin/bash
SKILL_DIR="/root/.opencode/skills/my-skill"
INPUT="${1:-}"
PROMPT=$(sed "s/{{INPUT}}/${INPUT}/g" "${SKILL_DIR}/prompt.md")
opencode run "${PROMPT}"
EOF
chmod +x /root/.opencode/skills/my-skill/run.sh
```

### Step 4: Test
```bash
/root/.opencode/skills/my-skill/run.sh "test input"
```

---

## OpenCode vs. OpenClaw vs. Claude Code

| Feature | OpenCode | OpenClaw | Claude Code |
|---------|----------|----------|-------------|
| Type | CLI tool | Agent platform | Agent platform |
| Skills | Shell scripts + prompts | SKILL.md auto-detect | SKILL.md auto-detect |
| Memory | None per run | Session-based | Session-based |
| Models | MiniMax, Kimi (buggy) | MiniMax, Kimi | Claude |
| Best for | One-shot tasks, cron jobs | Multi-step agent workflows | Interactive dev work |

---

## Best Practices

1. **Keep prompts under 2000 tokens** — OpenCode has no cache optimization
2. **Use wrapper scripts for repeated tasks** — Don't retype long prompts
3. **Pipe JSON data carefully** — Escape quotes when passing JSON to opencode run
4. **Log outputs** — OpenCode has no built-in history; redirect to files
5. **Use MiniMax as default** — Kimi model resolution is buggy in v1.14.25

---

*opencode-skill-pattern v1.0 | 2026-04-28 | OpenCode CLI convention*
