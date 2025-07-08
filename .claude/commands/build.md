**Purpose**: Universal project builder with Next.js + Tailwind CSS templates

---

@include shared/universal-constants.yml#Universal_Legend

## Command Execution
Execute: immediate. --plan→show plan first
Legend: Generated based on symbols used in command
Purpose: "[Action][Subject] in $ARGUMENTS"

Build project/feature based on req in $ARGUMENTS using modern Next.js + Tailwind CSS stack.

@include shared/flag-inheritance.yml#Universal_Always

Examples:
- `/build --nextjs --tailwind --shadcn` - Next.js app w/ component library
- `/build --nextjs --tailwind --components` - Next.js app w/ component generation
- `/build --nextjs --app-router --forms` - Complete app with forms
- `/build --api --c7` - API w/ docs
- `/build --nextjs --tailwind --dashboard` - Dashboard application

Pre-build: Remove artifacts (dist/, build/, .next/) | Clean temp files & cache | Validate deps | Remove debug

Build modes:
**--init:** New project w/ stack (Next.js|API|Fullstack|Mobile|CLI) | TS default | Testing setup | Git workflow
**--feature:** Impl feature→existing patterns | Maintain consistency | Include tests  
**--tdd:** Write failing tests→minimal code→pass tests→refactor

## Next.js + Tailwind Templates:
- **Next.js:** App Router|TS|Tailwind|shadcn/ui|testing
- **API:** Express|TS|auth|validation|OpenAPI  
- **Fullstack:** Next.js+tRPC+Prisma+Docker
- **Mobile:** React Native+Expo+NativeWind
- **CLI:** Commander.js+cfg+testing

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