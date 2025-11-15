# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-11-15

### Added
- **Complete project overhaul** with modern Python best practices
- **Comprehensive test suite** with 100+ tests and >90% coverage
- **Full type hints** throughout the codebase for better IDE support
- **Pre-commit hooks** configuration (black, isort, flake8, mypy)
- **Makefile** with 20+ development commands
- **CONTRIBUTING.md** with detailed contribution guidelines
- **Homebrew support** with formula for easy macOS installation
- **One-command installation script** (`install.sh`) for hassle-free setup
- **Enhanced CI/CD pipeline** with multi-version testing and automated deployment
- **Robust error handling** for permission errors, missing files, and edge cases
- **Performance optimizations** for large directory trees
- **Cross-platform compatibility** improvements
- **Multiple installation methods**: pip, pipx, Homebrew, source
- **Professional documentation** with badges and examples
- **Security scanning** with bandit and safety
- **Coverage reporting** with HTML and XML output
- **Tox configuration** for testing across Python versions

### Changed
- **Complete CLI rewrite** with improved argument parsing and help text
- **Modern packaging** using pyproject.toml (removed setup.py)
- **Clean project structure** with src/ layout
- **Enhanced unit conversion** with better accuracy
- **Improved output formatting** with consistent style
- **Better error messages** with clear, actionable feedback
- **Updated documentation** with comprehensive examples and installation guide
- **Streamlined dependencies** - now uses only Python standard library
- **Better exit codes** for different error scenarios

### Fixed
- **Version mismatch** across all project files
- **Inconsistent code style** and formatting issues
- **Missing error handling** for various edge cases
- **Incomplete type hints** throughout the codebase
- **Test coverage gaps** - now comprehensive for all features
- **Documentation inconsistencies** and outdated examples
- **Build process issues** with modern Python packaging
- **Installation complexity** - now multiple easy methods

### Removed
- **setup.py** - replaced with modern pyproject.toml
- **script.py** - test script no longer needed
- **README.de.md** - German documentation consolidated

### Security
- Added security scanning in CI/CD pipeline
- Improved input validation and sanitization
- Better handling of file system permissions

### Performance
- Optimized directory traversal for large trees
- Reduced memory footprint
- Faster unit conversion algorithms
- Improved error handling performance

### Documentation
- Complete README rewrite with professional formatting
- Added installation script documentation
- Homebrew installation instructions
- Contributing guidelines
- Comprehensive API documentation
- Performance benchmarks section

### Added
- Multi-unit support (B, KB, MB, GB, TB) with auto-detection
- Clean/raw byte output mode (`-c` flag)
- Recursive directory sizing (`-r` flag)
- Force specific units (`-u` flag)
- Cross-platform compatibility (Windows, macOS, Linux)
- Command-line interface with argparse
- Basic error handling

### Changed
- Complete rewrite of the CLI tool
- Improved output formatting
- Better user experience

## [1.0.0] - 2024-01-01

### Added
- Initial release
- Basic file size calculation
- Simple CLI interface

[2.0.0]: https://github.com/thaikolja/filesize-cli/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/thaikolja/filesize-cli/releases/tag/v1.0.0
