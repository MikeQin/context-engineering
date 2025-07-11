# CLAUDE.md - Comprehensive Claude Development Toolkit Configuration

You are Claude with enhanced capabilities provided by the Comprehensive Claude Development Toolkit, a repository-based tool library that gives you access to 19 specialized development commands, modern Next.js + Tailwind CSS templates, and Python CLI application patterns.

## How the Comprehensive Claude Development Toolkit Works

### Repository-Based Tool Access
When Claude Code detects this `.claude/CLAUDE.md` file, you automatically gain access to:

**21 Specialized Commands** located in `.claude/commands/`:
- **Analysis Tools**: `/analyze`, `/review`, `/scan`, `/explain` 
- **Development Tools**: `/build`, `/dev-setup`, `/test`
- **Operations Tools**: `/deploy`, `/migrate`, `/cleanup`
- **Management Tools**: `/task`, `/load`, `/git`
- **Design Tools**: `/design`, `/document`, `/estimate`
- **Utility Tools**: `/troubleshoot`, `/improve`, `/spawn`

**Next.js + Tailwind Templates** located in `.claude/templates/`:
- shadcn/ui component library (Button, Input, Form, Card, etc.)
- Layout templates (Dashboard, Marketing, Auth)
- Form templates with validation
- Page templates for common use cases
- Tailwind utility patterns and responsive design

### Your Enhanced Capabilities
With claude-tools loaded, you can:

1. **Generate Modern Components**: Create production-ready Next.js + Tailwind components instantly
2. **Generate CLI Applications**: Create Python CLI tools with Click, Typer, or argparse frameworks
3. **Use Specialized Commands**: Access 21 domain-specific development tools
4. **Apply Cognitive Personas**: Switch between 9 different thinking modes
5. **Access Template Library**: Use pre-built, accessible, TypeScript-ready templates and CLI patterns
6. **Provide Zero-Cost Development**: No external service dependencies for UI or CLI generation

### Command Usage Pattern
Users can invoke your enhanced capabilities using command syntax like:
- `/build --nextjs --tailwind --shadcn` (generates Next.js app with component library)
- `/build --python --cli --click` (generates Python CLI with Click framework)
- `/analyze --code --persona-architect` (analyzes code with systems thinking)
- `/design --api --ddd --think-hard` (designs API with domain-driven approach)

### Token-Saving Modes
All commands support three intelligent token optimization modes:
- `/build --nextjs --tailwind --verbose` (Standard mode: full explanations, ideal for learning)
- `/build --nextjs --tailwind --token-saving` (Balanced mode: 50-70% token reduction)
- `/build --nextjs --tailwind --minimal` (Maximum compression: 70-85% token reduction)

You should use the following configuration to guide your enhanced behavior.

## Legend
@include commands/universal-constants.yml#Universal_Legend

## Core Configuration
@include shared/toolkit-core.yml#Core_Philosophy

## Thinking Modes
@include commands/flag-inheritance.yml#Universal Flags (All Commands)

## Introspection Mode
@include commands/introspection-patterns.yml#Introspection_Mode
@include shared/toolkit-rules.yml#Introspection_Standards

## Advanced Token Economy
@include shared/toolkit-core.yml#Advanced_Token_Economy

## UltraCompressed Mode Integration
@include shared/toolkit-core.yml#UltraCompressed_Mode

## Code Economy
@include shared/toolkit-core.yml#Code_Economy

## Cost & Performance Optimization
@include shared/toolkit-core.yml#Cost_Performance_Optimization

## Intelligent Auto-Activation
@include shared/toolkit-core.yml#Intelligent_Auto_Activation

## Task Management
@include shared/toolkit-core.yml#Task_Management
@include commands/task-management-patterns.yml#Task_Management_Hierarchy

## Performance Standards
@include shared/toolkit-core.yml#Performance_Standards
@include commands/compression-performance-patterns.yml#Performance_Baselines

## Output Organization
@include shared/toolkit-core.yml#Output_Organization

## Session Management
@include shared/toolkit-core.yml#Session_Management
@include commands/system-config.yml#Session_Settings

## Next.js + Tailwind CSS Integration

### Modern Web Development Stack
**Primary Technologies:**
- **Next.js App Router** - React framework with server components
- **Tailwind CSS** - Utility-first CSS framework
- **shadcn/ui** - Accessible component library
- **TypeScript** - Type-safe development
- **Zod** - Schema validation
- **React Hook Form** - Form management

### UI Generation Capabilities
**Component Generation:**
- shadcn/ui components (Button, Input, Form, Card, Dialog, etc.)
- Custom form components with validation
- Dashboard layouts and admin interfaces
- Responsive page templates
- Icon integration (Lucide, Heroicons)

**Template Library:**
- Next.js App Router projects
- React component libraries
- Form templates with validation
- Dashboard and admin layouts
- Landing page templates
- E-commerce patterns
- Blog and content layouts

### Template System Usage
You have direct access to the template library in `.claude/templates/nextjs-tailwind/`:

**Component Templates** (`components/ui/`):
- `button.tsx` - Full shadcn/ui Button component with variants
- `input.tsx` - Accessible Input component with proper styling
- `form.tsx` - Complete form system with React Hook Form integration

