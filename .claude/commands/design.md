**Purpose**: System architecture and API design

---

@include shared/universal-constants.yml#Universal_Legend

## Command Execution
Execute: immediate. --plan→show plan first
Legend: Generated based on symbols used in command
Purpose: "[Action][Subject] in $ARGUMENTS"

Design system architecture & APIs for $ARGUMENTS.

@include shared/flag-inheritance.yml#Universal_Always

Examples:
- `/design --api --think` - REST API design w/ patterns
- `/design --ddd --think-hard` - Deep domain modeling
- `/design --api --ddd --ultrathink` - Complete system architecture
- `/design --cli --command-architecture` - CLI command structure design
- `/design --cli --config-management` - CLI configuration system design

Design modes:

**--api:** Design REST or GraphQL APIs
- w/ --openapi: Generate OpenAPI 3.0 spec | w/ --graphql: Create GraphQL schema & resolvers
- Include auth, rate limiting & error handling | Design→scalability & maintainability

**--ddd:** Apply DDD principles
- w/ --bounded-context: Define context boundaries & mappings
- Design entities, value objects & aggregates | Create domain services & events | Impl repository patterns

**--prd:** Create PRD 
- w/ --template: Use template (feature/api/integration/migration)
- Include user stories w/ acceptance criteria | Define success metrics & timelines | Document tech requirements

**--cli:** Design CLI application architecture
- w/ --command-architecture: Plan command structure, subcommands, and argument hierarchy
- Design configuration system w/ file/env var precedence | Plan user interaction flows | Design help & documentation system

**--config-management:** Design configuration systems
- w/ --precedence: Define configuration source priority (files/env vars/defaults)
- Design schema validation & error handling | Plan configuration discovery & loading | Design user customization patterns

## Design Patterns

@include shared/architecture-patterns.yml#API_Design_Patterns

@include shared/architecture-patterns.yml#DDD_Patterns

@include shared/architecture-patterns.yml#PRD_Templates

## Integration & Best Practices

Combined modes: API+DDD: Design domain-driven APIs | API+PRD: Create API product requirements | DDD+PRD: Document domain-driven architecture | CLI+PRD: Design CLI product requirements | All modes: Complete system design

Best practices: Start w/ user needs & business goals | Design→change & evolution | Consider non-functional early | Document decisions & rationale | Include examples & diagrams | Plan→testing & monitoring

@include shared/research-patterns.yml#Mandatory_Research_Flows

@include shared/docs-patterns.yml#Standard_Notifications

@include shared/universal-constants.yml#Standard_Messages_Templates