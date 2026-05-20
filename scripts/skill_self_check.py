#!/usr/bin/env python3
"""Check the Godot game development workflow skill folder."""

from __future__ import annotations

import re
import shutil
import sys
import argparse
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True


EXPECTED_SKILL_NAME = "godot-game-dev-workflow"
REF_RE = re.compile(r"`(references/[^`]+\.md)`")
SCRIPT_RE = re.compile(r"`(scripts/[^`]+\.py)")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
INDEX_REF_RE = re.compile(r"^- `([^`/]+\.md)`[:：]", re.MULTILINE)
REQUIRED_SECTIONS = [
    "## 计划档位",
    "## 自动提交规则",
    "## 不适用 / 边界",
    "## 工作流",
    "## Task Routing",
    "## 强制质量门",
    "## 上下文预算规则",
    "## Two-Stage Records",
    "## Reference Loading",
    "## Examples",
    "## Optional Scripts",
    "## Completion Criteria",
    "## Maintenance",
]
REQUIRED_REFERENCES = [
    "references/index.md",
    "references/skill-quality-gate.md",
    "references/external-repositories.md",
    "references/mcp-and-editor-workflow.md",
]
REQUIRED_REFERENCE_PHRASES = {
    "references/mcp-and-editor-workflow.md": [
        "MCP",
        "editor",
        "tool evidence",
        "file evidence",
        "manual acceptance",
    ],
    "references/game-project-doc-structure.md": [
        "Lite Layout",
        "Full Layout",
        "Hot Context",
        "Docs Owner",
        "2DA-style indexed docs",
        "GDD 存储规则",
    ],
    "references/spec-driven-gameplay-workflow.md": [
        "Requirement",
        "Design",
        "Plan",
        "Task",
        "Implementation Readiness",
    ],
    "references/planning-readiness-and-traceability.md": [
        "pending",
        "ready",
        "escalated",
        "Owned files / prohibited files",
        "manual playtest",
        "Agent selected tier",
        "User confirmation",
        "Tier tradeoff",
        "Reference research gate",
    ],
    "references/gameplay-implementation-plan-template.md": [
        "Reference research",
        "Sources checked",
        "Adopted patterns",
        "Rejected patterns",
        "Local mapping",
        "Open questions",
    ],
    "references/web-gameplay-reference-research.md": [
        "联网",
        "Sources checked",
        "Adopted patterns",
        "Rejected patterns",
        "Local mapping",
        "not needed",
        "manual acceptance",
    ],
    "references/large-project-planning.md": [
        "Task ID",
        "owned files",
        "visible runtime route",
        "Implementation Readiness",
        "Docs sync targets",
    ],
    "references/scene-signal-resource-checklist.md": [
        "played scene",
        "script attachment",
        "InputMap / Autoload",
        "signal connection",
        "resource",
    ],
    "references/godot-4-gdscript-rules.md": [
        "Script Contract",
        "Godot 4 API",
        "Code Quality",
        "生成代码前自检",
        "player-facing path",
    ],
    "references/project-doc-workflow.md": [
        "Source of Truth",
        "docs/INDEX.md",
        "Update current docs",
        "Update history",
        "NEXT-STEPS.md",
        "面向人查看的语言",
    ],
    "references/multi-agent-gameplay-plan.md": [
        "Owned files",
        "Prohibited files",
        "Integration Owner",
        "Stop rule",
        "non-owned file",
    ],
    "references/common-failure-modes.md": [
        "行为没变",
        "Played scene",
        "Attached script",
        "Resource instance",
        "runtime path",
    ],
    "references/validation-and-playtest.md": [
        "验证分层",
        "validate-project.ps1",
        "manual playtest",
        "exact controls",
        "F5",
        "F9",
        "ERROR",
        "push_error",
        "行为没变",
    ],
    "references/session-closeout-sync.md": [
        "Implementation Closeout",
        "Milestone Handoff",
        "Git Commit 描述",
        "不需要人工审查",
        "NEXT-STEPS.md",
        "manual acceptance",
    ],
}
REQUIRED_PHRASES = [
    "Do not infer the engine from parent folder names",
    "Implementation Readiness",
    "manual playtest",
    "current behavior did not change",
    "external reference intake",
    "Godot 项目管理",
    "high-quality gameplay code standards",
    "key project docs and reference files used",
    "中文",
    "commit message",
    "audit_doc_language.py",
    "mcp-and-editor-workflow.md",
    "快速档",
    "标准档",
    "严格档",
    "agent selected tier",
    "Reference research",
    "web-gameplay-reference-research.md",
    "同类成功游戏",
    "无需人工审查",
    "直接 commit",
    "exact controls",
    "保存读取步骤",
    "2DA-style indexed docs",
]
OPENAI_REQUIRED_TERMS = [
    "manage",
    "authoritative docs",
    "low-token",
    "quality",
    "readiness",
    "contract",
    "manual playtest",
    "closeout",
    "verification",
    "chinese",
    "mcp",
    "editor",
]
TEMPLATE_REQUIRED_PHRASES = {
    "assets/project-doc-templates/docs/current/AGENT-QUICK-CONTEXT.md": [
        "Godot version",
        "Main scene",
        "Run command",
        "Validation command",
        "Docs source of truth",
        "docs/current/STATUS.md",
        "Known blockers",
    ],
    "assets/project-doc-templates/docs/current/STATUS.md": [
        "Manual test scene",
        "MCP/editor status",
        "Docs source of truth",
        "AGENT-QUICK-CONTEXT.md",
        "Pending acceptance",
        "Last automated check",
        "Last manual playtest",
    ],
    "assets/project-doc-templates/docs/reference/INDEX.md": [
        "外部参考",
        "blueprint",
        "adopted pattern",
        "local mapping",
    ],
}
INIT_SCRIPT_REQUIRED_PHRASES = ["--dry-run", "--check", "argparse"]
DISALLOWED_DIRS = {"__pycache__"}
DISALLOWED_SUFFIXES = {".pyc", ".pyo"}
FORBIDDEN_TIER_PHRASES = [
    "用户确认 selected tier",
    "用户确认的档位",
    "用户确认后再进入对应 plan depth",
    "推荐快速档并等用户确认",
    "推荐严格档并等用户确认",
]
SLIM_DOC_LIMITS = {
    "docs/INDEX.md": 8,
    "docs/current/AGENT-QUICK-CONTEXT.md": 10,
    "docs/plans/NEXT-STEPS.md": 12,
}
REQUIRED_PROJECT_INDEXES = [
    "docs/current/INDEX.md",
    "docs/plans/INDEX.md",
    "docs/plans/gdd/INDEX.md",
    "docs/history/INDEX.md",
    "docs/history/gdd/INDEX.md",
    "docs/history/commits/INDEX.md",
    "docs/reference/INDEX.md",
]


