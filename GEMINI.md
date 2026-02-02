# Gemini Context: Greeter (Template Python Library)

## Project Overview

**Greeter** is a template Python library designed to demonstrate a modern, high-performance project structure. It serves as a "Hello World" implementation managed by modern tooling.

- **Primary Language:** Python (3.7+)
- **Package Manager:** `uv` (Fast Python package installer and resolver)
- **Build Backend:** `setuptools`
- **Version Control:** Git with Conventional Commits
- **Architecture:** Standard `src`-layout package structure.

## Building and Running

This project uses a `Makefile` to abstract common development tasks. `uv` is the primary tool for environment and dependency management.

### Prerequisites

- `uv`: Must be installed and in PATH.
- `asdf`: Recommended for Python version management (referenced in `Makefile`).

### Key Commands

| Action            | Command                | Description                                                |
| :---------------- | :--------------------- | :--------------------------------------------------------- |
| **Setup**         | `make setup`           | Installs dependencies via `uv sync` and sets up git hooks. |
| **Test**          | `make test`            | Runs the test suite using `pytest`.                        |
| **Lint (Check)**  | `make lint`            | Checks code style and quality using `ruff`.                |
| **Lint (Fix)**    | `make lint-fix`        | Auto-fixes lint/format issues with `ruff`.                 |
| **Release (Dry)** | `make release-dry-run` | Previews next version and changelog.                       |
| **Release**       | `make release`         | New release via `semantic-release`.                        |
| **Clean**         | `make clean`           | Removes build artifacts and caches.                        |

## Development Conventions

### Code Style & Quality

- **Formatter/Linter:** `ruff` is the single source of truth for linting and formatting.
- **Configuration:** Rules are defined in `pyproject.toml`.
  - **Quotes:** Double quotes.
  - **Line Length:** 88 characters.
  - **Target:** Python 3.7.
- **Typing:** Type hints are expected in function signatures
  (e.g., `def greet(self, name: Optional[str] = None) -> str:`).

### TDD Workflow (Strict)

This project mandates a strict Test-Driven Development (TDD) process for all AI
agents and contributors:

1. **RED**: Write a failing test first that describes the intended behavior.
2. **GREEN**: Write the minimum code necessary to make the test pass.
3. **REFACTOR**: Clean up the implementation. A refactor is only complete when:

- Code quality checks (`make lint`) pass without any issues.
- Code adheres to **SOLID** principles.
- Tests still pass.

### Dependency Management

- **Tool:** `uv` is used for all dependency operations.
- **Lockfile:** `uv.lock` is committed and should be kept in sync.
- **Adding Dependencies:** Use `uv add <package>` instead of manual `pip install`.

### Versioning & Commits

- **Strategy:** Semantic Versioning (SemVer) automated by `python-semantic-release`.
- **Commit Messages:** STRICT adherence to **Conventional Commits** is required.
  - Structure: `<type>(<scope>): <description>`
  - Types: `feat` (triggers minor), `fix` (triggers patch), `docs`, `style`,
      `refactor`, `perf`, `test`, `chore`.
  - **Enforcement:** A `commit-msg` git hook validates messages locally.

### Testing

- **Framework:** `pytest`.
- **Location:** All tests reside in the `tests/` directory.
- **Coverage:** The project aims for high test coverage.

## CI/CD & Releases

This project uses GitHub Actions for automated quality checks and a gated manual
release process.

### Quality Gate (CI)

- **Workflow:** `ci.yml`
- **Trigger:** Every push and pull request.
- **Requirement:** Code must pass linting (`ruff`) and testing (`pytest`) to
  maintain a "green" branch.

### Manual Release Process

- **Workflow:** `manual_release.yml`
- **Trigger:** Manual execution via GitHub Actions "**Run workflow**".
- **Safety Gate:** The release workflow automatically runs the full test suite
  again. It will fail if the branch is not green.
- **Selection:** Allows manual selection of release type: `patch` (default),
  `minor`, or `major`.
- **Automation:** Uses `python-semantic-release` to tag the version, update the
  changelog, and trigger the PyPI publication.

### Distribution

- **Workflow:** `publish.yml`
- **Trigger:** Automated by the creation of a new version tag (`v*`).

## Project Structure

- `src/greeter/`: Source code package.
- `tests/`: Unit tests.
- `scripts/`: Helper scripts (e.g., system setup, git hooks).
- `.github/workflows/`:
  - `ci.yml`: Standard validation on push/PR.
  - `manual_release.yml`: Gated manual release trigger.
  - `publish.yml`: Automated PyPI distribution.
