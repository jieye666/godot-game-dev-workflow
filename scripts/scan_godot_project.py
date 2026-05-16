#!/usr/bin/env python3
"""Summarize a Godot project root and common docs/folders."""

from __future__ import annotations

import sys
from pathlib import Path


def find_project_root(start: Path) -> Path | None:
    start = start.resolve()
    candidates = [start] if start.is_dir() else [start.parent]
    candidates.extend(candidates[0].parents)
    for path in candidates:
        if (path / "project.godot").is_file():
            return path
    for path in start.rglob("project.godot") if start.is_dir() else []:
        return path.parent
    return None


def read_project_settings(project_file: Path) -> dict[str, str]:
    text = project_file.read_text(encoding="utf-8", errors="replace")
    section = ""
    values: dict[str, str] = {}
    wanted = {
        "application": {"config/name", "run/main_scene"},
        "display": {
            "window/size/viewport_width",
            "window/size/viewport_height",
            "window/stretch/mode",
            "window/stretch/aspect",
        },
    }
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(";"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1]
            continue
        if "=" not in line or section not in wanted:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key in wanted[section]:
            values[key] = value.strip().strip('"')
    return values


def main() -> int:
    start = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = find_project_root(start)
    if root is None:
        print(f"No project.godot found from: {start}")
        return 1

    print(f"Godot root: {root}")
    settings = read_project_settings(root / "project.godot")
    for key, value in settings.items():
        print(f"{key}: {value}")

    for name in ("scenes", "scripts", "assets", "docs", "addons"):
        path = root / name
        print(f"{name}/: {'yes' if path.exists() else 'no'}")

    docs_index = root / "docs" / "INDEX.md"
    print(f"docs/INDEX.md: {'yes' if docs_index.exists() else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
