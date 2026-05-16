# Godot Game Dev Workflow Reference Index

维护 skill 或判断加载哪份 reference 时读本文件。普通任务优先使用 `SKILL.md` 的 Task Routing；不要默认加载完整 `references/`。

## 进入项目和文档

- `project-doc-workflow.md`：进入 documented project、判断 Source of Truth、同步 current/status/history。已读它时不要再读完整 history。
- `game-project-doc-structure.md`：初始化或审计 docs layout、hot context 字段、docs owner。只在新项目或文档结构混乱时加载。
- `context-memory-strategy.md`：需要降低 token、整理 hot/warm/cold context、处理 reference project intake 时加载。
- `session-closeout-sync.md`：完成 implementation、用户验收、milestone handoff 时加载；不要在刚进入项目时加载。

## 计划和执行

- `spec-driven-gameplay-workflow.md`：需求模糊、跨系统、需要先拆 Requirement / Design / Plan / Task 时加载。
- `large-project-planning.md`：大功能、原型、里程碑、多会话任务拆分时加载；不要用于 one-file patch。
- `planning-readiness-and-traceability.md`：从现有 plan 准备实现、判断 `pending` / `ready` / `escalated`、检查 coverage gaps 时加载。
- `gameplay-implementation-plan-template.md`：需要写 Task Plan 或 Compact Patch Plan 时加载。
- `implementation-contracts.md`：Task Plan 涉及 scene/script/signal/resource/InputMap/Autoload/ownership 时加载。
- `multi-agent-gameplay-plan.md`：只有并行能减少冲突且 owned-file boundaries 清楚时加载。

## Godot 实现检查

- `mcp-and-editor-workflow.md`：需要使用 MCP/editor、报告 tool evidence、区分自动验证和人工验收时加载。
- `scene-signal-resource-checklist.md`：改 `.tscn`、node path、signal connection、resource instance、InputMap/Autoload 时加载。
- `godot-4-gdscript-rules.md`：写或审查 GDScript、计划会影响代码形态时加载。
- `extensible-gameplay-architecture.md`：可复用系统、大功能、第二变体风险、coupling risk 时加载。
- `validation-and-playtest.md`：完成前验证、Godot output scan、manual playtest handoff 时加载。
- `common-failure-modes.md`：验证失败或用户说行为没变时加载；优先检查 played scene、attached script、main route。

## Skill 维护

- `skill-quality-gate.md`：维护本 skill、新增 reference/script/template、吸收外部 workflow idea 时加载。
- `external-repositories.md`：刷新外部来源、记录 local snapshot、追踪来源不确定性时加载。

## 路由原则

- 优先加载一个能回答当前问题的 focused reference，再按缺口补第二个。
- 如果一个 reference 已覆盖当前步骤，不为了“完整”再加载相邻 reference。
- 新增 reference 必须能减少重复加载、承载独立检查，或让 `SKILL.md` 更短。
- references 保持单层目录；深层目录只用于 assets 或项目模板。
