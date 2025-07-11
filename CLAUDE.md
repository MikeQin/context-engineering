# Context Engineering Framework Repository

## Repository Purpose

This is **The Three-Document Pattern Context Engineering Framework** - a systematic framework for AI-assisted development that transforms unreliable AI experimentation into predictable, professional delivery.

**Critical Distinction**: This repository serves framework development, not user projects. Users copy templates from `framework/` to their projects.

## Repository Architecture

### Core Components
- **`.claude/`** - Internal toolkit (21 commands, templates, configuration) - **Framework Core**
- **`framework/`** - User-facing templates and methodology - **User Interface**  
- **`example/`** - Real-world usage demonstration (Tetris game) - **Validation**
- **`docs/`** - Design decisions, methodology articles, and token-saving guides - **Documentation**
- **`toolkit/`** - Internal toolkit documentation - **Internal Docs**
- **`install.sh`** - MCP server installer (optional) - **Distribution**

### Key Relationships
- `.claude/CLAUDE.md` provides enhanced capabilities (21 commands, personas, templates, token-saving modes)
- `framework/CLAUDE.md` is user template for project methodology
- Examples must demonstrate current framework capabilities including token optimization
- Documentation must stay synchronized across all levels
- Token-saving documentation spans multiple directories (README.md, docs/, toolkit/)

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
- Token-saving mode support must be universal across all commands
- Training materials must reflect current implementation capabilities

## Development Standards

### Framework Quality Standards
- **Evidence-Based Methodology**: Documentation and validation required
- **Zero Dependencies**: Local generation without external API costs
- **Backward Compatibility**: Maintain compatibility for existing users
- **Cross-Component Testing**: Validate changes across multiple scenarios
- **Template Synchronization**: Keep internal and user-facing components aligned
- **Token Optimization**: Systematic approach to cost reduction while maintaining quality

### Technology Stack
- **Next.js + Tailwind CSS**: Modern web development with shadcn/ui components
- **Python CLI**: Click, Typer, argparse framework support
- **MCP Integration**: Optional Model Context Protocol server support
- **Configuration System**: Modular @include pattern for maintainability

### Architecture Patterns
- **Modular Configuration**: @include references throughout .claude/CLAUDE.md
- **Command-Based Architecture**: 21 specialized commands with flag inheritance
- **Template-Driven Development**: Production-ready components and CLI patterns
- **Separation of Concerns**: Clear distinction between internal toolkit and user templates
- **Token-Saving Architecture**: Three-mode system for optimal token usage (Standard, Token-Saving, Minimal)

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
- **Token-Saving Documentation**: Comprehensive guides for mode selection, symbol system, and team adoption

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
- Ensure token-saving mode compatibility across all commands
- Update team adoption and training materials

---

## Recent Updates (2025-07-10)

### Token-Saving Feature Implementation
- **Three-Mode System**: Standard (--verbose), Token-Saving (--token-saving), Minimal (--minimal)
- **Universal Flag Inheritance**: All 21 commands support token-saving modes
- **Production Development Guidance**: Clear recommendations for initial vs experienced production usage
- **Symbol System Training**: Comprehensive training materials for Minimal mode adoption
- **Team Adoption Strategy**: Enterprise-scale deployment methodology
- **Automation Recommendations**: AI-powered mode selection framework

### Documentation Enhancements
- **README.md**: Added comprehensive token-saving section with best practices
- **docs/DESIGN_DECISIONS.md**: Decision #002 documenting token-saving architecture
- **toolkit/SYMBOL_SYSTEM_TRAINING.md**: Internal training guide for framework optimization
- **docs/MODE_SELECTION_AUTOMATION.md**: Intelligent mode selection recommendations
- **docs/TEAM_ADOPTION_STRATEGY.md**: Systematic team and enterprise adoption guide
- **toolkit/README.md**: Updated with smart token-saving modes section

### Technical Implementation
- **flag-inheritance.yml**: Added complete token-saving flags to Universal_Always
- **execute_project.md**: Added universal flag inheritance
- **generate_design.md**: Added universal flag inheritance
- **Quality Validation**: Verified token-saving implementation across all framework components

### Framework Core Commands Usage Examples
```bash
# Standard Development Workflow (comprehensive explanations)
/generate_design --verbose ./my-project/PRODUCT_PRP.md
/execute_project --verbose ./my-project

# Production Development Workflow (50-70% token reduction)  
/generate_design --token-saving ./my-project/PRODUCT_PRP.md
/execute_project --token-saving ./my-project

# Expert Development Workflow (70-85% token reduction)
/generate_design --minimal ./my-project/PRODUCT_PRP.md
/execute_project --minimal ./my-project

# Framework Testing and Validation
/generate_design --token-saving ./example/TETRIS_PRP.md
/execute_project --token-saving ./example
```

---

**Framework Development Repository** | **Three-Document Pattern Context Engineering Framework v1.0.0** | **Repository for framework maintenance and improvement** | **Token-Saving Modes: 50-85% cost reduction**