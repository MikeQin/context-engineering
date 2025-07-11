# Generate DESIGN.md Command

Generate a comprehensive DESIGN.md document from a PRODUCT_PRP.md file following The Three-Document Pattern Context Engineering Framework.

## Universal Flags

@include flag-inheritance.yml#Universal_Always

## Usage

```bash
/generate_design [OPTIONS] [PRODUCT_PRP_FILE]
```

## Parameters

- `PRODUCT_PRP_FILE` (optional): Path to the Product Requirements Prompt file. Defaults to `PRODUCT_PRP.md` in current directory.

## Options

- `--token-saving` or `--uc`: Enable UltraCompressed mode for 70% token reduction
- `--minimal`: Maximum compression with optimized communication patterns
- `--verbose`: Detailed output with explanations (default)

## Token-Saving Mode

When `--token-saving` is used, the command generates:
- Concise technical architecture (vs. comprehensive)
- Optimized structure notation  
- Essential information only
- Compressed mermaid diagrams
- Optimized for implementation efficiency

Example:
```bash
/generate_design --token-saving ./my-project/PRODUCT_PRP.md
/generate_design --minimal ./my-project/PRODUCT_PRP.md
```

## Description

This command reads your PRODUCT_PRP.md file (extracting the product name for consistent referencing), reads the project's CLAUDE.md methodology file, then generates a comprehensive DESIGN.md document that includes complete technical architecture, implementation strategy, and project planning.

**Typical Developer Workflow:**
1. Clone the framework repository
2. Create a new project folder (e.g., `my-awesome-app/`)
3. Copy framework templates to the project folder
4. Customize the PRP template with your requirements
5. Use this command to generate your technical architecture

## What This Command Does

1. **Reads the specified PRODUCT_PRP.md file** (or PRODUCT_PRP.md by default)
2. **Extracts the product name** from the PRP file for consistent referencing
3. **Reads the CLAUDE.md methodology file** from the current project
4. **Generates a comprehensive `[PRODUCT_NAME]_DESIGN.md`** that includes:
   - Problem statement and context
   - Possible implementation approaches with trade-offs
   - Architecture and system design
   - Testing strategy (unit tests, integration tests, security scans)
   - Technology stack justification
   - Project structure (tree-style directory layout)
   - External dependencies and integrations
   - Documentation references
   - Acceptance criteria and success metrics
   - Technical diagrams (Mermaid diagrams when helpful)

## Output

Creates a `[PRODUCT_NAME]_DESIGN.md` file in the current directory with complete technical architecture and implementation planning. The product name is extracted from the **Product Name** field in the PRP file.

**Examples:**
- If Product Name is `Tetris Game`, creates `TETRIS_GAME_DESIGN.md`
- If Product Name is `TaskFlow Pro`, creates `TASKFLOW_PRO_DESIGN.md`
- If Product Name is `E-Commerce Platform`, creates `E_COMMERCE_PLATFORM_DESIGN.md`

## Prerequisites

- A valid `PRODUCT_PRP.md` file (or specified PRP file) must exist
- A `CLAUDE.md` file should exist in the project for development methodology
- Files should follow The Three-Document Pattern Context Engineering Framework format

## Examples

```bash
# After cloning framework and setting up your project folder:

# Generate design for your project folder
/generate_design ./my-awesome-app/PRODUCT_PRP.md

# Generate design using the slim template
/generate_design ./quick-prototype/PRODUCT_PRP_SLIM.md

# Generate design for the framework's example
/generate_design ./examples/web-app/TETRIS_PRP.md

# If PRP is in current directory (after cd into project folder)
/generate_design PRODUCT_PRP.md
```

## Command Implementation

The command will efficiently execute using the new 19 internal commands:

1. **Framework Initialization & Configuration Loading**
   - **Read `.claude/CLAUDE.md`** - Load complete internal toolkit configuration (19 commands, personas, templates, token-saving modes, MCP integration)
   - **Load shared configuration modules** - Import all @include references (toolkit-core.yml, toolkit-personas.yml, flag-inheritance.yml, etc.)
   - **Initialize framework capabilities** - Activate 19 specialized commands, 9 cognitive personas, Next.js + Tailwind templates, Python CLI patterns
   - **Apply universal flags** - Process all command flags including token-saving modes, thinking modes, persona selection, MCP controls
   - **Read repository `CLAUDE.md`** - Load framework development context and consistency requirements
   - `/load` - Load project context using framework-aware validation
   - `/scan --validate` - Validate all framework documents using framework quality standards

