# Godot 4 GDScript 规则

使用 Godot 4 API；明确 typed signals 和 public method contract；不猜 node path；必要时使用 deferred。目标是让生成代码能接进真实 scene，并且后续 variant 不需要重写首版。

## Script Contract

- 每个 gameplay script 写清 owner：这个 node/script 拥有什么状态，外部只能通过哪些 public methods、signals 或 exported config 交互。
- public method 名称表达 gameplay intent，不暴露临时实现细节。
- shared state 只能有一个权威 owner；UI、save、reward、combat 不各自复制一份状态。
- 可调参数优先 `@export` 或 resource config，避免把 tuning 数值散在多个函数里。
- 不为一次性测试新增 production-only shortcut；测试 helper 要和 player-facing path 分开。

## Godot 4 API

- 使用 Godot 4 signal 语法和 typed declarations，避免 Godot 3 风格混用。
- 优先显式类型：变量、参数、返回值、signal payload 能标就标。
- 生命周期函数保持清楚：`_ready()` 做引用和连接，`_physics_process()` 做物理输入/移动，`_process()` 做非物理表现。
- 需要等待 scene tree 稳定、碰撞帧或信号连接完成时，用 `call_deferred()` / `await get_tree().physics_frame`，并说明原因。

## Node / Signal / Resource

- 写 `$Node`、`%UniqueName`、`get_node()` 前先读真实 `.tscn`。
- `@onready` node reference 要能在 scene attachment 中解析；optional node 要显式处理缺失。
- signal contract 写 sender、receiver、payload 和 connection location；避免重复 connect。
- resource、PackedScene、preload/load 路径必须真实；共享 resource 修改前确认影响范围。
- InputMap action name 必须来自 `project.godot` 或 plan 中新增的 action contract。

## Code Quality

- 函数保持短且按 gameplay 阶段命名，例如 `enter_phase_two()`、`apply_reward()`、`restore_checkpoint()`。
- 避免深层布尔分支；状态多于两三种时考虑 enum 或小状态机。
- 错误路径要给可验证反馈：return bool、push_warning/push_error、whitebox label 或 test assertion。
- 不吞掉 Godot 错误；输出出现 `ERROR`、`SCRIPT ERROR`、`PARSE ERROR`、`push_error` 视为验证失败。
- 兼容旧接口时明确标注为 temporary compatibility，并在 docs/plan 说明移除条件。

## 生成代码前自检

- 这个 script 挂在哪个 scene node 上？
- 玩家实际路径会调用这段代码吗？
- 哪些 signals / InputMap actions / resources 必须已存在？
- 自动测试覆盖什么，manual playtest 还要看什么？
- 第二个同类玩法加入时是新增 config/scene instance，还是要复制改代码？

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
