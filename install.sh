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
    echo ""
    echo "🔧 MCP Server Integration (Optional):"
    echo "For enhanced capabilities, install MCP servers:"
    echo ""
    
    # Ask user if they want to install MCP servers
    read -p "Do you want to install MCP servers for enhanced capabilities? (y/n): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Installing MCP servers..."
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
else
    echo "❌ Installation failed - command files not found after copy"
    exit 1
fi