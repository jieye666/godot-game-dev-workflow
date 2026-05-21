# 游戏项目文档结构

初始化 Godot 项目 docs、审计 docs layout、或降低新 agent 入场 token 时加载。正文默认中文；路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。

默认推荐 2DA-style indexed docs，但不强制所有项目照搬。新 Godot 项目没有自己的文档规范时，建议初始化这套结构；已有 `AGENTS.md`、`docs/INDEX.md` 或项目 workflow 时，先按项目规范，再补缺失索引。

## Lite Layout

适合原型、单人项目或刚初始化项目：

- `AGENTS.md`：项目级操作规则和读取顺序。
- `docs/INDEX.md`：文档路由，不放长历史。
- `docs/current/INDEX.md`：当前真相目录索引。
- `docs/current/AGENT-QUICK-CONTEXT.md`：hot context。
- `docs/current/STATUS.md`：当前系统、验证命令、待验收项。
- `docs/plans/INDEX.md`：计划目录索引。
- `docs/plans/NEXT-STEPS.md`：下一步 task queue 和 readiness。
- `docs/history/INDEX.md`：历史证据目录索引。
- `docs/history/commits/INDEX.md`：提交批次记录索引。

## Full Layout

适合多系统、多 agent、多会话项目，在 Lite Layout 上增加：

- `docs/current/PROJECT-SNAPSHOT.md`：当前架构、runtime route、accepted behavior。
- `docs/plans/gdd/INDEX.md`：active GDD plan 索引；只放未完成 detailed GDD。
- `docs/history/gdd/INDEX.md`：completed / abandoned GDD 的唯一详细文件索引。
- `docs/plans/archive/INDEX.md`：非 GDD 旧协作计划或兼容说明。
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
- 当前系统结构、runtime route、accepted behavior：`docs/current/`；不写 completed GDD 时间线。
- 下一步任务：`NEXT-STEPS.md` 或 active plan。
- 完成证据：history / changelog。
- 外部参考：`docs/reference/INDEX.md`，不是本地真相。

## GDD 存储规则

- active GDD 放 `docs/plans/gdd/`。
- completed / abandoned GDD 的唯一详细文件放 `docs/history/gdd/`。
- `docs/plans/archive/` 不保存 GDD 详细文件，只保留非 GDD 协作计划或兼容说明。
- GDD 历史通过 `docs/history/gdd/INDEX.md` 快速定位；只有出现大问题或需要追溯决策时才打开具体 GDD。

## 初始化后检查

- 所有 hot context 字段都有值或明确 `TBD`。
- `docs/INDEX.md` 能路由到各目录 `INDEX.md`、current/status/next steps。
- 主要目录有 `INDEX.md`：`docs/current/`、`docs/plans/`、`docs/plans/gdd/`、`docs/history/`、`docs/history/gdd/`、`docs/history/commits/`、`docs/reference/`。
- completed / abandoned `GDD-*.md` 不同时存在于 `docs/plans/archive/` 和 `docs/history/gdd/`。
- active docs 不复制长历史；history 不作为当前入口。
- `STATUS.md`、`PROJECT-SNAPSHOT.md` 和 roadmap 不吸收历史流水；组织健康细则见 `project-organization-health.md`。
- 新增文档默认中文，机器字段和 Godot 标识符保持英文。
