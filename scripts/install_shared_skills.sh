#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${1:-/root/chimera-deploy}"
TARGET_SKILLS_HOME="${2:-/root/.kimi/skills}"

mkdir -p "$TARGET_SKILLS_HOME"

for name in \
  codex-runtime-router \
  objective-orchestration-loop \
  model-registry \
  github-manager \
  project-operations-manager \
  agent-session-resume \
  openclaw-replay-and-backtest \
  strategy-backtest-lab \
  pipeline-simulation-lab \
  openclaw-workspace
do
  if [ -d "$REPO_ROOT/skills/$name" ]; then
    rm -rf "$TARGET_SKILLS_HOME/$name"
    cp -R "$REPO_ROOT/skills/$name" "$TARGET_SKILLS_HOME/$name"
    echo "Installed $name"
  fi
done
