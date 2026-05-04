# Platform Enforcement Selection And Receipt Loop

Use this workflow when the task is not only "build the thing" but also "make sure the right enforcement surface is chosen and prove it fired."

## Trigger

Use this workflow when:

- a new workflow, skill, hook, command, wrapper, Task Flow, or Lobster path is being added
- the user asks how a platform should enforce behavior
- the user asks what should auto-trigger on different platforms
- we need proof of what actually fired instead of only saying a file exists

## Inputs

- the user objective
- target platform or platforms
- current instruction surfaces
- current hook, workflow, skill, or pipeline surfaces
- official docs when platform behavior is current or uncertain

## Steps

1. classify the change
   - hook
   - workflow
   - skill
   - command
   - permission rule
   - scheduler
   - Task Flow
   - Lobster
   - standing order
2. choose the lightest surface that can honestly enforce it
3. decide whether the platform is:
   - native-hook capable
   - command or rule capable
   - workflow only
   - guidance only
4. implement the surface
5. add or update an activation receipt path
6. verify:
   - exists
   - wired
   - used
   - auto-triggered
7. update:
   - workflow catalog
   - enforcement inventory
   - relevant skills
   - platform docs or startup docs
8. review outcome:
   - complete
   - iterate
   - blocked

## Platform Choice Rule

- Claude Code:
  - prefer native hooks for prompt start, risky tools, proof nudges, failure repair, subagent review, and stop gates
- OpenClaw:
  - prefer hooks for event reactions, Task Flow for durable pipeline state, Lobster for bounded deterministic subflows, standing orders for recurring authority, and schedulers only for wake-up
- OpenCode:
  - prefer rules, agents, commands, skills, permissions, and file-backed plans
  - do not pretend a native hook surface is proven if it is not
- OpenCowork:
  - prefer local skills and local plugins
  - if local hooks are available through a plugin, use them for prompt and stop guardrails
- Hermes:
  - prefer runtime bridge scripts, shared instructions, and scheduler-backed proof captures until a stronger native surface is proven

## Output

Leave behind:

- the implemented enforcement surface
- the activation receipt path
- the updated inventory and catalog entries
- a plain-English summary of what now fires automatically versus what still depends on instructions
