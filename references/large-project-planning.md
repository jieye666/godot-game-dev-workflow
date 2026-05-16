# 大型任务规划

用于 vague goal、prototype milestone、multi-system mechanic、multi-session work。目标是把“大方向”拆成下一位 agent 可以直接执行、验证和收尾的小任务。

## 什么时候使用

- 用户只给宏观目标、玩法方向、参考项目或里程碑。
- 任务跨 scene、script、UI、InputMap、resource、save/load、Boss、room flow 等多个系统。
- 需要多会话或多 agent 推进。
- 计划已经存在，但 task 不能判断 `pending` / `ready` / `escalated`。

## 拆分顺序

1. 先定位真实 Godot 项目根和 docs router：`project.godot`、quick context、`docs/INDEX.md`。
2. 把用户目标写成 requirements，不把猜测写成已确认事实。
3. 标出 non-goals：本轮不做的美术、音频、过场、正式竞技场锁门、平衡 polish 等。
4. 识别系统 owner：哪个 scene、script、resource 或 Autoload 是权威状态 owner。
5. 列出 visible runtime route：玩家实际打开哪个 scene，经由哪些 signals/input/resource 看到变化。
6. 拆 milestones：每个 milestone 只交付一个可验收能力或一个稳定基础设施层。
7. 拆 tasks：每个 task 必须有 Task ID、owned files、current evidence、verification、manual acceptance。
8. 给每个 task 标记 Implementation Readiness：`pending`、`ready`、`escalated`。

## Task 粒度

好的 task 应满足：

- 一句话能说明目标，且能追溯到 requirement、GDD、active plan、bug report 或 user accepted scope。
- 文件边界清楚：owned files 和 prohibited files 都明确。
- 能在一个上下文窗口内读完相关 scene/script/reference。
- 有独立自动验证，或明确说明只能 manual acceptance。
- 有 player-facing check：打开哪个 scene、做什么操作、期望看到什么。
- 失败时能判断责任边界，而不是“整个系统可能有问题”。

过大的 task 要继续拆：

- 同时改 movement、camera、UI、save、reward route。
- 同时改多个 `.tscn` 且没有 shared owner 说明。
- 需要先决定 architecture tradeoff 才能实现。
- 验证必须跨多个未稳定系统。

过小的 task 可以合并：

- 只改 docs 中同一事实的多处 routing。
- 同一 signal contract 的 script 和 scene connection 互相依赖。
- 同一个 visible behavior 必须同时改 test scene 和 player-facing scene 才有意义。

## Plan 必填块

- Intent：用户要达成的玩法或项目管理结果。
- Current evidence：读过的 docs、scene、script、reference、log。
- Requirements / non-goals。
- System map：owner、related systems、extension points。
- Milestones：每个 milestone 的交付物和验收方式。
- Task table：列出 Task ID、目标、owned files、依赖、readiness、verification 和 manual acceptance。
- Risk and escalation：哪些决策需要用户接受。
- Docs sync targets：完成后更新哪些 current/status/history/next steps。

## Readiness 应用

- `pending`：继续调查、拆 scope、补 evidence 或补验证，不写 gameplay code。
- `ready`：可以实现，且 implementation agent 不需要重新讨论 scope。
- `escalated`：必须报告原因和选项，例如 non-owned file、架构取舍、唯一验收是 manual playtest、验证环境不可用。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
