# Product Requirements Prompt (PRP) - CLI Application Template

> **Getting Started with this CLI Template**:
> 1. Clone the framework: `git clone [framework-repo-url]`
> 2. Create your project folder: `mkdir your-cli-app`
> 3. Copy this template: `cp framework/PRODUCT_PRP_CLI.md your-cli-app/`
> 4. Replace all `[PLACEHOLDER]` content with your specific CLI application details
> 5. Delete this instruction block when creating your actual PRP
> 6. Generate your architecture: `/generate_design ./your-cli-app/PRODUCT_PRP_CLI.md`
> 7. Execute your implementation: `/execute_project ./your-cli-app`
> 8. Deploy your production-ready CLI tool!

## Product Information

**Product Name**: `[CLI_TOOL_NAME]`

> **Usage**: This CLI tool name will be used throughout the documentation and as the command name. Use clear, descriptive names like "DataProcessor", "APIClient", or "DevTools". Avoid spaces - use kebab-case for multi-word tools.

## Product Objectives

Build `[CLI_TOOL_NAME]` - a command-line interface tool that [primary function] for [target users].

**Example patterns:**
- Build a CLI tool that processes [data type] files for [user group]
- Create a command-line utility to automate [task] in [domain/workflow]
- Develop a CLI client for [API/service] that enables [key capability]

## Project Location

Please create a subfolder named `[project-name]` to contain all code and artifacts of `[CLI_TOOL_NAME]`.

**CLI Naming conventions:**
- Use kebab-case: `my-cli-tool`
- Keep it short but descriptive
- Consider the command users will type: `my-tool --help`

## Command Structure & Interface

### Primary Command
**Base Command**: `[CLI_TOOL_NAME]` or `[SHORT_ALIAS]`

**Usage Pattern**: 
```bash
[CLI_TOOL_NAME] [COMMAND] [OPTIONS] [ARGUMENTS]
```

### Core Commands (MVP)
[List the essential commands needed for your CLI tool]

- **`[command1]`**: [Brief description of functionality and expected arguments]
- **`[command2]`**: [Brief description of functionality and expected arguments]  
- **`[command3]`**: [Brief description of functionality and expected arguments]

**Example Command Structures:**
```bash
[CLI_TOOL_NAME] process --input file.txt --output result.txt
[CLI_TOOL_NAME] config set api-key "your-key-here"
[CLI_TOOL_NAME] status --format json
```

### Global Options
[Define options that work across all commands]

- **`--verbose, -v`**: Enable verbose output
- **`--quiet, -q`**: Suppress non-essential output
- **`--config, -c`**: Specify custom configuration file
- **`--help, -h`**: Show help information
- **`--version`**: Display version information

### Advanced Commands (Future Phases)
[Optional: List commands for future development phases]

- **`[advanced_command1]`**: [Description]
- **`[advanced_command2]`**: [Description]

## User Experience Requirements

### Target Users
**Primary Users**: [Who will use this CLI tool? e.g., developers, system administrators, data analysts]

**Technical Level**: [Beginner/Intermediate/Advanced users]

**Usage Context**: [Where and how will they use it? e.g., CI/CD pipelines, daily workflows, automation scripts]

### User Workflows
[Describe the main workflows users will perform]

**Primary Workflow**:
1. User installs `[CLI_TOOL_NAME]`
2. User configures [initial setup if needed]
3. User runs `[CLI_TOOL_NAME] [main_command]` with [arguments]
4. Tool processes [input] and provides [output]
5. User can [follow-up actions]

**Error Handling**:
- Clear, actionable error messages
- Helpful suggestions for common mistakes
- Exit codes that follow UNIX conventions (0 = success, non-zero = error)

**Help and Documentation**:
- Built-in help system with `--help` flag
- Usage examples for each command
- Clear option descriptions and defaults

## Technical Stack and Specifications

### CLI Framework Technology
**Recommended**: Python with Click/Typer or Node.js with Commander.js

**Options:**
- **Python + Click**: Mature, feature-rich CLI framework with decorators
- **Python + Typer**: Modern CLI framework with type hints and autocompletion
- **Python + argparse**: Built-in, lightweight option for simple CLIs
- **Node.js + Commander.js**: JavaScript-based CLI with good ecosystem
- **Go + Cobra**: Fast, compiled binaries with excellent performance
- **Rust + clap**: High-performance, memory-safe CLI applications

**Reasoning**: [Explain why you chose this technology stack]

### Core Dependencies
[List essential libraries and their purposes]

- **CLI Framework**: [chosen framework for command parsing]
- **Configuration**: [config file handling - YAML, JSON, TOML]
- **Output Formatting**: [rich text, tables, progress bars]
- **HTTP Client**: [if API integration needed]
- **File Processing**: [if file operations required]

### Input/Output Specifications

**Input Sources**:
- [Command-line arguments and options]
- [Configuration files - specify format and location]
- [Standard input (stdin) support if applicable]
- [File inputs - specify supported formats]

**Output Formats**:
- [Default human-readable output format]
- [Structured output options: JSON, YAML, CSV]
- [Logging and error output to stderr]

**File Handling**:
- [File types the CLI will process]
- [Output file generation capabilities]
- [Temporary file management if needed]

## Configuration Management

### Configuration Sources
[Define how the CLI tool will be configured]