def frontmatter_fields(text: str) -> tuple[set[str], dict[str, str]]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return set(), {}
    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line or raw_line.startswith((" ", "\t")) or ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return set(fields), fields


def find_generated_artifacts(root: Path) -> list[Path]:
    generated: list[Path] = []
    for path in root.rglob("*"):
        rel_parts = set(path.relative_to(root).parts)
        if DISALLOWED_DIRS & rel_parts:
            generated.append(path.relative_to(root))
        if path.is_file() and path.suffix in DISALLOWED_SUFFIXES:
            generated.append(path.relative_to(root))
    return sorted(set(generated))


def find_slimming_issues(project_root: Path) -> list[str]:
    issues: list[str] = []
    if not project_root.is_dir():
        return issues
    if not (project_root / "project.godot").is_file():
        issues.append(f"{project_root} is not a Godot project root")
        return issues
    for rel in REQUIRED_PROJECT_INDEXES:
        if not (project_root / rel).is_file():
            issues.append(f"missing {rel}")
    archive_gdds = sorted((project_root / "docs" / "plans" / "archive").glob("GDD-*.md"))
    history_gdds = sorted((project_root / "docs" / "history" / "gdd").glob("GDD-*.md"))
    active_gdds = sorted((project_root / "docs" / "plans" / "gdd").glob("GDD-*.md"))
    duplicate_names = sorted({path.name for path in archive_gdds} & {path.name for path in history_gdds})
    if archive_gdds:
        issues.append(f"docs/plans/archive contains {len(archive_gdds)} GDD files; expected 0")
    if duplicate_names:
        issues.append("GDD duplicated in archive and history: " + ", ".join(duplicate_names[:3]))
    if active_gdds and any(path.name in {hist.name for hist in history_gdds} for path in active_gdds):
        issues.append("active GDD also exists in docs/history/gdd")
    for rel, max_completed_gdd_mentions in SLIM_DOC_LIMITS.items():
        path = project_root / rel
        if not path.is_file():
            issues.append(f"missing {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        mentions = len(re.findall(r"GDD-\d{3}", text))
        has_history_index = "docs/history/gdd/INDEX.md" in text
        if mentions > max_completed_gdd_mentions:
            issues.append(f"{rel} has {mentions} GDD mentions; expected <= {max_completed_gdd_mentions}")
        if rel != "docs/current/AGENT-QUICK-CONTEXT.md" and not has_history_index:
            issues.append(f"{rel} does not link docs/history/gdd/INDEX.md")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the Godot game development workflow skill folder.")
    parser.add_argument("root", nargs="?", default=".", help="Skill root directory")
    parser.add_argument("--fix-generated-artifacts", action="store_true", help="Remove __pycache__ and pyc/pyo files before checking")
    parser.add_argument("--project-root", help="Optional Godot project root for docs slimming checks")
    args = parser.parse_args()

    root = Path(args.root)
    root = root.resolve()

    if args.fix_generated_artifacts:
        for rel_dir in ("scripts", "tests"):
            base = (root / rel_dir).resolve()
            try:
                base.relative_to(root)
            except ValueError:
                continue

            pycache = base / "__pycache__"
            if pycache.exists():
                shutil.rmtree(pycache, ignore_errors=True)

            for generated_file in list(base.rglob("*.pyc")) + list(base.rglob("*.pyo")):
                try:
                    generated_file.unlink(missing_ok=True)
                except OSError:
                    pass
    skill = root / "SKILL.md"
    if not skill.is_file():
        print(f"Missing SKILL.md: {root}")
        return 1

    text = skill.read_text(encoding="utf-8", errors="replace")
    fields, field_values = frontmatter_fields(text)
    openai_yaml = root / "agents" / "openai.yaml"
    openai_text = openai_yaml.read_text(encoding="utf-8", errors="replace") if openai_yaml.is_file() else ""
    init_script = root / "scripts" / "init_godot_ai_docs.py"
    init_script_text = init_script.read_text(encoding="utf-8", errors="replace") if init_script.is_file() else ""
    index = root / "references" / "index.md"
    index_text = index.read_text(encoding="utf-8", errors="replace") if index.is_file() else ""
    reference_files = sorted((root / "references").glob("*.md")) if (root / "references").is_dir() else []
    indexed_reference_names = set(INDEX_REF_RE.findall(index_text))
    project_root = Path(args.project_root).resolve() if args.project_root else root.parent / "2da"

    generated_artifacts = find_generated_artifacts(root)
    forbidden_tier_hits = [
        phrase
        for phrase in FORBIDDEN_TIER_PHRASES
        if phrase in text or any(phrase in path.read_text(encoding="utf-8", errors="replace") for path in reference_files)
    ]
    slimming_issues = find_slimming_issues(project_root) if project_root.exists() else []

    checks: list[tuple[str, bool]] = [
        ("frontmatter present", bool(fields)),
        ("frontmatter only name/description", fields == {"name", "description"}),
        ("frontmatter name", field_values.get("name") == EXPECTED_SKILL_NAME),
        ("folder name matches frontmatter", root.name == field_values.get("name")),
        ("frontmatter description starts Use when", field_values.get("description", "").startswith("Use when")),
        ("frontmatter description length <= 900", len(field_values.get("description", "")) <= 900),
        ("SKILL.md line count <= 250", len(text.splitlines()) <= 250),
        ("agents/openai.yaml", openai_yaml.is_file()),
        (
            "agents/openai.yaml core terms"
            if all(term in openai_text.lower() for term in OPENAI_REQUIRED_TERMS)
            else "agents/openai.yaml core terms missing: "
            + ", ".join(term for term in OPENAI_REQUIRED_TERMS if term not in openai_text.lower()),
            all(term in openai_text.lower() for term in OPENAI_REQUIRED_TERMS),
        ),
        (
            "no generated cache files"
            if not generated_artifacts
            else f"no generated cache files ({', '.join(str(path) for path in generated_artifacts[:5])}); run --fix-generated-artifacts to clean",
            not generated_artifacts,
        ),
        (
            "no mandatory user tier confirmation phrasing"
            if not forbidden_tier_hits
            else "mandatory user tier confirmation phrasing: " + ", ".join(forbidden_tier_hits),
            not forbidden_tier_hits,
        ),
        (
            "project docs slimming checks"
            if not slimming_issues
            else "project docs slimming checks: " + "; ".join(slimming_issues[:5]),
            not slimming_issues,
        ),
        ("references dir", (root / "references").is_dir()),
        ("scripts dir", (root / "scripts").is_dir()),
        ("assets templates", (root / "assets" / "project-doc-templates").is_dir()),
        ("agents/openai.yaml skill token", f"${EXPECTED_SKILL_NAME}" in openai_text),
    ]
    checks.extend((f"section {section}", section in text) for section in REQUIRED_SECTIONS)
    checks.extend((f"required phrase {phrase}", phrase in text) for phrase in REQUIRED_PHRASES)
    checks.extend((rel, (root / rel).is_file()) for rel in REQUIRED_REFERENCES)
    checks.append(("examples count", text.count("### ") >= 3))

    for rel, phrases in REQUIRED_REFERENCE_PHRASES.items():
        ref_path = root / rel
        ref_text = ref_path.read_text(encoding="utf-8", errors="replace") if ref_path.is_file() else ""
        for phrase in phrases:
            checks.append((f"{rel} contains {phrase}", phrase in ref_text))

    for rel, phrases in TEMPLATE_REQUIRED_PHRASES.items():
        template_path = root / rel
        template_text = template_path.read_text(encoding="utf-8", errors="replace") if template_path.is_file() else ""
        for phrase in phrases:
            checks.append((f"{rel} contains {phrase}", phrase in template_text))

    for phrase in INIT_SCRIPT_REQUIRED_PHRASES:
        checks.append((f"scripts/init_godot_ai_docs.py contains {phrase}", phrase in init_script_text))

    for rel in sorted(set(REF_RE.findall(text))):
        checks.append((rel, (root / rel).is_file()))
    for rel in sorted(set(SCRIPT_RE.findall(text))):
        checks.append((rel, (root / rel).is_file()))
    for path in reference_files:
        checks.append((f"indexed reference {path.name}", path.name == "index.md" or path.name in indexed_reference_names))
    for name in sorted(indexed_reference_names):
        checks.append((f"index target {name}", (root / "references" / name).is_file()))

    failed = 0
    for name, ok in checks:
        print(f"[{'OK' if ok else 'FAIL'}] {name}")
        if not ok:
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
