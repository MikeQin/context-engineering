# Claude Code Session Management Guide

Great question! Here are the best approaches for preserving session context and loading it into new conversations, especially for the Context Engineering Framework:

## 🔄 Built-in Claude Code Session Management

### **1. Resume Flag (Primary Method)**
```bash
# Start new session with previous context
claude --resume

# Or resume with specific conversation ID
claude --resume [conversation-id]
```

### **2. Memory Integration**
Claude Code automatically preserves:
- Recent file modifications
- Git status and changes
- Project patterns and preferences
- Tool usage patterns

## 📋 Framework-Specific Context Preservation

### **3. Use Your /load Command**
```bash
# In new session, immediately load framework context
/load

# This analyzes your repository and provides comprehensive context about:
# - Current framework state
# - Recent changes and modifications  
# - Three-Document Pattern status
# - Available commands and capabilities
```

### **4. CLAUDE.md Context (Automatic)**
Your framework's `.claude/CLAUDE.md` automatically provides:
- 19 specialized commands
- Development methodology
- Coding standards and patterns
- MCP integration capabilities

### **5. Repository CLAUDE.md (Critical - Often Missed!)**
**ALWAYS read the root `./CLAUDE.md` file first** - it contains:
- Repository purpose and architecture
- Framework vs user project distinction
- Current development context and recent updates
- Critical consistency requirements
- Technology stack and architecture patterns

```bash
# Essential first step in any new session
cat ./CLAUDE.md

# This provides repository-level context including:
# - Core components (.claude/, framework/, examples/, docs/)
# - Recent updates and current framework state
# - Development standards and quality requirements
# - Best practices for framework work
```

## 🎯 Advanced Session Preservation

### **6. Session Summary Documentation**
Create a session summary before ending:

```bash
# Create session summary (automatically saved to docs/sessions/)
/document --session-summary

# Custom location and name
/document --session-summary --output ./custom/path.md --name "custom-session-name"

# Automatically creates: ./docs/sessions/SESSION_YYYY-MM-DD_HHMMSS.md
```

Or manually document key accomplishments:
```markdown
# Session Summary - [Date]

## Completed Work
- Enhanced framework with README.md requirements
- Updated token-saving mode documentation
- Added CLI application templates

## Current State
- All TODO items completed
- Framework ready for production use
- Repository in clean state

## Next Steps
- Test new README.md generation
- Validate token-saving modes in practice
- Consider additional framework enhancements
```

### **7. Git-Based Context Preservation**
```bash
# Commit current state with descriptive message
git add .
git commit -m "Framework enhancement: Added mandatory README.md generation

- Updated .claude/commands/build.md with README.md requirements
- Created comprehensive README.md template for Python CLI apps
- Enhanced framework/CLAUDE.md with documentation standards
- Added Documentation_Standards to Project_Quality rules

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Git log provides conversation context
git log --oneline -10
```

## 🏆 Best Practice: Multi-Layer Approach

### **For New Sessions, Use This Sequence:**

1. **Start with Resume**
   ```bash
   claude --resume
   ```

2. **Read Repository Context (CRITICAL)**
   ```bash
   # ALWAYS read this first - provides essential repository context
   cat ./CLAUDE.md
   ```

3. **Load Framework Context**
   ```bash
   /load
   ```

4. **Check Recent Git History**
   ```bash
   git log --oneline -10
   git status
   ```

5. **Review Key Files**
   ```bash
   # Check framework state
   ls -la .claude/
   ls -la framework/
   
   # Review recent documentation
   head -20 README.md
   ```

## 🔧 Framework Enhancement Opportunity

### **Add Session Management to Your Framework**

Consider enhancing your framework with dedicated session management:

```yaml
# .claude/commands/session.md
**Purpose**: Session context management and preservation

Commands:
- /session save    # Save current session context
- /session load    # Load previous session context  
- /session summary # Generate session summary
- /session status  # Show current session state
```

### **Context Engineering Pattern for Sessions**

Apply your Three-Document Pattern to session management:

```
📁 Session Context
├── SESSION_SUMMARY.md     # What was accomplished
├── CONTEXT_STATE.md       # Current project state  
└── NEXT_ACTIONS.md        # Planned next steps
```

## 💡 Immediate Recommendations

### **For Your Current Situation:**

1. **Use --resume flag** for immediate context continuation
2. **Read ./CLAUDE.md FIRST** - contains critical repository context and recent updates
3. **Run /load** at start of new sessions to analyze current framework state
4. **Create session summary documents** for complex multi-session work
5. **Leverage git commits** with detailed messages for session boundaries

### **For Complex Framework Development:**

1. **Document major changes** in `docs/DESIGN_DECISIONS.md`
2. **Update framework version** in key files when making significant changes
3. **Use descriptive git commits** that explain the "why" not just the "what"
4. **Maintain TODO lists** in persistent files, not just in session memory

The combination of `--resume` + **reading ./CLAUDE.md** + `/load` + git history will give you the most comprehensive context restoration for continuing your framework development work.

## ⚠️ Critical Reminder

**ALWAYS READ ./CLAUDE.md FIRST** in any new session. This file contains:
- Repository purpose and current development context
- Recent updates and framework state (like the 2025-07-10 token-saving implementation)
- Architecture patterns and consistency requirements
- Essential background that complements the toolkit capabilities

Missing this step means missing critical repository-level context that explains the current state and recent accomplishments.

---

**Generated**: 2025-07-10  
**Context**: Claude Code session management best practices for Context Engineering Framework  
**Status**: Production guidance for session continuity and context preservation