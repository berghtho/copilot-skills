"""File utility functions for daily use."""

import json
import os
from pathlib import Path
from typing import Iterator


def ensure_dir(path: str | Path) -> Path:
    """Create *path* (and any missing parents) if it does not exist.

    Returns the resolved :class:`~pathlib.Path` object.

    Example:
        >>> ensure_dir("/tmp/my/new/dir")
        PosixPath('/tmp/my/new/dir')
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def read_json(path: str | Path) -> object:
    """Read and return the parsed JSON contents of *path*.

    Example:
        >>> data = read_json("config.json")
    """
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: str | Path, data: object, indent: int = 2) -> None:
    """Serialise *data* as JSON and write it to *path*.

    The output file is UTF-8 encoded with *indent*-space indentation.

    Example:
        >>> write_json("config.json", {"key": "value"})
    """
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=indent, ensure_ascii=False)
        fh.write("\n")


def find_files(root: str | Path, pattern: str) -> Iterator[Path]:
    """Yield all files under *root* whose name matches the glob *pattern*.

    Example:
        >>> list(find_files(".", "*.py"))
    """
    yield from Path(root).rglob(pattern)
