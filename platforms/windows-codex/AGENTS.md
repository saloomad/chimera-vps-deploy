## INFRASTRUCTURE UPDATE — 2026-04-28

The old Linux PC (192.168.1.203, /home/open-claw/) has been replaced by the Kimi VPS.

- New Tailscale IP: 100.67.172.114
- New SSH: ssh root@100.67.172.114
- New home dir: /root/ (not /home/open-claw/)
- New workspace: /root/openclawtrading/
- Models: MiniMax M2.7-highspeed (primary), Kimi K2.6 (fallback)
- Read CHIMERA_BOOTSTRAP.md first for the full startup picture
- Read codex-runtime-router for platform, model, sync, and response-header rules
- Read VPS_CONNECTION.md for full details
- Read model-registry skill before answering model questions

When SSHing to the trading system, ALWAYS use root@100.67.172.114, NEVER open-claw@192.168.1.203.
When referencing paths, ALWAYS use /root/..., NEVER /home/open-claw/....

---

## HANDOFF PROTOCOL — Read Before Starting Work

Before doing ANY work, check for pending handoffs from other agents:

0. Read: C:/Users/becke/.codex/CHIMERA_BOOTSTRAP.md
1. Read: `codex-runtime-router`
2. Read: chimera-vps-deploy/handoffs/CHECKPOINT_*.md (latest first)
3. If a handoff exists: continue from the first unfinished action
4. If no handoff: proceed normally
5. At session end: create a new handoff using CHECKPOINT_TEMPLATE.md

## RESPONSE HEADER

At the beginning of every user-facing reply, include:

`Runtime: model=<name> | reasoning=<effort> | quota=<value-or-not-exposed> | phase=<plan|execute|review|mixed> | why=<short reason>`

If live quota is not exposed in the runtime, say `quota=not exposed`.
Do not invent quota numbers.
Try Codex CLI first for usage or quota, but if no verified quota command exists, keep the honest `not exposed` value.

## MODEL ROUTING DEFAULT

Before non-trivial work:

1. classify the work as planning, execution, review, research, or mixed
2. use `codex-runtime-router`
3. use `model-registry` if model choice, pricing, context, or benchmark claims matter

Preferred lanes:

- Planning: `gpt-5.5` with `high` or `xhigh`
- Execution: `gpt-5.4` with `medium`
- Review: `gpt-5.5` with `high` when judgment-heavy, otherwise `gpt-5.4` with `medium`
- Fast mechanical: `gpt-5.4-mini` with `low`

Important:

- spawned agents inherit the parent model by default unless there is a clear bounded reason to override
- do not pretend the runtime secretly auto-switched models unless that was verified
- if a result is weak, reroute to a stronger reasoning level or stronger model and say so plainly

Platforms in this ecosystem:
- Windows Claude (this session) — C:/Users/becke/claudecowork/
- Windows Codex — C:/Users/becke/.codex/
- VPS OpenClaw — 100.67.172.114 via Tailscale SSH
- space-agent.ai — web-based agent

How to create a handoff:
  cd chimera-vps-deploy/handoffs/
  cp CHECKPOINT_TEMPLATE.md CHECKPOINT_2026-04-28_claude.md
  Fill it out, then: git add . && git commit -m '[Windows] Session handoff' && git push

---

