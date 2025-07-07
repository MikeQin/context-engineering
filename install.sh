#!/bin/bash

# Simple installer for Context Engineering Framework commands
# Creates ~/.claude/commands directory and copies both command files

set -e  # Exit on error

CLAUDE_DIR="$HOME/.claude"
COMMANDS_DIR="$CLAUDE_DIR/commands"
GENERATE_COMMAND="generate_design.md"
EXECUTE_COMMAND="execute_project.md"
GENERATE_SOURCE=".claude/commands/$GENERATE_COMMAND"
EXECUTE_SOURCE=".claude/commands/$EXECUTE_COMMAND"

echo "Installing Context Engineering Framework commands..."

# Check if source files exist
if [[ ! -f "$GENERATE_SOURCE" ]]; then
    echo "❌ Error: Source file not found: $GENERATE_SOURCE"
    echo "Please run this script from the context-engineering directory."
    exit 1
fi

if [[ ! -f "$EXECUTE_SOURCE" ]]; then
    echo "❌ Error: Source file not found: $EXECUTE_SOURCE"
    echo "Please run this script from the context-engineering directory."
    exit 1
fi

# Create directories if they don't exist
echo "📁 Creating directory: $COMMANDS_DIR"
mkdir -p "$COMMANDS_DIR"

# Copy the command files
echo "📋 Copying command files..."
cp "$GENERATE_SOURCE" "$COMMANDS_DIR/"
cp "$EXECUTE_SOURCE" "$COMMANDS_DIR/"

# Verify installation
if [[ -f "$COMMANDS_DIR/$GENERATE_COMMAND" ]] && [[ -f "$COMMANDS_DIR/$EXECUTE_COMMAND" ]]; then
    echo "✅ Successfully installed Context Engineering Framework commands!"
    echo ""
    echo "📍 Installed to:"
    echo "  - $COMMANDS_DIR/$GENERATE_COMMAND"
    echo "  - $COMMANDS_DIR/$EXECUTE_COMMAND"
    echo ""
    echo "🚀 Complete Workflow:"
    echo "  1. Setup your project:"
    echo "     mkdir my-project && cd my-project && cp ../framework/* ."
    echo ""
    echo "  2. Generate architecture:"
    echo "     /generate_design ./my-project/PRODUCT_PRP.md"
    echo ""
    echo "  3. Execute implementation:"
    echo "     /execute_project ./my-project"
    echo ""
    echo "📚 Individual command usage:"
    echo "  /generate_design [PRP_FILE]     # Generate technical architecture"
    echo "  /execute_project [PROJECT_DIR]  # Implement complete project"
else
    echo "❌ Installation failed - command files not found after copy"
    exit 1
fi