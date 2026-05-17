# Chimera Pipeline Observability Template

Use this report to audit the whole trading research and lifecycle pipeline.

This is not a trading signal by itself. It is the monitor that explains what
happened, what data was used, which agent or script produced it, what Deezoh
currently believes, and what should happen next.

## Required Outputs

Machine report:

- `reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.json`

Operator report:

- `reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.md`

Deezoh round-state document:

- `reports/auto/DEEZOH_PIPELINE_ROUND_STATE.json`

## Core Questions

Every observability cycle must answer:

- what phase is the desk in now?
- which document owns this phase?
- what symbol and direction are in focus?
- what data sources were read?
- which data sources are fresh, aging, stale, or missing?
- which agents or scripts contributed?
- what did Deezoh decide this round?
- why did it progress, wait, reject, or stay flat?
- what is Deezoh waiting for?
- what one question would most improve the next decision?
- where will new information be written?
- what learning or memory pattern should carry forward?
- what issue should be fixed before the next cycle?

## Data Source Inventory

Each source row should include:

- `name`
- `owner`
- `category`
- `critical`
- `path`
- `exists`
- `status`
- `age_minutes`
- `modified_at`
- `summary`
- `key_fields`

Status meanings:

- `fresh`: usable for this round
- `aging`: usable with caution and should be checked if it can change the decision
- `stale`: should not be trusted for a phase promotion
- `missing`: report contract is not satisfied

## Deezoh Round-State Fields

The Deezoh round-state document should include:

- `current_phase`
- `primary_document`
- `focus_symbol`
- `focus_direction`
- `bias_now`
- `current_strategy`
- `watchlists`
- `needed_info`
- `where_new_info_gets_added`
- `agent_capability_map`
- `learning_and_review`

## Phase Decision Rule

Every round Deezoh must ask:

- should I pass this symbol to the next phase?
- should I wait?
- should I reject or thesis-stop it?
- what exact evidence would change that?

The answer belongs in:

- the current phase packet
- `CHIMERA_LIFECYCLE_CONTEXT.json`
- `SYMBOL_LIFECYCLE_STATE.json`
- `DEEZOH_PIPELINE_ROUND_STATE.json`

## Agent Interaction Rule

Every meaningful round should be traceable through:

- `DEEZOH_ROUND_DISPATCH.json`
- `DESK_INTERACTION_BUS.json`
- `DEEZOH_SLEEP_STATE.json`
- `ORCHESTRATOR_ACTIVITY.json`
- the target agent's own report

If a cycle did not ask agents, the observability report must say whether the
cycle was deterministic-only and why that was acceptable.

## Learning Rule

When a trade closes or thesis dies before entry, write the result into:

- `TRADE_CLOSEOUT_PACKET_latest.json` or `THESIS_STOP_REVIEW_PACKET_latest.json`
- `LIFECYCLE_LEARNING_QUEUE.json`
- `DEEZOH_THOUGHTS.json`
- `DEEZOH_PIPELINE_ROUND_STATE.json`

Then ask:

- what did we learn?
- what should Deezoh not repeat?
- which owner, source order, template, or workflow should change?
- should this become a memory pattern?

## Diagram

```text
source scripts and APIs
  -> source reports
  -> screener packet
  -> Deezoh screener decision
  -> research bundle
  -> Deezoh round state
  -> entry watch / active trade / closeout packets
  -> learning queue and memory patterns
  -> pipeline observability report
  -> review/debug and next improvement
```

## Acceptance Criteria

The observability pass is good only if it can show:

- source freshness
- agent interaction trace
- Deezoh's current bias and wait reason
- next best question
- exact place new information will be added
- phase owner and next owner
- issue list with owners
- learning loop state
