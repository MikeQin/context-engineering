# Execute Project Command

Execute the complete implementation of your project using The Three-Document Pattern Context Engineering Framework.

## Usage

```bash
/execute_project [OPTIONS] [PROJECT_FOLDER]
```

## Parameters

- `PROJECT_FOLDER` (optional): Path to the project folder containing your three framework documents. Defaults to current directory.

## Options

- `--token-saving` or `--uc`: Enable UltraCompressed mode for efficient implementation
- `--minimal`: Maximum compression with essential code only  
- `--verbose`: Detailed implementation with explanations (default)
- `--scaffold`: Generate project structure only
- `--core`: Implement core functionality only

## Token-Saving Mode

When `--token-saving` is used, the command generates:
- Essential code files only (no extensive examples)
- Minimal comments and documentation
- Core functionality without advanced features
- Optimized file structure
- Symbol-based progress reporting

Example:
```bash
/execute_project --token-saving ./my-project
/execute_project --minimal ./my-project  
/execute_project --scaffold ./my-project  # Structure only
```

## Description

This command reads all three framework documents and executes the complete product implementation following The Three-Document Pattern Context Engineering Framework methodology.

**Complete Developer Workflow:**
1. Clone the framework repository
2. Create a new project folder
3. Copy framework templates to the project folder
4. Customize the PRP template with your requirements
5. Generate your technical architecture with `/generate_design ./my-project/PRODUCT_PRP.md`
6. **Execute the implementation** with `/execute_project ./my-project`

## What This Command Does

1. **Validates and reads the complete three-document pattern**:
   - Locates the [PRODUCT_NAME]_DESIGN.md file in the project folder
   - Finds the corresponding PRODUCT_PRP.md (or PRODUCT_PRP_SLIM.md) file
   - Confirms CLAUDE.md methodology file is present
   - Validates all three documents are properly formatted and consistent

2. **Reads and analyzes all three documents**:
   - **PRODUCT_PRP.md**: Understands WHAT to build (requirements, features, specifications)
   - **[PRODUCT_NAME]_DESIGN.md**: Understands the technical architecture and implementation plan
   - **CLAUDE.md**: Follows HOW to build (methodology, standards, patterns)

3. **Executes systematic implementation**:
   - Creates the complete project structure as defined in DESIGN.md
   - Implements all features specified in the PRP
   - Follows all quality standards and patterns from CLAUDE.md
   - Includes comprehensive testing strategy
   - Implements all acceptance criteria

4. **Ensures production readiness**:
   - All code follows the specified methodology and standards
   - Comprehensive test coverage as defined in DESIGN.md
   - Complete documentation and setup instructions
   - Ready for deployment as specified in the technical architecture

## Output

Creates a complete, production-ready implementation of your product following the exact specifications in your three framework documents.

**Implementation includes:**
- Complete project structure (as defined in DESIGN.md)
- All source code files with proper organization
- Comprehensive test suite (unit, integration, performance)
- Configuration files and environment setup
- Documentation (README, API docs, deployment guides)
- Build and deployment scripts

## Prerequisites

Your project folder must contain the complete three-document pattern:
- **PRODUCT_PRP.md** (or PRODUCT_PRP_SLIM.md) - Product requirements
- **[PRODUCT_NAME]_DESIGN.md** - Technical architecture (generated with `/generate_design`)
- **CLAUDE.md** - Development methodology

## Examples

```bash
# Execute implementation for your project
/execute_project ./my-awesome-app

# Execute implementation for the framework's example
/execute_project ./example

# Execute from within your project folder
cd my-awesome-app
/execute_project

# Execute with specific project folder path
/execute_project ./projects/enterprise-app
```

## Path Handling

The command automatically handles path resolution:
- **Project Folder**: Accepts absolute or relative paths to project folders
- **Document Discovery**: Automatically finds all three framework documents in the folder
- **Validation**: Ensures complete three-document pattern exists
- **Output Location**: Creates all implementation files within the project folder
- **Relative References**: Maintains proper relative paths for all generated code

## Error Handling

The command will provide clear error messages for:
- Missing project folder or invalid path
- Incomplete three-document pattern (missing any of the three files)
- Multiple or ambiguous DESIGN.md files in the folder
- Invalid or malformed document formats
- File permission issues
- Any validation failures during implementation

## Quality Assurance

The executed implementation will:
- ✅ Implement every requirement specified in the PRODUCT_PRP.md
- ✅ Follow the exact architecture defined in [PRODUCT_NAME]_DESIGN.md
- ✅ Adhere to all development standards and patterns from CLAUDE.md
- ✅ Include comprehensive testing strategy as specified
- ✅ Provide complete project structure and organization
- ✅ Include all external dependencies and integrations
- ✅ Meet all acceptance criteria and success metrics
- ✅ Be ready for immediate deployment

## Integration with Framework

This command completes The Three-Document Pattern Context Engineering Framework workflow:

```mermaid
graph LR
    A[Clone Framework] --> B[Create Project Folder]
    B --> C[Copy Templates]
    C --> D[Customize PRP]
    D --> E[/generate_design]
    E --> F[[PRODUCT_NAME]_DESIGN.md]
    F --> G[Review & Approve]
    G --> H[/execute_project]
    H --> I[Complete Implementation]
    I --> J[Production Ready Product]
```