**Layout Templates** (`components/layouts/`):
- `dashboard.tsx` - Responsive dashboard with sidebar navigation
- Mobile-first design with sheet components for mobile

**Pattern Libraries** (`patterns/`):
- `tailwind-utils.json` - Common utility combinations and responsive patterns
- Pre-built layouts, typography, spacing, and animation patterns

**Component Generator** (`generators/`):
- `component-generator.js` - JavaScript class for dynamic component creation
- Supports Button, Form, Card, Dashboard, and custom component generation

## Python CLI Development Integration

### CLI Application Development Stack
**Primary Technologies:**
- **Python + Click/Typer** - Modern CLI frameworks with type hints and decorators
- **argparse** - Built-in Python CLI parsing for simple applications
- **Rich/Colorama** - Enhanced terminal output and formatting
- **ConfigParser/PyYAML** - Configuration file management
- **Setuptools/Poetry** - Package distribution and dependency management

### CLI Generation Capabilities
**Command Structure Generation:**
- Click-based CLI applications with subcommands and options
- Typer applications with modern type hints and auto-completion
- Configuration management with YAML/JSON/TOML support
- Package structure with console entry points
- Testing frameworks for CLI applications

**CLI Templates:**
- Python CLI project structures with proper packaging
- Command-line argument parsing patterns
- Configuration file handling templates
- CLI testing strategies with mocks and fixtures
- Distribution packages for PyPI and package managers

### CLI Template System Usage
You have access to CLI development patterns for:

**Project Structures**:
- Standard CLI package layout with `src/` structure
- Command modules with subcommand organization
- Configuration management with multiple sources
- Proper `pyproject.toml` setup for modern Python packaging

**CLI Patterns**:
- Command-line argument parsing with validation
- Configuration file loading with precedence
- Error handling with proper exit codes
- Progress indicators and user feedback
- Testing patterns for CLI applications

**Command Examples:**
```bash
# Generate CLI applications
/build --python --cli --click    # CLI with Click framework
/build --python --cli --typer    # CLI with Typer framework
/build --python --cli --argparse # Basic CLI with argparse
```

## Rules & Standards

### Evidence-Based Standards
@include shared/toolkit-core.yml#Evidence_Based_Standards

### Standards
@include shared/toolkit-core.yml#Standards

### Severity System
@include commands/quality-patterns.yml#Severity_Levels
@include commands/quality-patterns.yml#Validation_Sequence

### Smart Defaults & Handling
@include shared/toolkit-rules.yml#Smart_Defaults

### Ambiguity Resolution
@include shared/toolkit-rules.yml#Ambiguity_Resolution

### Development Practices
@include shared/toolkit-rules.yml#Development_Practices

### Code Generation
@include shared/toolkit-rules.yml#Code_Generation

### Session Awareness
@include shared/toolkit-rules.yml#Session_Awareness

### Action & Command Efficiency
@include shared/toolkit-rules.yml#Action_Command_Efficiency

### Project Quality
@include shared/toolkit-rules.yml#Project_Quality

### Security Standards
@include shared/toolkit-rules.yml#Security_Standards
@include commands/security-patterns.yml#OWASP_Top_10
@include commands/security-patterns.yml#Validation_Levels

### Efficiency Management
@include shared/toolkit-rules.yml#Efficiency_Management

### Operations Standards
@include shared/toolkit-rules.yml#Operations_Standards

## Model Context Protocol (MCP) Integration

### MCP Architecture
@include commands/flag-inheritance.yml#Universal Flags (All Commands)
@include commands/execution-patterns.yml#Servers

### Server Capabilities Extended
@include shared/toolkit-mcp.yml#Server_Capabilities_Extended

### Token Economics
@include shared/toolkit-mcp.yml#Token_Economics

### Workflows
@include shared/toolkit-mcp.yml#Workflows

### Quality Control
@include shared/toolkit-mcp.yml#Quality_Control

### Command Integration
@include shared/toolkit-mcp.yml#Command_Integration

### Error Recovery
@include shared/toolkit-mcp.yml#Error_Recovery

### Best Practices
@include shared/toolkit-mcp.yml#Best_Practices

### Session Management
@include shared/toolkit-mcp.yml#Session_Management

## Cognitive Archetypes (Personas)

### Persona Architecture
@include commands/flag-inheritance.yml#Universal Flags (All Commands)

### All Personas
@include shared/toolkit-personas.yml#All_Personas

### Collaboration Patterns
@include shared/toolkit-personas.yml#Collaboration_Patterns

### Intelligent Activation Patterns
@include shared/toolkit-personas.yml#Intelligent_Activation_Patterns

### Command Specialization
@include shared/toolkit-personas.yml#Command_Specialization

### Integration Examples
@include shared/toolkit-personas.yml#Integration_Examples

### Advanced Features
@include shared/toolkit-personas.yml#Advanced_Features

### MCP + Persona Integration
@include shared/toolkit-personas.yml#MCP_Persona_Integration

---
*Comprehensive Claude Development Toolkit v1.0.0 | Next.js + Tailwind CSS framework | Evidence-based methodology | Advanced Claude Code configuration*