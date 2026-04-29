Continue the approved objective using the mandatory `plan -> execute -> review` loop.

You are running on the Kimi VPS.

Read these first:

1. `/root/.kimi/CHIMERA_BOOTSTRAP.md`
2. `/root/.kimi/AGENTS.md`
3. `/root/openclawtrading/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md`
4. `/root/openclawtrading/harnesses/codex/chimera/CONTINUATION.md`
5. `/root/openclawtrading/harnesses/codex/chimera/KANBAN.md`
6. `/root/openclawtrading/harnesses/codex/chimera/WORK_LOG.md`
7. `/root/openclawtrading/tasks/TASK_REGISTRY.md`
8. `/root/openclawtrading/trace/ACTION_LOG.md`

Rules:

- Start with `Runtime: model=<name> | reasoning=<effort> | quota=<value-or-not-exposed> | phase=<plan|execute|review|mixed> | why=<short reason>`.
- Respect the heartbeat control file. If its status is not `active`, stop cleanly.
- Restate the objective and done criteria from the control file.
- Run a short plan pass.
- Do the next bounded safe execution step only.
- Run review and decide `complete`, `iterate`, or `blocked`.
- If meaningful progress happened, update:
  - `/root/openclawtrading/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md`
  - `/root/openclawtrading/harnesses/codex/chimera/CONTINUATION.md`
  - `/root/openclawtrading/harnesses/codex/chimera/WORK_LOG.md`
  - `/root/openclawtrading/tasks/TASK_REGISTRY.md`
  - `/root/openclawtrading/trace/ACTION_LOG.md`
- If review says the objective is complete, set `status: complete` in the heartbeat control file.
- If review says the objective is blocked, set `status: blocked` in the heartbeat control file and explain the blocker.
- If the result quality is weak, raise reasoning first, then split phases more cleanly, then escalate the model.
- Never stop at partial progress unless review says `blocked` or a new approval boundary appears.

End with a compact review closeout:

- objective
- execution step performed
- review outcome
- result quality
- next step
