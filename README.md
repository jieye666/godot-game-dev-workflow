# Godot Game Dev Workflow

`godot-game-dev-workflow` 是一个面向 Godot 游戏项目的 Codex skill，用于项目流程管理、玩法开发、AI 可读文档、MCP/editor 协作边界、验证、人工试玩交接和阶段收尾同步。

---

### 适用场景

当 Godot 项目需要以下能力时使用本 skill：

- 基于真实 `project.godot` 定位项目根目录
- 通过 `docs/INDEX.md` 进行低 token 文档路由
- 在改代码前生成 gameplay implementation plan
- 管理 scene、script、signal、resource、InputMap、Autoload 等 Godot 关系
- 审查 Godot 4 GDScript 写法
- 使用 MCP/editor 时区分 tool evidence、file evidence 和 manual acceptance
- 参考外部项目或资料时只吸收可验证的 Godot-specific 规则
- 验证时扫描 Godot 输出中的 `ERROR`、`SCRIPT ERROR`、`push_error`
- 为玩家可见行为提供 manual playtest steps
- 在完成任务后同步 current docs、history、next steps 和 handoff notes

### 安装方式

#### 用户级安装

把本仓库克隆到 Codex skills 目录：

```powershell
git clone https://github.com/jieye666/godot-game-dev-workflow.git "$env:USERPROFILE\.codex\skills\godot-game-dev-workflow"
```

然后开启新的 Codex 会话，使用：

```text
Use $godot-game-dev-workflow to inspect this Godot project and prepare the next task.
```

#### 项目级安装

也可以把整个文件夹直接放进你的项目级 skills 目录。文件夹名应保持为：

```text
godot-game-dev-workflow
```

复制后的目录需要保持 `SKILL.md` 在根目录：

```text
godot-game-dev-workflow/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

### 目录内容

- `SKILL.md`：skill 入口和任务路由规则。
- `agents/openai.yaml`：Codex UI 元数据。
- `references/`：按需加载的流程参考文档。
- `assets/project-doc-templates/`：Godot 项目 AI 协作文档模板。
- `scripts/scan_godot_project.py`：扫描 Godot 项目根和基础信息。
- `scripts/check_scene_references.py`：检查常见 scene/script 引用风险。
- `scripts/init_godot_ai_docs.py`：从模板初始化项目文档。
- `scripts/audit_godot_docs.py`：审计 Godot 项目文档健康度。
- `scripts/audit_doc_language.py`：检查文档语言约定。
- `scripts/skill_self_check.py`：检查本 skill 目录自身是否完整。

### 验证

运行内置自检：

```powershell
python .\scripts\skill_self_check.py .
```

运行脚本单元测试和默认语言审计：

```powershell
$env:PYTHONDONTWRITEBYTECODE = "1"
python -m unittest discover -s .\tests -p "test*.py"
python .\scripts\audit_doc_language.py .
```

运行临时 Godot 项目文档初始化 smoke test：

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

如果本机有 Codex 平台 skill validator，Windows 下建议用 UTF-8 模式运行：

```powershell
$env:PYTHONUTF8 = "1"
python -m pip install PyYAML
python <path-to-skill-creator>\scripts\quick_validate.py .
```

### 参考来源

塑造本 workflow 的外部仓库和本地参考资料记录在 `references/external-repositories.md`。

这些内容只作为来源追踪，不 vendor 到本仓库，保证 skill 体积小、可直接安装。

### 边界

本 skill 用于 Godot 项目流程、玩法实现、文档规范和验证交接。它不是：

- 最终美术、动画、音频或 polish pipeline
- manual playtest 的替代品
- Unity 或通用多引擎 workflow
- 跳过真实 `.tscn`、`.gd` 和项目文档检查的理由

### 维护

发布或修改 skill 前运行：

```powershell
python .\scripts\skill_self_check.py .
```

较大变更还应运行上面的 smoke test、语言审计和平台 validator。优先新增 focused references、scripts 或 templates，不要把 `SKILL.md` 写成长提示词。
