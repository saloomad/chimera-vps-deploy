# GitHub Coordination File Usage Registry

Updated: 2026-05-04

## Purpose

This file prevents dead-end coordination artifacts.

If a new durable coordination file is created, it should be added here with:

- what it is for
- who reads it
- when it is supposed to be used
- how we prove it is wired

## Registered Coordination Artifacts

| Artifact | Purpose | Automatic Reader Or Owner | Trigger | Proof Surface |
|---|---|---|---|---|
| `handoffs/CHECKPOINT_*.md` | carry forward the last meaningful state | all startup flows | platform startup | `github_coordination_guard.py startup-summary` |
| `session-states/*.yaml` | current platform task truth | startup flows and readiness gate | startup and task switch | `github_coordination_guard.py validate-platform` |
| `publish-queue/*.yaml` | unfinished or not-ready publish debt | startup flows and readiness gate | task switch when work is not publish-ready | `github_coordination_guard.py validate-platform` |
| `skills/github-coordination-gate/SKILL.md` | teach every platform to read shared coordination truth first | platform instructions and local skill homes | meaningful startup | `verify_github_coordination_system.py` |
| `skills/task-transition-publish/SKILL.md` | teach the task-switch publish contract | platform instructions and local skill homes | meaningful task switch | `verify_github_coordination_system.py` |
| `skills/task-change-readiness-gate/SKILL.md` | block leaving a task without honest shared truth | platform instructions, shared guard, OpenClaw runtime gate | new-task style message or task switch | `verify_github_coordination_system.py` and live OpenClaw smoke test |
| `skills/platform-live-repo-router/SKILL.md` | decide which repo owns the actual changed files | platform instructions and operators | publish decision | `verify_github_coordination_system.py` |
| `skills/coordination-artifact-lifecycle-guard/SKILL.md` | prevent coordination files from becoming dead ends | maintainers changing coordination surfaces | every coordination file creation or workflow edit | `verify_github_coordination_system.py` |
| `workflows/GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md` | official shared workflow for startup, task switch, proof, and repo routing | bootstrap-injected workspaces and operators | meaningful task switch | live OpenClaw bootstrap injection and verifier |
| `docs/GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md` | plain-English operating guide | bootstrap-injected workspaces and operators | startup and onboarding | live OpenClaw bootstrap injection and verifier |
| `docs/GITHUB_COORDINATION_ARCHITECTURE_2026-05-04.md` | picture of how the whole system fits together | operators and maintainers | onboarding, architecture, debugging | verifier and guide reference |
| `docs/GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md` | truth table for file purpose, reader, trigger, and proof | maintainers and verifier | coordination changes | `verify_github_coordination_system.py` |
| `scripts/github_coordination_guard.py` | guard for startup summary and readiness validation | humans, tests, and OpenClaw task gate | startup, task switch, regression test | `self-test`, `startup-summary`, `validate-platform` |
| `scripts/verify_github_coordination_system.py` | whole-system verification | humans and review loop | after coordination changes | exit code and JSON report |

## Rule

If a future coordination file is important enough to keep, it must be added here in the same pass.

If it is not important enough to register, it is probably not important enough to keep as a durable coordination artifact.
