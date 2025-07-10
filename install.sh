#!/bin/bash

# Context Engineering Framework - MCP Server Installer
# Installs required MCP servers for framework integration
# Commands are available automatically when working in the cloned repository

set -e  # Exit on error

echo "🚀 Context Engineering Framework - MCP Server Installation"
echo "=========================================================="
echo ""
echo "📋 About this installer:"
echo "  • Framework commands are auto-detected from .claude/ directory"
echo "  • No command copying required - they work directly from the repository"
echo "  • This script only installs required MCP servers for integration"
echo ""

# Function to check if MCP server is already installed
is_mcp_server_installed() {
    local server_name="$1"
    claude mcp list 2>/dev/null | grep -q "$server_name"
}

# Function to install MCP server (smart - skips if already installed)
install_mcp_server() {
    local server_name="$1"
    local server_command="$2"
    local description="$3"
    
    echo "🔧 Checking $server_name MCP server..."
    echo "   Purpose: $description"
    
    if is_mcp_server_installed "$server_name"; then
        echo "✅ $server_name MCP server already installed - skipping"
    else
        echo "   Installing $server_name..."
        # Run command and capture both exit code and output
        if eval "$server_command" 2>/dev/null; then
            echo "✅ $server_name MCP server installed successfully"
        else
            echo "❌ $server_name MCP server installation failed"
            echo "   Command attempted: $server_command"
            echo "   You can try manually: $server_command"
        fi
    fi
    echo ""
}

echo "🔧 MCP Server Installation"
echo "=========================="
echo ""

# Show current MCP server status
echo "📋 Current MCP servers:"
if claude mcp list 2>/dev/null; then
    echo ""
else
    echo "   No MCP servers currently installed (or Claude MCP not available)"
    echo ""
fi

echo "🎯 Checking required MCP servers for framework functionality:"

# Check each server and build installation plan
servers_to_install=()
echo "   • Context7 - External library documentation and API references"
if is_mcp_server_installed "context7"; then
    echo "     ✅ Already installed"
else
    echo "     📥 Needs installation"
    servers_to_install+=("context7")
fi

echo "   • Sequential-thinking - Advanced multi-step reasoning capabilities"
if is_mcp_server_installed "sequential-thinking"; then
    echo "     ✅ Already installed"
else
    echo "     📥 Needs installation"
    servers_to_install+=("sequential-thinking")
fi

echo "   • Puppeteer - Web automation and browser testing"
if is_mcp_server_installed "puppeteer"; then
    echo "     ✅ Already installed"
else
    echo "     📥 Needs installation"
    servers_to_install+=("puppeteer")
fi

echo ""

# Only ask for confirmation if there's something to install
if [ ${#servers_to_install[@]} -eq 0 ]; then
    echo "🎉 All required MCP servers are already installed!"
    echo "   No installation required - framework is ready to use with full capabilities."
    echo ""
    echo "🚀 You can now start using the framework:"
    echo "  1. Create project folder: mkdir my-project && cd my-project"
    echo "  2. Copy templates: cp ../framework/* ."
    echo "  3. Generate design: /generate_design ./PRODUCT_PRP.md"
    echo "  4. Execute project: /execute_project ."
    exit 0
else
    echo "📦 ${#servers_to_install[@]} server(s) need to be installed: ${servers_to_install[*]}"
    read -p "Continue with MCP server installation? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
    echo ""
fi

# Install Context7 MCP server (for external library documentation)
install_mcp_server "Context7" \
    "claude mcp add --transport http context7 https://mcp.context7.com/mcp" \
    "External library documentation and API references"

# Install Sequential-thinking MCP server (for complex reasoning)
install_mcp_server "Sequential-thinking" \
    "claude mcp add sequential-thinking npx @modelcontextprotocol/server-sequential-thinking" \
    "Advanced multi-step reasoning capabilities"

# Install Puppeteer MCP server (for web automation)
install_mcp_server "Puppeteer" \
    "claude mcp add puppeteer npx @modelcontextprotocol/server-puppeteer" \
    "Web automation and browser testing"

echo "🎉 MCP Server Installation Complete!"
echo ""

# Show final MCP server status
echo "📋 Final MCP server status:"
if claude mcp list 2>/dev/null; then
    echo ""
else
    echo "   Unable to list MCP servers (check Claude MCP configuration)"
    echo ""
fi
echo "🚀 Framework Ready! Quick Start:"
echo "  1. Create project folder: mkdir my-project && cd my-project"
echo "  2. Copy templates: cp ../framework/* ."
echo "  3. Generate design: /generate_design ./PRODUCT_PRP.md"
echo "  4. Execute project: /execute_project ."
echo ""
echo "📚 Available Commands (auto-detected from .claude/):"
echo "  • /generate_design - Generate technical architecture"
echo "  • /execute_project - Implement complete project"
echo "  • /build - Modern web & CLI development"
echo "  • /analyze - Multi-dimensional code analysis"
echo "  • /review - AI-powered code review"
echo "  • And 14 more specialized development tools"
echo ""
echo "🎯 Framework successfully configured!"
echo "All commands are available when working in this repository."