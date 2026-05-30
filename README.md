# filesize-cli

[![PyPI - Version](https://img.shields.io/pypi/v/filesize-cli)](https://pypi.org/project/filesize-cli/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/filesize-cli)](https://pypi.org/project/filesize-cli/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/filesize-cli)](https://pypi.org/project/filesize-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A zero-dependency command-line tool for calculating file and directory sizes with intelligent unit formatting and recursive traversal support.

## Features

- **Intelligent Unit Detection**: Automatically selects the most appropriate unit (B, KB, MB, GB, TB) based on file size
- **Recursive Directory Sizing**: Calculate total size of directories including all subdirectories with `-r`
- **Clean Raw Output**: Get raw byte sizes without formatting using `-c` flag
- **Force Specific Units**: Display sizes in specific units with `-u`
- **Zero External Dependencies**: Uses only Python standard library (`argparse`, `pathlib`, `typing`, `sys`)
- **Robust Error Handling**: Gracefully handles permission errors, missing files, and edge cases
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Well-Tested**: Comprehensive test suite with >90% coverage

## Requirements

- Python 3.9 or higher

## Installation

```bash
# From PyPI
pip install filesize-cli

# Using pipx (isolated environment)
pipx install filesize-cli

# From source
git clone https://github.com/thaikolja/filesize-cli.git
cd filesize-cli
pip install .
```

## Usage

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
```

## Command Reference

### Arguments

| Argument | Description |
|----------|-------------|
| `PATH [PATH ...]` | One or more files or directories to analyze (required) |

### Options

| Option | Description |
|--------|-------------|
| `-u, --unit {b,kb,mb,gb,tb}` | Force display in specific unit |
| `-c, --clean` | Display raw sizes in bytes only |
| `-r, --recursive` | Recurse into subdirectories |
| `-v, --version` | Show version and exit |
| `-h, --help` | Show help message and exit |

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | General error |
| `130` | Operation cancelled (Ctrl+C) |

## Examples

### Auto Unit Detection

```bash
$ filesize photo.jpg
photo.jpg: 2.45 MB (1 file)
```

### Force Specific Unit

```bash
$ filesize -u kb document.pdf
document.pdf: 1,247.00 KB (1 file)
```

### Raw Byte Output

```bash
$ filesize -c config.json
1543
```

### Directory Sizing

```bash
# Non-recursive (top-level only)
$ filesize ~/Documents
/Users/kolja/Documents: 45.20 MB (12 files)

# Recursive (including subdirectories)
$ filesize -r ~/Documents
/Users/kolja/Documents: 1.23 GB (1,456 files)
```

### Programmatic Usage

```python
from filesize_cli.cli import FilesizeCLI

cli = FilesizeCLI()
size_info = cli.get_size('/path/to/file.txt')
print(size_info)  # /path/to/file.txt: 1.23 MB (1 file)
```

## Development

### Setup

```bash
git clone https://github.com/thaikolja/filesize-cli.git
cd filesize-cli
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

### Commands

| Action | Command |
|--------|---------|
| format | `black src tests && isort src tests` |
| lint | `black --check src tests && isort --check-only src tests && flake8 src tests && mypy src` |
| test | `pytest` |
| coverage | `pytest --cov=filesize_cli --cov-report=html` |
| build | `python -m build` |

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Kolja Nolte** - [GitHub](https://github.com/thaikolja) | [Website](https://www.kolja-nolte.com)
