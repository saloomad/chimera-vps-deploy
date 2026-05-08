# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-02T18:50:04+03:00
- **Platform**: Windows Codex
- **Session focus**: diagnose and remove the daily Tailscale SSH approval blocker affecting live VPS automation

## Original Goal
Find the real cause of the recurring daily SSH interruption and fix it so Codex can reach the VPS reliably without repeated browser approval.

## Completed Work
- [x] Proved Tailscale network connectivity was healthy
- [x] Proved the repeated interruption was Tailscale SSH check-mode behavior, not a dead VPS or broken tailnet
- [x] Verified normal `sshd` on the VPS was active, listening, and compatible with root public-key auth
- [x] Verified the Windows machine's ED25519 public key was already present in `/root/.ssh/authorized_keys`
- [x] Enabled normal SSH at boot with `systemctl enable ssh`
- [x] Disabled Tailscale SSH on the VPS with `tailscale set --ssh=false --accept-risk=lose-ssh`
- [x] Re-verified plain SSH command execution from Windows to `root@100.67.172.114`
- [x] Logged the root cause and fix in the shared observations ledger

## Key Findings
- The daily blocker was Tailscale SSH intercepting port `22` on the Tailscale IP and demanding check-mode approval.
- The tailnet itself was healthy the whole time: `tailscale status`, `tailscale ping`, and TCP port `22` reachability were all fine.
- Standard OpenSSH on the VPS was already healthy, but it was not enabled at boot. That is now fixed.
- After disabling Tailscale SSH, the Windows client authenticated to the VPS using standard `publickey` auth instead of the Tailscale SSH path.

## Safe Changes Made
- Live VPS:
  - `systemctl enable ssh`
  - `tailscale set --ssh=false --accept-risk=lose-ssh`

## Verification
- `ssh root@100.67.172.114 "echo post_disable_ok"`: passed
- Debug trace after cutover showed:
  - standard public-key auth
  - standard OpenSSH host-key learning
  - no Tailscale SSH browser approval prompt

## Not Done
- [ ] No Deezoh/Hermes live observation rerun in this slice
- [ ] No additional cron or agent wiring changes in this slice

## Next Actions
1. **[PRIORITY]** Resume the real live Deezoh/Hermes improvement loop now that reliable SSH access is restored
2. **[MEDIUM]** If access friction ever returns, first verify that Tailscale SSH was not re-enabled on the VPS

## Reading List For Next Agent
- `C:\Users\becke\claudecowork\chimera-vps-deploy\research\operations\DEEZOH_HERMES_AGENT_IMPROVEMENT_OBSERVATIONS.md`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\CHECKPOINT_2026-05-02_tailscale-ssh-daily-prompt-fixed.md`
