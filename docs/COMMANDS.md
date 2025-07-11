# Context Engineering Framework - Command Reference

**Complete list of 21 specialized commands available in the Context Engineering Framework**

> **Framework Core**: The `/generate_design` and `/execute_project` commands are the heart of the Context Engineering Framework, implementing the complete Three-Document Pattern methodology.

---

## 📊 Analysis Tools (4 commands)

### `/analyze`
**Purpose**: Multi-dimensional code analysis and assessment  
**Usage**: `/analyze --code --security --performance`  
**Key Features**: Code quality analysis, security scanning, performance assessment, architectural review  
**Best For**: Understanding codebase quality, identifying technical debt, security audits

### `/explain`  
**Purpose**: Code explanation and documentation generation  
**Usage**: `/explain --function calculateTotal --detailed`  
**Key Features**: Function explanation, algorithm breakdown, documentation generation, learning support  
**Best For**: Understanding complex code, onboarding, documentation creation

### `/review`
**Purpose**: Code review and quality assessment  
**Usage**: `/review --pull-request --security --style`  
**Key Features**: Pull request review, coding standards validation, security review, quality gates  
**Best For**: Code review automation, quality assurance, team collaboration

### `/scan`
**Purpose**: Repository scanning and validation  
**Usage**: `/scan --vulnerabilities --dependencies --patterns`  
**Key Features**: Vulnerability scanning, dependency analysis, pattern detection, compliance checking  
**Best For**: Security audits, compliance validation, dependency management

---

## 🔧 Development Tools (4 commands)

### `/build`
**Purpose**: Universal project builder with Next.js + Tailwind CSS templates and Python CLI applications  
**Usage**: `/build --nextjs --tailwind --shadcn` or `/build --python --cli --click`  
**Key Features**: Next.js app generation, Python CLI creation, template-driven development, professional README.md generation  
**Best For**: Creating new projects, generating boilerplate, professional application scaffolding

### `/dev-setup`
**Purpose**: Development environment configuration and setup  
**Usage**: `/dev-setup --nextjs --python --docker`  
**Key Features**: Environment configuration, dependency installation, tool setup, development workflow  
**Best For**: Onboarding new developers, consistent environment setup, project initialization

### `/document`
**Purpose**: Professional documentation creation  
**Usage**: `/document --session-summary` or `/document --type api --format openapi`  
**Key Features**: Session documentation, API docs, README generation, professional formatting  
**Best For**: Creating comprehensive documentation, session management, API documentation

### `/test`
**Purpose**: Testing framework and execution  
**Usage**: `/test --unit --integration --coverage`  
**Key Features**: Test execution, coverage analysis, quality gates, automated testing  
**Best For**: Quality assurance, continuous integration, test automation

---

## ⚙️ Operations Tools (4 commands)

### `/cleanup`
**Purpose**: Project cleanup and maintenance  
**Usage**: `/cleanup --dependencies --cache --artifacts`  
**Key Features**: Dependency cleanup, cache clearing, artifact removal, project maintenance  
**Best For**: Project maintenance, disk space management, clean builds

### `/deploy`
**Purpose**: Production deployment automation  
**Usage**: `/deploy --production --docker --verify`  
**Key Features**: Deployment automation, environment configuration, verification, rollback support  
**Best For**: Production deployments, CI/CD integration, automated releases

### `/migrate`
**Purpose**: System migration and updates  
**Usage**: `/migrate --database --version --validate`  
**Key Features**: Database migrations, version updates, data migration, validation  
**Best For**: System updates, database changes, version migrations

### `/troubleshoot`
**Purpose**: Debugging and problem resolution  
**Usage**: `/troubleshoot --errors --performance --logs`  
**Key Features**: Error diagnosis, performance analysis, log analysis, solution suggestions  
**Best For**: Debugging issues, performance optimization, problem resolution

---

## 📋 Management Tools (4 commands)

### `/git`
**Purpose**: Git integration and workflow management  
**Usage**: `/git --commit --push --branch`  
**Key Features**: Git workflow automation, commit management, branch operations, repository management  
**Best For**: Version control automation, workflow standardization, repository operations

### `/improve`
**Purpose**: Code improvement and optimization  
**Usage**: `/improve --performance --security --maintainability`  
**Key Features**: Code optimization, refactoring suggestions, performance improvements, best practices  
**Best For**: Code quality improvement, technical debt reduction, optimization

### `/load`
**Purpose**: Repository context loading and analysis  
**Usage**: `/load --analyze --context --summary`  
**Key Features**: Repository analysis, context loading, project understanding, framework detection  
**Best For**: Understanding new projects, session restoration, context analysis

### `/task`
**Purpose**: Task management and tracking  
**Usage**: `/task --create --update --status`  
**Key Features**: Task creation, progress tracking, status management, workflow coordination  
**Best For**: Project management, progress tracking, team coordination

---

## 🏗️ Framework Core Commands (2 commands)

