## Objective

Repair the live OpenClaw `main` agent stuck-session / gateway-timeout behavior on the Kimi VPS and prove what is actually fixed versus what still needs hardening.

## What was wrong

1. The live gateway defaults were `MiniMax-M2.7-highspeed`, but the `main` agent itself was still pinned to `kimi-coding/k2.6`.
2. Manual local tests were hitting the wrong front door:
   - `openclaw agent --agent main ...`
   - with no `--channel`, OpenClaw uses the `main` session channel
   - on this VPS, that means the Kimi IM session lane, not a clean isolated local run
3. Old rogue `openclaw` / `openclaw-agent` processes from May 2 were still alive outside systemd and polluting runtime truth.
4. Cold-start requests can still hit a handshake timeout while the gateway is starting channels, browser control, and the TradingView Jackson MCP adapter.
5. After handshake fallback, the embedded lane can still time out when the run uses heavier defaults with truncated `USER.md` and `MEMORY.md` in prompt context.

## What was fixed live

### 1. Main agent routing/model mismatch fixed

Patched live `/root/.openclaw/openclaw.json`:

- `agents.list.main.model.primary`
  - from: `kimi-coding/k2.6`
  - to: `minimax/MiniMax-M2.7-highspeed`
- `agents.list.main.model.fallbacks`
  - to: `["kimi-coding/k2.6", "kimi-coding/k2.5"]`

Backup created:

- `/root/.openclaw/openclaw.json.bak-20260505-main-model-fix`

### 1b. Live main agent switched back to Kimi on request

Later live change on May 5:

- `agents.list.main.model.primary`
  - from: `minimax/MiniMax-M2.7-highspeed`
  - to: `kimi-coding/k2.6`
- `agents.list.main.model.fallbacks`
  - to: `["minimax/MiniMax-M2.7-highspeed", "kimi-coding/k2.5"]`

Additional backup created:

- `/root/.openclaw/openclaw.json.bak-20260505-main-kimi-request`

### 2. Gateway restarted cleanly under systemd

Real live owner remained:

- `/root/.config/systemd/user/openclaw-gateway.service`

Post-fix live PID:

- `552162`

### 3. Orphan rogue processes removed

Killed and cleared:

- old `openclaw` pid `272561`
- old `openclaw-agent` pid `272575`

After cleanup, only the systemd-managed gateway remained active.

## Live proof

### Proof that the old routing problem was real

Before the fix, logs repeatedly showed:

- `Thinking level "high" is not supported for kimi-coding/k2.6`
- `stuck session: sessionKey=agent:main:main`
- gateway websocket connect failures while local tests were really falling into the Kimi main-session lane

### Proof that the corrected low-latency path now works

Successful live command:

```text
openclaw agent --agent main --channel discord --session-id main-lowlatency-proof-20260505 --thinking off --timeout 180 --json --message 'Reply with exactly OK.'
```

Successful result:

- status: `ok`
- payload text: `OK`
- provider: `minimax`
- model: `MiniMax-M2.7-highspeed`
- duration: about `37.7s`

Artifacts:

- `/root/.openclaw/agents/main/sessions/main-lowlatency-proof-20260505.jsonl`
- `/root/.openclaw/agents/main/sessions/main-lowlatency-proof-20260505.trajectory.jsonl`

### Proof after the Kimi-first switch

Current live config truth:

- `main` is now Kimi-first again
- fallback is now MiniMax

Important nuance:

- immediate post-restart Kimi proofs were polluted by the same cold-start problem as before
- if the proof fires before the gateway is fully `ready`, the CLI can still report gateway connect timeout or gateway closed during warm-up

After the gateway reached `ready`, the live gateway log showed successful agent responses:

- `2026-05-05T07:36:28` `ws res agent 4561ms`
- `2026-05-05T07:36:31` `ws res agent 3686ms`

So the live runtime did process agent runs successfully after the Kimi-first switch, but the wrapper-style proof command remains noisy if it is launched too early or without a carefully bounded profile.

## What is still not fully hardened

1. A cold `main` request can still hit websocket handshake timeout while the gateway is spinning up:
   - Kimi channel startup
   - browser control
   - TradingView Jackson MCP adapter registration
