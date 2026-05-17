# Chimera Scenario Pack Index

These are the first scenario families the Chimera review/debug lane should cover.

## 1. Screener vs Bundle Focus Conflict

Question:

- why is the bundle focused on a symbol that is not the latest screener top pick

Check:

- selection provenance
- entry-watch precedence
- whether no-trade should still win

## 2. No-Trade Should Win

Question:

- did the system preserve no-trade even when one narrow lane looked ready

Check:

- final posture
- veto owner
- handoff after alert

## 3. Illegal Phase Promotion

Question:

- did the lifecycle move from screener to bundle, or bundle to entry-watch, without enough proof

Check:

- transition reason
- rejected alternative
- missing proof before stronger action

## 4. Stale Helper Misleads Decision

Question:

- did helper-grade or stale evidence get treated like ready evidence

Check:

- source status
- freshness
- whether consumer downgraded confidence

## 5. Wrong Owner Handoff

Question:

- did the correct owner exist but the wrong owner act next

Check:

- next owner
- packet owner
- consumer decision trace

## 6. Strategy Looks Good But Desk Use Is Bad

Question:

- does strategy edge exist while Deezoh still asks poor questions or makes poor timing decisions

Check:

- backtest lane vs behavior lane

## 7. Replay Passes But Live Is Still Weak

Question:

- are we overclaiming because synthetic replay is cleaner than live runtime truth

Check:

- replay vs live divergence
- synthetic assumptions
- live unresolved risks
