# Model Routing Spec

Updated: 2026-04-28
Purpose: one compact routing sheet for Windows Codex, Windows Claude, Kimi VPS, and shared GitHub handoffs.

## Core Rule

Use benchmarks and pricing as routing hints, not as absolute truth.

- real task shape beats leaderboard vanity
- official docs beat memory
- if quota is not exposed, say that plainly
- if the result quality is weak, rerun on a stronger lane and record that lesson

## Windows Codex Runtime

Current verified default on this machine:

- model: `gpt-5.4`
- reasoning: `medium`

Verified CLI truth:

- `codex login status` works
- verified quota command: not found yet
- response header quota value: `not exposed`

Spawned-agent model options exposed by this runtime:

- `gpt-5.5`
- `gpt-5.4`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5.3-codex-spark`
- `gpt-5.2`

## Model Table

### OpenAI runtime models

| Model | Best use | Reasoning | Context | Approx API price / 1M input | Approx API price / 1M output | Benchmark signals |
|---|---|---|---|---|---|---|
| `gpt-5.5` | hard planning, architecture, review | `none` to `xhigh` | 1M | $5.00 | $30.00 | Terminal-Bench 2.0 `82.7`, SWE-Bench Pro `58.6`, GPQA Diamond `93.6`, HLE w/ tools `52.2` |
| `gpt-5.4` | strong default implementation | `none` to `xhigh` | 1.05M | $2.50 | $15.00 | GPT-5.4 official docs + Kimi comparison: Terminal-Bench 2.0 `65.4`, SWE-Bench Pro `57.7`, HLE w/ tools `52.1`, GPQA Diamond `92.8` |
| `gpt-5.4-mini` | cheaper mechanical work | `none` to `xhigh` | 400K | $0.75 | $4.50 | use when task is low-judgment and cost-sensitive |
| `gpt-5.3-codex` | coding-focused fallback | runtime-dependent | 400K | $1.75 | $14.00 | coding-oriented route when explicit override helps |
| `gpt-5.3-codex-spark` | ultra-fast coding fallback | runtime-dependent | runtime-dependent | runtime-dependent | runtime-dependent | use only when speed matters more than depth |
| `gpt-5.2` | lower-cost strong fallback | `low` to `xhigh` | runtime-dependent | $1.75 | $14.00 | useful when price matters more than frontier performance |

### VPS models

| Model | Platform | Best use | Thinking support | Context | Approx price / 1M input | Approx price / 1M output | Benchmark signals |
|---|---|---|---|---|---|---|---|
| `MiniMax-M2.7-highspeed` | Kimi VPS / OpenClaw | default live agent work, fast code, lower cost | provider-specific | 200K | $0.60 | $2.40 | vendor says same performance as M2.7 with faster inference |
| `MiniMax-M2.5` | Kimi VPS / OpenClaw | cheaper fallback | provider-specific | 200K | $0.30 | $1.20 | lower-cost fallback lane |
| `k2.6` | Kimi VPS / OpenClaw | hard coding, deep research, review reruns | thinking mode supported | 256K | about $0.95 cache-miss input | about $4.00 | HLE w/ tools `54.0`, DeepSearchQA acc `83.0`, Terminal-Bench 2.0 `66.7`, SWE-Bench Pro `58.6` |
| `k2.5` | Kimi VPS / OpenClaw | fallback reasoning and coding | thinking mode supported | 256K | about $0.58 to $0.60 input equivalent | about $3.00 to $3.10 output equivalent | older but still strong fallback |

## Routing By Task Type

| Task type | Preferred lane | Preferred model | Preferred reasoning |
|---|---|---|---|
| architecture or planning | planning | `gpt-5.5` | `high` or `xhigh` |
| coding implementation | execution | `gpt-5.4` | `medium` |
| code review or failure analysis | review | `gpt-5.5` or `gpt-5.4` | `high` or `medium` |
| repetitive formatting | fast mechanical | `gpt-5.4-mini` | `low` |
| live VPS execution | execution | `MiniMax-M2.7-highspeed` | provider default |
| live VPS deep coding or rerun | review or planning | `k2.6` | thinking on |

## Escalation Ladder

1. raise reasoning effort
2. split planning from execution
3. rerun review on a stronger model
4. record what route would be better next time

## Proof Pattern

To prove the routing worked, close out with:

- task type
- chosen platform
- chosen model
- chosen reasoning level
- why this lane was selected
- whether a rerun was needed
- result quality

## Sources

- OpenAI GPT-5.5: https://openai.com/index/introducing-gpt-5-5/
- OpenAI GPT-5.4 docs: https://developers.openai.com/api/docs/models/gpt-5.4/
- OpenAI pricing: https://platform.openai.com/docs/pricing/
- MiniMax pricing: https://platform.minimax.io/docs/guides/pricing-paygo
- MiniMax models intro: https://platform.minimax.io/docs/guides/models-intro
- Kimi K2.6 benchmark blog: https://www.kimi.com/blog/kimi-k2-6
- Kimi K2.6 API quickstart: https://platform.kimi.com/docs/guide/kimi-k2-6-quickstart
- Kimi K2.6 pricing: https://www.kimi.com/resources/kimi-k2-6-pricing
