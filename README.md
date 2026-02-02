# Greeter 🚀

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, high-performance Python library designed as a template for extensible "Hello World" implementations. Built with modern tooling, it provides a simple yet powerful greeting API.

## ✨ Features

- **Simple API**: Easy-to-use greeting functionality.
- **Modern Tooling**: Managed with [uv](https://github.com/astral-sh/uv) and [Ruff](https://github.com/astral-sh/ruff).
- **Cross-Platform**: Fully supports macOS and Debian-based Linux.
- **CI/CD Ready**: Includes a production-quality `Makefile` and `pyproject.toml`.
- **High Quality**: 100% test coverage with `pytest` and strict linting.

## 💻 OS Support

This library supports:

- **macOS** (Apple Silicon and Intel)
- **Debian-based Linux** (Ubuntu, Debian, etc.)

## 🛠️ System Setup

Before development, ensure you have system-level dependencies. We provide a bootstrap script:

```bash
./scripts/setup_system.sh
```

Ensure `uv` and `asdf` are in your `PATH`. Then, initialize the development environment:

```bash
make setup
```

## 📦 Installation

To install the CLI tool locally:

```bash
# Using uv (recommended)
uv add greeter

# or using pip
pip install greeter
```

### Adding as a Project Dependency

If you want to use this library in another project, add it via one of the following methods:

#### Using `uv` (Recommended)

```bash
# Add as a local path dependency
uv add --path /path/to/greeter-library greeter

# Add as a git dependency
uv add git+https://github.com/jalvarezsamayoa/template-python-library.git
```

#### Using `pip`

```bash
# Add to your requirements.txt
greeter @ file:///path/to/greeter-library
# or
greeter @ git+https://github.com/jalvarezsamayoa/template-python-library.git
```

## 🚀 Usage

```python
from greeter import Greeter

# Initialize the greeter
greeter = Greeter()

# Classic greeting
print(greeter.greet())
# Output: Hello World

# Personalized greeting
print(greeter.greet("Alice"))
# Output: Hello Alice
```

## 📝 Logging

The `greeter` library uses Python's standard `logging` module. By default, it is silent (using `logging.NullHandler`).

### Simple Setup

For quick debugging, you can use the built-in helper:

```python
import greeter
import logging

# Quickly enable debug logging for the library
greeter.setup_logging(level=logging.DEBUG)

g = greeter.Greeter()
g.greet()  # This will now print debug logs to stderr
```

### Advanced Configuration

If you want to integrate with your application's logging configuration, you can target the `greeter` logger:

```python
import logging

# Configure the 'greeter' logger manually
logger = logging.getLogger("greeter")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("app.log"))
```

## 📂 Project Structure

```text
.
├── src/                # Source code
│   └── greeter/        # Package directory
├── tests/              # Test suite
├── scripts/            # Automation scripts
├── Makefile            # Development commands
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

## 🧪 Development

We favor `uv` for lightning-fast environment management. You can see all available development commands by running:

```bash
make help
```

| Command                | Description                                           |
| :--------------------- | :---------------------------------------------------- |
| `make help`            | Display a help screen with all available commands.    |
| `make setup`           | Install all development dependencies.                 |
| `make test`            | Run the test suite with `pytest`.                     |
| `make lint`            | Check code style and quality with `ruff`.             |
| `make lint-fix`        | Automatically fix linting and formatting issues.      |
| `make release-dry-run` | Preview the next version and changelog.               |
| `make release`         | Create a new release (tags, version bump, changelog). |
| `make clean`           | Remove build artifacts and caches.                    |

## 🤝 Contributing

This project enforces [Conventional Commits](https://www.conventionalcommits.org/). Our CI and automated tooling rely on this format.

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-new-feature`
3. Make your changes and ensure tests pass: `make test`
4. Commit your changes following the convention:
    - `feat: ...` for new features
    - `fix: ...` for bug fixes
    - `docs: ...`, `style: ...`, `refactor: ...`, `perf: ...`, `test: ...`, `chore: ...`
5. Push to the branch: `git push origin feature/my-new-feature`
6. Submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
