# Contributing to filesize-cli

Thank you for your interest in contributing to filesize-cli! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

1. **Check existing issues**: Search the [issue tracker](https://gitlab.com/thaikolja/filesize-cli/issues) to see if the bug has already been reported.
2. **Create a new issue**: If not found, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce the bug
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages or stack traces

### Suggesting Features

1. **Check existing issues**: Search for similar feature requests.
2. **Create a new issue** with:
   - Clear description of the feature
   - Use case or problem it solves
   - Proposed implementation (if applicable)
   - Label: `enhancement`

### Pull Requests

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/filesize-cli.git
   cd filesize-cli
   ```

3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   pre-commit install
   ```

4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

5. **Make your changes**:
   - Write clean, readable code
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

6. **Run tests and checks**:
   ```bash
   # Run tests
   pytest

   # Run linting
   make lint

   # Run type checking
   make type-check

   # Run pre-commit hooks
   pre-commit run --all-files
   ```

7. **Commit your changes**:
   - Use [conventional commits](https://www.conventionalcommits.org/):
     - `feat:` New feature
     - `fix:` Bug fix
     - `docs:` Documentation changes
     - `style:` Code style changes
     - `refactor:` Code refactoring
     - `test:` Adding or updating tests
     - `chore:` Maintenance tasks
   - Example: `feat: add support for custom units`

8. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Submit a Pull Request**:
   - Go to the original repository on GitHub
   - Click "Create pull request"
   - Fill in the description with:
     - What changes you made
     - Why you made them
     - Any breaking changes
     - Related issue numbers (e.g., "Fixes #123")

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use Black for code formatting (line length: 88)
- Use isort for import sorting
- Use type hints for all functions and methods
- Write docstrings for all public functions/classes

### Testing

- Write tests for all new functionality
- Maintain >90% code coverage
- Use pytest for testing
- Include unit tests and integration tests
- Test edge cases and error conditions

### Documentation

- Update README.md if adding user-facing features
- Add docstrings to all functions and classes
- Keep examples up to date
- Update CHANGELOG.md for significant changes

### Performance

- Consider performance implications of changes
- Profile code if working with large files/directories
- Optimize for common use cases

## Project Structure

```
filesize-cli/
├── src/
│   └── filesize_cli/
│       ├── __init__.py
│       └── cli.py          # Main CLI implementation
├── tests/
│   └── test_cli.py         # Test suite
├── docs/                   # Documentation
├── .gitignore
├── .pre-commit-config.yaml # Pre-commit hooks
├── .gitlab-ci.yml         # CI/CD configuration
├── pyproject.toml         # Project metadata and tool config
├── Makefile              # Development commands
├── README.md
├── CONTRIBUTING.md       # This file
├── CHANGELOG.md          # Version history
└── LICENSE
```

## Release Process

1. Update version in `pyproject.toml` and `src/filesize_cli/__init__.py`
2. Update `CHANGELOG.md` with new version and changes
3. Create a new commit: `git commit -m "chore: bump version to X.Y.Z"`
4. Create a tag: `git tag vX.Y.Z`
5. Push: `git push origin main --tags`
6. CI/CD will automatically build and deploy to PyPI

## Getting Help

- **Issues**: Use the [issue tracker](https://github.com/thaikolja/filesize-cli/issues) with label `bug`
- **Features**: Use the issue tracker with label `enhancement`
- **Questions**: Use the issue tracker with label `question`
- **Discussions**: Use GitLab discussions on issues/MRs
- **Email**: kolja.nolte@gmail.com (for private matters)

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for significant contributions
- Project documentation
- Release notes

Thank you for contributing to filesize-cli!
