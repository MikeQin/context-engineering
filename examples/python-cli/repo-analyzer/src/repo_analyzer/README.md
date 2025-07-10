# Repo Analyzer

🔍 **Comprehensive repository analysis tool for code quality, patterns, dependencies, and metrics**

Repo Analyzer is a powerful command-line tool that provides deep insights into your codebase across multiple programming languages. It helps developers understand code quality, identify technical debt, and maintain consistent coding standards.

## ✨ Features

### 🏗️ **Structure Analysis**
- Directory organization and file distribution
- Programming language detection and statistics  
- Project size and complexity overview
- File type categorization and patterns

### 📦 **Dependency Analysis**
- Package manager detection (pip, npm, go mod, cargo, etc.)
- Direct and transitive dependency mapping
- Circular dependency detection
- Vulnerability scanning for known security issues

### 📊 **Code Quality Metrics**
- Cyclomatic complexity calculation
- Cognitive complexity assessment
- Maintainability index scoring
- Technical debt ratio analysis

### 📈 **Comprehensive Reporting**
- Terminal-formatted output with rich formatting
- JSON export for programmatic usage
- HTML reports with interactive visualizations
- CSV export for spreadsheet analysis
- Historical trend tracking and comparison

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install repo-analyzer

# Development installation
git clone <repository>
cd repo-analyzer
pip install -e ".[dev]"
```

### Basic Usage

```bash
# Analyze repository structure
repo-analyzer analyze structure ./my-project

# Check dependencies and vulnerabilities
repo-analyzer analyze dependencies ./my-project --check-vulnerabilities

# Generate comprehensive quality report
repo-analyzer analyze quality ./my-project

# Export analysis to HTML report
repo-analyzer report export ./my-project --format html --output analysis.html
```

### Configuration

Initialize a configuration file for your project:

```bash
cd my-project
repo-analyzer config init --preset python
```

This creates a `.repo-analyzer.yml` file with sensible defaults for Python projects.

## 📋 Command Reference

### Analysis Commands

- `analyze structure` - Repository structure and file organization
- `analyze dependencies` - Package dependencies and imports
- `analyze complexity` - Code complexity metrics
- `analyze quality` - Overall code quality assessment
- `analyze patterns` - Design pattern detection
- `analyze security` - Basic security vulnerability scan

### Reporting Commands

- `report summary` - High-level overview with key metrics
- `report detailed` - Comprehensive analysis report
- `report compare` - Compare metrics between commits/branches
- `report export` - Export to JSON, CSV, HTML formats

### Configuration Commands

- `config init` - Initialize analysis configuration
- `config show` - Display current configuration
- `config languages` - Configure language-specific rules

### History Commands

- `history list` - Show analysis history
- `history clean` - Clean up old analysis data

## 🔧 Configuration

Example `.repo-analyzer.yml`:

```yaml
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

## 🎯 Supported Languages

- **Python** - Full AST analysis, import tracking, complexity metrics
- **JavaScript/TypeScript** - Module analysis, dependency tracking
- **Java** - Package structure, class relationships
- **Go** - Module analysis, interface patterns
- **Rust** - Crate analysis, ownership patterns
- **C/C++** - Header dependencies, complexity analysis

## 📊 Example Output

```bash
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

## 🔗 CI/CD Integration

### GitHub Actions

```yaml
- name: Analyze code quality
  run: |
    pip install repo-analyzer
    repo-analyzer analyze quality --fail-on-regression
    repo-analyzer report export --format json --output analysis.json
```

### Pre-commit Hook

```bash
repos:
  - repo: local
    hooks:
      - id: repo-analyzer
        name: Repository Analysis
        entry: repo-analyzer analyze quality --fail-on-regression
        language: system
        pass_filenames: false
```

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=repo_analyzer --cov-report=html

# Run specific test categories
pytest -m "not slow"  # Skip slow tests
pytest -m integration  # Run only integration tests
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run the test suite: `pytest`
5. Run linting: `ruff check . && black --check .`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built using the [Context Engineering Framework](https://github.com/context-engineering/framework) for systematic AI-assisted development.

---

**Transform your code understanding from manual inspection into systematic, data-driven insights with Repo Analyzer.**