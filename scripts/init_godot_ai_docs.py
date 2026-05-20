#!/usr/bin/env python3
"""Create missing Godot AI collaboration docs from bundled templates."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


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


def copy_template(src: Path, dest: Path, root: Path) -> None:
    if src.suffix.lower() in {".md", ".txt", ".yaml", ".yml"}:
        text = src.read_text(encoding="utf-8", errors="replace")
        text = text.replace("{{GODOT_PROJECT_ROOT}}", str(root))
        dest.write_text(text, encoding="utf-8", newline="\n")
        return
    shutil.copyfile(src, dest)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or inspect missing Godot AI collaboration docs from bundled templates.",
    )
    parser.add_argument("path", nargs="?", default=".", help="Godot project root or parent directory")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="List files that would be created without writing")
    mode.add_argument("--check", action="store_true", help="Report missing template files without writing")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])
    start = Path(args.path)
    root = find_project_root(start)
    if root is None:
        print(f"No project.godot found from: {start}")
        return 1

    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "assets" / "project-doc-templates"
    if not template_root.is_dir():
        print(f"Template folder missing: {template_root}")
        return 1

    created: list[Path] = []
    skipped: list[Path] = []
    missing: list[Path] = []
    for src in template_root.rglob("*"):
        if src.is_dir():
            continue
        rel = src.relative_to(template_root)
        dest = root / rel
        if dest.exists():
            skipped.append(rel)
            continue
        missing.append(rel)
        if args.dry_run or args.check:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        copy_template(src, dest, root)
        created.append(rel)

    print(f"Godot root: {root}")
    if args.check:
        print(f"Missing: {len(missing)}")
        for path in missing:
            print(f"  ! {path}")
    elif args.dry_run:
        print(f"Would create: {len(missing)}")
        for path in missing:
            print(f"  + {path}")
    else:
        print(f"Created: {len(created)}")
        for path in created:
            print(f"  + {path}")
    print(f"Skipped existing: {len(skipped)}")
    for path in skipped:
        print(f"  = {path}")
    print("Complete these fields after initialization:")
    print("  - docs/current/AGENT-QUICK-CONTEXT.md: Godot version, main scene, run command, blockers")
    print("  - docs/current/STATUS.md: manual test scene, implemented systems, pending acceptance, verification records")
    print("  - docs/plans/NEXT-STEPS.md: active task queue and readiness")
    print("  - docs/reference/INDEX.md: external/reference project routing when needed")
    return 2 if args.check and missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
