# Agent Improvement Backlog

Updated: 2026-05-03

Use this file as the fallback improvement ledger when Linear is unavailable, disabled, or not configured.

## Open Items

### 1. Communication skill is not truly auto-enforced in every Codex response

- Trigger:
  - meaningful replies can still drift into artifact-heavy or system-heavy explanations
- Current impact:
  - Sal may still need to pull the answer out of tooling language
- Current enforcement:
  - instructions and skills exist
  - Claude-side prompt/session hooks now explicitly name `sal-communication-contract` and `response-structure-enforcer`
- Still needed:
  - stronger Codex-native response review gate, because Codex does not expose the same hook model as Claude Code
- Best prevention owner:
  - `response-structure-enforcer`
  - `sal-communication-contract`
  - `vibe-coding-monitor`

### 2. Agent session resume should trigger more aggressively on continuation asks

- Trigger:
  - `continue`, transcript follow-up, handoff follow-up, or resume-type prompts
- Current impact:
  - agents can continue from memory or recent chat instead of reconstructing the real stopping point first
- Current enforcement:
  - hook and startup guidance now mention `agent-session-resume`
- Still needed:
  - stronger platform parity so the same resume rule exists outside Claude-style hook surfaces
- Best prevention owner:
  - `agent-session-resume`
  - `objective-orchestration-loop`

### 3. Model routing is documented more strongly than it is automatically enforced

- Trigger:
  - non-trivial tasks that should surface model-routing guidance
- Current impact:
  - good routing policy exists, but some platforms still depend on the agent following docs honestly
- Current enforcement:
  - prompt/session/instruction guidance now points to `codex-runtime-router` and `model-registry`
- Still needed:
  - stronger platform-specific startup reminders and review checks
- Best prevention owner:
  - `codex-runtime-router`
  - `model-registry`

### 4. Markdown artifacts can still become dead-end docs

- Trigger:
  - meaningful `.md` file gets created or updated
- Current impact:
  - a document may exist without being wired into skills, workflows, registries, or mirrors
- Current enforcement:
  - new markdown governance workflow exists
- Still needed:
  - use it consistently and mirror where needed
- Best prevention owner:
  - `markdown-artifact-governance-and-closeout-loop.md`

### 5. Cross-platform skill parity still needs a deliberate audit loop

- Trigger:
  - local skill updated in Codex or Claude-facing surfaces
- Current impact:
  - mirrors can lag and platforms can drift
- Current enforcement:
  - shared registry and mirrors exist
- Still needed:
  - a regular parity audit and stronger platform-by-platform verification
- Best prevention owner:
  - `detector-registry-and-learning-promotion-loop.md`
  - shared registry docs

### 6. Linear is present in OpenCowork but currently not usable here

- Trigger:
  - project management asks that would benefit from a real issue tracker
- Current impact:
  - we fall back to markdown, GitHub, and PM files
- Current enforcement:
  - OpenCowork plugin exists on disk but is disabled and not configured for active use there
  - Codex-side Linear connector is not currently usable in this session
- Alternative in use:
  - this backlog
  - GitHub issues
  - PM registry markdown
- Best prevention owner:
  - future platform configuration pass, not current execution

## Review Rule

Read this backlog when the task is about:

- communication quality
- orchestration drift
- response shape
- session resume
- model routing
- platform parity
- project-management tooling
- workflow or skill promotion
