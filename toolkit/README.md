# Claude Toolkit (Internal Use Only)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/MikeQin/claude-toolkit)

**Description**: "An internal toolkit for enhanced Claude development with specialized tools, modern templates, and structured methodologies"

A modern configuration framework that enhances Claude Code with Next.js + Tailwind CSS, specialized commands, cognitive personas, and zero-cost UI generation.

## 🌟 Modern Technology Stack
- **Next.js App Router** - Latest React patterns with server components
- **Tailwind CSS** - Utility-first styling with responsive design
- **shadcn/ui** - Professional component library with accessibility
- **TypeScript** - Type-safe development by default
- **Zod + React Hook Form** - Robust form validation
- **Lucide + Heroicons** - Beautiful icon libraries

## ✨ Features

**Claude Toolkit** enhances `Claude Code` with:
- **19 Specialized Commands** covering complete development lifecycle
- **9 Cognitive Personas** for domain-specific approaches
- **Next.js + Tailwind CSS Templates** for modern web development
- **Zero External Dependencies** for UI generation
- **Evidence-Based Methodology** encouraging documentation
- **MCP Integration** with Context7, Sequential, Puppeteer
- **Git Checkpoint Support** for safe experimentation
- **Introspection Mode** for framework improvement and troubleshooting

## 💡 Core Capabilities

### 🎨 Next.js + Tailwind CSS Generation
Modern component and application generation:

```bash
/build --nextjs --tailwind --shadcn              # Complete Next.js app
/build --nextjs --app-router --forms --dashboard # Dashboard with forms
/build --react --tailwind --components           # React component library
/build --nextjs --tailwind --responsive          # Mobile-first design
```

### 🧠 **Cognitive Personas (Now as Flags!)**
Switch between different approaches with persona flags:

```bash
/analyze --code --persona-architect     # Systems thinking approach
/build --nextjs --persona-frontend      # UX-focused development  
/scan --security --persona-security     # Security-first analysis
/troubleshoot --prod --persona-analyzer # Root cause analysis approach
```

### ⚡ **19 Commands**
Development lifecycle coverage:

**Development Commands**
```bash
/build --nextjs --tailwind --shadcn    # Modern web development
/dev-setup --nextjs --tailwind         # Environment setup
/test --coverage --e2e --pup           # Testing strategies
```

**Analysis & Quality**
```bash
/review --quality --evidence --persona-qa     # AI-powered code review
/analyze --architecture --seq          # System analysis
/troubleshoot --prod --five-whys       # Issue resolution
/improve --performance --iterate       # Optimization
/explain --depth expert --visual       # Documentation
```

**Operations & Security**
```bash
/deploy --env prod --plan             # Deployment planning
/scan --security --owasp --deps       # Security audits
/migrate --dry-run --rollback         # Database migrations
/cleanup --all --validate             # Maintenance tasks
```

### 🎛️ MCP Integration Required
- **Context7**: Access to library documentation
- **Sequential**: Multi-step reasoning capabilities
- **Puppeteer**: Browser testing and automation

**⚠️ Important:** Claude Toolkit does not include MCP servers. You need to install them separately in Claude Code's MCP settings to use MCP-related flags (--c7, --seq, --pup).

**MCP Server Integration**
```sh
# Add context7 mcp server integration
claude mcp add --transport http context7 https://mcp.context7.com/mcp
# Remove after instegration
claude mcp remove context7

# Add sequential-thinking mcp server integration
claude mcp add sequential-thinking npx @modelcontextprotocol/server-sequential-thinking
# Remove after instegration
claude mcp remove sequential-thinking

# Add puppeteer mcp server integration
claude mcp add puppeteer npx @modelcontextprotocol/server-puppeteer
# Remove after instegration
claude mcp remove puppeteer
```

### 📊 **Token Efficiency**
**Claude Toolkit**'s `@include` template system helps manage token usage:
- **UltraCompressed mode** option for token reduction
- **Template references** for configuration management
- **Local generation** eliminates external API token costs
- **Context-aware compression** options

## 🎮 Example Workflows

### Modern Web Application Development
```bash
/design --nextjs --app-architecture --persona-architect    # Next.js architecture
/estimate --detailed --nextjs-complexity --seq             # Resource planning
/scan --security --nextjs --persona-security               # Security review
/build --nextjs --tailwind --shadcn --forms                # Implementation
```

### Component Library Creation
```bash
/build --react --tailwind --components --storybook         # Component library
/test --components --visual-regression --pup               # Visual testing
/document --components --storybook --interactive           # Documentation
/scan --accessibility --components --persona-qa            # Accessibility audit
```

