#!/usr/bin/env python3
"""Install thin slash-callable wrapper skills for the Godot workflow."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LEGACY_WRAPPER_NAMES = [
    "godot-execution",
    "godot-reference-research",
    "godot-scene-signal",
    "godot-gdscript",
    "godot-validation",
    "godot-failure-debug",
    "godot-org-health",
    "godot-mcp-editor",
    "godot-skill-maintenance",
]

WRAPPER_MARKERS = [
    "thin explicit-invocation wrapper",
    "godot-game-dev-workflow",
]


def default_codex_skills_dir() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "skills"
    return Path.home() / ".codex" / "skills"


def skill_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def load_manifest(skill_root: Path) -> list[dict[str, object]]:
    manifest = skill_root / "assets" / "slash-skill-wrappers" / "manifest.json"
    return json.loads(manifest.read_text(encoding="utf-8"))


def render_skill_md(item: dict[str, object], canonical_root: Path) -> str:
    name = str(item["name"])
    description = str(item["description"])
    references = [str(ref) for ref in item["references"]]
    task = str(item["task"])
    reference_lines = "\n".join(f"- `{canonical_root / 'references' / ref}`" for ref in references)
    return f"""---
name: {name}
description: {description} This is a thin explicit-invocation wrapper for the canonical godot-game-dev-workflow skill.
---

# {name}

这是 `godot-game-dev-workflow` 的主动调用 wrapper。它只负责让用户可以通过 slash / skill picker 点名调用；规则真相仍在 canonical skill。

## Canonical Source

- Main skill: `{canonical_root / 'SKILL.md'}`
- Reference files:
{reference_lines}

## Workflow

1. 先读取 canonical `SKILL.md`，遵守其档位、验证、文档、manual acceptance 和 commit 规则。
2. 再按本 wrapper listed references 加载 focused reference，不默认读取完整 `references/`。
3. 当前任务目标：{task}
4. 如果 canonical path 不存在，报告缺失路径，并在当前 workspace 中查找 `godot-game-dev-workflow/SKILL.md` 后继续。

## Boundary

- 不把本 wrapper 当作独立规则 owner。
- 不复制或覆盖 canonical reference 中的细节。
- 新规则应先写回 canonical skill，再重新安装 wrappers。
"""


def render_openai_yaml(item: dict[str, object]) -> str:
    name = str(item["name"])
    display_name = str(item["display_name"])
    short_description = str(item["short_description"])
    task = str(item["task"])
    return f"""interface:
  display_name: "{display_name}"
  short_description: "{short_description}"
  default_prompt: "Use ${name} for this Godot workflow subtask. {task}"
"""


def install_one(item: dict[str, object], target_root: Path, canonical_root: Path, dry_run: bool) -> Path:
    name = str(item["name"])
    target = target_root / name
    skill_md = render_skill_md(item, canonical_root)
    openai_yaml = render_openai_yaml(item)
    if dry_run:
        return target
    (target / "agents").mkdir(parents=True, exist_ok=True)
    (target / "SKILL.md").write_text(skill_md, encoding="utf-8", newline="\n")
    (target / "agents" / "openai.yaml").write_text(openai_yaml, encoding="utf-8", newline="\n")
    return target


def is_managed_wrapper(target: Path) -> bool:
    skill_path = target / "SKILL.md"
    if not skill_path.is_file():
        return False
    text = skill_path.read_text(encoding="utf-8", errors="replace")
    return all(marker in text for marker in WRAPPER_MARKERS)


def remove_wrapper_dir(target: Path, issues: list[str]) -> bool:
    if not target.exists():
        return False
    if not is_managed_wrapper(target):
        issues.append(f"refusing to remove unmanaged wrapper directory {target}")
        return False
    shutil.rmtree(target)
    return True


def check_installed(manifest: list[dict[str, object]], target_root: Path, canonical_root: Path) -> list[str]:
    issues: list[str] = []
    for name in LEGACY_WRAPPER_NAMES:
        target = target_root / name
        if target.exists():
            issues.append(f"legacy wrapper still installed {target}")
    for item in manifest:
        name = str(item["name"])
        target = target_root / name
        expected_skill = render_skill_md(item, canonical_root)
        expected_yaml = render_openai_yaml(item)
        skill_path = target / "SKILL.md"
        yaml_path = target / "agents" / "openai.yaml"
        if not skill_path.is_file():
            issues.append(f"missing {skill_path}")
            continue
        if not yaml_path.is_file():
            issues.append(f"missing {yaml_path}")
            continue
        if skill_path.read_text(encoding="utf-8", errors="replace") != expected_skill:
            issues.append(f"stale {skill_path}")
        if yaml_path.read_text(encoding="utf-8", errors="replace") != expected_yaml:
            issues.append(f"stale {yaml_path}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Install slash-callable Godot workflow wrapper skills.")
    parser.add_argument("--target", default=str(default_codex_skills_dir()), help="Target Codex skills directory")
    parser.add_argument("--canonical-root", default=str(skill_root_from_script()), help="Canonical godot-game-dev-workflow root")
    parser.add_argument("--dry-run", action="store_true", help="Print target paths without writing")
    parser.add_argument("--check", action="store_true", help="Check installed wrappers without writing")
    parser.add_argument("--clean", action="store_true", help="Remove previously installed wrapper directories before reinstalling")
    args = parser.parse_args()

    canonical_root = Path(args.canonical_root).resolve()
    target_root = Path(args.target).resolve()
    manifest = load_manifest(canonical_root)

    if args.check:
        issues = check_installed(manifest, target_root, canonical_root)
        if issues:
            for issue in issues:
                print(f"[FAIL] {issue}")
            return 1
        print(f"[OK] {len(manifest)} slash skill wrappers installed in {target_root}")
        return 0

    if args.dry_run:
        print(f"Target: {target_root}")
        for item in manifest:
            print(target_root / str(item["name"]))
        return 0

    target_root.mkdir(parents=True, exist_ok=True)
    clean_issues: list[str] = []
    if args.clean:
        names_to_remove = sorted({str(item["name"]) for item in manifest} | set(LEGACY_WRAPPER_NAMES))
        removed = 0
        for name in names_to_remove:
            if remove_wrapper_dir(target_root / name, clean_issues):
                removed += 1
        if clean_issues:
            for issue in clean_issues:
                print(f"[FAIL] {issue}")
            return 1
        if removed:
            print(f"Removed {removed} managed slash skill wrapper directories")

    installed: list[Path] = []
    for item in manifest:
        installed.append(install_one(item, target_root, canonical_root, dry_run=False))

    print(f"Installed {len(installed)} slash skill wrappers:")
    for path in installed:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
