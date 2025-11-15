#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# filesize-cli - Calculate file and directory sizes from the command line
#
# Copyright (C) 2024-2025 Kolja Nolte
# https://www.kolja-nolte.com
#
# Licensed under the MIT License (see the LICENSE file for details).
#
# Author: Kolja Nolte
# E-Mail: kolja.nolte@gmail.com
# Website: https://www.kolja-nolte.com

"""
Command-line interface for calculating file and directory sizes.

This module provides a CLI tool to calculate and display the size of files
and directories with support for multiple units, recursive traversal, and
various output formats.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Union

from . import __version__

# Constants for binary units (base 1024)
KB = 1024
MB = KB**2
GB = KB**3
TB = KB**4

# Mapping of unit abbreviations to (factor, suffix)
UNIT_MAP = {
    "b": (1, "B"),
    "kb": (KB, "KB"),
    "mb": (MB, "MB"),
    "gb": (GB, "GB"),
    "tb": (TB, "TB"),
}


class FilesizeCLI:
    """Command-line interface for file and directory size calculations."""

    def __init__(self, args: Optional[List[str]] = None) -> None:
        """Initialize CLI with command-line arguments."""
        self.args = self._parse_args(args)

    @staticmethod
    def _parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
        """Parse command-line arguments."""
        parser = argparse.ArgumentParser(
            description="Calculate file and directory sizes",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
			Examples:
				filesize file.txt              # Show size with auto unit
				filesize -u mb file.txt        # Force megabytes
				filesize -c file.txt           # Raw bytes only
				filesize -r directory/         # Recursive directory size
				filesize file1.txt file2.txt   # Multiple paths
			""",
        )

        parser.add_argument(
            "paths",
            nargs="+",
            metavar="PATH",
            help="One or more files or directories to analyze",
        )

        parser.add_argument(
            "-c",
            "--clean",
            action="store_true",
            help="Display raw sizes in bytes without formatting",
        )

        parser.add_argument(
            "-r",
            "--recursive",
            action="store_true",
            help="Recurse into subdirectories",
        )

        parser.add_argument(
            "-u",
            "--unit",
            choices=list(UNIT_MAP.keys()),
            help="Force display in specific unit (b, kb, mb, gb, tb)",
        )

        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"%(prog)s {__version__}",
            help="Show version and exit",
        )

        return parser.parse_args(args)

    def get_size(
        self, input_paths: Optional[Union[str, List[str]]] = None
    ) -> Optional[str]:
        """
        Calculate and display sizes for provided paths.

        Args:
                        input_paths: Single path string or list of path strings. If None,
                                                                        uses paths from command-line arguments.

        Returns:
                        Formatted output string if input_paths provided, None otherwise.
        """
        paths = self._normalize_paths(input_paths)
        results = []

        for path_str in paths:
            try:
                result = self._process_path(Path(path_str))
                results.append(result)
            except (FileNotFoundError, PermissionError, OSError) as e:
                results.append(f"{path_str}: Error - {e}")

        output = "\n".join(results)

        if input_paths is not None:
            return output

        print(output)
        return None

    def _normalize_paths(
        self, input_paths: Optional[Union[str, List[str]]]
    ) -> List[str]:
        """Normalize input paths to a list of strings."""
        if input_paths is None:
            return self.args.paths

        if isinstance(input_paths, str):
            return [input_paths]

        if isinstance(input_paths, list):
            return input_paths

        raise TypeError("input_paths must be str or list")

    def _process_path(self, path: Path) -> str:
        """Process a single path and return formatted output."""
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")

        stats = self._compute_size(path)
        formatted_size = self._format_size(stats["size"])

        if self.args.clean:
            return f"{int(stats['size'])}"

        files_label = "file" if stats["files"] == 1 else "files"
        return f"{path}: {formatted_size} ({stats['files']} {files_label})"

    def _compute_size(self, path: Path) -> dict:
        """
        Compute total size and file count for a path.

        Args:
                        path: Path to file or directory

        Returns:
                        Dictionary with 'files', 'size', and 'unit' keys
        """
        if path.is_file():
            try:
                stat = path.stat()
                return {"files": 1, "size": stat.st_size, "unit": "bytes"}
            except OSError as e:
                raise OSError(f"Cannot access file {path}: {e}")

        if path.is_dir():
            total_size = 0
            file_count = 0

            try:
                iterator = path.rglob("*") if self.args.recursive else path.iterdir()

                for item in iterator:
                    if item.is_file():
                        try:
                            total_size += item.stat().st_size
                            file_count += 1
                        except OSError:
                            continue

                return {"files": file_count, "size": total_size, "unit": "bytes"}
            except OSError as e:
                raise OSError(f"Cannot access directory {path}: {e}")

        raise ValueError(f"Path is neither file nor directory: {path}")

    def _format_size(self, size: int) -> str:
        """
        Format size in bytes to human-readable string.

        Args:
                        size: Size in bytes (must be non-negative)

        Returns:
                        Formatted string like "12.34 MB"
        """
        if not isinstance(size, (int, float)) or size < 0:
            raise ValueError("Size must be a non-negative number")

        if self.args.unit:
            factor, suffix = UNIT_MAP[self.args.unit]
            value = size / factor
            return f"{value:.2f} {suffix}" if factor != 1 else f"{int(value)} {suffix}"

        for unit_key in ("tb", "gb", "mb", "kb", "b"):
            factor, suffix = UNIT_MAP[unit_key]
            if size >= factor:
                value = size / factor
                return (
                    f"{value:.2f} {suffix}" if factor != 1 else f"{int(value)} {suffix}"
                )

        return f"{int(size)} B"


def main() -> int:
    """Entry point for the CLI tool."""
    try:
        cli = FilesizeCLI()
        cli.get_size()
        return 0
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
