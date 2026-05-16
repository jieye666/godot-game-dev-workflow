#!/usr/bin/env python3
"""Audit Markdown files for the Chinese-first documentation convention."""

from __future__ import annotations

import re
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


TECH_RE = re.compile(
    r"(`[^`]+`|https?://\S+|res://\S+|user://\S+|[A-Za-z]:\\\S+|"
    r"[\w./\\-]+\.(?:md|gd|tscn|tres|res|ps1|py|yaml|yml|svg|txt)|"
    r"GDD-\d+|[A-Z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)?|[a-z]+_[a-z0-9_]+)"
)
ALLOWED_TERMS = {
    "Godot",
    "InputMap",
    "Autoload",
    "GDD",
    "HUD",
    "Boss",
    "Smoke",
    "Test",
    "Runtime",
    "Reference",
    "README",
    "AGENTS",
    "SKILL",
    "Markdown",
    "PowerShell",
    "Python",
    "Git",
    "MCP",
    "AI",
    "API",
    "UI",
}
WORD_RE = re.compile(r"[A-Za-z]{3,}")


def strip_technical_text(line: str) -> str:
    line = TECH_RE.sub(" ", line)
    for term in ALLOWED_TERMS:
        line = re.sub(rf"\b{re.escape(term)}\b", " ", line)
    return line


def audit_file(path: Path) -> list[str]:
    issues: list[str] = []
    in_code_block = False
    for lineno, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not line:
            continue

        stripped = strip_technical_text(line)
        words = WORD_RE.findall(stripped)
        chinese_chars = re.findall(r"[\u4e00-\u9fff]", line)

        if line.startswith("#") and len(words) >= 3 and not chinese_chars:
            issues.append(f"{path}:{lineno}: English-looking heading: {line}")
        elif len(words) >= 9 and len(chinese_chars) < 3:
            issues.append(f"{path}:{lineno}: English-looking sentence: {line[:140]}")
    return issues


def markdown_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix.lower() in {".md", ".yaml", ".yml"} else []
    skipped = {".git", ".godot", ".tmp", "__pycache__", "reference"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in skipped for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml"}:
            files.append(path)
    return sorted(files)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: audit_doc_language.py <path> [<path> ...]")
        return 2

    issues: list[str] = []
    for raw in sys.argv[1:]:
        root = Path(raw).resolve()
        if not root.exists():
            issues.append(f"{root}: path does not exist")
            continue
        for file_path in markdown_files(root):
            issues.extend(audit_file(file_path))

    if issues:
        print("Chinese-first documentation audit failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Chinese-first documentation audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
