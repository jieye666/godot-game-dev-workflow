# 游戏项目文档结构

初始化 Godot 项目 docs、审计 docs layout、或降低新 agent 入场 token 时加载。正文默认中文；路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。

## Lite Layout

适合原型、单人项目或刚初始化项目：

- `AGENTS.md`：项目级操作规则和读取顺序。
- `docs/INDEX.md`：文档路由，不放长历史。
- `docs/current/AGENT-QUICK-CONTEXT.md`：hot context。
- `docs/current/STATUS.md`：当前系统、验证命令、待验收项。
- `docs/plans/NEXT-STEPS.md`：下一步 task queue 和 readiness。
- `docs/history/development-log.md`：完成记录和验收证据。

## Full Layout

适合多系统、多 agent、多会话项目，在 Lite Layout 上增加：

- `docs/current/PROJECT-SNAPSHOT.md`：当前架构、runtime route、accepted behavior。
- `docs/plans/active/`：正在执行的 detailed task plans。
- `docs/plans/archive/`：完成或废弃计划，只作为证据。
- `docs/reference/INDEX.md`：参考项目、外部资料和本地化说明。
- `docs/decisions/`：架构决策或长期约束。

## Hot Context 必填字段

`AGENT-QUICK-CONTEXT.md` 或等价入口应包含：

- Godot project root
- Godot version
- Main scene
- Manual test scene
- Validation command
- MCP/editor status
- Docs source of truth
- Current milestone / accepted behavior
- Known blockers / next task

## Docs Owner 规则

- 项目身份、主场景、验证命令：quick context / status。
- 当前系统结构、runtime route、accepted behavior：`docs/current/`。
- 下一步任务：`NEXT-STEPS.md` 或 active plan。
- 完成证据：history / changelog。
- 外部参考：`docs/reference/INDEX.md`，不是本地真相。

## 初始化后检查

- 所有 hot context 字段都有值或明确 `TBD`。
- `docs/INDEX.md` 能路由到 current/status/next steps。
- active docs 不复制长历史；history 不作为当前入口。
- 新增文档默认中文，机器字段和 Godot 标识符保持英文。