2. The TradingView Jackson adapter is still slow/noisy during warm-up and can fail to start within `30000ms`.
3. Heavier embedded failover runs can still timeout with the current prompt surface because `USER.md` and `MEMORY.md` are both large and truncated into context.
4. `openclaw agent --agent main ...` without a deliberate run profile is still a bad proof command for this VPS because it defaults to the main session channel semantics, not a clean bounded local health-check style run.
5. Even with Kimi restored as the `main` primary model, cold-start timing is still the main source of false failure signals. The model order is no longer the whole story.

## Root cause that actually mattered

The biggest practical root cause was not only model order. It was the timeout stack.

What the live evidence showed:

- warm Kimi `main` runs could succeed, but they often took much longer than the old timeout stack allowed
- the CLI or fallback path would often give up early even when the session file later showed a successful reply
- the prompt surface for even a trivial `OK` run is very large because the runtime injects:
  - `AGENTS.md`
  - `SOUL.md`
  - `TOOLS.md`
  - `IDENTITY.md`
  - truncated `USER.md`
  - truncated `MEMORY.md`
  - loaded skill summaries

That means Kimi was being judged too early for this runtime shape.

## Durable live fix

Patched live `/root/.openclaw/openclaw.json` again:

- `agents.defaults.timeoutSeconds = 180`
- `models.providers.kimi-coding.timeoutSeconds = 180`
- `models.providers.minimax.timeoutSeconds = 180`

Backup created:

- `/root/.openclaw/openclaw.json.bak-20260505-timeout-tune`

## Proof that the timeout fix worked

Successful live command after the timeout tune:

```text
openclaw agent --agent main --session-id main-kimi-timeout-tuned-20260505 --thinking off --json --message 'Reply with exactly OK.'
```

Successful result:

- status: `ok`
- payload text: `OK`
- provider: `kimi-coding`
- model: `k2.6`
- duration: about `103.3s`

Artifacts:

- `/root/.openclaw/agents/main/sessions/main-kimi-timeout-tuned-20260505.jsonl`
- `/root/.openclaw/agents/main/sessions/main-kimi-timeout-tuned-20260505.trajectory.jsonl`

## Updated status

The `main` Kimi-first lane is now working again with proof.

What remains is optimization, not the original blocker:

1. first-turn gateway warm-up is still heavier than it should be
2. Kimi subscribe ping reconnect noise still exists
3. the injected bootstrap surface is still oversized for tiny requests

## Recommended next slice

1. Add one durable local proof wrapper for bounded health checks that always uses:
   - explicit non-Kimi reply lane
   - `thinking off`
   - longer timeout
2. Decide whether TradingView Jackson should be deferred or warmed separately so it does not slow first-turn gateway handshakes.
3. Reduce or re-point the injected bootstrap surfaces for `USER.md` / `MEMORY.md` if faster default `main` runs are now more important than broad continuity in every turn.

## 2026-05-05 follow-up hardening pass

### Council conclusion

Three live-risk reviews were compared:

- prompt trimming:
  - lowest-risk prompt idea was to reduce only oversized bootstrap payload, not rewrite instructions
- cold-start startup:
  - biggest user-facing pain is still first-touch startup before the gateway can really accept the run
- session-state hygiene:
  - stale or broken `agent:main:main` state can poison later runs even when the gateway itself is up

The prompt-budget tweak was tested first and rejected as the chosen fix for this slice because it did not address the front-door failure mode directly.

### Reverted unproven bootstrap tweak

I briefly added:

- `agents.defaults.bootstrapMaxChars = 10000`
- `agents.defaults.bootstrapTotalMaxChars = 60000`

That was reverted in the same pass because the CLI never reached a clean embedded run where the new cap could even be exercised, so it was not the right first lever and was not left behind as an unproven global behavior change.

### New root-cause evidence

The stronger live finding was session-state corruption:

- `/root/.openclaw/agents/main/sessions/sessions.json` still had an `agent:main:main` entry
- that entry pointed to:
  - `/root/.openclaw/agents/main/sessions/80268552-74dd-4c29-b51a-f78847598929.jsonl`
- that transcript file did not exist

So the main direct-session registry was carrying a broken pointer. That matches the gateway repeatedly logging:

- `stuck session: sessionKey=agent:main:main`
- long `sessions.json.lock` holds

