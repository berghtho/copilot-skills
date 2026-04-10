"""Tests for file_utils module."""

from pathlib import Path
from skills.file_utils import ensure_dir, find_files, read_json, write_json


class TestEnsureDir:
    def test_creates_new_directory(self, tmp_path):
        new_dir = tmp_path / "a" / "b" / "c"
        result = ensure_dir(new_dir)
        assert result.is_dir()
        assert result == new_dir

    def test_existing_directory_no_error(self, tmp_path):
        ensure_dir(tmp_path)  # already exists
        assert tmp_path.is_dir()

    def test_returns_path_object(self, tmp_path):
        result = ensure_dir(str(tmp_path / "new"))
        assert isinstance(result, Path)


class TestReadWriteJson:
    def test_round_trip(self, tmp_path):
        data = {"key": "value", "number": 42, "list": [1, 2, 3]}
        path = tmp_path / "test.json"
        write_json(path, data)
        assert read_json(path) == data

    def test_file_has_trailing_newline(self, tmp_path):
        path = tmp_path / "test.json"
        write_json(path, {})
        content = path.read_text(encoding="utf-8")
        assert content.endswith("\n")

    def test_unicode_preserved(self, tmp_path):
        data = {"greeting": "こんにちは"}
        path = tmp_path / "unicode.json"
        write_json(path, data)
        assert read_json(path) == data


class TestFindFiles:
    def test_finds_matching_files(self, tmp_path):
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.txt").write_text("b")
        (tmp_path / "c.py").write_text("c")
        results = list(find_files(tmp_path, "*.txt"))
        assert len(results) == 2

    def test_recursive_search(self, tmp_path):
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "nested.txt").write_text("n")
        (tmp_path / "top.txt").write_text("t")
        results = list(find_files(tmp_path, "*.txt"))
        assert len(results) == 2

    def test_no_matches_returns_empty(self, tmp_path):
        results = list(find_files(tmp_path, "*.xyz"))
        assert results == []
