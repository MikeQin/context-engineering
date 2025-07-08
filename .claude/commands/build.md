**Purpose**: Universal project builder with Next.js + Tailwind CSS templates and Python CLI applications

---

@include shared/universal-constants.yml#Universal_Legend

## Command Execution
Execute: immediate. --plan→show plan first
Legend: Generated based on symbols used in command
Purpose: "[Action][Subject] in $ARGUMENTS"

Build project/feature based on req in $ARGUMENTS using modern Next.js + Tailwind CSS stack or Python CLI frameworks.

@include shared/flag-inheritance.yml#Universal_Always

Examples:
- `/build --nextjs --tailwind --shadcn` - Next.js app w/ component library
- `/build --python --cli --click` - Python CLI w/ Click framework
- `/build --python --cli --typer` - Python CLI w/ Typer framework
- `/build --nextjs --app-router --forms` - Complete app with forms
- `/build --api --c7` - API w/ docs
- `/build --cli --argparse` - Basic CLI w/ argparse

Pre-build: Remove artifacts (dist/, build/, .next/) | Clean temp files & cache | Validate deps | Remove debug

Build modes:
**--init:** New project w/ stack (Next.js|API|Fullstack|Mobile|CLI) | TS default | Testing setup | Git workflow
**--feature:** Impl feature→existing patterns | Maintain consistency | Include tests  
**--tdd:** Write failing tests→minimal code→pass tests→refactor

## Next.js + Tailwind Templates:
- **Next.js:** App Router|TS|Tailwind|shadcn/ui|testing
- **API:** Express|TS|auth|validation|OpenAPI  
- **Fullstack:** Next.js+tRPC+Prisma+Docker
- **Mobile:** React Native+Expo+NativeWind (roadmap - toolkit integration planned)

## Python CLI Templates:
- **CLI + Click:** Python|Click decorators|subcommands|config|testing
- **CLI + Typer:** Python|Typer types|autocompletion|rich output|testing  
- **CLI + argparse:** Python|argparse|basic CLI|lightweight|testing
- **CLI + Fire:** Python|Google Fire|automatic CLI|object methods|testing

## UI Generation Flags:
**--nextjs:** Next.js App Router setup | TypeScript default | Modern patterns | SEO optimization
**--tailwind:** Tailwind CSS integration | Utility-first styling | Responsive design | Dark mode support
**--shadcn:** shadcn/ui component library | Accessible components | Professional design | Radix primitives
**--components:** Advanced component generation | Reusable patterns | Type-safe props | Template library
**--forms:** Form generation | Zod validation | React Hook Form | Accessible forms | Error handling
**--responsive:** Responsive design utilities | Mobile-first approach | Breakpoint management | Container queries
**--dashboard:** Dashboard patterns | Data visualization ready | Admin interfaces | Navigation layouts
**--icons:** Icon library integration | Lucide React | Heroicons | Type-safe icons | Customizable
**--animations:** Animation utilities | Framer Motion ready | Tailwind animations | Micro-interactions

## CLI Generation Flags:
**--cli:** Generic CLI application | Auto-detect best framework | Project structure | Testing setup
**--python:** Python-based CLI | Virtual environment | Modern packaging | Type hints
**--click:** Click framework CLI | Decorators | Subcommands | Auto-help | Configuration support
**--typer:** Typer framework CLI | Type hints | Auto-completion | Rich output | Modern Python patterns
**--argparse:** Standard library CLI | Lightweight | Basic argument parsing | No external dependencies
**--fire:** Google Fire CLI | Automatic CLI generation | Object method exposure | Minimal setup
**--config:** Configuration management | YAML/JSON/TOML support | Environment variables | Config precedence
**--rich:** Rich terminal output | Progress bars | Tables | Syntax highlighting | Colors
**--testing:** CLI testing setup | Command testing | Argument validation | Integration tests

## CLI Template Generation:
**Command Structure:** Main CLI|Subcommands|Options|Arguments|Help system
**Configuration:** Config files|Environment variables|Precedence handling|Validation
**Testing Patterns:** Command testing|Argument parsing|Integration|Mock inputs
**Packaging:** pyproject.toml|Console entry points|Distribution|Installation
**Documentation:** Help text|Usage examples|Man pages|API documentation

## Template Generation:
**Component Library:** shadcn/ui Button|Input|Form|Card|Dialog|Table|Navigation
**Layout Templates:** Dashboard|Marketing|Auth|Blog|E-commerce|Documentation
**Form Templates:** Contact|Login|Registration|Settings|Survey|Multi-step
**Page Templates:** Landing|About|Pricing|Blog Post|Product|Profile
**Pattern Templates:** CRUD operations|Data tables|File uploads|Search|Filtering

**--watch:** Continuous build | Real-time feedback | Incremental | Live reload
**--interactive:** Step-by-step cfg | Interactive deps | Build customization

@include shared/research-patterns.yml#Mandatory_Research_Flows

@include shared/execution-patterns.yml#Git_Integration_Patterns

@include shared/universal-constants.yml#Standard_Messages_Templates