2. **Project Context Engineering Integration**
   - **Read project's `CLAUDE.md`** - Load Three-Document Pattern methodology, coding standards, and project-specific patterns
   - **Validate framework compatibility** - Ensure project follows framework architecture patterns and quality standards
   - **Merge framework configurations** - Combine internal toolkit + repository context + project methodology
   - **Apply cognitive persona** - Use specified persona (--persona-architect, --persona-frontend, etc.) for domain-specific thinking
   - **Configure MCP integration** - Apply MCP flags (--c7, --seq, --pup) for enhanced capabilities
   - `/analyze --arch --think` - Analyze using framework thinking modes and architectural patterns
   - `/review --quality --evidence` - Review using framework evidence-based methodology
   - `/scan --security` - Apply framework security patterns and OWASP standards

3. **Framework-Driven Architecture Design**
   - `/design --api --ddd --persona-architect` - Create system architecture using domain-driven design patterns
   - `/design --prd --think-hard` - Generate comprehensive product requirements analysis
   - `/analyze --profile --seq` - Assess performance using Sequential thinking for complex analysis
   - **Apply framework architectural patterns** - Use modular configuration, command-based architecture, template-driven development
   - **Integrate technology stack** - Apply framework standards for Next.js + Tailwind CSS, Python CLI, MCP integration

4. **Framework-Aligned Technical Planning**
   - `/estimate --detailed --persona-architect` - Create project estimation using systems thinking
   - `/scan --deps --c7` - Analyze dependencies using Context7 for library documentation
   - `/build --init --nextjs --tailwind` - Plan project structure using framework templates and patterns
   - **Apply framework quality standards** - Evidence-based methodology, zero dependencies, backward compatibility
   - **Ensure cross-component validation** - Validate against framework consistency requirements

5. **Framework-Standard Documentation Generation**
   - `/document --depth expert --visual` - Generate comprehensive DESIGN.md following framework documentation standards
   - `/explain --depth expert --visual --persona-mentor` - Create technical diagrams with teaching/mentoring approach
   - `/review --evidence --quality` - Validate design using framework evidence-based methodology
   - **Apply framework output organization** - Follow framework documentation management standards
   - **Ensure template synchronization** - Keep generated design aligned with framework templates

6. **Framework Quality Assurance & Validation**
   - `/scan --strict --security --owasp` - Validate against framework security patterns and standards
   - `/analyze --security --persona-security` - Security-focused analysis using framework threat modeling
   - `/task --feature --tdd` - Create implementation tasks following framework development practices
   - **Validate framework compliance** - Ensure design follows framework architecture patterns and quality standards
   - **Apply framework best practices** - Consider user impact, maintain template consistency, update documentation

This systematic approach ensures comprehensive, high-quality DESIGN.md generation using the full capabilities of the specialized command toolkit.

**Note:** The internal commands execute automatically and transparently. Users simply run `/generate_design` and Claude internally uses the appropriate specialized commands to deliver optimal results without requiring user awareness or intervention.

## Triple Configuration System

This command operates with three complementary CLAUDE.md files for complete framework integration:

1. **`.claude/CLAUDE.md`** (Internal Toolkit Configuration)
   - **Purpose**: Complete framework toolkit including 19 specialized commands, 9 cognitive personas, Next.js + Tailwind templates, Python CLI patterns, token-saving modes, MCP integration
   - **Source**: Based on SuperClaude project enhanced for Context Engineering Framework
   - **Scope**: Internal tool library providing all framework capabilities
   - **Configuration**: All shared modules (toolkit-core.yml, toolkit-personas.yml, flag-inheritance.yml, etc.)
   - **Usage**: Read first to initialize complete framework capabilities

