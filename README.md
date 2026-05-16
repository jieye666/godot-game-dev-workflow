# Godot Game Dev Workflow

`godot-game-dev-workflow` is a Codex skill for managing Godot game projects with AI-readable documentation, gameplay implementation plans, readiness gates, MCP/editor collaboration boundaries, validation checks, manual playtest handoffs, and closeout synchronization.

The skill is designed to be copied or cloned as a complete folder and used directly by Codex. Keep the folder name as `godot-game-dev-workflow` so it matches the skill name in `SKILL.md`.

## What This Skill Is For

Use this skill when working on Godot projects that need:

- project intake based on the real `project.godot` root
- low-token documentation routing through `docs/INDEX.md`
- gameplay implementation plans before code changes
- scene, script, signal, resource, InputMap, and Autoload discipline
- Godot 4 GDScript review rules
- MCP/editor collaboration with clear evidence boundaries
- external reference intake without blindly copying full repositories
- validation output scanning beyond process exit codes
- manual playtest steps for player-facing behavior
- closeout sync for current docs, history, next steps, and handoff notes

## Install

### User-Level Installation

Clone this repository into your Codex skills directory:

```powershell
git clone https://github.com/jieye666/godot-game-dev-workflow.git "$env:USERPROFILE\.codex\skills\godot-game-dev-workflow"
```

Start a new Codex session and ask:

```text
Use $godot-game-dev-workflow to inspect this Godot project and prepare the next task.
```

### Project-Level Installation

You can also place this whole folder inside a project-specific skills directory used by your Codex setup.

The copied folder must contain `SKILL.md` at its root:

```text
godot-game-dev-workflow/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

## Repository Contents

- `SKILL.md`: the skill entrypoint and workflow router.
- `agents/openai.yaml`: Codex UI metadata for skill discovery.
- `references/`: focused reference files loaded only when needed.
- `assets/project-doc-templates/`: starter AI collaboration docs for Godot projects.
- `scripts/scan_godot_project.py`: finds Godot project roots and basic project metadata.
- `scripts/check_scene_references.py`: scans common scene/script reference risks.
- `scripts/init_godot_ai_docs.py`: initializes recommended project documentation from templates.
- `scripts/audit_godot_docs.py`: checks Godot project documentation health.
- `scripts/audit_doc_language.py`: checks documentation language expectations.
- `scripts/skill_self_check.py`: validates this skill folder.

## Validate the Skill

Run the built-in self-check:

```powershell
python .\scripts\skill_self_check.py .
```

Run a smoke test for project documentation initialization:

```powershell
$tmp = Join-Path $env:TEMP "godot-game-dev-workflow-smoke"
Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $tmp | Out-Null
Set-Content -Path (Join-Path $tmp "project.godot") -Value "; Engine configuration file`nconfig_version=5`n" -Encoding UTF8
python .\scripts\init_godot_ai_docs.py $tmp
python .\scripts\init_godot_ai_docs.py $tmp --check
python .\scripts\audit_godot_docs.py $tmp
Remove-Item -LiteralPath $tmp -Recurse -Force
```

If you have Codex's platform skill validator available on Windows, run it with UTF-8 mode:

```powershell
$env:PYTHONUTF8 = "1"
python <path-to-skill-creator>\scripts\quick_validate.py .
```

## Reference Sources

External repositories and local reference material that shaped this workflow are listed in `references/external-repositories.md`.

Those sources are tracked as references only. They are not vendored into this repository, keeping the skill small and directly installable.

## Scope and Limits

This skill is for Godot project workflow, gameplay implementation, documentation discipline, and validation handoff.

It is not:

- a final art, animation, audio, or polish pipeline
- a replacement for manual playtesting
- a generic Unity or multi-engine workflow
- a reason to skip reading the actual `.tscn`, `.gd`, and project documentation files

## Maintenance

Before shipping skill changes, run:

```powershell
python .\scripts\skill_self_check.py .
```

For substantial changes, also run the smoke test above and the platform skill validator when available.

Prefer adding focused references, scripts, or templates over expanding `SKILL.md`. The main skill file should stay a router; detailed behavior belongs in `references/`.
