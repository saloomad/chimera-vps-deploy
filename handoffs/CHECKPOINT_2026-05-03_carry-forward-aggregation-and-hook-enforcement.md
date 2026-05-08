# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-03T20:55:00+03:00
- **Platform**: Windows Codex
- **Session focus**: corrected the reply carry-forward contract so open objectives, approvals, and remaining work stay aggregated across prior relevant conversations for the same project objective rather than only the current thread, while keeping automation routing capped at `gpt-5.4` `medium` or lower unless the user explicitly approves stronger

## Original Goal
Do not only require a carry-forward block in instructions. Make it stronger by requiring aggregated open items with brief descriptions, carried forward across prior relevant conversations for the same project objective rather than scoped only to the current conversation or objective thread, and enforce a default automation model ceiling of `gpt-5.4` `medium` or lower unless the user explicitly approves stronger routing.

## Completed Work
- [x] Strengthened the carry-forward rule in:
  - `C:\Users\becke\.codex\AGENTS.md`
  - `C:\Users\becke\claudecowork\AGENTS.md`
  - `C:\Users\becke\claudecowork\CLAUDE.md`
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\platforms\windows-codex\AGENTS.md`
  - `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
- [x] Upgraded the carry-forward wording so it now requires:
  - one short aggregated block
  - brief plain-English descriptions for each open item
  - continued carry-forward across side-topic drift
- [x] Updated `sal-communication-contract` and `objective-orchestration-loop` so the carry-forward block is part of the reusable answer contract, not just top-level instructions
- [x] Updated `automation-design-best-practices` so automations now default to `gpt-5.4` with reasoning `medium` or lower unless the user explicitly approves a stronger model
- [x] Updated `automation-design-best-practices` so automation prompts now require carry-forward aggregation across prior relevant conversations for the same project objective, with short descriptions
- [x] Updated `codex-runtime-router` so runtime routing now states:
  - automation and heartbeat passes stay on `gpt-5.4` `medium` or lower by default
  - stronger automation routing needs explicit user approval
  - carry-forward blocks must accumulate still-relevant open items across prior conversations for the same project objective and organize them by objective when needed
- [x] Expanded `.claude/OBJECTIVE_CONTRACT.md` guidance so future active contracts track:
  - `unapproved_items`
  - `remaining_work`
- [x] Updated local Claude Code project hooks to nudge this behavior at:
  - `UserPromptSubmit`
  - `PostToolUse`
  - `SessionStart`
  - `Stop`
- [x] Updated the live local OpenCowork enforcement plugin hooks to nudge this behavior at:
  - `UserPromptSubmit`
  - `PostToolUse`
  - `Stop`
- [x] Mirrored the same OpenCowork and Claude Code hook guidance into the shared `chimera-vps-deploy` platform bundles
- [x] Updated platform enforcement docs so this behavior is now documented as:
  - instruction + skill enforcement on Codex/OpenCode
  - hook-backed nudges on Claude Code and OpenCowork
  - instruction + runtime-owner guidance for Kimi/OpenClaw

## Not Done
- [ ] No fresh app-session proof was captured yet showing the updated OpenCowork hook text firing through the actual UI runtime after this exact patch
- [ ] No live OpenClaw runtime hook was patched yet specifically for this carry-forward block; Kimi/OpenClaw currently has stronger instruction guidance, not a newly proven runtime hook for this behavior
- [ ] No Codex-native hook surface was added because this runtime still does not have a separately proven general hook API here

