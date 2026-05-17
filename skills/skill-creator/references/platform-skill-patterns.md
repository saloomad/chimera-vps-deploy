# Cross-Platform Skill Patterns

Updated: 2026-05-05

## Official patterns that matter

### OpenAI / Codex

- OpenAI describes skills as reusable workflows that can bundle instructions, examples, and code.
- OpenAI also says the built-in `skill-creator` is the default helper when users ask ChatGPT to create or modify a skill.
- OpenAI Academy recommends small building-block skills instead of one massive workflow when possible.

### Claude Code

- Anthropic says subagent delegation depends heavily on the `description`.
- Anthropic recommends specific, action-oriented descriptions.
- Anthropic also notes that phrases like `use proactively` or `must be used` can encourage stronger auto-delegation.

### Kimi Code

- Kimi discovers skills from layered brand and generic roots.
- Brand roots can merge by priority when `merge_all_available_skills = true`.
- Kimi recommends keeping `SKILL.md` under about 500 lines and moving deeper content into `scripts/`, `references/`, or `assets/`.
- Kimi documents `/usage` as the quota surface, but it is an interactive slash-command surface rather than a normal shell subcommand.

### OpenClaw

- OpenClaw uses Agent Skills-compatible folders and explicit precedence across workspace, project-agent, personal-agent, managed, bundled, and extra roots.
- OpenClaw also separates visibility from allowlisting, so a copied skill is not automatically usable by every agent.

### OpenCowork / OpenCode

- OpenCowork ships with built-in skills and supports added custom skills.
- OpenCode-oriented ecosystems commonly use `.agents/skills`, `.claude/skills`, `.codex/skills`, or platform config roots as skill surfaces.
- Practical rule here: mirror only the platforms that actually consume the skill, and keep one source-of-truth copy.

## Local rules from this workspace

- Avoid inline `Triggers:` labels inside single-line YAML descriptions.
- Avoid control characters and mojibake in frontmatter.
- Keep descriptions short, explicit, and natural-language searchable.
- Mirror only after the source copy validates.
- Do not call a skill fixed until the host runtime loads it without the old warnings.
- Distinguish `exists`, `wired`, `used`, and `runtime-proof` in closeouts.
