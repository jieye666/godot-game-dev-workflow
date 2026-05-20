#!/usr/bin/env python3
"""Roughly compare GDScript node references with node names in Godot scenes."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NODE_RE = re.compile(r'^\[node name="([^"]+)"')
DOLLAR_RE = re.compile(r'(?<![\w])\$([A-Za-z0-9_/%.\-]+)')
UNIQUE_RE = re.compile(r'(?<![\w])%([A-Za-z0-9_]+)')
STRING_RE = re.compile(r'("([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\')')
SKIPPED_DIRS = {".git", ".godot", ".tmp", "__pycache__", "reference"}


def strip_string_literals(line: str) -> str:
    return STRING_RE.sub('""', line)


def iter_project_files(root: Path, pattern: str):
    for path in root.rglob(pattern):
        try:
            rel_parts = path.relative_to(root).parts
        except ValueError:
            continue
        if any(part in SKIPPED_DIRS for part in rel_parts):
            continue
        yield path


def collect_scene_nodes(root: Path) -> set[str]:
    names: set[str] = set()
    for scene in iter_project_files(root, "*.tscn"):
        text = scene.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            match = NODE_RE.match(line)
            if match:
                names.add(match.group(1))
    return names


def collect_script_refs(root: Path) -> list[tuple[Path, int, str, str]]:
    refs: list[tuple[Path, int, str, str]] = []
    for script in iter_project_files(root, "*.gd"):
        text = script.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
            code_line = strip_string_literals(line)
            for match in DOLLAR_RE.finditer(code_line):
                path = match.group(1)
                first = path.split("/")[0]
                if first and first not in (".", ".."):
                    refs.append((script, lineno, "$", first))
            for match in UNIQUE_RE.finditer(code_line):
                refs.append((script, lineno, "%", match.group(1)))
    return refs


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    project = root / "project.godot"
    if not project.is_file():
        print(f"Not a Godot project root: {root}")
        return 1

    scene_nodes = collect_scene_nodes(root)
    refs = collect_script_refs(root)
    missing = [(p, line, prefix, name) for p, line, prefix, name in refs if name not in scene_nodes]

    print(f"Scene node names: {len(scene_nodes)}")
    print(f"Script node references: {len(refs)}")
    print(f"Potential unmatched references: {len(missing)}")
    for path, line, prefix, name in missing[:100]:
        rel = path.relative_to(root)
        print(f"{rel}:{line}: {prefix}{name}")

    if len(missing) > 100:
        print(f"... {len(missing) - 100} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
