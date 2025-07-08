#!/bin/bash

# Complete installation script for Context Engineering Framework
# FOR INTERNAL USE ONLY - Framework contributors and internal development
# 
# This script installs the complete toolkit configuration to $HOME/.claude
# For regular framework users, use ./install.sh instead
#
# Installs all commands, configurations, and MCP server integrations

set -e  # Exit on error

CLAUDE_DIR="$HOME/.claude"
REPO_CLAUDE_DIR=".claude"
TOOLKIT_DIR="$(dirname "$0")"
REPO_ROOT="$(cd "$TOOLKIT_DIR/.." && pwd)"

echo "🚀 Context Engineering Framework - Complete Installation"
echo "======================================================"
echo ""

# Check if we're in the right directory
if [[ ! -d "$REPO_ROOT/$REPO_CLAUDE_DIR" ]]; then
    echo "❌ Error: .claude directory not found in repository"
    echo "Please run this script from the context-engineering directory."
    exit 1
fi

echo "📁 Installation directories:"
echo "  Repository: $REPO_ROOT"
echo "  Target: $CLAUDE_DIR"
echo ""

# Create ~/.claude directory structure if it doesn't exist
echo "📁 Creating Claude directory structure..."
mkdir -p "$CLAUDE_DIR"
mkdir -p "$CLAUDE_DIR/commands"
mkdir -p "$CLAUDE_DIR/shared"
mkdir -p "$CLAUDE_DIR/templates"
mkdir -p "$CLAUDE_DIR/settings"

# Copy main CLAUDE.md configuration
echo "📋 Installing main configuration..."
cp "$REPO_ROOT/$REPO_CLAUDE_DIR/CLAUDE.md" "$CLAUDE_DIR/"

# Copy all commands
echo "📋 Installing 19 specialized commands..."
cp -r "$REPO_ROOT/$REPO_CLAUDE_DIR/commands/"* "$CLAUDE_DIR/commands/"

# Copy shared configuration modules
echo "📋 Installing shared configuration modules..."
cp -r "$REPO_ROOT/$REPO_CLAUDE_DIR/shared/"* "$CLAUDE_DIR/shared/"

# Copy templates
echo "📋 Installing Next.js + Tailwind CSS templates..."
cp -r "$REPO_ROOT/$REPO_CLAUDE_DIR/templates/"* "$CLAUDE_DIR/templates/"

# Copy settings if they exist
if [[ -f "$REPO_ROOT/$REPO_CLAUDE_DIR/settings.local.json" ]]; then
    echo "📋 Installing local settings..."
    cp "$REPO_ROOT/$REPO_CLAUDE_DIR/settings.local.json" "$CLAUDE_DIR/settings/"
fi

# Verify installation
echo "✅ Verifying installation..."
REQUIRED_FILES=(
    "$CLAUDE_DIR/CLAUDE.md"
    "$CLAUDE_DIR/commands/analyze.md"
    "$CLAUDE_DIR/commands/build.md"
    "$CLAUDE_DIR/commands/generate_design.md"
    "$CLAUDE_DIR/commands/execute_project.md"
    "$CLAUDE_DIR/shared/toolkit-core.yml"
    "$CLAUDE_DIR/shared/toolkit-personas.yml"
    "$CLAUDE_DIR/templates/nextjs-tailwind/components/ui/button.tsx"
)

MISSING_FILES=()
for file in "${REQUIRED_FILES[@]}"; do
    if [[ ! -f "$file" ]]; then
        MISSING_FILES+=("$file")
    fi
done

if [[ ${#MISSING_FILES[@]} -gt 0 ]]; then
    echo "❌ Installation incomplete - missing files:"
    for file in "${MISSING_FILES[@]}"; do
        echo "  - $file"
    done
    exit 1
fi

echo "✅ Successfully installed Context Engineering Framework!"
echo ""
echo "📍 Installed components:"
echo "  - Main configuration: $CLAUDE_DIR/CLAUDE.md"
echo "  - Commands: $CLAUDE_DIR/commands/ (19 specialized tools)"
echo "  - Shared modules: $CLAUDE_DIR/shared/ (core configurations)"
echo "  - Templates: $CLAUDE_DIR/templates/ (Next.js + Tailwind CSS)"
echo ""

# MCP Server Integration
echo "🔧 MCP Server Integration (Optional)"
echo "=================================="
echo ""
echo "For enhanced capabilities, you can install MCP servers:"
echo ""

# Function to install MCP server
install_mcp_server() {
    local server_name="$1"
    local server_command="$2"
    
    echo "Installing $server_name MCP server..."
    if eval "$server_command"; then
        echo "✅ $server_name MCP server installed successfully"
    else
        echo "⚠️  $server_name MCP server installation failed (optional)"
    fi
    echo ""
}

# Ask user if they want to install MCP servers
read -p "Do you want to install MCP servers for enhanced capabilities? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Installing MCP servers..."
    echo ""
    
    # Install Context7 MCP server
    install_mcp_server "context7" "claude mcp add --transport http context7 https://mcp.context7.com/mcp"
    
    # Install Sequential-thinking MCP server
    install_mcp_server "sequential-thinking" "claude mcp add sequential-thinking npx @modelcontextprotocol/server-sequential-thinking"
    
    # Install Puppeteer MCP server
    install_mcp_server "puppeteer" "claude mcp add puppeteer npx @modelcontextprotocol/server-puppeteer"
    
    echo "🎉 MCP servers installation completed!"
else
    echo "⏭️  Skipping MCP servers installation"
    echo ""
    echo "You can install them later using these commands:"
    echo ""
    echo "# Add context7 mcp server integration"
    echo "claude mcp add --transport http context7 https://mcp.context7.com/mcp"
    echo ""
    echo "# Add sequential-thinking mcp server integration"
    echo "claude mcp add sequential-thinking npx @modelcontextprotocol/server-sequential-thinking"
    echo ""
    echo "# Add puppeteer mcp server integration"
    echo "claude mcp add puppeteer npx @modelcontextprotocol/server-puppeteer"
fi

echo ""
echo "🚀 Complete Installation Summary"
echo "=============================="
echo ""
echo "✅ Installed Components:"
echo "  - 19 specialized commands for complete development lifecycle"
echo "  - 9 cognitive personas for domain-specific approaches"
echo "  - Next.js + Tailwind CSS templates and components"
echo "  - Core configuration modules and patterns"
echo "  - Evidence-based development methodology"
echo ""
echo "🎯 Available Features:"
echo "  - Modern web development with Next.js + Tailwind CSS"
echo "  - Component generation with shadcn/ui"
echo "  - Zero-cost UI generation (no external dependencies)"
echo "  - Complete development lifecycle commands"
echo "  - Enhanced AI capabilities through MCP integration"
echo ""
echo "🚀 Quick Start Workflow:"
echo "  1. Create project: mkdir my-project && cd my-project"
echo "  2. Copy templates: cp $REPO_ROOT/framework/* ."
echo "  3. Generate design: /generate_design ./my-project/PRODUCT_PRP.md"
echo "  4. Execute project: /execute_project ./my-project"
echo ""
echo "📚 Command Examples:"
echo "  /build --nextjs --tailwind --shadcn    # Generate Next.js app"
echo "  /analyze --code --persona-architect     # Analyze with systems thinking"
echo "  /scan --security --owasp               # Security analysis"
echo "  /test --coverage --e2e                 # Testing framework"
echo ""
echo "🎉 Context Engineering Framework is now ready to use!"
echo "Visit the toolkit documentation for complete command reference."