# 实现契约

Task Plan 涉及 Godot 行为时必须写清 Scene Tree、Script Plan、Signals、Resources/InputMap/Autoload、Verification。

## 什么时候必须升级 Task Plan

- 改 `.tscn`、node path、signal connection、resource preload/export。
- 新增或移动 script ownership。
- 改输入配置、全局生命周期、存档读写、场景路线、生成/重生、战斗伤害、相机或 UI runtime path。
- 多个系统共享状态，或需要后续扩展同类玩法。

## Compact Patch Plan 最小字段

- Goal：这次只修什么。
- Owned files：只允许改哪些文件。
- Current evidence：读过哪些代码、scene、log、docs。
- Risk：可能影响哪些可见行为。
- Verification：自动命令和 manual check。
- Doc sync：是否需要同步 docs/history。

## Task Plan 必填契约

- User intent / non-goals：用户要什么、不做什么。
- Requirement/design source：GDD、active plan、reference、用户确认范围。
- Owned files / prohibited files。
- System ownership：哪个 node/script/resource 是权威 owner。
- Related systems：输入、移动、相机、UI、存档、房间流、敌人、Boss、奖励等相关路径。
- Extension points：后续第二种 variant 如何接入，不重写首版。
- Scene tree changes：新增/删除/移动 node，父节点，唯一名，groups。
- Script plan：核心函数、信号处理、状态字段、生命周期函数。
- Signals：sender、receiver、connection location、payload。
- Resources/scenes：`.tscn`、`.tres`、export variables、preload/load。
- InputMap：新增/复用 action，默认绑定，冲突检查。
- Autoload decision：使用或不使用 Autoload 的理由。
- Verification：parser/headless/smoke/tests，Godot output error scan。
- Manual acceptance：scene、操作、期望结果、失败反馈。
- Doc sync targets：`docs/current/`、plans、history、quick context。
- Implementation Readiness：`pending` / `ready` / `escalated`。

## 禁止项

- 未读真实 `.tscn` / `.gd` 就写 node path。
- 把 test-only route 当成 player-facing route。
- 为快速实现新增平行状态 owner，导致 save/UI/gameplay 分裂。
- 在未说明范围时重构 unrelated systems。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
