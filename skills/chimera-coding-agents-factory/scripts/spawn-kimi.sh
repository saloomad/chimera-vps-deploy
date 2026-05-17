#!/usr/bin/env bash
# Kimi Code wrapper (needs MiniMax proxy setup)
TASK="${1:?Usage: $0 <task> [workdir]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"
PROXY_PORT=3001
# Note: MiniMax proxy script required - see SKILL.md
echo "Kimi Code requires minimax-proxy.sh setup - see chimera-coding-agents-factory skill"
