# Godot Game Dev Workflow

Codex skill for Godot game project management, gameplay implementation, Chinese-first documentation, AI-readable planning, MCP/editor collaboration boundaries, quality gates, validation, and closeout sync.

## Install

Use this repository folder directly as the skill folder. The folder name must stay:

```text
godot-game-dev-workflow
```

For user-level installation on Windows:

```powershell
git clone https://github.com/jieye666/godot-game-dev-workflow.git "$env:USERPROFILE\.codex\skills\godot-game-dev-workflow"
```

For project-level use, copy this whole folder into the project's skill location used by your Codex setup, keeping `SKILL.md` at the root of the copied folder.

Then start a new Codex session and ask:

```text
Use $godot-game-dev-workflow to inspect this Godot project and prepare the next task.
```

## What It Contains

- `SKILL.md`: skill entrypoint and routing workflow.
- `agents/openai.yaml`: Codex UI metadata.
- `references/`: focused workflow references loaded only when needed.
- `assets/project-doc-templates/`: starter AI collaboration docs for Godot projects.
- `scripts/`: advisory checks for skill health, Godot project intake, doc audit, language audit, scene references, and doc initialization.

## Validate

Run the built-in self-check:

```powershell
python .\scripts\skill_self_check.py .
```

Run a smoke test for project-doc initialization:

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

External repositories and local reference material that shaped the workflow are listed in `references/external-repositories.md`. They are tracked as sources, not vendored into this repository.

## Scope

This skill is for Godot project workflow and gameplay development. It is not a final art-production pipeline, a replacement for manual playtesting, or a generic Unity workflow.