### `/generate_design`
**Purpose**: Automated architecture generation from requirements (Framework Core)  
**Usage**: `/generate_design ./PRODUCT_PRP.md`  
**Token-Saving Examples**:
```bash
# Standard mode (comprehensive explanations)
/generate_design --verbose ./my-project/PRODUCT_PRP.md

# Production mode (50-70% token reduction)
/generate_design --token-saving ./my-project/PRODUCT_PRP.md

# Expert mode (70-85% token reduction)
/generate_design --minimal ./my-project/PRODUCT_PRP.md
```
**Key Features**: Three-Document Pattern implementation, automated DESIGN.md generation, requirements-to-architecture conversion, framework methodology enforcement  
**Best For**: **Core framework workflow**, converting PRODUCT_PRP.md to DESIGN.md, systematic architecture generation  
**Framework Significance**: **Essential component of Three-Document Pattern** - bridges requirements and implementation

### `/execute_project`
**Purpose**: Complete project execution using Three-Document Pattern (Framework Core)  
**Usage**: `/execute_project ./my-project`  
**Token-Saving Examples**:
```bash
# Standard mode (full implementation with explanations)
/execute_project --verbose ./my-project

# Production mode (efficient implementation)
/execute_project --token-saving ./my-project

# Expert mode (essential code only)
/execute_project --minimal ./my-project
```
**Key Features**: **End-to-end framework implementation**, Three-Document Pattern orchestration, complete project realization, methodology demonstration  
**Best For**: **Complete framework workflow execution**, systematic development following Context Engineering principles  
**Framework Significance**: **The ultimate framework command** - executes entire methodology from requirements through deployment

---

## 🎨 Design Tools (2 commands)

### `/design`
**Purpose**: System architecture design and planning  
**Usage**: `/design --api --database --architecture`  
**Key Features**: System design, architecture planning, API design, database schema design  
**Best For**: System architecture, API design, technical planning

### `/estimate`
**Purpose**: Project estimation and planning  
**Usage**: `/estimate --features --timeline --complexity`  
**Key Features**: Effort estimation, timeline planning, complexity analysis, resource planning  
**Best For**: Project planning, resource allocation, timeline estimation

---

## 🚀 Utility Tools (1 command)

### `/spawn`
**Purpose**: Process spawning and automation  
**Usage**: `/spawn --process --monitor --automate`  
**Key Features**: Process automation, background tasks, monitoring, workflow automation  
**Best For**: Automation tasks, background processes, workflow management

---

## 🎯 Universal Features

### **Token-Saving Modes** (All Commands)
- **`--verbose`**: Standard mode with full explanations (ideal for learning)
- **`--token-saving`**: Balanced mode with 50-70% token reduction (production development)  
- **`--minimal`**: Maximum compression with 70-85% token reduction (expert operations)

### **Cognitive Personas** (Selected Commands)
- **`--persona-architect`**: Systems thinking and architecture focus
- **`--persona-frontend`**: UI/UX and frontend development focus
- **`--persona-security`**: Security-first approach and threat modeling
- **`--persona-qa`**: Quality assurance and testing focus
- **Plus 5 additional specialized personas**

### **MCP Integration** (Enhanced Commands)
- **`--c7`**: Context7 server for library documentation
- **`--seq`**: Sequential thinking for complex analysis
- **`--pup`**: Puppeteer for browser automation

### **Framework Integration**
- **Three-Document Pattern**: PRODUCT_PRP.md + CLAUDE.md + DESIGN.md support (**Core: `/generate_design` and `/execute_project`**)
- **Template Library**: Next.js + Tailwind CSS and Python CLI templates
- **Professional Standards**: Enterprise-grade documentation and code generation
- **Zero Dependencies**: Local generation without external API costs
- **Complete Methodology**: End-to-end implementation from requirements to deployment

---

## 📚 Command Categories Summary

| Category | Commands | Primary Use Case |
|----------|----------|------------------|
| **Framework Core** | generate_design, execute_project | **Three-Document Pattern implementation and execution** |
| **Analysis** | analyze, explain, review, scan | Understanding and evaluating code |
| **Development** | build, dev-setup, document, test | Creating and developing projects |
| **Operations** | cleanup, deploy, migrate, troubleshoot | Managing and maintaining systems |
| **Management** | git, improve, load, task | Coordinating and optimizing workflows |
| **Design** | design, estimate | Planning and architecting systems |
| **Utility** | spawn | Process automation and workflow management |

---

## 🎯 Getting Started

### **For New Users**
1. **Start with**: `/load` to analyze your repository
2. **Learn the core**: `/generate_design ./PRODUCT_PRP.md` to understand Three-Document Pattern
3. **Create projects**: `/build --nextjs --tailwind` or `/build --python --cli`
4. **Generate documentation**: `/document --session-summary`
5. **Use standard mode**: Add `--verbose` flag for learning

### **For Experienced Users**
1. **Master the framework**: Use `/generate_design` → `/execute_project` workflow
2. **Use token-saving**: Add `--token-saving` flag for efficient development
3. **Leverage personas**: Use `--persona-architect` for design work
4. **Integrate workflows**: Combine commands for complete development cycles

### **For Expert Teams**
1. **Framework mastery**: Leverage full `/execute_project` capabilities for complex implementations
2. **Minimal mode**: Use `--minimal` flag for maximum efficiency
3. **Advanced integration**: Leverage MCP servers with `--c7`, `--seq`, `--pup`
4. **Custom workflows**: Create sophisticated automation with framework core commands

---

**Framework Version**: v1.0.0  
**Total Commands**: 21 specialized tools  
**Documentation**: Complete command reference with usage examples  
**Status**: Production ready with comprehensive capabilities