## Decisions Made
- **Decision**: require aggregated open-work summaries, not just category labels | **Why**: otherwise the reply can technically satisfy the rule while still hiding the actual unfinished work
- **Decision**: use hooks where the platform already has a proven event surface, and use instructions/workflows/contract files where it does not | **Why**: honest enforcement is better than pretending every platform has the same automation model
- **Decision**: carry forward still-relevant open items across prior conversations when they belong to the same project objective, but do not pull in unrelated older work | **Why**: this preserves real project continuity without polluting the active contract with stale unrelated work
- **Decision**: keep automations on `gpt-5.4` `medium` or cheaper by default | **Why**: automations should stay cost-bounded unless the user explicitly approves a stronger lane

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `C:\Users\becke\.codex\AGENTS.md` | Windows Codex | strengthened carry-forward rule with aggregation and brief-description requirement |
| `C:\Users\becke\claudecowork\AGENTS.md` | Shared workspace | same stronger carry-forward rule |
| `C:\Users\becke\claudecowork\CLAUDE.md` | Claude-family | stronger carry-forward rule |
| `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md` | Windows Codex startup | stronger carry-forward contract |
| `C:\Users\becke\.codex\skills\sal-communication-contract\SKILL.md` | Shared reply skill | requires aggregated carry-forward block with brief descriptions |
| `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md` | Shared orchestration skill | requires carry-forward tracking for open approvals and remaining work |
| `C:\Users\becke\.codex\skills\automation-design-best-practices\SKILL.md` | Shared automation skill | defaults automations to `gpt-5.4` `medium` or lower and scopes carry-forward prompts to the current thread |
| `C:\Users\becke\.codex\skills\codex-runtime-router\SKILL.md` | Shared routing skill | caps automation routing at `gpt-5.4` `medium` or lower by default and scopes carry-forward blocks to the current thread |
| `C:\Users\becke\claudecowork\.claude\OBJECTIVE_CONTRACT.md` | Claude local | added `unapproved_items` and `remaining_work` guidance |
| `C:\Users\becke\claudecowork\.claude\hooks\*.py` | Claude local | prompt-start, post-tool, session-start, and stop nudges now mention carry-forward fields |
| `C:\Users\becke\AppData\Roaming\open-cowork\claude\plugins\runtime\chimera-enforcement-bundle\hooks\*.py` | OpenCowork local runtime | prompt-start, post-tool, and stop nudges now mention carry-forward fields |
| `C:\Users\becke\claudecowork\chimera-vps-deploy\platforms\claude-code\project-bundle\.claude\*` | Shared Claude bundle | mirrored carry-forward hook guidance |
| `C:\Users\becke\claudecowork\chimera-vps-deploy\platforms\opencowork\local-bundle\chimera-enforcement-bundle\*` | Shared OpenCowork bundle | mirrored carry-forward hook guidance |
| `C:\Users\becke\claudecowork\chimera-vps-deploy\platforms\opencode\AGENTS.md` | Shared OpenCode guidance | added carry-forward block rule for meaningful replies |
| `C:\Users\becke\claudecowork\chimera-vps-deploy\platforms\kimi-vps\AGENTS.md` | Shared Kimi guidance | added carry-forward block rule for meaningful replies |
| `C:\Users\becke\claudecowork\docs\PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md` | Docs | documented carry-forward hook usage |
| `C:\Users\becke\claudecowork\docs\ENFORCEMENT_IMPLEMENTATION_INVENTORY_2026-05-02.md` | Docs | recorded carry-forward enforcement surfaces |
| `C:\Users\becke\claudecowork\docs\PLATFORM_WORKFLOW_AND_SKILL_ENFORCEMENT_CATALOG_2026-05-02.md` | Docs | catalog now describes carry-forward duty for the starter stack |
| `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\CHECKPOINT_2026-05-03_carry-forward-aggregation-and-hook-enforcement.md` | Shared workspace | this handoff |

## Next Actions (for next agent)
1. Capture real app-session proof that the updated OpenCowork hook prompts fire through the UI runtime after this patch
2. Decide whether to add a dedicated OpenClaw runtime hook or Task Flow reminder for carry-forward blocks that aggregate still-relevant open items across prior conversations for the same project objective, or keep Kimi/OpenClaw on instruction-plus-contract enforcement for now
3. Mirror the new automation model ceiling into any other routing or automation surfaces if the user later asks for wider enforcement
