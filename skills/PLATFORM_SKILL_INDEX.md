# Platform Skill Index — Chimera Ecosystem

> **Master reference for all skill-creator skills and platform-specific skill systems.**
> Updated: 2026-04-28

---

## Skill Systems by Platform

| Platform | Location | Format | Discovery | Skill Creator Skill |
|----------|----------|--------|-----------|---------------------|
| **Claude Code** (Windows) | `C:\Users\becke\.claude\skills\` | YAML + Markdown | Auto-detect at session start | `skill-creator` (`.claude/skills/skill-creator/`) |
| **Codex** (Windows) | `C:\Users\becke\.codex\skills\` | YAML + Markdown | Auto-detect at session start | `skill-creator` (`.codex/skills/skill-creator/`) |
| **OpenClaw** (VPS) | `/root/.openclaw/skills/` + `/workspace/skills/` | YAML + Markdown + metadata JSON | Agent runtime + ClawHub | `skill-creator` (`workspace/skills/skill-creator/`) |
| **OpenCode** (VPS CLI) | `/root/.opencode/skills/` (convention) | Shell scripts + prompt templates | Manual (no auto-detect) | `opencode-skill-pattern` (`workspace/skills/opencode-skill-pattern/`) |
| **Space Agent** (VPS Browser) | `/srv/space/customware/L1/_admin/mod/chimera/ext/skills/` | YAML + Markdown + JS | Auto-detect at runtime | `space-agent-integration` (`chimera-vps-deploy/skills/space-agent-integration/`) |

---

## Quick Reference: Creating a Skill on Any Platform

### Claude Code
```powershell
# 1. Create directory
mkdir C:\Users\becke\.claude\skills\my-skill

# 2. Write SKILL.md with YAML frontmatter + triggers
# 3. Test: start new Claude session, ask matching trigger question
# 4. Done — auto-discovered
```

### Codex
```powershell
# 1. Create directory
mkdir C:\Users\becke\.codex\skills\my-skill

# 2. Write SKILL.md with YAML frontmatter + triggers
# 3. Test: start new Codex session, ask matching trigger question
# 4. Done — auto-discovered
```

### OpenClaw
```bash
# 1. Choose location
mkdir /root/.openclaw/workspace/skills/my-skill    # custom
# OR
mkdir /root/.openclaw/skills/my-skill              # system

# 2. Write SKILL.md with YAML frontmatter + metadata JSON
# 3. Test: clawhub search "topic" OR ask agent
# 4. Commit to GitHub
```

### OpenCode
```bash
# 1. Create directory (convention)
mkdir -p /root/.opencode/skills/my-skill

# 2. Write prompt.md (prompt template)
# 3. Optional: write run.sh (wrapper script)
# 4. Test: /root/.opencode/skills/my-skill/run.sh "input"
# 5. No auto-discovery — call manually or from cron
```

---

## Trigger Keyword Strategy

Each platform's skill-creator has overlapping but distinct triggers:

| Keyword | Claude | Codex | OpenClaw | OpenCode |
|---------|--------|-------|----------|----------|
| create skill | ✅ | ✅ | ✅ | ❌ |
| new skill | ✅ | ✅ | ✅ | ❌ |
| skill best practices | ✅ | ✅ | ✅ | ❌ |
| codex skill | ❌ | ✅ | ❌ | ❌ |
| openclaw skill | ❌ | ❌ | ✅ | ❌ |
| clawhub skill | ❌ | ❌ | ✅ | ❌ |
| opencode skill | ❌ | ❌ | ❌ | ✅ |
| opencode prompt | ❌ | ❌ | ❌ | ✅ |
| opencode wrapper | ❌ | ❌ | ❌ | ✅ |

**Rule**: Platform-specific keywords (e.g., "codex skill", "openclaw skill") ensure the RIGHT skill-creator is invoked on the RIGHT platform.

---

## Key Differences Between Platforms

| Aspect | Claude Code | Codex | OpenClaw | OpenCode | Space Agent |
|--------|-------------|-------|----------|----------|-------------|
| **Model** | Claude Sonnet/Opus | GPT-5.4/5.5 | MiniMax / Kimi | MiniMax (Kimi buggy) | MiniMax / Kimi / OpenRouter |
| **OS** | Windows + Linux | Windows | Linux (Ubuntu 24.04) | Linux | Linux (browser UI) |
| **Skill format** | YAML + Markdown | YAML + Markdown | YAML + Markdown + JSON | Shell + Markdown | YAML + Markdown + JS |
| **Auto-discovery** | ✅ Session start | ✅ Session start | ✅ Agent runtime | ❌ None | ✅ Runtime |
| **Path style** | `C:\Users\...` | `C:\Users\...` | `/root/...` | `/root/...` | `/srv/space/customware/...` |
| **Needs metadata** | ❌ No | ❌ No | ✅ Yes (JSON block) | ❌ No | ✅ Yes (YAML frontmatter) |
| **Needs triggers** | ✅ Yes | ✅ Yes | ✅ Yes | N/A | ✅ Yes |
| **GitHub sync** | Manual | Manual | Via `chimera-deploy/` | Manual | Manual |

---

## GitHub Sync for Skills

**Windows → GitHub**: Skills in `chimera-vps-deploy/skills/` are committed and pushed.
**VPS → GitHub**: Skills in `/root/chimera-deploy/skills/` are committed and pushed.
**Cross-sync**: Both platforms pull from `saloomad/chimera-vps-deploy`.

**Best practice**: Create skills in `chimera-vps-deploy/skills/` on Windows, commit, push, then VPS pulls. This keeps both platforms in sync.

---

## Testing Discoverability

### Claude Code
1. Start fresh session
2. Ask: "I want to create a new skill for trading analysis"
3. Expected: Claude references `skill-creator` skill

### Codex
1. Start fresh session
2. Ask: "How do I make a codex skill?"
3. Expected: Codex references `skill-creator` skill

### OpenClaw
1. Ask agent: "Find me skills about creating new skills"
2. Expected: Agent references `skill-creator` or `clawhub-discovery`

### OpenCode
1. Run: `ls /root/.opencode/skills/`
2. Expected: Directory listing shows available prompt packs

### Space Agent
1. Open: `http://100.67.172.114:3000`
2. Ask agent: "List available skills"
3. Expected: Agent discovers `chimera-dashboard` skill and can use it

---

*Platform Skill Index v1.1 | 2026-04-29 | Chimera Ecosystem*
