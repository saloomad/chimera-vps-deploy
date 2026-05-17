---
name: chimera-research-bundle-section-upgrader
description: Upgrade a Chimera research-bundle section into a decision-grade, source-proven contract using live examples, trader review, and simulation routing. Use when improving Deezoh decision usefulness, section fields, owning agents, or section-level proof.
---

# Chimera Research Bundle Section Upgrader

> **READ THIS FIRST** before changing any bundle section, owning agent, or section example.
> **Platform**: Windows Codex primary | shared mirror and VPS sync required when the result is durable.

## What This Skill Is For

Use this skill when the job is to make one Chimera bundle section more useful for Deezoh and the final decision flow.

This skill is for:

- missing section fields
- weak trader interpretation
- weak Deezoh usefulness
- source-owner ambiguity
- chart confirmation boundaries
- bad or incomplete section examples
- section-specific replay or simulation improvement

This skill is **not** only for rewriting prose.
It must produce:

- better section fields
- better owning-agent instructions
- a clearer source contract
- a worked example
- proof of what improved

## Read First

1. `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
2. `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md`
3. `C:\Users\becke\.codex\skills\pipeline-simulation-lab\SKILL.md`
4. `C:\Users\becke\.codex\skills\strategy-backtest-lab\SKILL.md`
5. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
6. the owning agent folder for the target section
7. the newest section source matrix, capability audit, or worked example for that section
8. the newest shared `CHECKPOINT_*.md` when this work continues a previous pass

## Default Workflow

Follow this exact loop:

1. define the exact Deezoh decision questions the section must answer
2. define what does **not** belong in the section
3. prove the real source-owner order by field family
   - list primary owners
   - list cross-check-only sources
   - list obvious sources that are not actually wired today
4. produce or refresh one honest live or replay example
5. run trader/expert review on that example
6. upgrade the bundle template
7. upgrade the owning agent instructions
8. refresh the source matrix or capability audit
9. decide which next proof lane is needed:
   - `pipeline-simulation-lab` when testing Deezoh, workflow, or agent behavior
   - `strategy-backtest-lab` when testing edge or strategy logic
10. sync durable files to shared mirror and live VPS surfaces when the section contract changed

## Mandatory Questions

For every section upgrade, answer:

- what decisions should Deezoh be able to make from this section alone?
- what fields are still too descriptive and not actionable?
- which source owns each field?
- which sources are cross-check only?
- which obvious sources are not actually wired, even if people keep mentioning them?
- when is chart confirmation mandatory?
- what signals are active now versus only historical?
- what example proves the new section is actually more useful?
- are the persistent context files current, and are they refreshed independently or only by manual repair?
- if you mention files in the answer, did you explain in plain English what each file actually is?

## Required Outputs

You must leave:

- template diff proof
- owning-agent diff proof
- source-owner proof
- source-registry proof
- one worked section example
- one plain-English Deezoh read
- one persistent-context freshness audit when the section depends on spawned-agent context
- plain-English explanation of each key artifact when citing files in the answer
- one checkpoint when the contract changed materially

## File Targets

Always consider these targets:

- bundle template:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- owning agent:
  - `C:\Users\becke\claudecowork\agents\<section-owner>\AGENTS.md`
  - `C:\Users\becke\claudecowork\agents\<section-owner>\TOOLS.md` when source rules changed
- source matrix or capability note:
  - `C:\Users\becke\claudecowork\research\platforms\YYYY-MM-DD-<section>-source-matrix.md`
  - or `...capability-audit.md`
- worked example:
  - `C:\Users\becke\claudecowork\research\platforms\YYYY-MM-DD-<symbol>-<section>-deezoh-example.md`
- shared checkpoint:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\CHECKPOINT_*.md`

If the change is durable, also mirror the updated section contract to:

- `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\`
- `/root/openclawtrading/skills`
- `/root/.openclaw/kimi-skills`
- `/root/.openclaw/workspace/agents/<section-owner>/`

## Decision Gates

Do not accept the section as “good enough” unless all are true:

- the section answers a real Deezoh decision question
- fields are not vague labels without interpretation
- lower timeframe vs higher timeframe ownership is explicit
- active vs historical divergence is separated
- chart confirmation rules are explicit
- the final write-up says which real data sources were used and which were not
- the persistent context bundle status is explicit when spawned agents rely on it
- example output includes:
  - verdict
  - why not long
  - why not short
  - what to wait for
  - what invalidates the bias

## Routing Rule

Use:

- `pipeline-simulation-lab` when the question is:
  - would Deezoh ask the right follow-up?
  - would the pipeline make the right wait/long/short decision?
  - did instructions improve decision quality?

- `strategy-backtest-lab` when the question is:
  - does this indicator or setup logic have edge?
  - did the strategy change improve performance?

Do not blur those together.

## Proof Contract

The final proof set should include:

1. field-diff proof
2. source-owner proof
3. one filled example
4. one decision-quality proof
5. divergence proof if divergence is part of the section
6. chart-confirmation proof when chart confirmation was required

## Closeout Shape

Always close with:

- what changed
- why it makes Deezoh better
- what is still unproven
- which next proof lane should run next

---
*chimera-research-bundle-section-upgrader v1.0 | 2026-05-05 | Platform: Codex*
