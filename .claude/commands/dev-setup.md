**Purpose**: Professional development environment setup

---

@include shared/universal-constants.yml#Universal_Legend

## Command Execution
Execute: immediate. --plan→show plan first
Legend: Generated based on symbols used in command
Purpose: "[Action][Subject] in $ARGUMENTS"

Configure comprehensive development environments and CI/CD pipelines for $ARGUMENTS.

@include shared/flag-inheritance.yml#Universal_Always

Examples:
- `/dev-setup --type node --ci github --tools` - Node.js project with GitHub Actions
- `/dev-setup --type python --tools --think` - Python project with comprehensive tooling
- `/dev-setup --type cli --python --click --tools` - Python CLI development environment
- `/dev-setup --type monorepo --ci gitlab --think-hard` - Full-stack monorepo with GitLab CI
- `/dev-setup --type react --tools --ci github` - React project with quality tools

## Setup Types

--type flag:
- node: Node.js/TypeScript project setup
- python: Python virtual environment & tooling
- cli: CLI application development environment
- react: React + Vite/Next.js configuration
- fullstack: Complete full-stack environment
- monorepo: Multi-package monorepo setup

--ci flag:
- github: GitHub Actions workflows
- gitlab: GitLab CI/CD pipelines
- jenkins: Jenkins pipeline configuration
- circleci: CircleCI configuration
- custom: Custom CI/CD solution

--tools flag:
- Include dev tools: linters, formatters, pre-commit hooks
- Configure VS Code settings & extensions
- Setup debugging configurations
- Install recommended tooling

## Setup Components

Environment Configuration:
- Package manager setup (npm/yarn/pnpm)
- Version management (.nvmrc, .python-version)
- Environment variables & .env structure
- Docker configuration if needed

Code Quality:
- ESLint/Prettier configuration
- Pre-commit hooks (husky, lint-staged)
- Test framework setup (Jest, Pytest, etc)
- Code coverage configuration

CI/CD Pipeline:
- Build & test workflows
- Deployment configurations
- Security scanning (SAST/DAST)
- Dependency vulnerability checks
- Release automation

Development Tools:
- VS Code workspace settings
- Debug configurations
- Task runners & scripts
- Documentation generation

## CLI Development Setup

CLI-Specific Environment:
- Python virtual environment with CLI frameworks
- CLI testing frameworks (Click testing, subprocess testing)
- Shell completion configuration and testing
- CLI debugging and profiling tools
- Package distribution setup (PyPI, wheel building)

CLI Development Tools:
- Click/Typer development dependencies
- Rich library for enhanced terminal output
- Configuration management libraries (PyYAML, TOML)
- CLI testing utilities and mock frameworks
- Terminal debugging and logging setup

CLI Quality & Testing:
- CLI-specific linting rules and patterns
- Command-line argument validation testing
- Integration testing with different shells
- CLI performance testing (startup time, memory)
- Cross-platform compatibility testing

CLI Distribution:
- pyproject.toml configuration for modern packaging
- Console entry points and script configuration
- Virtual environment and dependency management
- Package building and distribution automation
- Installation and upgrade testing

## Best Practices

Security:
- Never commit secrets or credentials
- Use environment variables for sensitive data
- Configure security scanning in CI
- Implement dependency vulnerability checks

Performance:
- Cache dependencies in CI
- Parallelize test execution
- Optimize build processes
- Use appropriate resource limits

Maintainability:
- Consistent tooling across team
- Clear documentation
- Automated quality checks
- Reproducible environments

## Examples

```bash
# Node.js project with GitHub Actions
/dev-setup --type node --ci github --tools

# Python project with comprehensive tooling
/dev-setup --type python --tools --think

# Full-stack monorepo with GitLab CI
/dev-setup --type monorepo --ci gitlab --think-hard

# React project with all quality tools
/dev-setup --type react --tools --ci github
```

## Deliverables

- Complete environment configuration files
- CI/CD pipeline definitions
- Development tool configurations
- Setup documentation & README updates
- Scripts for common development tasks

@include shared/universal-constants.yml#Standard_Messages_Templates