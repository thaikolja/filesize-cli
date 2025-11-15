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

"""Tests for filesize-cli."""

import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from filesize_cli.cli import FilesizeCLI, main


@pytest.fixture
def temp_file():
	"""Create a temporary file with known content."""
	with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
		f.write("Hello, World!")
		temp_path = f.name

	yield Path(temp_path)

	# Cleanup
	if os.path.exists(temp_path):
		os.unlink(temp_path)


@pytest.fixture
def temp_dir():
	"""Create a temporary directory with test files."""
	temp_path = Path(tempfile.mkdtemp())

	# Create test files
	(temp_path / "file1.txt").write_text("a" * 100)
	(temp_path / "file2.txt").write_text("b" * 200)

	# Create subdirectory
	subdir = temp_path / "subdir"
	subdir.mkdir()
	(subdir / "file3.txt").write_text("c" * 300)

	yield temp_path

	# Cleanup
	import shutil
	shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def cli():
	"""Create CLI instance with default args."""
	return FilesizeCLI([])


class TestFilesizeCLI:
	"""Test FilesizeCLI class."""

	def test_version(self):
		"""Test version flag."""
		with patch('sys.argv', ['filesize', '--version']):
			with pytest.raises(SystemExit) as exc:
				FilesizeCLI()
			assert exc.value.code == 0

	def test_parse_args_no_paths(self):
		"""Test that parser requires paths."""
		with pytest.raises(SystemExit):
			FilesizeCLI([])

	def test_parse_args_with_paths(self):
		"""Test parsing with paths."""
		cli = FilesizeCLI(['test.txt'])
		assert cli.args.paths == ['test.txt']

	def test_parse_args_multiple_paths(self):
		"""Test parsing with multiple paths."""
		cli = FilesizeCLI(['file1.txt', 'file2.txt'])
		assert cli.args.paths == ['file1.txt', 'file2.txt']

	def test_parse_args_clean(self):
		"""Test clean flag."""
		cli = FilesizeCLI(['-c', 'test.txt'])
		assert cli.args.clean is True

	def test_parse_args_recursive(self):
		"""Test recursive flag."""
		cli = FilesizeCLI(['-r', 'test.txt'])
		assert cli.args.recursive is True

	def test_parse_args_unit(self):
		"""Test unit flag."""
		cli = FilesizeCLI(['-u', 'mb', 'test.txt'])
		assert cli.args.unit == 'mb'

	def test_normalize_paths_none(self, cli):
		"""Test path normalization with None."""
		cli.args.paths = ['test.txt']
		assert cli._normalize_paths(None) == ['test.txt']

	def test_normalize_paths_string(self, cli):
		"""Test path normalization with string."""
		assert cli._normalize_paths('test.txt') == ['test.txt']

	def test_normalize_paths_list(self, cli):
		"""Test path normalization with list."""
		paths = ['file1.txt', 'file2.txt']
		assert cli._normalize_paths(paths) == paths

	def test_normalize_paths_invalid(self, cli):
		"""Test path normalization with invalid type."""
		with pytest.raises(TypeError):
			cli._normalize_paths(123)

	def test_compute_size_file(self, cli, temp_file):
		"""Test computing size for a file."""
		stats = cli._compute_size(temp_file)
		assert stats['files'] == 1
		assert stats['size'] == 13  # "Hello, World!" is 13 bytes
		assert stats['unit'] == 'bytes'

	def test_compute_size_directory(self, cli, temp_dir):
		"""Test computing size for a directory."""
		stats = cli._compute_size(temp_dir)
		assert stats['files'] == 2  # Only top-level files
		assert stats['size'] == 300  # 100 + 200 bytes

	def test_compute_size_directory_recursive(self, cli, temp_dir):
		"""Test computing size for a directory recursively."""
		cli.args.recursive = True
		stats = cli._compute_size(temp_dir)
		assert stats['files'] == 3  # All files including subdirectory
		assert stats['size'] == 600  # 100 + 200 + 300 bytes

	def test_compute_size_nonexistent(self, cli):
		"""Test computing size for non-existent path."""
		with pytest.raises(FileNotFoundError):
			cli._compute_size(Path('/nonexistent/path'))

	def test_compute_size_not_file_or_dir(self, cli, temp_dir):
		"""Test computing size for non-file, non-directory path."""
		# Create a symlink (if supported)
		try:
			link = temp_dir / "link"
			link.symlink_to("/nonexistent")
			with pytest.raises(ValueError):
				cli._compute_size(link)
		except (OSError, NotImplementedError):
			pytest.skip("Symlinks not supported on this platform")

	def test_format_size_bytes(self, cli):
		"""Test formatting size in bytes."""
		assert cli._format_size(0) == "0 B"
		assert cli._format_size(512) == "512 B"

	def test_format_size_kilobytes(self, cli):
		"""Test formatting size in kilobytes."""
		assert cli._format_size(1024) == "1.00 KB"
		assert cli._format_size(1536) == "1.50 KB"

	def test_format_size_megabytes(self, cli):
		"""Test formatting size in megabytes."""
		assert cli._format_size(1024 ** 2) == "1.00 MB"
		assert cli._format_size(1536 * 1024) == "1.50 MB"

	def test_format_size_gigabytes(self, cli):
		"""Test formatting size in gigabytes."""
		assert cli._format_size(1024 ** 3) == "1.00 GB"

	def test_format_size_terabytes(self, cli):
		"""Test formatting size in terabytes."""
		assert cli._format_size(1024 ** 4) == "1.00 TB"

	def test_format_size_forced_unit(self, cli):
		"""Test formatting with forced unit."""
		cli.args.unit = 'mb'
		assert cli._format_size(1024 ** 2) == "1.00 MB"
		assert cli._format_size(100) == "0.00 MB"

	def test_format_size_invalid(self, cli):
		"""Test formatting invalid size."""
		with pytest.raises(ValueError):
			cli._format_size(-1)
		with pytest.raises(ValueError):
			cli._format_size("invalid")

	def test_process_path_file(self, cli, temp_file):
		"""Test processing a file path."""
		result = cli._process_path(temp_file)
		assert str(temp_file) in result
		assert "13 B" in result
		assert "(1 file)" in result

	def test_process_path_directory(self, cli, temp_dir):
		"""Test processing a directory path."""
		result = cli._process_path(temp_dir)
		assert str(temp_dir) in result
		assert "300 B" in result
		assert "(2 files)" in result

	def test_process_path_clean(self, cli, temp_file):
		"""Test processing with clean output."""
		cli.args.clean = True
		result = cli._process_path(temp_file)
		assert result == "13"

	def test_process_path_nonexistent(self, cli):
		"""Test processing non-existent path."""
		with pytest.raises(FileNotFoundError):
			cli._process_path(Path('/nonexistent'))

	def test_get_size_returns_string(self, cli, temp_file):
		"""Test get_size returns string when paths provided."""
		result = cli.get_size(str(temp_file))
		assert isinstance(result, str)
		assert str(temp_file) in result

	def test_get_size_prints(self, cli, temp_file):
		"""Test get_size prints when no paths provided."""
		cli.args.paths = [str(temp_file)]
		with patch('builtins.print') as mock_print:
			cli.get_size()
			mock_print.assert_called_once()

	def test_get_size_multiple_paths(self, cli, temp_file, temp_dir):
		"""Test get_size with multiple paths."""
		paths = [str(temp_file), str(temp_dir)]
		result = cli.get_size(paths)
		lines = result.split('\n')
		assert len(lines) == 2
		assert str(temp_file) in lines[0]
		assert str(temp_dir) in lines[1]

	def test_get_size_error_handling(self, cli):
		"""Test get_size error handling."""
		result = cli.get_size('/nonexistent/path')
		assert "Error" in result
		assert "/nonexistent/path" in result


