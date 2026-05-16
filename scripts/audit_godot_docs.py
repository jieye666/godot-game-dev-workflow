#!/usr/bin/env python3
"""Audit Godot AI collaboration docs for context health."""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RELATIVE_TIME_RE = re.compile(r"今天|昨天|刚刚|最近|上周|today|yesterday|recently", re.IGNORECASE)


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


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8", errors="replace").splitlines())


def contains(path: Path, pattern: str) -> bool:
    return pattern in path.read_text(encoding="utf-8", errors="replace")


def is_cold_doc(root: Path, path: Path) -> bool:
    rel = path.relative_to(root).as_posix().lower()
    return rel.startswith("docs/history/") or rel.startswith("docs/plans/archive/") or "/archive/" in rel


def first_relative_time_hit(root: Path, path: Path) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    for idx, line in enumerate(text.splitlines(), start=1):
        if RELATIVE_TIME_RE.search(line):
            return f"{path.relative_to(root)}:{idx}"
    return None


def main() -> int:
    start = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = find_project_root(start)
    if root is None:
        print(f"No project.godot found from: {start}")
        return 1

    checks: list[tuple[str, bool, str]] = []
    infos: list[tuple[str, str]] = []
    docs = root / "docs"
    required = [
        "docs/INDEX.md",
        "docs/current/AGENT-QUICK-CONTEXT.md",
        "docs/current/STATUS.md",
        "docs/plans/NEXT-STEPS.md",
    ]
    for rel in required:
        path = root / rel
        checks.append((rel, path.is_file(), "required doc exists"))

    history_candidates = [
        "docs/history/development-log.md",
        "docs/history/CHANGELOG.md",
    ]
    history_existing = [rel for rel in history_candidates if (root / rel).is_file()]
    checks.append((
        "docs/history log",
        bool(history_existing),
        "one of " + ", ".join(history_candidates) + (" exists: " + ", ".join(history_existing) if history_existing else ""),
    ))

    for rel, limit in [("AGENTS.md", 300), ("docs/current/AGENT-QUICK-CONTEXT.md", 120)]:
        path = root / rel
        if path.is_file():
            checks.append((rel, line_count(path) <= limit, f"line count <= {limit}"))

    md_files: list[Path] = []
    if docs.is_dir():
        md_files.extend(docs.rglob("*.md"))
    if (root / "AGENTS.md").is_file():
        md_files.append(root / "AGENTS.md")

    active_md_files = [path for path in md_files if not is_cold_doc(root, path)]
    cold_md_files = [path for path in md_files if is_cold_doc(root, path)]

    active_relative_hits = []
    cold_relative_hits = []
    for path in active_md_files:
        hit = first_relative_time_hit(root, path)
        if hit:
            active_relative_hits.append(hit)
    for path in cold_md_files:
        hit = first_relative_time_hit(root, path)
        if hit:
            cold_relative_hits.append(hit)
    checks.append(("active relative-time wording", not active_relative_hits, ", ".join(active_relative_hits[:20])))
    if cold_relative_hits:
        infos.append(("cold relative-time wording", ", ".join(cold_relative_hits[:20])))

    active_identity_files = []
    cold_identity_files = []
    for path in md_files:
        if contains(path, "Godot version") or contains(path, "Main scene") or contains(path, "Godot project root"):
            if is_cold_doc(root, path):
                cold_identity_files.append(str(path.relative_to(root)))
            else:
                active_identity_files.append(str(path.relative_to(root)))
    checks.append(("active identity fact locations", len(active_identity_files) <= 3, ", ".join(active_identity_files[:20])))
    if cold_identity_files:
        infos.append(("cold identity fact locations", ", ".join(cold_identity_files[:20])))

    print(f"Godot root: {root}")
    failed = 0
    for name, ok, detail in checks:
        status = "OK" if ok else "WARN"
        if not ok:
            failed += 1
        print(f"[{status}] {name} - {detail}")
    for name, detail in infos:
        print(f"[INFO] {name} - {detail}")
    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