**Priority Order** (highest to lowest):
1. Command-line options
2. Environment variables
3. Configuration file
4. Default values

**Configuration File**:
- **Location**: `~/.config/[CLI_TOOL_NAME]/config.[yaml|json|toml]`
- **Format**: [Choose: YAML, JSON, or TOML]
- **Sections**: [List main configuration sections]

**Environment Variables**:
- **Prefix**: `[CLI_TOOL_NAME]_` or `[SHORT_PREFIX]_`
- **Key Variables**: [List important environment variables]

### Configuration Examples
```yaml
# Example config file structure
api:
  endpoint: "https://api.example.com"
  timeout: 30
  retries: 3

output:
  format: "table"
  color: true
  verbose: false

[other_sections]:
  [key]: [value]
```

## Distribution and Installation

### Package Distribution
**Primary Method**: [Choose primary distribution method]

**Options:**
- **PyPI Package**: `pip install [CLI_TOOL_NAME]` (for Python CLIs)
- **npm Package**: `npm install -g [CLI_TOOL_NAME]` (for Node.js CLIs)
- **Homebrew**: `brew install [CLI_TOOL_NAME]` (for macOS)
- **GitHub Releases**: Direct binary downloads
- **Docker Image**: Containerized distribution
- **Package Managers**: apt, yum, pacman for Linux distributions

### Installation Requirements
**System Requirements**:
- **Operating Systems**: [Windows/macOS/Linux support]
- **Runtime Requirements**: [Python 3.8+, Node.js 16+, etc.]
- **Dependencies**: [External tools or libraries required]

**Installation Command**:
```bash
# Primary installation method
[installation_command]

# Alternative methods
[alternative_installations]
```

## Development Requirements

### Project Structure
[Define the CLI project organization]

```
[CLI_TOOL_NAME]/
├── src/[cli_package]/
│   ├── __init__.py
│   ├── __main__.py          # Entry point for python -m [package]
│   ├── cli.py               # Main CLI interface
│   ├── commands/            # Command implementations
│   │   ├── __init__.py
│   │   ├── command1.py
│   │   └── command2.py
│   ├── config/              # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── helpers.py
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_commands/
├── docs/                    # Documentation
│   ├── installation.md
│   ├── usage.md
│   └── api.md
├── pyproject.toml           # Package configuration
├── README.md                # Project overview and quick start
├── LICENSE                  # Software license
└── .env.example             # Environment variables template
```

### Quality Assurance Standards
[Define quality gates and testing requirements]

- **Code Quality**: Linting with [tool] and formatting with [tool]
- **Testing Strategy**: Unit tests for all commands, integration tests for workflows
- **CLI Testing**: Test all command combinations and error scenarios
- **Documentation**: Comprehensive help text and usage examples
- **Performance**: Command execution time requirements

## Security Requirements

### Input Validation
- Sanitize all user inputs and file paths
- Validate configuration values and ranges
- Prevent injection attacks in shell commands

### Credential Management
- Secure storage of API keys and tokens
- Support for credential files with proper permissions
- Environment variable fallbacks for CI/CD

### File System Security
- Restrict file access to intended directories
- Validate file permissions before operations
- Safe handling of temporary files

## Testing Strategy

### CLI Testing Approaches
[Define how to test the CLI application]

**Unit Testing**:
- Test individual command functions
- Mock external dependencies (APIs, file system)
- Test configuration parsing and validation

**Integration Testing**:
- Test complete command workflows
- Test configuration file loading
- Test output formatting and error handling

**CLI Functional Testing**:
- Test command-line argument parsing
- Test help text and usage information
- Test exit codes and error messages

**Performance Testing**:
- Test with large input files
- Test command execution time limits
- Test memory usage with large datasets

## Acceptance Criteria

`[CLI_TOOL_NAME]` is complete when:

- [ ] All core commands work correctly with expected arguments
- [ ] Help system provides clear usage information for all commands
- [ ] Configuration system works with all specified sources
- [ ] Error handling provides helpful messages and correct exit codes
- [ ] Installation and distribution packages work on target platforms
- [ ] All tests pass with adequate coverage (>80%)
- [ ] Documentation is complete and accurate
- [ ] Performance requirements are met
- [ ] Security requirements are satisfied

## Success Metrics

### Functionality Metrics
- All core commands execute successfully
- Configuration loading works from all sources
- Help system covers all commands and options
- Error handling covers all failure scenarios

### Performance Metrics
- Command startup time: [< X seconds]
- File processing speed: [X files/records per second]
- Memory usage: [< X MB for typical operations]

### User Experience Metrics
- Help text clarity and completeness
- Error message usefulness
- Installation success rate
- User workflow completion rate

## Development Guidance

### Architecture and Design Process
- Before implementation, create the CLI architecture and present it for review
- Design command structure and option parsing before coding
- Plan configuration system and file handling strategies
- Follow established patterns from CLAUDE.md for code organization

### CLI-Specific Best Practices
- Follow UNIX CLI conventions and standards
- Provide consistent command structure across all subcommands
- Implement proper signal handling (SIGINT, SIGTERM)
- Use appropriate exit codes for different scenarios
- Support common patterns like pipes and redirection
- Provide machine-readable output options
- Include progress indicators for long-running operations