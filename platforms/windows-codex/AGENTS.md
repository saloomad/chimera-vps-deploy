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

## OBJECTIVE LOOP

For every non-trivial objective, use:

`plan -> execute -> review -> repeat`

Before each meaningful reply, also run the orchestration precheck and say:

- whether the full loop is needed
- which orchestration class fits
- why that route fits
- what the done contract is

Rules:

- plan defines the `ultimate objective`, the current bounded slice, done criteria, platform, and route
- execute does the next bounded real step
- review decides `complete`, `iterate`, or `blocked`
- only use `complete` when the real user objective is done
- if a slice finished but the broader mission is still open, the correct outcome is `iterate`
- do not stop at partial progress unless review says blocked or approval is needed

## KNOWLEDGE WIKI RULE

Use the shared Chimera knowledge wiki at:

- `C:\Users\becke\claudecowork\research\chimera-knowledge-wiki`

Read it early when the task involves:

- prior research
- building or implementation patterns
- skills or workflow design
- architecture decisions
- contradictions across docs or notes

Update it before closeout when the task creates durable knowledge in those areas.

Do not use it as primary truth for live runtime state.

## DEFAULT STARTER STACK FOR SOFTWARE WORK

For meaningful build, fix, refactor, test, finish, shipping, workflow, or project-organization work, start with:

1. `prompt-upgrade-engineer`
2. `sal-communication-contract`
3. `vibe-coding-operator`
4. `objective-orchestration-loop`

If friction, weak explanation, missed skill activation, or orchestration drift appears, also use:

5. `vibe-coding-monitor`

If architecture or system-wide tradeoffs exist, also use:

6. `major-build-council-orchestrator`

Treat this as the normal path unless the request is truly tiny.

## COMMUNICATION CONTRACT FOR SAL

For meaningful replies, also use `sal-communication-contract`.

That means the answer should usually make these things clear:

- what we are working on
- brief context
- what has been done
- what is being done now
- what is left
- what the proof artifacts mean in plain English
- the bottom line
- what happens next

Do not dump commit ids, branch names, workflow names, or filenames without explaining what they mean.

## CODEX THREAD HEARTBEAT ENFORCEMENT

When a non-trivial objective in Codex will need more than one pass:

1. create or update a thread heartbeat named `Thread Objective Completion Guard`
2. use the heartbeat only for the current thread
3. choose the cadence from the expected duration of one meaningful pass instead of using one fixed default
4. for passes around `1` to `3` minutes, prefer a `5` minute wake
5. for passes around `3` to `8` minutes, prefer a `10` minute wake
6. for passes around `8` to `15` minutes, prefer a `15` minute wake
7. use `30` minutes only when the next pass is truly long-running or mostly waiting on something external
8. keep it cheap first and concise
9. stop it only when the `ultimate objective` is `complete`
10. stop it when the objective is `blocked`
11. stop it after `3` consecutive wakes with no meaningful visible progress
12. after that stop, require fresh manual input from Sal before any further attempts

Important:

- a Codex heartbeat is thread-attached, so one heartbeat cannot automatically cover all future threads
- the enforced rule is therefore: if orchestration starts in a new Codex thread and continuation is needed, create or update the guarded heartbeat for that thread too
- do not let a Codex thread heartbeat run forever
- if the estimated pass length changes, update the heartbeat instead of keeping a stale cadence

## ORCHESTRATION AUTO-TRIGGER RULE

Treat the following kinds of user wording as an explicit instruction to use `objective-orchestration-loop` without waiting for the user to name the skill:

- `continue until complete`
- `continue until done`
- `keep going`
- `until the objective is achieved`
- `until the contract is achieved`
- `do not stop`
- `stay on this`
- `use orchestration`
- `keep checking`
- `follow through`

When these cues appear:

1. classify the work into the orchestration classes in `objective-orchestration-loop`
2. if more than one pass is likely, create or update the current-thread heartbeat
3. choose cadence from expected pass duration, not habit
4. keep using `plan -> execute -> review -> repeat` until review says the `ultimate objective` is `complete` or `blocked`
5. if a mini-goal or slice lands but the real objective remains open, record `iterate` and continue

Cadence guardrails:

- for a `direct task`, do not create a heartbeat just to follow habit
- for a `deep research swarm`, prefer `15` to `30` minutes based on real synthesis and verification pass length
- for an `always-on pipeline`, prefer the platform-native scheduler or loop instead of a Codex thread heartbeat when possible

## ORCHESTRATION IMPROVEMENT RULE

If orchestration itself fails, drifts, or misses an obvious continuation cue:

1. capture the issue durably with `issue`, `symptom`, `root_cause`, `missed_trigger_or_wrong_rule`, `impact`, `proof`, `owner`, `next_fix`, and `prevention_change`
2. fix safe bounded instruction or skill gaps in the same pass when possible
3. route larger fixes to the right owner:
   - `architect` for delivery, continuity, heartbeat policy, or automation shape
   - `architect-codex` for Codex instruction drift, orchestration mechanics, or skill gaps
   - `orchestrator` for current-task decomposition or review failure
   - `worker` for a bounded implementation slice that failed inside an otherwise-correct route
4. store the issue in `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\ORCHESTRATION_ISSUES.md` when that shared surface is available, and also mention it in the active `CHECKPOINT_*.md` when it matters to the current run
5. leave proof that the prevention rule was added so the same miss is less likely next time

Quick proof chain:

- trigger observed
- class chosen
- heartbeat created or updated when needed
- review outcome recorded
- heartbeat stopped or issue filed

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