### Production Issue Resolution
```bash
/troubleshoot --investigate --prod --persona-analyzer      # Analysis
/analyze --profile --nextjs --seq                         # Performance review
/improve --performance --nextjs --threshold 95%            # Optimization
/test --integration --e2e --pup                           # Validation
```

### Framework Troubleshooting & Improvement
```bash
/troubleshoot --introspect                                # Debug claude-toolkit behavior
/analyze --introspect --seq                               # Analyze framework patterns
/improve --introspect --uc                                # Optimize token usage
```

## 🎨 **Next.js + Tailwind CSS Templates**

### **Component Library**
- **shadcn/ui Components**: Button, Input, Form, Card, Dialog, Table, Navigation
- **Layout Templates**: Dashboard, Marketing, Auth, Blog, E-commerce
- **Form Templates**: Contact, Login, Registration, Settings, Multi-step
- **Page Templates**: Landing, About, Pricing, Blog Post, Product, Profile

### **Advanced Patterns**
- **Responsive Design**: Mobile-first, container queries, breakpoint management
- **Dark Mode**: Built-in dark mode support with system preference detection
- **Accessibility**: WCAG compliant components with proper ARIA attributes
- **Performance**: Optimized components with lazy loading and code splitting
- **Type Safety**: Full TypeScript support with proper prop types

### **Generation Examples**
```bash
# Generate specific components
/component --shadcn button --variant destructive --with-icon
/component --form contact --validation --responsive
/component --layout dashboard --sidebar --navigation

# Generate complete pages
/page --nextjs landing --hero --features --pricing
/page --nextjs dashboard --charts --tables --forms
/page --nextjs blog --mdx --search --categories
```

## 🎭 Available Personas

| Persona | Focus Area | Tools | Use Cases |
|---------|-----------|-------|-----------|
| **architect** | System design | Sequential, Context7 | Architecture planning |
| **frontend** | User experience | Next.js + Tailwind, Context7 | UI development |
| **backend** | Server systems | Context7, Sequential | API development |
| **security** | Security analysis | Sequential, Context7 | Security reviews |
| **analyzer** | Problem solving | All MCP tools | Debugging |
| **qa** | Quality assurance | Puppeteer, Context7 | Testing |
| **performance** | Optimization | Puppeteer, Sequential | Performance tuning |
| **refactorer** | Code quality | Sequential, Context7 | Code improvement |
| **mentor** | Knowledge sharing | Context7, Sequential | Documentation |

## 🛠️ Configuration Options

### Next.js + Tailwind CSS Integration
```bash
# Component generation
/build --nextjs --tailwind --shadcn

# Advanced patterns
/build --nextjs --app-router --server-actions

# Responsive design
/build --nextjs --tailwind --responsive --dark-mode
```

### Thinking Depth Control
```bash
# Standard analysis
/analyze --think

# Deeper analysis  
/design --think-hard

# Maximum depth
/troubleshoot --ultrathink
```

### Introspection Mode
```bash
# Enable self-aware analysis for claude-tools improvement
/analyze --introspect

# Debug claude-tools behavior
/troubleshoot --introspect --seq

# Optimize framework performance
/improve --introspect --persona-performance
```

### Token Management
```bash
# Standard mode
/build --nextjs --tailwind

# With compression
/analyze --architecture --uc

# Native tools only
/scan --security --no-mcp
```

## 📋 Command Categories

### Development (3 Commands)
- `/build` - Project builder with Next.js + Tailwind templates
- `/dev-setup` - Development environment setup
- `/test` - Testing framework

### Analysis & Improvement (5 Commands)
- `/review` - AI-powered code review with evidence-based recommendations
- `/analyze` - Code and system analysis
- `/troubleshoot` - Debugging and issue resolution
- `/improve` - Enhancement and optimization
- `/explain` - Documentation and explanations

### Operations (6 Commands)
- `/deploy` - Application deployment
- `/migrate` - Database and code migrations
- `/scan` - Security and validation
- `/estimate` - Project estimation
- `/cleanup` - Project maintenance
- `/git` - Git workflow management

### Design & Workflow (5 Commands)
- `/design` - System architecture
- `/spawn` - Parallel task execution
- `/document` - Documentation creation
- `/load` - Project context loading
- `/task` - Task management

## 🔧 Technical Architecture

**Claude Toolkit**'s architecture enables modern web development:

