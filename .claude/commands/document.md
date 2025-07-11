**Purpose**: Professional documentation creation

---

@include shared/universal-constants.yml#Universal_Legend

## Command Execution
Execute: immediate. --plan→show plan first
Legend: Generated based on symbols used in command
Purpose: "[Action][Subject] in $ARGUMENTS"

Generate comprehensive documentation for code, APIs, or systems specified in $ARGUMENTS.

@include shared/flag-inheritance.yml#Universal_Always

Examples:
- `/document --type api --format openapi` - Generate API documentation
- `/document --type readme --style detailed` - Create comprehensive README
- `/document --type user --style tutorial` - User guide w/ tutorials
- `/document --cli --help-generation` - CLI help text and man pages
- `/document --cli --user-guide --style tutorial` - CLI user documentation
- `/document --session-summary` - Generate professional session documentation

Documentation modes:

**--type:** Documentation type
- api: API documentation (OpenAPI/Swagger) | code: Code documentation (JSDoc/docstrings)
- readme: Project README files | architecture: System architecture docs
- user: End-user documentation | dev: Developer guides
- cli: CLI-specific documentation (help text, man pages, usage guides)

**--format:** Output format  
- markdown: Markdown format (default) | html: HTML documentation
- pdf: PDF output | docusaurus: Docusaurus compatible | mkdocs: MkDocs compatible

**--style:** Documentation style
- concise: Brief, essential information only | detailed: Comprehensive with examples
- tutorial: Step-by-step guide format | reference: API reference style

**--cli:** CLI application documentation
- w/ --help-generation: Generate comprehensive help text and usage information
- Create man pages & command reference | Document configuration options | Generate installation guides

**--help-generation:** Generate CLI help systems
- w/ --man-pages: Create Unix man pages | w/ --completion: Shell completion documentation
- Auto-generate help text from code | Create usage examples | Document command hierarchies

**--user-guide:** Create user-facing CLI documentation
- w/ --installation: Include installation instructions | w/ --examples: Rich usage examples
- Create getting started guides | Document common workflows | Include troubleshooting sections

**--session-summary:** Generate professional session documentation
- **Default Location**: `./docs/sessions/SESSION_YYYY-MM-DD_HHMMSS.md`
- **Auto-Create Directories**: Creates `docs/sessions/` if not exists
- **Professional Format**: Executive summary, technical details, business impact, next steps
- **Context Preservation**: Session continuation instructions and current state documentation
- **Flags**:
  - `--output`: Custom output file path (overrides default location)
  - `--name`: Custom filename (uses timestamp if not specified)
  - `--format`: Output format (markdown default, html, pdf available)

@include shared/docs-patterns.yml#Project_Documentation

## CLI Documentation Patterns

**CLI Help Systems:**
- Command-line help text generation with proper formatting
- Interactive help with examples and usage patterns
- Context-sensitive help for subcommands and options
- Auto-generation from docstrings and type annotations

**CLI User Documentation:**
- Installation guides for different platforms and package managers
- Getting started tutorials with step-by-step examples
- Configuration documentation with file formats and precedence
- Troubleshooting guides for common issues and error messages

**CLI Reference Documentation:**
- Complete command reference with all options and arguments
- Configuration file schema and validation rules
- API documentation for programmatic usage
- Plugin/extension development guides

@include shared/docs-patterns.yml#Standard_Notifications

@include shared/universal-constants.yml#Standard_Messages_Templates