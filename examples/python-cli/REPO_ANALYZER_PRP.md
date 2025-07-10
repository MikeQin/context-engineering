# Product Requirements Prompt (PRP) - Repo Analyzer CLI Tool

## Product Information

**Product Name**: `repo-analyzer`

**Product Type**: Python CLI Application

## Product Objectives

Build a comprehensive command-line repository analysis tool that helps developers understand code quality, patterns, dependencies, and metrics across any programming language repository. The tool should provide actionable insights for code maintenance, technical debt assessment, and project health monitoring.

## Project Location

Please create a subfolder named `repo-analyzer` to contain all code and artifacts of `repo-analyzer`.

## Features

### Core Features (MVP)

#### Analysis Commands
- **`analyze structure`** - Directory structure analysis, file organization patterns
- **`analyze dependencies`** - Package dependencies, imports, circular dependencies  
- **`analyze complexity`** - Code complexity metrics (cyclomatic, cognitive complexity)
- **`analyze quality`** - Code quality indicators, technical debt assessment
- **`analyze patterns`** - Design patterns, architectural patterns detection
- **`analyze security`** - Basic security scan for common vulnerabilities

#### Reporting Commands  
- **`report summary`** - High-level overview with key metrics
- **`report detailed`** - Comprehensive analysis report
- **`report compare`** - Compare analysis between different commits/branches
- **`report export`** - Export results to JSON, CSV, HTML formats

#### Configuration & Management
- **`config init`** - Initialize analysis configuration file
- **`config show`** - Display current configuration  
- **`config languages`** - Configure language-specific analysis rules
- **`history list`** - Show analysis history for repository
- **`history clean`** - Clean up old analysis data

### Advanced Features (Future Phases)

#### Enhanced Analysis
- **Real-time monitoring** - Watch mode for continuous analysis
- **Git integration** - Analyze changes between commits, blame analysis  
- **Multi-repository** - Analyze multiple repositories for portfolio insights
- **Team insights** - Contributor analysis, code ownership patterns
- **Performance metrics** - Identify performance bottlenecks and hotspots

#### Integrations
- **CI/CD integration** - GitHub Actions, GitLab CI workflow support
- **IDE plugins** - VS Code, PyCharm integration
- **Dashboard web UI** - Browser-based visualization of analysis results

## Technology Specifications

### Core Technology Stack
- **Framework**: Python with **Click** for CLI interface
- **Analysis Engine**: AST parsing with language-specific parsers
- **Configuration**: YAML-based configuration files with JSON schema validation
- **Output Formats**: JSON, CSV, HTML, terminal-formatted text
- **Testing**: pytest with comprehensive CLI testing strategies

### Language Support Priority
1. **Python** - Full AST analysis, import tracking, complexity metrics
2. **JavaScript/TypeScript** - Module analysis, dependency tracking
3. **Java** - Package structure, class relationships
4. **Go** - Module analysis, interface patterns
5. **Rust** - Crate analysis, ownership patterns
6. **C/C++** - Header dependencies, complexity analysis

### Data Storage & Caching
- **Local SQLite database** for analysis history and caching
- **Configuration files** in `~/.repo-analyzer/` directory
- **Temporary analysis cache** for incremental updates
- **Export capabilities** to external databases (PostgreSQL, MySQL)

## User Experience & Interface

### Command Line Interface Design
```bash
# Primary workflow
repo-analyzer analyze structure ./my-project
repo-analyzer analyze dependencies ./my-project --language python
repo-analyzer report summary ./my-project
repo-analyzer report export ./my-project --format html --output ./reports/

# Configuration management
repo-analyzer config init ./my-project
repo-analyzer config languages --enable python,javascript --disable java

# Historical tracking
repo-analyzer history list ./my-project
repo-analyzer analyze quality ./my-project --compare-with HEAD~10
```