**🏗️ Next.js + Tailwind Integration**
- **CLAUDE.md** – Core configuration with Next.js + Tailwind focus
- **.claude/templates/** – Component and pattern templates
- **Local Generation** – Zero external dependencies for UI creation
- **TypeScript Native** – Type-safe development patterns

**🎯 Enhanced Command System**
- **19 Commands** – Complete development lifecycle coverage
- **Flag Inheritance** – Universal flags on all commands
- **Persona Integration** – 9 cognitive modes as flags
- **Modern Stack Support** – Next.js, Tailwind, TypeScript focus

**📦 Architecture Benefits**
- **Zero External Costs** – No paid service dependencies
- **Instant Performance** – Local template generation
- **Production Ready** – Enterprise-grade component library
- **Full Customization** – Complete control over output
- **Future Proof** – Based on modern, stable technologies

## 🔮 Use Cases for Internal Use

**Development Teams**
- Modern Next.js application development
- Component library creation
- Rapid prototyping with production-quality output
- Standardized development workflows

**Technical Leaders**
- Architecture reviews with modern web patterns
- Performance optimization for React/Next.js apps
- Code quality improvement with TypeScript
- Team knowledge sharing with consistent patterns

**Enterprise**
- Zero-cost UI development
- Self-contained development stack
- Compliance-friendly open source approach
- Scalable component architecture

## 🎯 Suitability

**Perfect fit for:**
- ✅ Modern web development with React/Next.js
- ✅ Teams wanting zero-cost UI generation
- ✅ TypeScript-first development approaches
- ✅ Enterprise environments requiring self-contained tools
- ✅ Projects needing accessible, production-ready components

**May not suit:**
- ❌ Legacy web frameworks (PHP, jQuery, etc.)
- ❌ Non-web development projects
- ❌ Teams committed to other CSS frameworks

## 🚦 Internal Quick Tool Guide

1. **Verify Claude Access**
   ```bash
   # Claude automatically reads .claude/CLAUDE.md and gains access to:
   # - 19 specialized commands
   # - Next.js + Tailwind templates  
   # - Enhanced development capabilities
   ```

2. **Start Building**
   ```bash
   /load                                           # Load project context
   /analyze --code --think                         # Test analysis capabilities
   /build --nextjs --tailwind --shadcn            # Generate Next.js components
   ```

3. **Example Modern Workflow**
   ```bash
   /design --nextjs --app-architecture            # Architecture design
   /build --nextjs --tailwind --shadcn --forms    # Implementation
   /test --coverage --e2e                         # Quality assurance
   /deploy --env staging --plan                   # Deployment
   ```

## 🛟 Helpful Information

- **Command Reference**: Check `.claude/commands/` for all available tools
- **Template Library**: Explore `.claude/templates/nextjs-tailwind/` for components
- **Configuration**: Review `.claude/CLAUDE.md` for Claude's capabilities

**📊 Framework Details:**
- **Commands**: 19 specialized commands (unchanged)
- **Personas**: 9 cognitive approaches (unchanged)
- **UI Generation**: Next.js + Tailwind CSS
- **Templates**: 50+ components and patterns
- **Methodology**: Evidence-based approach (enhanced)
- **Usage**: Modern web development teams

## 🎉 Enhance AI Capabilities

**Claude Toolkit** provides a structured approach to using `Claude Code` with specialized commands, personas, and modern Next.js + Tailwind CSS development patterns - completely free and self-contained.

## 💳 References and Credits

### **Attribution**
**Claude Toolkit** is built upon and adapted from [SuperClaude](https://github.com/NomenAK/SuperClaude) by @NomenAK, released under MIT License. 

### **What We Adapted**
- **Command Architecture**: Core structure of the 19 specialized commands
- **Cognitive Personas**: Framework for 9 specialized thinking modes  
- **Configuration System**: Modular @include template system and .yml configuration files
- **Token Economy**: Advanced token optimization and UltraCompressed mode
- **MCP Integration**: Model Context Protocol integration patterns

### **Our Contributions**
- **Removed Magic MCP Server**: Replaced the paid Magic MCP server integration with Next.js + Tailwind CSS for zero-cost UI generation
- **Next.js + Tailwind Focus**: Replaced generic React with Next.js + Tailwind CSS + shadcn/ui
- **Context Engineering Integration**: Adapted for Three-Document Pattern methodology
- **Local Template System**: Zero-cost UI generation without external dependencies
- **Framework Commands**: Added `/generate_design` and `/execute_project` for context engineering workflows

### **Legal Compliance**
This adaptation maintains full compliance with SuperClaude's MIT License terms. All original copyright and license terms are preserved. The SuperClaude project enables derivative works and modifications under MIT License, which this project follows.

---

*Claude Toolkit v1.0.0 – Comprehensive Claude Development Framework*