#!/usr/bin/env bash
# Fix Hermes/OpenClaw commands on Linux PC
# Run this on the Linux PC: 100.116.214.127

echo "=== Linux PC Hermes/OpenClaw Command Fix ==="

WORKSPACE="/home/open-claw/openclawtrading"
cd "$WORKSPACE"

# ----------------------------------------------------------------
# 1. Check if node_modules/openclaw exists
# ----------------------------------------------------------------
if [ ! -d "node_modules/openclaw" ]; then
    echo "OpenClaw not installed. Installing..."
    npm install openclaw
else
    echo "OpenClaw already installed"
fi

# ----------------------------------------------------------------
# 2. Add to PATH permanently
# ----------------------------------------------------------------
BASHRC="$HOME/.bashrc"
OPENCLAW_BIN="$WORKSPACE/node_modules/.bin"

# Remove any old PATH lines for openclawtrading
grep -v "openclawtrading.*node_modules" "$BASHRC" > "$BASHRC.tmp" || true
mv "$BASHRC.tmp" "$BASHRC"

# Add PATH
echo "" >> "$BASHRC"
echo "# OpenClaw from workspace" >> "$BASHRC"
echo "export PATH=\"$OPENCLAW_BIN:$PATH\"" >> "$BASHRC"

# Create convenience aliases
echo "" >> "$BASHRC"
echo "# OpenClaw aliases" >> "$BASHRC"
echo "alias openclaw-tui='openclaw run --profile default'" >> "$BASHRC"
echo "alias openclaw='openclaw'" >> "$BASHRC"

# Source bashrc
source "$BASHRC"

# ----------------------------------------------------------------
# 3. Test commands
# ----------------------------------------------------------------
echo ""
echo "=== Testing commands ==="
command -v openclaw && echo "openclaw: $(openclaw --version 2>/dev/null || echo 'installed')" || echo "openclaw: NOT FOUND"

# ----------------------------------------------------------------
# 4. Hermes skills sync (if .hermes exists)
# ----------------------------------------------------------------
if [ -d "$HOME/.hermes/skills" ]; then
    echo ""
    echo "Hermes skills: $HOME/.hermes/skills ($(ls $HOME/.hermes/skills 2>/dev/null | wc -l) skills)"
fi

# ----------------------------------------------------------------
# 5. Pull latest from GitHub
# ----------------------------------------------------------------
echo ""
echo "=== Pulling latest from GitHub ==="
git pull origin main 2>/dev/null || git pull origin master 2>/dev/null || echo "Git pull skipped"

echo ""
echo "=== Done ==="
echo "Run 'source ~/.bashrc' or restart terminal, then try: openclaw --help"