2. **Repository `CLAUDE.md`** (Framework Development Context)
   - **Purpose**: Framework development methodology, consistency requirements, quality standards, architecture patterns
   - **Source**: Context Engineering Framework repository knowledge base
   - **Scope**: Framework maintenance and improvement guidelines
   - **Standards**: Evidence-based methodology, zero dependencies, backward compatibility, cross-component validation
   - **Usage**: Read to understand framework context and ensure consistency

3. **Project's `CLAUDE.md`** (Three-Document Pattern Methodology)  
   - **Purpose**: Project-specific implementation of Three-Document Pattern methodology, coding standards, token-saving guidelines
   - **Source**: Framework template customized for specific project needs
   - **Scope**: Project methodology aligned with framework standards
   - **Integration**: Token-saving modes, architectural patterns, quality standards from framework
   - **Usage**: Read to understand project's specific "HOW to build" requirements within framework context

**Framework Integration Process**: The command systematically combines all three configuration layers to create complete framework-native operation:
1. **Internal Toolkit Layer**: Provides core capabilities and tools
2. **Framework Context Layer**: Ensures consistency and quality standards  
3. **Project Methodology Layer**: Applies specific implementation requirements
4. **Command Flag Override**: User-specified flags take precedence over all configuration defaults

This triple-layer integration ensures every generated design is fully framework-compliant while meeting specific project needs.

## Quality Assurance

The generated `[PRODUCT_NAME]_DESIGN.md` will:
- ✅ Address every requirement specified in the PRODUCT_PRP.md
- ✅ Use the product name consistently throughout the document
- ✅ Follow development standards and patterns from CLAUDE.md
- ✅ Include comprehensive testing strategy
- ✅ Provide clear project structure and organization
- ✅ Include risk assessment and mitigation strategies
- ✅ Define acceptance criteria and success metrics
- ✅ Be ready for immediate implementation

## Path Handling

The command automatically handles path resolution:
- **PRP File Location**: Accepts absolute or relative paths to PRP files
- **CLAUDE.md Location**: Looks for CLAUDE.md in the same directory as the PRP file
- **Output Location**: Creates the DESIGN.md file in the same directory as the PRP file
- **Reference Links**: Uses correct relative paths based on file locations

## Error Handling

The command will provide clear error messages for:
- Missing PRODUCT_PRP.md or specified PRP file
- Invalid or malformed PRP file format
- Missing CLAUDE.md methodology file in the same directory
- File permission issues
- Any other validation failures

## Integration with Framework

This command is part of The Three-Document Pattern Context Engineering Framework workflow:

```mermaid
graph LR
    A[PRODUCT_PRP.md] --> B[/generate_design command]
    B --> C[Extract Product Name]
    C --> D[[PRODUCT_NAME]_DESIGN.md generated]
    D --> E[Review & Approve Design]
    E --> F[Implement with CLAUDE.md]
    F --> G[Quality Gates]
    G --> H[Working Product]
```

## Best Practices

1. **Set up properly**: Clone framework, create project folder, copy templates
2. **Customize thoroughly**: Fill in all placeholders in your PRP template
3. **Review the generated DESIGN.md** before proceeding with implementation
4. **Request revisions** if any requirements are unclear or missing
5. **Validate technical feasibility** of the proposed architecture
6. **Ensure team alignment** on the technical approach before coding
7. **Use the DESIGN.md** as the single source of truth for implementation

## Complete Developer Workflow

```bash
# Step 1: Get the framework
git clone [framework-repository-url]
cd context-engineering

# Step 2: Create your project
mkdir my-new-product
cd my-new-product
cp ../framework/* .

# Step 3: Customize your requirements
# Edit PRODUCT_PRP.md (or PRODUCT_PRP_SLIM.md) with your specific needs

# Step 4: Generate architecture
cd ..
/generate_design ./my-new-product/PRODUCT_PRP.md

# Step 5: Execute implementation
/execute_project ./my-new-product

# Step 6: Deploy your complete product!
# Your three documents have been transformed into a working product:
# - PRODUCT_PRP.md (WHAT to build) ✅ Implemented
# - CLAUDE.md (HOW to build) ✅ Standards followed
# - [PRODUCT_NAME]_DESIGN.md (Technical architecture) ✅ Architecture realized
```

---

*This command simplifies the DESIGN.md generation process while maintaining the comprehensive quality and standards of The Three-Document Pattern Context Engineering Framework.*