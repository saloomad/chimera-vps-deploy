# Objective Heartbeat Control

status: paused
objective: Replace this line with the approved objective.
done_criteria:
- Replace this line with a concrete done check.
approved_scope: Safe approved continuation only. Stop on destructive changes, unclear scope, or new approval boundaries.
platform_owner: kimi-vps
heartbeat_interval: 15m
current_reality: Replace this line with the current state.
next_step: Replace this line with the next bounded execution step.
last_review_outcome: iterate
last_result_quality: acceptable
updated_at_utc: 2026-04-29T00:00:00Z

## Notes

- The heartbeat runner reads this file on each wake.
- If `status` is not `active`, the timer exits without running Kimi.
- Kimi should update `current_reality`, `next_step`, `last_review_outcome`, `last_result_quality`, and `updated_at_utc` after each meaningful pass.
- When the objective is done, set `status: complete`.
- When a real blocker appears, set `status: blocked` and explain it here.