## Implementation Strategy

The command efficiently executes using the new 19 internal commands in a systematic approach:

### Phase 1: Internal Configuration & Project Setup
- **Read `.claude/CLAUDE.md`** - Load internal toolkit configuration and capabilities
- **Initialize internal tools** - Access 19 specialized commands and templates
- `/load` - Load and validate three-document pattern
- `/scan --validate` - Validate all framework documents
- **Read project's `CLAUDE.md`** - Load context engineering methodology and standards
- **Merge configurations** - Combine internal toolkit with project methodology
- `/analyze --arch --think` - Analyze requirements and architecture consistency
- `/dev-setup` - Initialize development environment

### Phase 2: Core Implementation
- `/build --init` - Create project structure as defined in DESIGN.md
- `/build --feature` - Implement core features following PRP specifications
- `/build --nextjs --tailwind --shadcn` - Generate modern UI components (if applicable)
- `/spawn` - Execute parallel implementation tasks efficiently

### Phase 3: Quality Assurance
- `/test --coverage --e2e` - Implement comprehensive testing strategy
- `/review --quality --evidence` - Ensure code quality and standards compliance
- `/scan --security --strict` - Validate security requirements
- `/analyze --performance` - Validate performance criteria

### Phase 4: Production Readiness
- `/document` - Generate complete documentation and setup guides
- `/deploy --plan` - Create deployment configuration
- `/cleanup --validate` - Final validation and cleanup
- `/git` - Commit and prepare for deployment

This systematic approach leverages the full capabilities of the specialized command toolkit to ensure efficient, high-quality implementation execution.

**Note:** The internal commands execute automatically and transparently. Users simply run `/execute_project` and Claude internally uses the appropriate specialized commands to deliver optimal results without requiring user awareness or intervention.

## Dual Configuration System

This command operates with two complementary CLAUDE.md files:

1. **`.claude/CLAUDE.md`** (Internal Toolkit Configuration)
   - **Purpose**: Provides access to 19 specialized commands and Next.js + Tailwind templates
   - **Source**: Based on SuperClaude project for enhanced Claude capabilities
   - **Scope**: Internal tool library for efficient task execution
   - **Usage**: Read first to initialize internal toolkit capabilities

2. **Project's `CLAUDE.md`** (Context Engineering Methodology)  
   - **Purpose**: Defines development methodology, coding standards, and project-specific patterns
   - **Source**: Three-Document Pattern Context Engineering Framework
   - **Scope**: Project-specific methodology and quality standards
   - **Usage**: Read second to understand project's "HOW to build" requirements

**Configuration Merge Process**: The command combines both configurations to leverage internal toolkit efficiency while adhering to project-specific methodology and standards.

## Best Practices

1. **Complete your planning first**: Ensure PRP is comprehensive and DESIGN.md is approved
2. **Review all three documents**: Verify consistency between requirements, design, and methodology
3. **Validate technical feasibility**: Confirm the architecture is implementable before execution
4. **Monitor the implementation**: Review generated code for quality and correctness
5. **Test thoroughly**: Validate that all requirements are met and acceptance criteria satisfied
6. **Follow deployment guides**: Use the generated documentation for proper deployment

## Advanced Features

### Incremental Implementation
The command supports incremental development:
- Updates existing implementations when documents change
- Preserves custom modifications while applying new requirements
- Maintains version consistency across the three-document pattern

### Quality Validation
Built-in quality checks ensure:
- Code follows specified methodology and standards
- All requirements are implemented and tested
- Architecture patterns are correctly applied
- Production readiness criteria are met

### Documentation Generation
Automatically generates:
- Comprehensive README with setup instructions
- API documentation (if applicable)
- Deployment guides and configuration
- Code documentation and inline comments

## Troubleshooting

**Common Issues:**

1. **Missing Documents**: Ensure all three framework documents exist in the project folder
2. **Invalid Product Name**: Verify DESIGN.md filename matches the product name in PRP
3. **Inconsistent Requirements**: Check that PRP and DESIGN.md are aligned
4. **Methodology Conflicts**: Ensure CLAUDE.md standards are compatible with architecture

**Getting Help:**
- Review the three-document pattern for completeness
- Validate that `/generate_design` was run successfully
- Check that all placeholders in templates were replaced
- Ensure project folder structure follows framework conventions

---

## Success Validation

This command ensures your implementation will:

1. **✅ Fully Satisfy PRP Requirements**: Every specification implemented and tested
2. **✅ Follow DESIGN.md Architecture**: Exact technical architecture implementation
3. **✅ Adhere to CLAUDE.md Standards**: Code quality and organizational patterns
4. **✅ Include Complete Testing**: Comprehensive test coverage as specified
5. **✅ Be Production Ready**: Deployable with full documentation and configuration

**Expected Outcome**: A complete, production-ready implementation that perfectly matches your three-document specifications and demonstrates the full power of The Three-Document Pattern Context Engineering Framework.

---

*This command completes the systematic AI-assisted development workflow, transforming your planning documents into a working product.*