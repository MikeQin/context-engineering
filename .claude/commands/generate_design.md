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

The command will:

1. **Validate input files exist and are readable**
2. **Read and parse the PRP file** to understand project requirements
3. **Extract the product name** from the `**Product Name**: \`[NAME]\`` field
4. **Read the CLAUDE.md file** (from same directory as PRP) to understand development methodology
5. **Generate comprehensive `[PRODUCT_NAME]_DESIGN.md`** in the same directory as the PRP file
6. **Use correct relative paths** for all document references based on file locations
7. **Use the product name consistently** throughout the generated design document
8. **Ensure the design addresses all requirements** specified in the PRP
9. **Follow architecture patterns and quality standards** defined in CLAUDE.md
10. **Include technical diagrams** where helpful for understanding
11. **Create actionable implementation strategy** with clear next steps

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