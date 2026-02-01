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

| Action            | Command                | Description                                                    |
| :---------------- | :--------------------- | :------------------------------------------------------------- |
| **Setup**         | `make setup`           | Installs dependencies via `uv sync` and sets up git hooks.     |
| **Test**          | `make test`            | Runs the test suite using `pytest`.                            |
| **Lint (Check)**  | `make lint`            | Checks code style and quality using `ruff`.                    |
| **Lint (Fix)**    | `make lint-fix`        | Automatically fixes linting and formatting issues with `ruff`. |
| **Release (Dry)** | `make release-dry-run` | Previews the next version and changelog.                       |
| **Release**       | `make release`         | Creates a new release using `semantic-release`.                |
| **Clean**         | `make clean`           | Removes build artifacts, caches, and virtual environments.     |

## Development Conventions

### Code Style & Quality

- **Formatter/Linter:** `ruff` is the single source of truth for linting and formatting.
- **Configuration:** Rules are defined in `pyproject.toml`.
    - **Quotes:** Double quotes.
    - **Line Length:** 88 characters.
    - **Target:** Python 3.7.
- **Typing:** Type hints are expected in function signatures (e.g., `def greet(self, name: Optional[str] = None) -> str:`).

### Dependency Management

- **Tool:** `uv` is used for all dependency operations.
- **Lockfile:** `uv.lock` is committed and should be kept in sync.
- **Adding Dependencies:** Use `uv add <package>` instead of manual `pip install`.

### Versioning & Commits

- **Strategy:** Semantic Versioning (SemVer) automated by `python-semantic-release`.
- **Commit Messages:** STRICT adherence to **Conventional Commits** is required.
    - Structure: `<type>(<scope>): <description>`
    - Types: `feat` (triggers minor), `fix` (triggers patch), `docs`, `style`, `refactor`, `perf`, `test`, `chore`.
    - **Enforcement:** A `commit-msg` git hook validates messages locally.

### Testing

- **Framework:** `pytest`.
- **Location:** All tests reside in the `tests/` directory.
- **Coverage:** The project aims for high test coverage.

### Project Structure

- `src/greeter/`: Source code package.
- `tests/`: Unit tests.
- `scripts/`: Helper scripts (e.g., system setup, git hooks).
- `.github/workflows/`: CI/CD pipelines (GitHub Actions).
