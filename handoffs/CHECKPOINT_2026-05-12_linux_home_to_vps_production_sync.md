# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-12T21:50:00+08:00
- **Platform**: Windows Codex
- **Session focus**: continue the three-platform standardization by syncing the approved Linux-home lane into the VPS runtime safely.

## Original Goal
Continue the platform standardization work and actually sync Linux-home-approved code to the VPS without violating the new guardrails against copying the dirty draft workspace directly into live execution.

## Completed Work
- [x] Verified the Linux-home draft repo remains heavily dirty and therefore is not a safe direct sync source.
- [x] Verified the clean Linux-home staging gate at `/home/open-claw/openclawtrading-staging` is clean and that `origin/staging` and `origin/production` both point to commit `b0033e48d`.
- [x] Added a local `production` branch in the Linux-home staging gate so future promotions and comparisons have a real local branch.
- [x] Fixed the VPS deploy sync script `scripts/sync-from-main-repo.sh` so it now syncs from `production` instead of `main` and can refresh a non-Git runtime tree with `rsync`.
- [x] Copied that script to `/root/chimera-deploy/scripts/sync-from-main-repo.sh` and executed it on the VPS.
- [x] Refreshed `/root/openclawtrading` on the VPS from approved production commit `b0033e48d4934195d2ed25867555d6cdc07b595f`.
- [x] Proved the VPS runtime now matches the clean Linux-home lane on representative files by SHA256:
  - `AGENTS.md`
  - `trading_system/scripts/chimera_entry_exit_sim.py`

## Partially Done
- [~] The VPS runtime is now aligned with the approved production snapshot, but the runtime tree is still not a Git checkout. The durable sync script handles that, but the runtime is still an overlay target rather than a normal repo clone.

## Not Done
- [ ] Full runtime-health testing after the production refresh was not run in this pass.
- [ ] The broader Windows main-repo dirty-state cleanup remains open.

## Decisions Made
- **Decision**: do not sync the dirty Linux-home draft repo directly into the VPS. | **Why**: that would bypass the control-plane and staging-gate protections we just put in place.
- **Decision**: treat the clean Linux-home staging gate and `production` snapshot as the safe source for VPS sync. | **Why**: that is the approved tested lane in the new three-platform model.
- **Decision**: fix the VPS sync script instead of doing a one-off manual copy only. | **Why**: the old script still pulled `main` and assumed the runtime was a Git repo, which would keep breaking future syncs.

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `scripts/sync-from-main-repo.sh` | shared repo | Reworked the VPS sync logic to use `production` and support non-Git runtime refresh with `rsync`. |
| `/root/chimera-deploy/scripts/sync-from-main-repo.sh` | Kimi VPS | Live deploy copy updated and executed. |
| `handoffs/CHECKPOINT_2026-05-12_linux_home_to_vps_production_sync.md` | shared repo | New handoff for this Linux-home-to-VPS production sync pass. |

## Skills Created / Updated
- [ ] none

## Other Durable Outputs Created
- [x] Linux-home local `production` branch in the clean staging gate

## Sync Status
- **GitHub status**: script and handoff are ready to publish from the shared repo branch
- **Other platforms that should pull this**: Kimi VPS, Windows Codex, Windows Claude
- **What still needs sync**: push the new script and handoff on the shared repo branch so future platform pulls inherit the fixed production-sync behavior

## Routing Used
- **Task lane**: mixed
- **Model used**: gpt-5.4
- **Reasoning used**: medium
- **Result quality**: strong
- **Rerun needed**: no
- **Better route next time**: same

## Next Actions (for next agent)
1. **[PRIORITY]** Run the key live runtime health checks on the VPS after this production refresh.
2. **[MEDIUM]** Push the shared repo script and handoff update so the fixed production-sync logic is not stranded only on the live VPS copy.
3. **[MEDIUM]** Decide later whether `/root/openclawtrading` should remain an overlay runtime tree or be converted back into a normal Git checkout.

## Skills to Read Before Starting
- [x] `platform-access-and-sync-guide`
- [x] `github-manager`
- [x] `linux-access`

## Live System State (if applicable)
- **OpenClaw Gateway**: not checked in this pass
- **TradingView Desktop**: not checked in this pass
- **Discord Bot**: not checked in this pass
- **Last data update**: VPS runtime refreshed from production commit `b0033e48d4934195d2ed25867555d6cdc07b595f`

## Reading List for Next Agent
- `scripts/sync-from-main-repo.sh`
- `handoffs/CHECKPOINT_2026-05-12_three_platform_standardization_and_sync.md`
- `handoffs/CHECKPOINT_2026-05-12_linux_home_to_vps_production_sync.md`