### Live fix applied

Backups created:

- `/root/.openclaw/agents/main/sessions/sessions.json.bak-20260505-stale-main-session`
- archived broken entry:
  - `/root/.openclaw/agents/main/sessions/agent-main-main-entry-20260505.json`

Live mutation:

- removed only the broken `agent:main:main` entry from `sessions.json`
- left other explicit and subagent session records intact

Then restarted the gateway.

### Verification result

After restart:

- `sessions.json` no longer contains `agent:main:main`
- the reverted bootstrap-cap keys are no longer present in `/root/.openclaw/openclaw.json`

What is still not fully proven:

- a clean fresh `openclaw agent --agent main ...` proof still gets trapped in the heavy cold-start lane before writing a new explicit session file
- the gateway still spends a long time on:
  - Kimi subscribe lifecycle
  - Discord reconnect churn
  - TradingView Jackson startup and registration

### Updated next owner slice

The next honest hardening target is no longer prompt budget first.

It is:

1. keep the broken-session-entry cleanup
2. prove whether the stale `agent:main:main` poison is gone on the next clean human-triggered run
3. then harden the real remaining blocker:
   - first-touch channel/bootstrap readiness
   - Kimi subscribe reconnect instability
   - TradingView Jackson startup on the critical path

## 2026-05-06 startup and routing pass

### Plain-English finding

TradingView Jackson was not merely "available as a tool."

It had been wired through the `openclaw-mcp-adapter` plugin, which means the gateway was trying to connect to it during startup and register its tool catalog before the system was really ready.

That is why TradingView kept showing up in startup even though the desired operating model is "call it when needed."

### Live changes applied

1. TradingView startup decoupling

- removed `openclaw-mcp-adapter` from `plugins.allow`
- set `plugins.entries.openclaw-mcp-adapter.enabled = false`
- kept top-level `mcp.servers.tradingview-jackson` in place so TradingView still exists as a configured MCP server instead of being deleted outright

Backup:

- `/root/.openclaw/openclaw.json.bak-20260506-deezoh-routing-tv-startup`

2. User-facing Deezoh ownership route

Changed the live Discord `main` route binding from:

- `agentId = main`

to:

- `agentId = deezoh`

Meaning:

- incoming Discord `main` traffic now routes to Deezoh
- this is the safe user-facing ownership change
- it does **not** delete or rename the internal `main` agent entry used by the platform itself

3. Gateway service timing

Patched the user systemd unit:

- `OPENCLAW_HANDSHAKE_TIMEOUT_MS=30000`
- `TimeoutStartSec=120`
- `TimeoutStopSec=90`

Backup:

- `/root/.config/systemd/user/openclaw-gateway.service.bak-20260505-handshake`

4. Local CLI gateway-call timeout

The standalone `openclaw` CLI had a separate hardcoded gateway call timeout of `10000ms`, so local admin commands could still fail even after the service-side handshake was relaxed.

Patched:

- `/usr/lib/node_modules/openclaw/dist/call-CP7A3sdw.js`
  - default gateway call timeout:
    - from `1e4`
    - to `3e4`

Backup:

- `/usr/lib/node_modules/openclaw/dist/call-CP7A3sdw.js.bak-20260506-gateway-timeout`

### Verification

Verified config truth:

- `bindings[].agentId` for Discord `main` is now `deezoh`
- `plugins.allow` no longer includes `openclaw-mcp-adapter`
- `plugins.entries.openclaw-mcp-adapter.enabled = false`
- `mcp.servers.tradingview-jackson` still exists

Verified runtime evidence:

- fresh logs after the new restart no longer show the gateway actively starting TradingView through `mcp-adapter`
- instead, the restart summary reports:
  - `plugins.entries.openclaw-mcp-adapter: plugin disabled`

### What remains open

The startup bottleneck is reduced but not finished.

The remaining heavy surfaces now look more like:

- Kimi subscribe / IM bridge instability
- Discord reconnect churn
- very slow general gateway bootstrap before HTTP becomes responsive

Even after the CLI timeout was raised to `30000ms`, `openclaw health --json` still timed out in the current cold state. That means the next blocker is no longer TradingView startup on the mandatory path; it is broader gateway/bootstrap latency and Kimi/Discord readiness.
