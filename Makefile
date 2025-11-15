# Makefile for filesize-cli development
# Provides common development tasks

.PHONY: help install install-dev test test-cov test-watch lint format type-check clean build upload-docs security-check

# Default target
help:
	@echo "filesize-cli Development Commands"
	@echo "=================================="
	@echo "install        - Install package in production mode"
	@echo "install-dev    - Install package with development dependencies"
	@echo "test           - Run tests"
	@echo "test-cov       - Run tests with coverage report"
	@echo "test-watch     - Run tests in watch mode (requires pytest-watch)"
	@echo "lint           - Run linting (black, isort, flake8)"
	@echo "format         - Format code (black, isort)"
	@echo "type-check     - Run mypy type checking"
	@echo "clean          - Clean build artifacts"
	@echo "build          - Build distribution packages"
	@echo "upload         - Upload to PyPI (requires credentials)"
	@echo "upload-test    - Upload to Test PyPI (requires credentials)"
	@echo "security-check - Run security checks (bandit, safety)"
	@echo "pre-commit     - Install and run pre-commit hooks"
	@echo "tox            - Run tests across multiple Python versions"
	@echo "docs           - Generate documentation (if available)"
	@echo "benchmark      - Run performance benchmarks"

# Installation
install:
	pip install .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

# Testing
test:
	pytest

test-cov:
	pytest --cov=filesize_cli --cov-report=term-missing --cov-report=html

test-watch:
	@echo "Installing pytest-watch if needed..."
	pip install pytest-watch
	ptw -- --testmon

# Linting and formatting
lint:
	@echo "Running black..."
	black --check src tests
	@echo "Running isort..."
	isort --check-only src tests
	@echo "Running flake8..."
	flake8 src tests
	@echo "Running mypy..."
	mypy src

format:
	@echo "Formatting with black..."
	black src tests
	@echo "Formatting with isort..."
	isort src tests

type-check:
	mypy src

# Pre-commit
pre-commit:
	pre-commit install
	pre-commit run --all-files

# Cleanup
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Building
build: clean
	@echo "Building distribution packages..."
	python -m build

# Upload to PyPI
upload-test: build
	@echo "Uploading to Test PyPI..."
	python -m twine upload --repository testpypi dist/*

upload: build
	@echo "Uploading to PyPI..."
	python -m twine upload dist/*

# Security checks
security-check:
	@echo "Running bandit security check..."
	pip install bandit
	bandit -r src/
	@echo "Running safety check..."
	pip install safety
	safety check

# Tox for multi-version testing
tox:
	tox

# Benchmarking
benchmark:
	@echo "Running benchmarks..."
	python -m pytest tests/ -k "benchmark" --benchmark-only

# Release process (requires version bump)
release-patch: check-clean check-tests
	bump2version patch
	git push --tags

release-minor: check-clean check-tests
	bump2version minor
	git push --tags

release-major: check-clean check-tests
	bump2version major
	git push --tags

check-clean:
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "Error: Working directory is not clean"; \
		git status; \
		exit 1; \
	fi

check-tests:
	pytest

# Documentation (placeholder)
docs:
	@echo "Documentation generation not configured yet"

# Performance test
perf-test:
	@echo "Creating large test directory..."
	@mkdir -p /tmp/perf-test
	@dd if=/dev/zero of=/tmp/perf-test/large-file.bin bs=1M count=10 2>/dev/null
	@echo "Running performance test..."
	@time filesize /tmp/perf-test -r
	@rm -rf /tmp/perf-test
