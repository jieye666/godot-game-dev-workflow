#!/usr/bin/env python3
"""Audit Markdown files for the Chinese-first documentation convention."""

from __future__ import annotations

import argparse
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
CHINESE_RE = re.compile(r"[\u4e00-\u9fff]")


DEFAULT_HEADING_WORD_LIMIT = 5
DEFAULT_SENTENCE_WORD_LIMIT = 14
DEFAULT_STREAK_WORD_LIMIT = 8
STRICT_HEADING_WORD_LIMIT = 3
STRICT_SENTENCE_WORD_LIMIT = 9
STRICT_STREAK_WORD_LIMIT = 6


def strip_technical_text(line: str) -> str:
    line = TECH_RE.sub(" ", line)
    for term in ALLOWED_TERMS:
        line = re.sub(rf"\b{re.escape(term)}\b", " ", line)
    return line


def english_words_after_technical_strip(line: str) -> list[str]:
    return WORD_RE.findall(strip_technical_text(line))


def chinese_char_count(line: str) -> int:
    return len(CHINESE_RE.findall(line))


def audit_file(path: Path, *, strict: bool = False) -> list[str]:
    issues: list[str] = []
    in_code_block = False
    english_streak: list[tuple[int, str]] = []
    heading_limit = STRICT_HEADING_WORD_LIMIT if strict else DEFAULT_HEADING_WORD_LIMIT
    sentence_limit = STRICT_SENTENCE_WORD_LIMIT if strict else DEFAULT_SENTENCE_WORD_LIMIT
    streak_limit = STRICT_STREAK_WORD_LIMIT if strict else DEFAULT_STREAK_WORD_LIMIT

    for lineno, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if line.startswith("```"):
            in_code_block = not in_code_block
            english_streak.clear()
            continue
        if in_code_block or not line:
            english_streak.clear()
            continue

        words = english_words_after_technical_strip(line)
        chinese_chars = chinese_char_count(line)

        if line.startswith("#"):
            english_streak.clear()
            if len(words) >= heading_limit and not chinese_chars:
                issues.append(f"{path}:{lineno}: English-looking heading: {line}")
            continue

        if len(words) >= sentence_limit and chinese_chars < 3:
            issues.append(f"{path}:{lineno}: English-looking sentence: {line[:140]}")
            english_streak.clear()
        elif len(words) >= streak_limit and chinese_chars < 3:
            english_streak.append((lineno, line))
            if len(english_streak) >= 3:
                first_line, first_text = english_streak[0]
                issues.append(
                    f"{path}:{first_line}: English-looking paragraph starts here: {first_text[:140]}"
                )
                english_streak.clear()
        else:
            english_streak.clear()

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


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit Markdown/YAML files for the Chinese-first documentation convention.",
    )
    parser.add_argument("paths", nargs="+", help="Files or folders to audit")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail shorter English-only headings and shorter English-looking sentences.",
    )
    return parser.parse_args(argv)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: audit_doc_language.py [--strict] <path> [<path> ...]")
        return 2

    args = parse_args(sys.argv[1:])
    issues: list[str] = []
    for raw in args.paths:
        root = Path(raw).resolve()
        if not root.exists():
            issues.append(f"{root}: path does not exist")
            continue
        for file_path in markdown_files(root):
            issues.extend(audit_file(file_path, strict=args.strict))

    if issues:
        print("Chinese-first documentation audit failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Chinese-first documentation audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
