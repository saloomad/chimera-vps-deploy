# Chimera Deployment Tiers

Updated: 2026-05-12

## What This Document Is For

This is the current three-platform operating model for Chimera.

Use it when deciding:

- where a task should start
- where Linux testing should happen
- when GitHub should be updated
- what the VPS is allowed to consume

## The Three Platforms

| Platform | Machine | Main Role | Main Repo Or Path |
|----------|---------|-----------|-------------------|
| Windows | Windows Codex workspace | Control plane, review, GitHub decisions, shared docs, handoffs | `C:\Users\becke\claudecowork` |
| Linux home | Home Linux PC | Draft and test lane for Linux-native work | `/home/open-claw/openclawtrading` |
| Kimi VPS | Live VPS | Finished tested execution only | `/root/openclawtrading` |

## Role Split

### Windows

Windows is the control plane.

Use it for:

- user coordination
- repo comparison
- GitHub merges and branch decisions
- handoffs
- shared skills and instruction updates

### Linux Home

Linux home is the draft-and-test lane.

Use it for:

- first drafts of Linux-side work
- experiments
- replay and backtest
- Linux-native dependency checks
- pre-production testing

Linux home should not be described as the permanent live machine.

### Kimi VPS

Kimi VPS is the execution lane.

Use it for:

- finished tested execution
- runtime services
- cron and systemd validation
- live report checks
- rollback if needed

Do not use the VPS as the default drafting workspace.

## Branch Model

Use this branch contract:

- `main` = shared integration branch
- `staging` = Linux-home test gate
- `production` = live branch or deployment source for the VPS

## Default Flow

Use this order unless Sal explicitly wants a different route:

1. Windows defines the slice and checks current branch and handoff truth.
2. Linux home does the Linux-native draft or test work.
3. Windows reviews the result and prepares the shared publish.
4. Ready work lands on `main`.
5. Windows promotes the approved slice from `main` to `staging`.
6. Linux home tests `staging` from a clean checkout or worktree.
7. If the staging test passes, Linux home fast-forwards `production`.
8. Kimi VPS consumes `production` only.

Short version:

`Windows control -> Linux home draft/test -> Windows review -> main -> staging -> production -> VPS`

## Linux Home Workspace Split

Linux home should not use one dirty checkout for both rough work and clean staging promotion.

Keep two lanes:

- Draft workspace:
  - `/home/open-claw/openclawtrading`
- Clean staging gate:
  - `/home/open-claw/openclawtrading-staging`

The draft workspace can stay messy while active work is in flight.
The staging gate should stay clean and should be the only place that pulls and tests `staging`.

## Current Host And Path Truth

As of 2026-05-12:

- preferred reachable Linux-home SSH path from Windows: `ssh open-claw@100.116.214.127`
- older `192.168.1.203` timed out in this pass
- Linux-home active Git repo in use: `/home/open-claw/openclawtrading`
- `/home/open-claw/chimera` exists but was not a Git repo in this pass
- Kimi VPS live SSH path: `ssh root@100.67.172.114`

## Promotion Rules

### Windows -> Main

Windows is the GitHub control plane.

That means Windows should:

- inspect the diff
- decide whether the slice is ready
- merge or publish to `main`
- update shared handoffs and skill mirrors when needed

### Main -> Staging

Promote to `staging` only when:

- the slice is bounded enough to test cleanly
- the intended Linux-home test is known
- the work is ready for Linux-side validation

### Staging -> Production

Promote to `production` only when the clean Linux-home staging lane passes the required checks.

### Production -> VPS

The VPS should:

- pull or consume `production` only
- never pull `main` or `staging`
- never be treated as the first place to clean up unfinished code

## Clean Test Gate Rule

Do not pull `staging` into a dirty Linux-home working tree.

Use one of these:

- a clean second checkout
- a clean Git worktree

The reason is simple: one workspace should not be both the messy draft area and the clean promotion gate.

## GitHub Rules

- GitHub is the shared checkpoint between platforms.
- Do not store tokens inside repo remote URLs.
- Use credential helpers, GitHub CLI, or other secret-safe auth surfaces instead.
- Do not claim work is cross-platform synced unless:
  - the source platform was updated
  - the shared GitHub truth was updated when needed
  - the target platform received the intended copy

## VPS Runtime Note

If `/root/openclawtrading` is acting as an unpacked runtime copy instead of a full Git checkout, treat `/root/chimera-deploy` and the deployment workflow as the Git-facing promotion surface.

Do not improvise hotfixes inside an unpacked runtime tree unless the work is a bounded emergency repair and the reply says so plainly.

## Guardrails

- Do not treat Linux home as the live VPS.
- Do not treat `192.168.1.203` as the preferred Linux-home host while `100.116.214.127` is the verified path.
- Do not treat `/home/open-claw/chimera` as the active repo without rechecking it.
- Do not let the same Linux-home checkout act as both the messy draft lane and the clean staging gate.
- Do not let the VPS consume unfinished work.

## Read Next

- `platforms/linux-home/AGENTS.md`
- `platforms/linux-home/CHIMERA_BOOTSTRAP.md`
- `platforms/windows-codex/CHIMERA_BOOTSTRAP.md`
- `platforms/kimi-vps/CHIMERA_BOOTSTRAP.md`
- `skills/platform-access-and-sync-guide/`
- `skills/github-manager/`
