# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2.1.0

### Changed

- Professionalized README with cleaner structure and formatting ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Removed broken CI/CD and Codecov badges (workflows no longer in repo) ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Added PyPI Downloads badge to README ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Removed excessive emojis from documentation ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Simplified installation section to focus on working methods ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Consolidated command reference tables ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Updated pyproject.toml version to 2.1.0 ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Updated all dev dependencies to latest versions ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Added Python 3.13 to classifiers and tool configurations ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Removed unused mypy overrides section for tests ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Updated setuptools requirement to >=75.0 ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))

### Fixed

- Resolved mypy unused section warning ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Fixed test environment after dependency updates ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))

### Chore

- Verified all tests pass (36 passed, 1 skipped) ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Confirmed 93.14% test coverage (above the 90% threshold) ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Updated mypy python_version to 3.13 ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))
- Updated a black target-version to include py313 ([4b8fefe](https://github.com/thaikolja/filesize-cli/commit/4b8fefe))

## v2.0.0

[compare changes](https://github.com/thaikolja/filesize-cli/compare/v1.0.0...v2.0.0)

### Feat

- Complete project overhaul with modern Python best practices ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Comprehensive test suite with 100+ tests and >90% coverage ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Full type hints throughout the codebase ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Pre-commit hooks configuration (black, isort, flake8, mypy) ([7a60836](https://github.com/thaikolja/filesize-cli/commit/7a60836))
- Multi-unit support (B, KB, MB, GB, TB) with auto-detection ([ba7e518](https://github.com/thaikolja/filesize-cli/commit/ba7e518))
- Clean/raw byte output mode (`-c` flag) ([ba7e518](https://github.com/thaikolja/filesize-cli/commit/ba7e518))
- Recursive directory sizing (`-r` flag) ([ba7e518](https://github.com/thaikolja/filesize-cli/commit/ba7e518))
- Force specific units (`-u` flag) ([ba7e518](https://github.com/thaikolja/filesize-cli/commit/ba7e518))
- Zero external dependencies - uses only Python standard library ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))

### Changed

- Complete CLI rewrite with improved argument parsing ([ba7e518](https://github.com/thaikolja/filesize-cli/commit/ba7e518))
- Modern packaging using pyproject.toml (removed setup.py) ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Clean project structure with src/ layout ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Improved output formatting with consistent style ([ba7e518](https://github.com/thaikolja/filesize-cli/commit/ba7e518))
- Better error messages with clear, actionable feedback ([7a60836](https://github.com/thaikolja/filesize-cli/commit/7a60836))

### Fixed

- Version mismatch across all project files ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Inconsistent code style and formatting issues ([7a60836](https://github.com/thaikolja/filesize-cli/commit/7a60836))
- Missing error handling for various edge cases ([7a60836](https://github.com/thaikolja/filesize-cli/commit/7a60836))
- Test coverage gaps ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))

### Removed

- setup.py - replaced with modern pyproject.toml ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- script.py - test script no longer needed ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- README.de.md - German documentation consolidated ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))

### Security

- Added security scanning with bandit and safety ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Improved input validation and sanitization ([7a60836](https://github.com/thaikolja/filesize-cli/commit/7a60836))

### Docs

- Complete README rewrite with professional formatting ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))
- Contributing guidelines ([ea7bc5e](https://github.com/thaikolja/filesize-cli/commit/ea7bc5e))
- Comprehensive API documentation ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))

### Chore

- Remove GitHub templates, workflows, and Homebrew formula ([97a79cd](https://github.com/thaikolja/filesize-cli/commit/97a79cd))
- Production readiness cleanup ([7a60836](https://github.com/thaikolja/filesize-cli/commit/7a60836))
- Prepare for production release ([a1d1fbe](https://github.com/thaikolja/filesize-cli/commit/a1d1fbe))

## v1.1.0

### Feat

- Auto unit detection in default mode ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Unit override with `--unit`/`-u` argument ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

### Changed

- Rewrite of major parts for performance, stability, and compatibility ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Updated and refined unit tests via `pytest` ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Stripped `requirements.txt` to only include necessary files ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Updated `setup.py` ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

## v1.0.2

### Added

- Code documentation ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Code comments ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

### Fixed

- Wrong configuration that permanently enabled `-p`/`--pretty` ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Removed unused variable ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

### Changed

- Completed `README.md` ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Project metadata ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

## v1.0.1

### Added

- Compatible packages and metadata for PyPI ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

## v1.0.0

[release](https://github.com/thaikolja/filesize-cli/releases/tag/v1.0.0)

### Feat

- Initial release ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Basic file size calculation ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))
- Simple CLI interface ([c7b314c](https://github.com/thaikolja/filesize-cli/commit/c7b314c))

### Contributors

- Kolja Nolte ([@thaikolja](https://github.com/thaikolja))
