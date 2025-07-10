# Context Engineering Framework Repository

## Repository Purpose

This is **The Three-Document Pattern Context Engineering Framework** - a systematic framework for AI-assisted development that transforms unreliable AI experimentation into predictable, professional delivery.

**Critical Distinction**: This repository serves framework development, not user projects. Users copy templates from `framework/` to their projects.

## Repository Architecture

### Core Components
- **`.claude/`** - Internal toolkit (19 commands, templates, configuration) - **Framework Core**
- **`framework/`** - User-facing templates and methodology - **User Interface**  
- **`examples/`** - Real-world usage demonstration (Tetris game) - **Validation**
- **`docs/`** - Design decisions and methodology articles - **Documentation**
- **`toolkit/`** - Internal toolkit documentation - **Internal Docs**
- **`install.sh`** - MCP server installer (optional) - **Distribution**

### Key Relationships
- `.claude/CLAUDE.md` provides enhanced capabilities (19 commands, personas, templates)
- `framework/CLAUDE.md` is user template for project methodology
- Examples must demonstrate current framework capabilities
- Documentation must stay synchronized across all levels

## Development Context

### Framework vs User Project
- **Framework Development** (this repository): Focus on maintaining and improving the framework itself
- **User Project Development** (user projects): Focus on building applications using the framework

### Critical Consistency Requirements
- Changes to internal toolkit must align with user templates
- Template updates must maintain accessibility and TypeScript compatibility
- Command modifications require documentation updates
- Examples must remain current with framework changes
- Cross-component validation required

## Development Standards

### Framework Quality Standards
- **Evidence-Based Methodology**: Documentation and validation required
- **Zero Dependencies**: Local generation without external API costs
- **Backward Compatibility**: Maintain compatibility for existing users
- **Cross-Component Testing**: Validate changes across multiple scenarios
- **Template Synchronization**: Keep internal and user-facing components aligned

### Technology Stack
- **Next.js + Tailwind CSS**: Modern web development with shadcn/ui components
- **Python CLI**: Click, Typer, argparse framework support
- **MCP Integration**: Optional Model Context Protocol server support
- **Configuration System**: Modular @include pattern for maintainability

### Architecture Patterns
- **Modular Configuration**: @include references throughout .claude/CLAUDE.md
- **Command-Based Architecture**: 19 specialized commands with flag inheritance
- **Template-Driven Development**: Production-ready components and CLI patterns
- **Separation of Concerns**: Clear distinction between internal toolkit and user templates

## Working with this Repository

### Development Workflow
1. **Understand Impact**: Changes affect all framework users
2. **Validate Across Components**: Test internal toolkit, user templates, examples
3. **Maintain Documentation**: Update README.md, docs/, and toolkit/ as needed
4. **Version Compatibility**: Handle breaking changes with migration guides
5. **Cross-Reference Updates**: Keep all CLAUDE.md files synchronized

### Quality Assurance
- **Framework Changes**: Validate across multiple scenarios
- **Template Updates**: Maintain accessibility and TypeScript compatibility
- **Command Modifications**: Update documentation and examples
- **MCP Integration**: Test with and without MCP servers
- **Example Maintenance**: Ensure examples demonstrate current capabilities

### Contribution Guidelines
- **Framework Consistency**: Align changes with existing patterns
- **Documentation First**: Update docs before implementing changes
- **Backward Compatibility**: Maintain existing user workflows
- **Testing Strategy**: Validate framework changes across different scenarios
- **Cross-Component Validation**: Test internal toolkit, templates, and examples

## Repository Maintenance

### Documentation Management
- **Multiple Audiences**: Framework developers, users, contributors
- **Synchronized Updates**: Keep README.md, docs/, toolkit/ aligned
- **Version Management**: Handle framework versioning and releases
- **Template Maintenance**: Manage Next.js + Tailwind templates and CLI patterns

### Technical Considerations
- **Internal Toolkit**: .claude/ directory provides enhanced Claude capabilities
- **User Templates**: framework/ directory contains templates users copy to projects
- **Active Development**: Many modified files suggest ongoing improvements
- **Compatibility**: Maintain compatibility between internal toolkit and user templates

## Best Practices

### When Working on Framework
- Always consider user impact of changes
- Test across multiple project types (web, CLI, API)
- Maintain template consistency and accessibility
- Update documentation proactively
- Validate MCP integration compatibility

### When Adding Features
- Follow modular configuration patterns
- Maintain flag inheritance system
- Update command documentation
- Add appropriate examples
- Consider cross-component interactions

---

**Framework Development Repository** | **Three-Document Pattern Context Engineering Framework v1.0.0** | **Repository for framework maintenance and improvement**