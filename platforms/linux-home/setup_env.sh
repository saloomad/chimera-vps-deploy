#!/usr/bin/env bash
# Linux PC Hermes/OpenClaw/Claude CLI Setup
# Run: curl -fsSL <this-script-url> | bash
# Or copy to ~/.bashrc

set -euo pipefail

echo "=== Linux PC Hermes/OpenClaw Setup ==="

# ----------------------------------------------------------------
# 1. OpenClaw workspace binary
# ----------------------------------------------------------------
OPENCLAW_WORKSPACE="/home/open-claw/openclawtrading"
if [ -d "$OPENCLAW_WORKSPACE" ]; then
    # Check if openclaw is there as a node_modules binary
    if [ -f "$OPENCLAW_WORKSPACE/node_modules/.bin/openclaw" ]; then
        export PATH="$OPENCLAW_WORKSPACE/node_modules/.bin:$PATH"
        echo "Added OpenClaw to PATH: $OPENCLAW_WORKSPACE/node_modules/.bin"
        
        # Alias for convenience
        alias openclaw-tui='openclaw run --profile default'
        alias openclaw='openclaw'
        echo "Created aliases: openclaw, openclaw-tui"
    fi
fi

# ----------------------------------------------------------------
# 2. Hermes skills — if installed in ~/.hermes/skills
# ----------------------------------------------------------------
HERMES_SKILLS="$HOME/.hermes/skills"
if [ -d "$HERMES_SKILLS" ]; then
    echo "Hermes skills found: $HERMES_SKILLS"
    echo "  Hermes is a Windows runtime. On Linux, use Hermes skills via:"
    echo "  - Claude CLI with hermes skills: claude --skills-dir $HERMES_SKILLS"
    echo "  - Or run scripts in: $HERMES_SKILLS/../scripts/"
fi

# ----------------------------------------------------------------
# 3. Claude CLI
# ----------------------------------------------------------------
if ! command -v claude &> /dev/null; then
    echo "Claude CLI not installed."
    echo "  Install: npm install -g @anthropic-ai/claude"
    echo "  Or: curl -fsSL https://storage.googleapis.com/ep-www-builds/linux/claude -o /usr/local/bin/claude && chmod +x /usr/local/bin/claude"
else
    echo "Claude CLI: $(claude --version 2>/dev/null || echo 'installed')"
fi

# ----------------------------------------------------------------
# 4. Hermes script runner (if scripts installed)
# ----------------------------------------------------------------
HERMES_SCRIPTS="$HOME/.hermes/scripts"
if [ -d "$HERMES_SCRIPTS" ]; then
    export PATH="$HERMES_SCRIPTS:$PATH"
    echo "Added Hermes scripts to PATH: $HERMES_SCRIPTS"
fi

# ----------------------------------------------------------------
# 5. Git repo pull for latest skills
# ----------------------------------------------------------------
if [ -d "$OPENCLAW_WORKSPACE/.git" ]; then
    echo ""
    echo "=== Pulling latest from GitHub ==="
    (cd "$OPENCLAW_WORKSPACE" && git pull origin main 2>/dev/null || git pull origin master 2>/dev/null || echo "Git pull skipped (dirty or detached HEAD)")
fi

echo ""
echo "=== Setup complete ==="
echo "Try: openclaw --help"
echo "Or:  openclaw-tui"
echo ""
