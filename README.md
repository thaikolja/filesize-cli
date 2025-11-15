# filesize CLI

[![PyPI - Version](https://img.shields.io/pypi/v/filesize-cli)](https://pypi.org/project/filesize-cli/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/filesize-cli)](https://pypi.org/project/filesize-cli/)
[![GitHub CI](https://github.com/thaikolja/filesize-cli/workflows/CI/badge.svg)](https://github.com/thaikolja/filesize-cli/actions)
[![Coverage](https://codecov.io/gh/thaikolja/filesize-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/thaikolja/filesize-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

**filesize CLI** is a fast, reliable command-line tool for calculating file and directory sizes with intelligent unit formatting and recursive traversal support.

## ✨ Features

- **🎯 Intelligent Unit Detection**: Automatically selects the most appropriate unit (B, KB, MB, GB, TB) based on file size
- **📁 Recursive Directory Sizing**: Calculate total size of directories including all subdirectories with `-r`
- **🔢 Clean Raw Output**: Get raw byte sizes without formatting using `-c` flag
- **📏 Force Specific Units**: Display sizes in specific units (bytes, KB, MB, GB, TB) with `-u`
- **⚡ Fast & Efficient**: Optimized for performance with large directory trees
- **🛡️ Robust Error Handling**: Gracefully handles permission errors, missing files, and edge cases
- **🖥️ Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **🧪 Well-Tested**: Comprehensive test suite with >90% coverage
- **📦 Easy Installation**: Available on PyPI, install via pip or pipx

## 🔧 Requirements

- Python 3.9 or higher

## 🚀 Quick Start

### Installation

Choose one of the following installation methods:

#### 🍎 One-Command Installation (Easiest)

```bash
# Download and run the installation script
curl -sSL https://gitlab.com/thaikolja/filesize-cli/-/raw/main/install.sh | bash
```

#### 🍺 Homebrew (macOS/Linux)

```bash
# Install via Homebrew (recommended for macOS)
brew install filesize-cli

# Or tap and install
brew tap thaikolja/homebrew-filesize-cli
brew install filesize-cli
```

#### 📦 pipx (Cross-Platform, Isolated)

```bash
# Install with pipx (recommended for cross-platform)
pipx install filesize-cli

# If pipx is not installed:
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install filesize-cli
```

#### 🐍 pip (System-wide)

```bash
# Install from PyPI
pip install filesize-cli

# For user-only installation
pip install --user filesize-cli
```

#### 🔧 From Source

```bash
# Clone and install from source
git clone https://github.com/thaikolja/filesize-cli.git
cd filesize-cli
pip install .
```

### Basic Usage

```bash
# Show size of a file (auto unit detection)
filesize document.pdf

# Show size of a directory
filesize ~/Documents

# Recursive directory sizing
filesize -r ~/Projects

# Force specific unit
filesize -u mb image.jpg

# Raw bytes output
filesize -c data.bin

# Multiple paths
filesize file1.txt file2.txt directory/

# Combine flags
filesize -r -u gb ~/Downloads
```

## 🍺 Homebrew Support

For Homebrew users, filesize-cli is available as a formula:

```bash
# Standard installation
brew install filesize-cli

# Update to latest version
brew upgrade filesize-cli

# Uninstall
brew uninstall filesize-cli
```

### For Tap Maintainers

The Homebrew formula is located at `homebrew/filesize-cli.rb`. To submit to Homebrew core:

1. Update the SHA256 hash for the release
2. Submit a pull request to homebrew-core

## 📖 Command Reference

### Arguments

- `PATH [PATH ...]`: One or more files or directories to analyze (required)

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `-u, --unit {b,kb,mb,gb,tb}` | Force display in specific unit | `filesize -u mb file.txt` |
| `-c, --clean` | Display raw sizes in bytes only | `filesize -c file.txt` |
| `-r, --recursive` | Recurse into subdirectories | `filesize -r dir/` |
| `-v, --version` | Show version and exit | `filesize -v` |
| `-h, --help` | Show help message and exit | `filesize -h` |

### Exit Codes

- `0`: Success
- `1`: General error
- `130`: Operation cancelled (Ctrl+C)

## 💡 Examples

### 1. Auto Unit Detection

```bash
$ filesize photo.jpg
photo.jpg: 2.45 MB (1 file)
```

### 2. Force Specific Unit

```bash
$ filesize -u kb document.pdf
document.pdf: 1,247.00 KB (1 file)

$ filesize -u gb large-file.iso
large-file.iso: 4.50 GB (1 file)
```

### 3. Raw Byte Output

```bash
$ filesize -c config.json
1543
```

### 4. Directory Sizing

```bash
# Non-recursive (top-level only)
$ filesize ~/Documents
/Users/kolja/Documents: 45.20 MB (12 files)

# Recursive (including subdirectories)
$ filesize -r ~/Documents
/Users/kolja/Documents: 1.23 GB (1,456 files)
```

### 5. Multiple Paths

```bash
$ filesize file1.txt file2.txt dir/
file1.txt: 100 B (1 file)
file2.txt: 200 B (1 file)
dir/: 1.50 KB (3 files)
```

### 6. Development Usage

```python
from filesize_cli.cli import FilesizeCLI

# Create instance
cli = FilesizeCLI()

# Get size of a file
size_info = cli.get_size('/path/to/file.txt')
print(size_info)  # /path/to/file.txt: 1.23 MB (1 file)

# Get size with specific options
cli = FilesizeCLI(['-u', 'kb', '/path/to/file.txt'])
size_info = cli.get_size('/path/to/file.txt')
print(size_info)  # /path/to/file.txt: 1,259.00 KB (1 file)
```

## 🧪 Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/thaikolja/filesize-cli.git
cd filesize-cli

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Available Make Commands

```bash
make help          # Show all available commands
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Run all linters
make format        # Format code
make type-check    # Run mypy type checking
make build         # Build distribution packages
make clean         # Clean build artifacts
make security-check # Run security checks
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=filesize_cli --cov-report=html

# Run specific test file
pytest tests/test_cli.py

# Run with verbose output
pytest -v

# Run tests in watch mode
pytest-watch
```

### Code Quality

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pre-commit**: Automated checks before commits

```bash
# Run all checks
make lint

# Format code
make format

# Type checking
make type-check

# Run pre-commit hooks
pre-commit run --all-files
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. **Fork** the repository on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/filesize-cli.git
   cd filesize-cli
   ```
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Make changes** and **add tests**
5. **Run tests**: `pytest`
6. **Run linters**: `make lint`
7. **Commit**: `git commit -m "feat: add your feature"`
8. **Push**: `git push origin feature/your-feature-name`
9. **Submit a Merge Request**

### Reporting Issues

- **Bugs**: Use the [issue tracker](https://github.com/thaikolja/filesize-cli/issues) with label `bug`
- **Features**: Use the issue tracker with label `enhancement`
- **Questions**: Use the issue tracker with label `question`

## 📊 Performance

filesize-cli is optimized for performance:

- Efficient directory traversal using `pathlib`
- Minimal memory footprint
- Fast unit conversion algorithms
- Handles large directory trees (10,000+ files) efficiently

### Benchmarks

```bash
# Run performance benchmarks
make benchmark

# Manual performance test
make perf-test
```

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## 🧑‍💻 Authors

- **Kolja Nolte** - Initial work - [GitLab](https://gitlab.com/thaikolja)

## 🙏 Acknowledgments

- Python community for excellent tooling
- Contributors and bug reporters

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/thaikolja/filesize-cli/issues)
- **Email**: kolja.nolte@gmail.com
- **Website**: https://www.kolja-nolte.com

---

**Made with ❤️ by Kolja Nolte**
