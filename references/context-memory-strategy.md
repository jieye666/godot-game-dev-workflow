# 上下文与记忆策略

用 hot/warm/cold context 降低 token 成本。目标是少读重复材料，但不跳过当前任务的 source evidence。

## Context Tiers

| Tier | 放什么 | 何时读 |
| --- | --- | --- |
| Hot | project root、当前 active scene、验证命令、当前 plan、常见陷阱 | 每次进入项目先读 |
| Warm | system docs、current status、NEXT-STEPS、reference index | 当前任务相关时读 |
| Cold | archived plans、`docs/history/gdd/`、`docs/history/commits/`、external references、old memory | 需要证据或追溯决策时读 |

## Token 预算规则

- `SKILL.md` 只负责触发、边界、路由；细节按 Task Routing 读对应 reference。
- 项目 `docs/INDEX.md` 是 router；不要默认全量加载 docs。
- reference project 先读 `docs/reference/INDEX.md` 或 manifest，再读 selected files。
- old memory 只当索引；当前 truth 以代码、scene、current docs 为准。
- 计划已 accepted 时不重写大段背景，只补 risk、verification、readiness。

## 默认 Intake Budget

进入已有 Godot 项目时默认只读：

1. `project.godot` 或 helper script 确认真实 root。
2. hot context：`docs/current/AGENT-QUICK-CONTEXT.md`、project identity，或项目指定等价文件。
3. `docs/INDEX.md`，再按它指向读取 `STATUS.md`、`NEXT-STEPS.md` 或 active plan。
4. 当前任务直接相关的 `.tscn`、`.gd`、resource、InputMap、Autoload 或验证脚本。

只有在当前证据不足时才读取 history、archived plans、旧 memory 或外部 reference。

## 推荐项目文件职责

| 文件类型 | 内容 | 不放什么 |
| --- | --- | --- |
| `AGENTS.md` / project AI rules | 入口规则、语言规范、验证入口、不可破坏边界 | 完整历史和长计划 |
| `docs/INDEX.md` | docs router、source-of-truth 指向、常用入口、历史索引链接 | 重复身份事实和 completed GDD 长列表 |
| `docs/current/AGENT-QUICK-CONTEXT.md` | 每次进入项目必读 hot context | 长日志、completed GDD 串和过期方案 |
| `docs/current/STATUS.md` | 当前系统状态、验证命令、验收状态 | 过去尝试的细节 |
| `docs/plans/NEXT-STEPS.md` | 下一批可执行任务和 readiness | 已完成任务堆积 |
| `docs/history/gdd/INDEX.md` | 已完成/废弃 GDD 历史索引 | 当前状态的唯一真相 |
| `docs/history/commits/INDEX.md` | 提交批次记录索引 | 当前任务入口 |
| `docs/history/development-log.md` | 旧总日志和历史证据 | 当前状态的唯一真相 |

## Reference Project Intake

- 先找 reference manifest / README / docs index，确认哪些文件对应当前功能。
- 只读取 selected implementation files 和必要 assets metadata；不扫描完整参考项目。
- 输出本地化 mapping：参考文件、可复刻机制、本项目落点、不同点、验证方式。
- 参考项目代码只能作为 blueprint；最终实现必须服从本项目 scene tree、InputMap、资源命名和 docs policy。

## Source-of-Truth Rules

- identity、Godot version、main scene、validation command 只在项目指定 owner file 保留当前值。
- 其他 docs 链接到 owner file，或写“见 X”，不要复制第二份。
- memory、archived plan、external reference 是证据层；行动前必须用当前 docs/code 校验。
- 发现冲突时更新 owner file，并在 history 记录冲突来源和修正依据。

## 写文档时降噪

- quick context 写热信息和下一步，不写完整历史或 completed GDD 串。
- current docs 写当前结构和 contract，不写探索过程。
- `docs/history/gdd/` 保存 completed / abandoned GDD 的唯一详细文件和索引，`docs/history/commits/` 写每次提交批次证据，不复制 current docs。
- task plan 写可执行字段，不贴长日志。

## Closeout Memory Extraction

收尾时只抽取能帮助下一位 agent 少走弯路的信息：

- 当前 accepted behavior、manual acceptance scene/action、最后验证命令。
- 仍然 pending / escalated 的具体缺口。
- 用户确认的 durable preference 或项目 policy。
- 发生过的 visible runtime path 问题和最终真实路径。

不要把完整实现叙事、失败日志或已归档计划复制进 hot context。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
