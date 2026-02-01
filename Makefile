.DEFAULT_GOAL := help
.PHONY: help check-deps setup test lint lint-fix clean install-hooks release-dry-run release

help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

check-deps: ## Check if system dependencies (uv, asdf) are installed
	@command -v uv >/dev/null 2>&1 || { echo >&2 "uv is not installed. Please install it first."; exit 1; }
	@command -v asdf >/dev/null 2>&1 || { echo >&2 "asdf is not installed. Please install it first."; exit 1; }
	@echo "All dependencies (uv, asdf) are installed."

setup: install-hooks ## Setup the development environment (sync dependencies and install hooks)
	uv sync --all-extras

install-hooks: ## Install git hooks
	@echo "Installing git hooks..."
	@mkdir -p .git/hooks
	@cp scripts/git-hooks/commit-msg .git/hooks/commit-msg
	@chmod +x .git/hooks/commit-msg
	@echo "Git hooks installed."

test: ## Run tests using pytest
	uv run pytest

lint: ## Run linting checks using ruff
	uv run ruff check src tests
	uv run ruff format --check src tests

lint-fix: ## Automatically fix linting and formatting issues
	uv run ruff check --fix src tests
	uv run ruff format src tests

release-dry-run: ## Preview the next version and changelog
	uv run semantic-release version --print

release: ## Create a new release and update version
	uv run semantic-release version

clean: ## Remove build artifacts and caches
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type d -name .venv -exec rm -rf {} +