### Configuration File Structure
```yaml
# .repo-analyzer.yml
project:
  name: "My Project"
  languages: ["python", "javascript"]
  exclude_patterns: ["*.pyc", "node_modules/", ".git/"]

analysis:
  complexity:
    cyclomatic_threshold: 10
    cognitive_threshold: 15
  quality:
    min_test_coverage: 80
    max_line_length: 120
  dependencies:
    check_vulnerabilities: true
    track_licenses: true

output:
  default_format: "terminal"
  reports_directory: "./reports"
  include_history: true
```

### Output Examples
```bash
# Terminal output
Repository Analysis Summary
==========================
📁 Structure:    156 files, 23 directories
🐍 Languages:    Python (78%), JavaScript (22%)
📊 Complexity:   Average: 4.2, Max: 15 (moderate)
🔍 Quality:      Score: 8.2/10 (good)
⚠️  Issues:      3 high, 12 medium, 45 low
📦 Dependencies: 23 direct, 156 total (2 vulnerable)

Top Issues:
  🔴 High complexity in src/parser.py:45 (complexity: 15)
  🟡 Unused import in utils/helpers.py:12
  🟡 Long function in main.py:156 (85 lines)
```

## Technical Architecture

### CLI Command Structure
```
repo-analyzer/
├── src/
│   ├── repo_analyzer/
│   │   ├── __init__.py
│   │   ├── __main__.py              # Entry point for python -m repo_analyzer
│   │   ├── cli.py                   # Main CLI interface with Click
│   │   ├── commands/                # Individual command implementations
│   │   │   ├── __init__.py
│   │   │   ├── analyze.py          # Analysis command group
│   │   │   ├── report.py           # Reporting command group  
│   │   │   ├── config.py           # Configuration management
│   │   │   └── history.py          # History management
│   │   ├── analyzers/              # Language-specific analyzers
│   │   │   ├── __init__.py
│   │   │   ├── base.py             # Abstract base analyzer
│   │   │   ├── python_analyzer.py  # Python AST analysis
│   │   │   ├── js_analyzer.py      # JavaScript analysis
│   │   │   └── generic_analyzer.py # Generic file analysis
│   │   ├── reports/                # Report generation
│   │   │   ├── __init__.py
│   │   │   ├── generators.py       # Report format generators
│   │   │   ├── templates/          # HTML/text templates
│   │   │   └── formatters.py       # Output formatting utilities
│   │   ├── config/                 # Configuration management
│   │   │   ├── __init__.py
│   │   │   ├── settings.py         # Configuration loading/validation
│   │   │   └── schemas.py          # JSON schema definitions
│   │   ├── storage/                # Data persistence
│   │   │   ├── __init__.py
│   │   │   ├── database.py         # SQLite database operations
│   │   │   └── models.py           # Data models
│   │   └── utils/                  # Utility functions
│   │       ├── __init__.py
│   │       ├── file_utils.py       # File operations
│   │       ├── git_utils.py        # Git integration
│   │       └── metrics.py          # Metric calculations
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── conftest.py                 # pytest configuration
│   ├── test_cli.py                 # CLI testing with click.testing
│   ├── test_analyzers/             # Analyzer unit tests
│   ├── test_reports/               # Report generation tests
│   └── fixtures/                   # Test data and repositories
├── pyproject.toml                  # Modern Python packaging
├── README.md                       # User documentation
├── CHANGELOG.md                    # Version history
└── requirements/                   # Dependency management
    ├── base.txt                    # Core dependencies
    ├── dev.txt                     # Development dependencies
    └── test.txt                    # Testing dependencies
```

