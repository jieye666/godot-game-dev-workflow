# 会话收尾同步

implementation、milestone、doc cleanup 或 handoff 后使用。同步 current docs、history、plans、AI-facing rules，而不膨胀上下文。

## 什么时候必须收尾

- 代码或 scene 行为改变。
- 用户完成 manual acceptance。
- milestone / prototype slice 结束。
- docs cleanup、计划归档、skill 规则更新。
- 发现旧 docs、memory、quick context 与当前代码冲突。

## 同步原则

- current docs 写当前真相；history/log 写证据；archive plans 保留过去方案。
- 不把同一个身份事实复制到多个 active docs；用 `docs/INDEX.md` 指向权威位置。
- quick context 只放下一位 agent 必读的 hot context：项目根、当前状态、验证命令、常见陷阱。
- 计划文件记录 task status、verification evidence、manual acceptance result、next recommended task。
- 外部 reference 或旧记忆只能作为证据，最终以当前代码和项目 docs 为准。

## Implementation Closeout

- 列 changed files。
- 写 automated checks 和结果，包含 Godot output error scan。
- 写 manual steps 或用户 acceptance。
- 更新状态：完成、部分完成、阻塞、下一步。
- 如果行为、节点、信号、resource、输入、存档、路由改变，同步对应 docs/current 或 active plan。
- 面向人查看的 closeout 说明用中文；路径、命令、API、Godot 标识符、GDD 编号保留英文。

## Milestone Handoff

- 确认 active plan 是否应归档或保留。
- `NEXT-STEPS.md` 只保留下一个可执行任务，不堆积已完成细节。
- `development-log.md` 记录日期、改动、验证、验收。
- 如果新增 workflow 教训，先写项目 docs；只有可复用规则才考虑补进 skill。

## Impact to Docs Mapping

| 变化 | 默认同步位置 |
| --- | --- |
| 当前玩法行为、主场景、验证命令 | `docs/current/STATUS.md` 或项目指定 source of truth |
| 下一步任务、readiness、blocker | `docs/plans/NEXT-STEPS.md` 或 active plan |
| 已完成计划、人工验收、验证证据 | `docs/history/development-log.md`，必要时 archive plan |
| AI 进入项目必读陷阱 | `docs/current/AGENT-QUICK-CONTEXT.md` 或 `AGENTS.md` |
| 参考项目 intake 或来源变化 | `docs/reference/INDEX.md` 或对应 manifest |
| 可复用 workflow 教训 | 先项目 docs；确认跨项目有效后再维护 skill |

## Mechanical Checks

- rerun 项目认可的验证命令；Godot 输出中 `ERROR`、`SCRIPT ERROR`、`push_error` 算失败。
- 如果改了 docs，再跑 docs audit 或项目 closeout validator。
- 如果改了 skill，再跑 `scripts/skill_self_check.py <skill-root>` 和平台 validator。
- 如果平台 validator 在 Windows 因中文解码失败，用 UTF-8 模式重跑：`$env:PYTHONUTF8='1'; python <quick_validate.py> <skill-root>`。
- commit 前确认没有无关临时文件、cache、日志、外部参考仓库大目录被误加入。

## Git Commit 描述

- 用户要求 commit 或项目 policy 要求 commit 时，commit message 默认中文。
- 保留必要英文：路径、命令、Godot API、InputMap action、signal、class/resource/scene 文件名、GDD 编号、issue/PR 编号、约定式 commit type。
- 推荐格式：`docs: 同步 GDD-080 交接状态`、`fix: 修复 BossRewardRouteTest 的完成标记`、`feat: 接入 MovementTest 白盒反馈`。
- commit 前后报告给用户的摘要也用中文，明确 changed files、验证命令、结果、未做的 manual acceptance。

## 防膨胀规则

- 不把完整日志贴进 quick context。
- 不在多个 docs 重复大段相同事实。
- 不把未验证猜测写成当前真相。
- 不把自动验证当 manual acceptance。

## Final Report Shape

最终回复默认包含：改了什么、关键文件、自动验证命令和结果、Godot 输出错误扫描结果、manual playtest 是否执行、docs sync 是否完成、下一步建议。未执行的 editor/MCP/manual acceptance 必须明确说未执行。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
