# AGENTS.md — filesize-cli

## Setup

```bash
pip install -e ".[dev]"
pre-commit install
```

## Commands

| Action | Command |
|--------|---------|
| format | `black src tests && isort src tests` |
| lint | `black --check src tests && isort --check-only src tests && flake8 src tests && mypy src` |
| type-check | `mypy src` |
| test | `pytest` |
| test (single file) | `pytest tests/test_cli.py -v` |
| coverage (HTML) | `pytest --cov=filesize_cli --cov-report=html` |
| pre-commit all | `pre-commit run --all-files` |
| build | `python -m build` |
| security | `bandit -r src/ && safety check` |

Order: `make lint -> make test` before pushing.

## Architecture

- **Zero external dependencies** — stdlib only (`argparse`, `pathlib`, `typing`, `sys`)
- **Binary units** (1024 base): KB=1024, MB=1024², GB=1024³, TB=1024⁴
- **Entrypoint**: `filesize` command → `filesize_cli.cli:main` (via `[project.scripts]`)
- **Public API**: `FilesizeCLI().get_size(paths)` returns `Optional[str]`
- **src layout**: source lives under `src/filesize_cli/`
- **Single file**: entire implementation is `src/filesize_cli/cli.py` (249 lines)

## Quality gates

- **mypy strict mode** on `src/`; tests exempt from `disallow_untyped_defs`
- **Coverage must be ≥ 90%** (`--cov-fail-under=90`). Currently 81% — tests fail without improvement.
- **black** line-length: 88. **isort** profile: black.
- **Flake8** ignores `E203, W503`.

## Testing quirks

- Symlink test (`test_compute_size_not_file_or_dir`) skipped on platforms without symlink support.
- Markers `slow`, `integration` defined but not used in any test.
- Fixtures: `temp_file` (13-byte file), `temp_dir` (dir with 3 files), `cli` (empty-arg CLI instance).

## Gotchas

- **License mismatch**: `LICENSE` file is AGPL-3.0, but `pyproject.toml` metadata says MIT. Resolve before release.
- **CI workflows** (`.github/workflows/ci.yml`, `release.yml`) exist only in git history — deleted from working tree.
- **Tox** is a dev dependency but no `tox.ini` exists.
- **bump2version** referenced in `Makefile` release targets but not listed in dev dependencies.
- Pre-commit hooks include mypy, flake8, black, isort — `pre-commit run --all-files` checks everything.