class TestMainFunction:
	"""Test main function."""

	def test_main_success(self):
		"""Test main function success."""
		with patch('sys.argv', ['filesize', __file__]):
			with patch('builtins.print'):
				result = main()
				assert result == 0

	def test_main_keyboard_interrupt(self):
		"""Test main function with keyboard interrupt."""
		with patch('sys.argv', ['filesize', __file__]):
			with patch.object(FilesizeCLI, 'get_size', side_effect=KeyboardInterrupt()):
				result = main()
				assert result == 130

	def test_main_unexpected_error(self):
		"""Test main function with unexpected error."""
		with patch('sys.argv', ['filesize', __file__]):
			with patch.object(FilesizeCLI, 'get_size', side_effect=Exception("Test error")):
				result = main()
				assert result == 1


class TestIntegration:
	"""Integration tests."""

	def test_full_cli_workflow(self, temp_dir):
		"""Test complete CLI workflow."""
		cli = FilesizeCLI([str(temp_dir), '-r'])
		result = cli.get_size()
		assert result is None  # Should print, not return

	def test_unit_conversion_accuracy(self):
		"""Test unit conversion accuracy."""
		cli = FilesizeCLI(['-u', 'mb', __file__])

		# Test exact conversions
		assert cli._format_size(1024 ** 2) == "1.00 MB"
		assert cli._format_size(2 * 1024 ** 2) == "2.00 MB"

		# Test rounding
		assert cli._format_size(1024 ** 2 + 512 * 1024) == "1.50 MB"

	def test_file_count_accuracy(self, temp_dir):
		"""Test file counting accuracy."""
		cli = FilesizeCLI([str(temp_dir), '-r'])
		stats = cli._compute_size(temp_dir)
		assert stats['files'] == 3
		assert stats['size'] == 600
