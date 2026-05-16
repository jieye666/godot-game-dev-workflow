# 项目文档工作流

项目文档是协作真相来源，但必须尊重职责边界，避免重复事实。源码和 scene 最权威；`docs/INDEX.md` 定义文档角色。

## 进入项目

1. 先找 `project.godot`，不要从父目录名推断引擎或项目身份。
2. 有 quick context 时先读 quick context / identity，再读 `docs/INDEX.md`。
3. 只读 `docs/INDEX.md` 指向的 current/status/next-step 文件，不默认加载全部 docs。
4. 如果 docs 与代码冲突，以当前 `.tscn`、`.gd`、`.tres`、validation logs 为准，并把冲突写入 plan 或 closeout。

## Source of Truth

| 信息类型 | 推荐 owner | 说明 |
| --- | --- | --- |
| 项目身份、当前集成场景、验证命令 | quick context / status | 下一位 agent 的 hot context |
| 当前系统结构、runtime route、accepted behavior | `docs/current/` | 当前真相，不写长历史 |
| 下一步任务 | `NEXT-STEPS.md` 或 active plan | 只保留可执行 next task |
| 已完成任务和验收证据 | history / development log / changelog | 证据，不作为当前入口 |
| 参考项目或外部资料 | `docs/reference/INDEX.md` | 只作为 blueprint，不是本地真相 |

## 同步时机

必须同步：

- scene tree、signal、resource、InputMap、Autoload、save flag、UI route 或 main scene route 改变时。
- user manual acceptance 通过或反馈行为没变。
- task readiness、owned files、verification result、next task 改变。
- 发现旧 docs、memory、reference 与当前代码冲突。

可以不同步：

- 纯内部重命名且 current docs 没提到。
- 一次失败实验，没有进入 active plan 或代码。
- 自动生成临时日志。

## 去重规则

- 同一事实只保留一个 active owner；其他文档链接或摘要。
- quick context 写“读哪里”和“当前阻塞”，不复制完整 plan。
- status 写当前状态和下一步，不堆积已完成细节。
- history 写日期、变更、验证、验收，不覆盖 current docs。
- archived plans 是过去证据，不要当作当前 scope 直接执行。

## 文档收尾最小清单

- Update current docs：当前行为、scene route、owner、input/resource/signal contract。
- Update plan/status：task status、readiness、verification、manual acceptance。
- Update history：日期、changed files、commands、结果、用户验收或未验收。
- Update next steps：只写下一步可执行 task 和是否 `pending` / `ready` / `escalated`。
- Report key project docs and reference files used。

## 面向人查看的语言

- docs sync、history、status、NEXT-STEPS、plan closeout、final handoff 默认用中文描述。
- commit message 默认用中文描述变更意图和范围；路径、命令、Godot API、InputMap action、signal、class name、GDD 编号、commit type、issue/PR 编号保留英文。
- 给人看的验收步骤、风险、失败原因、下一步尽量用中文，不把英文工作流短语当正文。
- 机器字段或模板字段可以保留英文，例如 `Owned files`、`Verification`、`Implementation Readiness`。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
