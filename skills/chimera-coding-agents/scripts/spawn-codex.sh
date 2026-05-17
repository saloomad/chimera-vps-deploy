#!/usr/bin/env bash
# Spawn Codex for a Chimera task
# Usage: ./spawn-codex.sh "task description" [workdir]

set -e

TASK="${1:?Usage: $0 <task> [workdir]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"

cd "$WORKDIR"
echo "[$(date)] Starting Codex: $TASK"
codex exec --full-auto "$TASK" 2>&1
echo "[$(date)] Codex done"
