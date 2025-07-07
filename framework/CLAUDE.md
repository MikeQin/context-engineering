# CLAUDE.md - Development Methodology

> **Framework Setup Complete!** This file was copied from the Context Engineering Framework.
> Your project now has the complete Three-Document Pattern:
> - **PRODUCT_PRP.md** (or PRODUCT_PRP_SLIM.md) - WHAT to build  
> - **CLAUDE.md** (this file) - HOW to build
> - **[PRODUCT_NAME]_DESIGN.md** (generate with `/generate_design`) - Technical architecture

### 🔄 Project Awareness & Context
- **Always read `*_PRP.md`** as product requirements prompt or product requirements document at the start of a new conversation to understand product requirements.
- **Always read `DESIGN.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `DESIGN.md`.
- **Use venv_linux** (the virtual environment) whenever executing Python commands, including for unit tests.
- **For Next.js projects**, always check `package.json` for dependencies and scripts before adding new packages or running commands.

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.

#### Python Projects (Backend/API/Agents)
- **Project structure by type**:
  - **Web APIs**: 
    - `main.py` - FastAPI application entry point
    - `api/` - API routes and endpoints
    - `models/` - Pydantic models and database schemas
    - `services/` - Business logic layer
    - `db/` - Database configuration and migrations
  - **AI Agents**:
    - `agent.py` - Main agent definition and execution logic 
    - `tools.py` - Tool functions used by the agent 
    - `prompts.py` - System prompts
  - **General Python**:
    - `src/` - Main source code directory
    - `config/` - Configuration files and settings
    - `utils/` - Utility functions and helpers
    - `tests/` - Test files mirroring source structure
- **Package organization**:
  - **Use clear, consistent imports** (prefer relative imports within packages)
  - **Follow Python packaging standards** with `__init__.py` files
  - **Separate business logic from framework code**
- **Environment and dependencies**:
  - **Use `python-dotenv` and `.env` files** for environment variables
  - **Prefer Poetry or pip-tools** for dependency management
  - **Pin dependency versions** in production
  - **Use virtual environments** (`venv_linux` or project-specific)

#### Next.js Projects (Frontend)
  - **Follow App Router structure** - Use `app/` directory for Next.js 13+
  - **Page organization**:
    - `app/page.js` - Home page
    - `app/[feature]/page.js` - Feature pages
    - `app/[feature]/layout.js` - Feature-specific layouts
  - **Component organization**:
    - `components/` - Reusable UI components
    - `components/ui/` - Basic UI primitives (buttons, inputs, etc.)
    - `components/features/` - Feature-specific components
  - **Utility organization**:
    - `utils/` - Pure utility functions
    - `hooks/` - Custom React hooks
    - `lib/` - External library configurations
  - **Use absolute imports** with path mapping in `next.config.js` when beneficial
  - **Environment variables**: Use `.env.local` for Next.js environment variables

### 🧪 Testing & Reliability

#### Python Testing (Backend/API)
- **Test structure and organization**:
  - **Tests should live in a `/tests` folder** mirroring the main app structure
  - **Use descriptive test file names**: `test_feature_name.py`
  - **Group related tests in classes** with descriptive names
- **Testing patterns and requirements**:
  - **Always create Pytest unit tests for new features** (functions, classes, routes, etc)
  - **After updating any logic**, check whether existing unit tests need to be updated
  - **Include comprehensive test coverage**:
    - 1 test for expected/happy path use
    - 1+ edge cases (boundary conditions, empty inputs)
    - 1+ failure cases (invalid inputs, error conditions)
    - Integration tests for API endpoints
- **Testing tools and fixtures**:
  - **Use pytest fixtures** for setup and teardown
  - **Use pytest-asyncio** for async function testing
  - **Use pytest-mock** or `unittest.mock` for mocking dependencies
  - **Use factories or builders** for test data generation
- **API testing specifics**:
  - **Use FastAPI TestClient** for endpoint testing
  - **Test authentication and authorization** where applicable
  - **Test request/response serialization**
  - **Mock external dependencies** (databases, APIs, services)
- **Database testing**:
  - **Use test database or in-memory SQLite** for isolation
  - **Use database fixtures** for consistent test data
  - **Test database migrations** and schema changes

#### Next.js Testing (Frontend)
- **Use Jest and React Testing Library** for component testing
- **Test file location**: Co-locate tests with components or use `__tests__` folders
- **Testing patterns**:
  - `ComponentName.test.js` for component tests
  - `utils.test.js` for utility function tests
  - `hooks.test.js` for custom hook tests
- **Include tests for**:
  - Component rendering and props
  - User interactions (clicks, form submissions)
  - Hook behavior and state changes
  - Utility function logic
- **Always run `npm run build` before declaring code complete** to catch build-time errors
- **Run `npm run lint` to ensure code quality** and fix any ESLint warnings

### ✅ Task Management & Progress
- **Follow the requirements in the PRP document** as the source of truth for project scope
- **Track implementation progress** against the DESIGN.md architecture plan
- **Use Claude Code's built-in TodoWrite tool** for dynamic task tracking during development sessions
- **Update DESIGN.md** when architectural decisions change or new technical requirements emerge
- **Communicate progress clearly** with status updates and completion confirmations

### 📎 Style & Conventions

#### Technology Stack
- **Backend**: Python with FastAPI, SQLAlchemy/SQLModel for ORM
- **Frontend**: Next.js (App Router), JavaScript, Tailwind CSS
- **Database**: PostgreSQL (Production), SQLite (Dev/Sandbox)

#### Python Style (Backend/API)
- **Code formatting and style**:
  - **Follow PEP8** with line length of 88 characters (Black default)
  - **Use `black` for code formatting** and `isort` for import sorting
  - **Use `ruff` or `flake8`** for additional linting
  - **Use type hints consistently** for all function parameters and returns
- **Documentation standards**:
  - **Write docstrings for every function, class, and module** using Google style:
    ```python
    def process_data(data: list[dict], validate: bool = True) -> dict:
        """
        Process input data and return summary statistics.

        Args:
            data: List of dictionaries containing raw data
            validate: Whether to validate data before processing

        Returns:
            Dictionary with processed results and metadata

        Raises:
            ValueError: If data is empty or invalid format
            ValidationError: If validation fails
        """
    ```
  - **Include type information in docstrings** when types are complex
  - **Document exceptions that can be raised**
- **Code organization patterns**:
  - **Use `pydantic` for data validation** and serialization
  - **Use dependency injection** for services and database connections
  - **Separate concerns**: models, services, repositories, controllers
  - **Use async/await** for I/O operations (database, HTTP requests)
- **Error handling and logging**:
  - **Use structured logging** with `structlog` or Python's `logging`
  - **Create custom exception classes** for domain-specific errors
  - **Handle errors gracefully** with proper HTTP status codes
  - **Log meaningful context** (user IDs, request IDs, etc.)
- **Configuration and settings**:
  - **Use Pydantic Settings** for configuration management
  - **Separate config by environment** (dev, staging, prod)
  - **Never commit secrets** - use environment variables
  - **Use typed configuration classes**:
    ```python
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        database_url: str
        api_key: str
        debug: bool = False
        
        class Config:
            env_file = ".env"
    ```

#### Next.js/React Style (Frontend)
- **Use functional components with hooks** - No class components
- **Follow React naming conventions**:
  - Components: `PascalCase` (e.g., `UserProfile.js`)
  - Files: `PascalCase` for components, `camelCase` for utilities
  - Custom hooks: `useCamelCase` (e.g., `useGameState.js`)
- **Use 'use client' directive** when using browser APIs or hooks in App Router
- **Prefer named exports** for components to improve debugging
- **Use JSDoc comments for component props**:
  ```javascript
  /**
   * User profile component.
   *
   * @param {Object} props - Component props
   * @param {string} props.username - User's display name
   * @param {boolean} props.isActive - Whether user is currently active
   * @returns {JSX.Element} UserProfile component
   */
  export function UserProfile({ username, isActive }) {
    // Component implementation
  }
  ```
- **State management patterns**:
  - Local state: `useState` for simple state
  - Complex state: `useReducer` for state machines
  - Global state: Context API or external library (Zustand, Redux Toolkit)
- **Styling conventions**:
  - **Primary**: Tailwind CSS utility classes
  - **Component variants**: Use conditional classes with logical operators
  - **Responsive design**: Mobile-first approach with Tailwind breakpoints
  - **Dark mode**: Use Tailwind's dark mode classes with next-themes

#### Code Organization Patterns
- **Imports order**:
  1. React imports
  2. Next.js imports  
  3. Third-party libraries
  4. Internal components/hooks
  5. Utility functions
  6. Types/constants
- **File naming**:
  - Components: `ComponentName.js`
  - Pages: `page.js` (App Router convention)
  - Layouts: `layout.js` (App Router convention)
  - Utilities: `functionName.js` or descriptive names
- **Export patterns**:
  - Default export for pages and single-purpose files
  - Named exports for components and utilities

### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.

#### Python Documentation
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.
- Use docstrings for all functions, classes, and modules.

#### Next.js Documentation  
- **Comment complex React patterns** and state logic
- **Document component APIs** with JSDoc for props and return types
- **Explain business logic** in comments, not just implementation details
- **Add README sections for**:
  - Setup and installation
  - Environment variables
  - Development scripts
  - Deployment instructions
  - Component usage examples

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to do so or if required by the project requirements.

#### Python-Specific Rules
- **Package and dependency management**:
  - **Only use verified Python packages** – check `requirements.txt`, `pyproject.toml`, or `poetry.lock` first
  - **Confirm virtual environment** is activated before installing packages
  - **Check package compatibility** with Python version and other dependencies
- **Code quality and patterns**:
  - **Avoid circular imports** - restructure code if needed
  - **Use dependency injection** instead of global variables
  - **Follow SOLID principles** for class design
  - **Prefer composition over inheritance**
  - **Use context managers** for resource management (files, connections)
- **Async programming patterns**:
  - **Use async/await consistently** in async functions
  - **Don't mix sync and async patterns** without proper handling
  - **Use asyncio for concurrent operations**
  - **Handle async context managers properly**
- **Performance considerations**:
  - **Use generators** for large data processing
  - **Implement pagination** for database queries
  - **Cache expensive computations** when appropriate
  - **Use connection pooling** for database connections

#### Next.js-Specific Rules  
- **Only use verified npm packages** – check `package.json` dependencies first
- **Check Next.js version compatibility** before suggesting features or patterns
- **Verify App Router vs Pages Router** - default to App Router unless specified otherwise
- **Always test imports** - ensure components and utilities exist before importing
- **Respect React patterns** - use hooks correctly and avoid anti-patterns
- **Check for 'use client' needs** - add directive when using browser APIs or interactive hooks
- **Validate Tailwind classes** - use standard Tailwind utilities, avoid custom CSS unless necessary

### 🔧 Development Workflow

#### Python Development
- **Environment setup**:
  - Use virtual environment (`venv_linux` or project-specific)
  - Install dependencies: `pip install -r requirements.txt` or `poetry install`
- **Code quality checks**:
  - Format code: `black .` and `isort .`
  - Lint code: `ruff check .` or `flake8`
  - Type checking: `mypy .` (if configured)
  - Security scan: `bandit -r .` (for security issues)
- **Testing workflow**:
  - Run tests: `pytest` or `python -m pytest`
  - Coverage: `pytest --cov=src --cov-report=html`
  - Specific tests: `pytest tests/test_feature.py::test_function`
- **Database operations**:
  - Migrations: `alembic upgrade head` (if using Alembic)
  - Schema validation: Check model changes against database
- **Local development**:
  - Development server: `uvicorn main:app --reload` (for FastAPI)
  - Environment variables: Copy `.env.example` to `.env`

#### Next.js Development  
- Install dependencies: `npm install`
- Development server: `npm run dev`
- Build verification: `npm run build`
- Linting: `npm run lint`
- Testing: `npm test` (if configured)

### 🚀 Quality Gates

#### Python Projects
- **Code quality**: All linting passes (`ruff`, `black`, `isort`)
- **Type safety**: Type checking passes (`mypy`)
- **Testing**: All tests pass with adequate coverage (>80%)
- **Security**: Security scan passes (`bandit`)
- **Dependencies**: All dependencies are up-to-date and secure
- **Documentation**: All functions have docstrings, README updated

#### Next.js Projects  
- **Build verification**: `npm run build` succeeds
- **Code quality**: ESLint passes with no warnings
- **Type safety**: No TypeScript errors (if using TypeScript)
- **Testing**: Component and utility tests pass
- **Performance**: No console errors or warnings
- **Documentation**: Component APIs documented, README updated

#### Both Project Types
- **Documentation complete**: README, API docs, setup instructions
- **Environment configuration**: Example env files provided
- **Code review**: Code follows established patterns and conventions
- **Security**: No secrets committed, proper error handling