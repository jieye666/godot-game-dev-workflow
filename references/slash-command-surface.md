# Slash Command Surface

本文件只维护用户可主动调用的 Godot slash wrapper 表面。Canonical 规则仍在 `SKILL.md`、Task Routing 和 focused references。

## User Command Surface

- `/godot-workflow`：总代理入口。仅当用户输入 `/godot-workflow`、明确说启动完整 Godot workflow，或要求自动判断 intake / plan / code / docs / closeout 阶段时使用。
- `/godot-intake`：进入项目，确认真实 `project.godot` root、hot context、docs router、当前状态和下一步。
- `/godot-plan`：制定计划，处理 task shape、agent selected tier、readiness、owned files、验证和人工验收口径。
- `/godot-code`：代码和场景入口。先判断请求是审查、修复还是诊断，再加载 scene/signal、GDScript、common failure 或 implementation contract。
- `/godot-docs`：文档和组织健康入口，处理 source of truth、索引化、文档瘦身、roadmap/current/history 边界和组织效率。
- `/godot-closeout`：验证和收尾入口，处理 Godot output scan、manual playtest handoff、docs/history sync 和 commit policy。

## Internal Routing

- 不再为 `godot-execution`、`godot-reference-research`、`godot-scene-signal`、`godot-gdscript`、`godot-validation`、`godot-failure-debug`、`godot-org-health`、`godot-mcp-editor`、`godot-skill-maintenance` 安装用户可见 wrapper。
- AI 内部仍按 `SKILL.md` 的 Task Routing 读取 focused references；不要把每个 reference 都暴露成 slash 命令。
- 如果用户启动 `/godot-workflow`，先读 canonical `SKILL.md`，再由 Task Routing 选择 focused references，不默认加载完整 `references/`。

## Wrapper Policy

- Wrapper 必须是 thin explicit-invocation wrapper，只负责触发和路由，不复制 canonical 规则。
- 生成的 wrapper 必须包含 `Managed by: godot-game-dev-workflow/scripts/install_slash_skills.py` marker，并指向 canonical `godot-game-dev-workflow`。
- `assets/slash-skill-wrappers/manifest.json` 是用户命令清单的 source of truth；`scripts/install_slash_skills.py --check` 和 `scripts/skill_self_check.py` 必须能发现旧 wrapper 残留、manifest 漂移和生成内容不一致。
