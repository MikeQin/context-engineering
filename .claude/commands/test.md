**Purpose**: Comprehensive testing framework

---

@include shared/universal-constants.yml#Universal_Legend

## Command Execution
Execute: immediate. --plan→show plan first
Legend: Generated based on symbols used in command
Purpose: "[Action][Subject] in $ARGUMENTS"

Create or run comprehensive test suites for code specified in $ARGUMENTS using modern testing frameworks and methodologies.

@include shared/flag-inheritance.yml#Universal_Always

Examples:
- `/test --tdd` - Test-driven development workflow
- `/test --coverage` - Generate coverage report
- `/test --cli --command-testing` - CLI command interaction testing
- `/test --integration` - Run integration tests
- `/test --e2e` - Run end-to-end tests

## Command-Specific Flags
--tdd: "Test-driven development workflow (write failing test→implement→pass)"
--coverage: "Generate detailed coverage reports w/ uncovered lines"
--integration: "Run integration tests across components/services"
--e2e: "Run end-to-end tests w/ real browser/environment"
--unit: "Focus on unit tests only (default)"
--mutation: "Run mutation testing to verify test quality"
--snapshot: "Update/verify snapshot tests"
--watch: "Run tests continuously on file changes"
--bail: "Stop on first test failure"
--parallel: "Run tests in parallel workers"
--update-snapshots: "Update all snapshot tests"
--cli: "CLI application testing mode"
--command-testing: "Test CLI command interactions and outputs"
--cli-args: "Test command-line argument parsing and validation"
--cli-integration: "Test CLI with real subprocess execution"

## Testing Approaches

**Unit Testing:** Isolated component/function tests | Mock all dependencies | Fast execution | High coverage target

**Integration Testing:** Component interaction tests | Real service calls | Database transactions | API endpoint tests

**E2E Testing:** Full user workflows | Browser automation | Real environment | Critical path coverage

**TDD Workflow:** Red→Green→Refactor cycle | Write minimal code | Comprehensive coverage | Design emergence

**CLI Testing:** Command interaction tests | Argument parsing validation | Exit code verification | Output format testing

## Testing Patterns

**Test Structure:** Arrange-Act-Assert (AAA) | Given-When-Then (BDD) | Setup→Execute→Verify→Teardown

**Coverage Targets:** Statements: 80%+ | Branches: 75%+ | Functions: 90%+ | Lines: 80%+

**Test Organization:** 
- `__tests__/` or `test/` directories
- `*.test.{js,ts}` or `*.spec.{js,ts}` naming
- Mirror source structure in test directories
- Group by feature or component

## CLI Testing Patterns

**CLI Test Structure:**
- `tests/test_cli.py` - Main CLI interface testing
- `tests/test_commands/` - Individual command testing
- `tests/fixtures/` - Test data and configuration files
- `tests/integration/` - CLI integration testing

**CLI Testing Strategies:**
- Click CliRunner for isolated command testing
- Subprocess testing for real CLI execution
- Mock external dependencies and file systems
- Test argument parsing and validation
- Verify exit codes and error messages
- Test configuration loading and precedence

**CLI Test Patterns:**
- Test help text and usage information
- Test command combinations and option flags
- Test with various input formats and edge cases
- Test interactive prompts and user input
- Test output formatting (JSON, table, plain text)
- Test error handling and recovery scenarios

@include shared/quality-patterns.yml#Test_Quality_Standards

## Framework Support

**JavaScript/TypeScript:** Jest (default) | Mocha + Chai | Vitest | Testing Library

**Python:** pytest (default) | unittest | nose2 | doctest | Click testing utilities

**Go:** Built-in testing | Testify | Ginkgo/Gomega

**Java:** JUnit 5 | TestNG | Mockito | Spring Test

**Other:** Framework-specific best practices | Native test runners

## Deliverables

**Test Files:** Created in appropriate test directories | Following naming conventions | Comprehensive test cases

**Coverage Reports:** HTML report in `coverage/` | Console summary | Uncovered line identification

**CI Configuration:** GitHub Actions | CircleCI | Jenkins | GitLab CI

**Documentation:** Test plan | Test cases | Coverage goals | CI/CD integration

@include shared/universal-constants.yml#Standard_Messages_Templates