### Core Dependencies
```toml
[project]
dependencies = [
    "click>=8.0.0",          # CLI framework
    "rich>=13.0.0",          # Terminal formatting and progress bars
    "pyyaml>=6.0.0",         # Configuration file parsing
    "gitpython>=3.1.0",      # Git repository interaction
    "jsonschema>=4.0.0",     # Configuration validation
    "sqlalchemy>=2.0.0",     # Database ORM
    "jinja2>=3.1.0",         # HTML report templating
    "toml>=0.10.0",          # TOML configuration support
    "pathspec>=0.11.0",      # gitignore pattern matching
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",        # Testing framework
    "pytest-cov>=4.0.0",    # Coverage reporting
    "black>=23.0.0",        # Code formatting
    "ruff>=0.1.0",          # Linting and formatting
    "mypy>=1.0.0",          # Type checking
]

[project.scripts]
repo-analyzer = "repo_analyzer.cli:main"
```

## Quality & Testing Strategy

### Testing Requirements
- **Unit Tests**: 90%+ code coverage for all analyzers and utilities
- **Integration Tests**: CLI command testing with various repository types
- **End-to-End Tests**: Full workflow testing with real repository samples
- **Performance Tests**: Analysis speed benchmarks for large repositories

### Code Quality Standards
- **Type Hints**: Full type annotation with mypy validation
- **Documentation**: Comprehensive docstrings and user documentation
- **Error Handling**: Graceful error handling with helpful user messages
- **Logging**: Structured logging for debugging and monitoring

## Distribution & Deployment

### Package Distribution
- **PyPI Package**: `pip install repo-analyzer` for end users
- **Homebrew Formula**: `brew install repo-analyzer` for macOS users  
- **Docker Image**: `docker run repo-analyzer` for containerized usage
- **GitHub Releases**: Binary distributions for major platforms

### Installation Methods
```bash
# Primary installation method
pip install repo-analyzer

# Development installation
git clone <repository>
cd repo-analyzer
pip install -e ".[dev]"

# Docker usage
docker run --rm -v $(pwd):/workspace repo-analyzer analyze structure /workspace
```

## Usage Examples & Workflows

### Quick Start Workflow
```bash
# Initialize configuration for a project
cd my-project
repo-analyzer config init

# Perform basic analysis
repo-analyzer analyze structure
repo-analyzer analyze dependencies
repo-analyzer report summary

# Generate comprehensive report
repo-analyzer report detailed --format html --output ./analysis-report.html
```

### Advanced Workflow
```bash
# Continuous monitoring setup
repo-analyzer analyze quality --watch --threshold-file .quality-thresholds.yml

# Historical comparison
repo-analyzer analyze complexity --compare-with v1.0.0 --format json

# Multi-format reporting
repo-analyzer report export --format json,csv,html --output ./reports/
```

### CI/CD Integration Example
```yaml
# .github/workflows/code-analysis.yml
name: Code Analysis
on: [push, pull_request]
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - name: Install repo-analyzer
      run: pip install repo-analyzer
    - name: Analyze repository
      run: |
        repo-analyzer analyze quality --fail-on-regression
        repo-analyzer report export --format json --output analysis.json
    - name: Upload analysis results
      uses: actions/upload-artifact@v3
      with:
        name: analysis-results
        path: analysis.json
```

## Success Metrics

### Functional Success Criteria
- **Analysis Accuracy**: 95%+ accurate detection of code patterns and issues
- **Performance**: Analyze 10,000+ file repositories within 30 seconds
- **Language Coverage**: Support for 6+ programming languages at launch
- **Report Quality**: Actionable insights with clear remediation suggestions

### User Experience Success Criteria  
- **Ease of Installation**: One-command installation via pip
- **Learning Curve**: New users productive within 15 minutes
- **Documentation Quality**: Complete user guide with examples
- **Error Handling**: Clear, actionable error messages for all failure cases

### Technical Success Criteria
- **Code Quality**: 90%+ test coverage, type-safe implementation
- **Extensibility**: Plugin architecture for custom analyzers
- **Compatibility**: Python 3.8+ support, cross-platform functionality
- **Maintenance**: Automated CI/CD with comprehensive testing

---

**Repo Analyzer CLI Tool**: A comprehensive repository analysis solution that transforms code understanding from manual inspection into systematic, automated insights for better software development practices.