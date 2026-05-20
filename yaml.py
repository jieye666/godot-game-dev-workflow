"""
Minimal YAML shim for Codex skill validation on machines without PyYAML.

This module intentionally supports only the tiny YAML subset used by SKILL.md
frontmatter in this repository: a top-level mapping of scalar string values.

It exists so the platform `quick_validate.py` script (which does `import yaml`)
can run without requiring an external dependency.
"""

from __future__ import annotations

import re
from typing import Dict


class YAMLError(Exception):
    pass


_KEY_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def safe_load(text: str) -> Dict[str, str]:
    if not isinstance(text, str):
        raise YAMLError("Input must be a string")

    result: Dict[str, str] = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        i += 1

        if not line or line.startswith("#"):
            continue

        if ":" not in raw:
            raise YAMLError(f"Unsupported YAML line: {raw!r}")

        key, rest = raw.split(":", 1)
        key = key.strip()
        if not _KEY_RE.match(key):
            raise YAMLError(f"Invalid key: {key!r}")

        value = rest.lstrip()
        if value in ("|", ">"):
            block_lines = []
            while i < len(lines):
                nxt = lines[i]
                if nxt.startswith("  ") or nxt.startswith("\t"):
                    block_lines.append(nxt.lstrip(" \t"))
                    i += 1
                    continue
                break
            value = "\n".join(block_lines).rstrip("\n")
        else:
            value = value.strip()
            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                value = value[1:-1]

        result[key] = value

    return result

