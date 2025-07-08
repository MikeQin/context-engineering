# Generate DESIGN.md Command

Generate a comprehensive DESIGN.md document from a PRODUCT_PRP.md file following The Three-Document Pattern Context Engineering Framework.

## Usage

```bash
/generate_design [PRODUCT_PRP_FILE]
```

## Parameters

- `PRODUCT_PRP_FILE` (optional): Path to the Product Requirements Prompt file. Defaults to `PRODUCT_PRP.md` in current directory.

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
/generate_design ./example/TETRIS_PRP.md

# If PRP is in current directory (after cd into project folder)
/generate_design PRODUCT_PRP.md
```

## Command Implementation

The command will efficiently execute using the new 19 internal commands:

1. **Internal Configuration & Setup**
   - **Read `.claude/CLAUDE.md`** - Load internal toolkit configuration and capabilities
   - **Initialize internal tools** - Access 19 specialized commands and templates
   - `/load` - Load project context and validate input files
   - `/scan --validate` - Validate PRP and CLAUDE.md file formats
   - `/analyze --code` - Parse PRP file and extract product name

2. **Context Engineering Configuration**
   - **Read project's `CLAUDE.md`** - Load context engineering methodology and standards
   - **Merge configurations** - Combine internal toolkit with project methodology
   - `/analyze --arch --think` - Analyze project requirements and constraints
   - `/review --quality` - Review PRP completeness and clarity
   - `/scan --security` - Identify security considerations from requirements

3. **Architecture Design**
   - `/design --api --ddd` - Create system architecture and API design
   - `/design --prd` - Generate product requirements analysis
   - `/analyze --profile` - Assess performance and scalability needs

4. **Technical Planning**
   - `/estimate --detailed` - Create project estimation and timeline
   - `/scan --deps` - Analyze external dependencies and integrations
   - `/build --init` - Plan project structure and technology stack

5. **Documentation Generation**
   - `/document` - Generate comprehensive DESIGN.md with all sections
   - `/explain --depth expert` - Create technical diagrams and explanations
   - `/review --evidence` - Validate design completeness and accuracy

6. **Quality Assurance**
   - `/scan --strict` - Validate design against quality standards
   - `/analyze --security` - Ensure security considerations are addressed
   - `/task` - Create actionable implementation tasks and next steps

This systematic approach ensures comprehensive, high-quality DESIGN.md generation using the full capabilities of the specialized command toolkit.

**Note:** The internal commands execute automatically and transparently. Users simply run `/generate_design` and Claude internally uses the appropriate specialized commands to deliver optimal results without requiring user awareness or intervention.

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