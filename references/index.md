# Godot Game Dev Workflow Reference Index

维护 skill 或判断加载哪份 reference 时读本文件。普通任务优先使用 `SKILL.md` 的 Task Routing；不要默认加载完整 `references/`。

路由原则：先判断 task shape，再只读一个能回答当前问题的 focused reference；仍有缺口时再补第二个。references 保持单层目录，深层目录只用于 assets 或项目模板。

## intake/docs

- `project-doc-workflow.md`：进入 documented project、判断 Source of Truth、同步 current/status/history。不要在纯代码 one-file patch 且 docs 不变时读取。
- `game-project-doc-structure.md`：初始化或审计 docs layout、hot context 字段、docs owner。不要在已有 docs 结构清楚、只需读当前状态时读取。
- `context-memory-strategy.md`：需要降低 token、整理 hot/warm/cold context、处理 reference project intake 时加载。不要把它当普通功能实现前置步骤。
- `project-organization-health.md`：审查 docs/current/plans 是否吸收历史、主场景脚本或 smoke test 是否过大、组织效率是否下降时加载。不要在没有组织健康问题的小修中读取。

## planning

- `agent-execution-discipline.md`：计划前、玩家可见 polish、流程复盘、文档收尾或提交前加载；约束 task shape、最小闭环、暂停点、验证节奏和文档时机。不要在已确认的 trivial one-file patch 中扩展成大计划。
- `spec-driven-gameplay-workflow.md`：需求模糊、跨系统、需要先拆 Requirement / Design / Plan / Task 时加载。不要用于需求已经明确的小修。
- `large-project-planning.md`：大功能、原型、里程碑、多会话任务拆分时加载。不要用于 one-file patch 或已 ready 的单任务实现。
- `planning-readiness-and-traceability.md`：从现有 plan 准备实现、判断 `pending` / `ready` / `escalated`、检查 coverage gaps 时加载。不要在没有计划文档的快速修复中读取。
- `gameplay-implementation-plan-template.md`：需要写 Task Plan 或 Compact Patch Plan 时加载。不要在只回答问题且不改文件时读取。
- `web-gameplay-reference-research.md`：制定高风险玩家可见 gameplay、关卡、Boss、UI flow、movement、combat、save/load、unlock 等计划前加载，先查同类成功例子再本地化。不要在纯本地 bug、docs、validation 修复中读取；写 `Reference research: not needed` 和理由即可。
- `multi-agent-gameplay-plan.md`：只有并行能减少冲突且 owned-file boundaries 清楚时加载。不要为了“更正式”在单人小任务中读取。

## implementation

- `implementation-contracts.md`：Task Plan 涉及 scene/script/signal/resource/InputMap/Autoload/ownership 时加载。不要在 docs-only、只读问答或无 runtime path 风险的小 patch 中读取。
- `scene-signal-resource-checklist.md`：改 `.tscn`、node path、signal connection、resource instance、InputMap/Autoload 时加载。不要在纯脚本内部算法或小文案改动中读取。
- `godot-4-gdscript-rules.md`：写或审查 GDScript、计划会影响代码形态时加载。不要在只改 markdown、assets manifest 或非 GDScript 脚本时读取。
- `extensible-gameplay-architecture.md`：可复用系统、大功能、第二变体风险、coupling risk 时加载。不要为了首个小 prototype 预建大框架。
- `mcp-and-editor-workflow.md`：需要使用 MCP/editor、报告 tool evidence、区分自动验证和人工验收时加载。不要用 MCP/editor 输出替代 `.tscn`、`.gd` 或项目 docs。
- `common-failure-modes.md`：验证失败或用户说行为没变时加载；优先检查 played scene、attached script、main route。不要在根因已经由错误日志明确定位时读取完整清单。

## closeout/maintenance

- `validation-and-playtest.md`：完成前验证、Godot output scan、manual playtest handoff 时加载。不要在开发中每个小 patch 后默认跑完整 validation。
- `session-closeout-sync.md`：完成 implementation、用户验收、milestone handoff、docs cleanup 时加载。不要在刚进入项目或主观验收未完成时读取。
- `skill-quality-gate.md`：维护本 skill、新增 reference/script/template、吸收外部 workflow idea 时加载。不要在普通 Godot 项目功能开发中读取。
- `external-repositories.md`：刷新外部来源、记录 local snapshot、追踪来源不确定性时加载。不要在普通 gameplay 实现中扫描外部仓库清单。
- `slash-command-surface.md`：调整 `/godot-workflow`、5 个用户子命令、wrapper manifest、安装清理和旧命令收敛策略时加载。不要在不涉及 slash wrapper 的 skill 文档维护中读取。
