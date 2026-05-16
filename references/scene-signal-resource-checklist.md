# 场景信号资源检查表

修改 scene、signal、resource 前使用。读真实 `.tscn`，确认 node hierarchy、signals、collision、monitoring、resources。

## 修改前检查

- 确认项目根：先找 `project.godot`。
- 确认 played scene：`project.godot` main scene、启动脚本、测试 scene、当前用户实际打开的 scene 是否一致。
- 读目标 `.tscn`：node 名、parent、unique name、groups、script attachment、export values。
- 读相关 `.gd`：`$Node`、`%UniqueName`、`get_node()`、signal connect、preload/load。
- 如果有 inherited scene 或 packed scene instance，确认改的是 instance 还是 source scene。

## Node Path

- 不从截图、记忆、旧 docs 猜 node path。
- 改名 node 前搜索所有 `$Name`、`%Name`、`NodePath` export、animation track、signal connection。
- 使用 `%UniqueName` 前确认 scene 中真的设置了 unique name。
- 动态生成 node 要说明创建时机和 parent。

## Signal

- 写清 sender、receiver、signal name、payload、连接位置。
- 避免重复 connect；必要时先判断 `is_connected`。
- Godot 4 signal 写法保持一致，不混用旧风格。
- 如果 signal 只在测试里连通，要确认 player-facing scene 也连通。

## Resource / Scene Instance

- 检查 `.tres`、`.res`、`PackedScene`、export var 的真实引用。
- 修改 resource 默认值前确认是否被多个 scene 共享。
- preload 路径必须是真实路径；移动文件后检查引用。
- save/load flag、reward state、UI display state 要有单一 owner。

## InputMap / Autoload

- 改输入前检查 `project.godot` 中已有 `input/*` action，确认是新增 action 还是复用 action。
- 记录默认绑定、键鼠/手柄差异、冲突 action，以及玩家实际会按的 action name。
- 检查代码读取的是 `Input.is_action_pressed()`、`is_action_just_pressed()` 还是 remap UI / settings resource。
- 改 Autoload 前确认生命周期、初始化顺序、scene-local owner 是否会被绕过。
- 不为一个局部玩法临时新增全局 owner，除非 Task Plan 已说明原因和退出策略。

## Collision / Area

- 改 `Area2D` / `CollisionShape2D` 时确认 layer、mask、monitoring、monitorable、disabled。
- 检查进入/退出 signal 和物理帧时序，别只依赖默认初始重叠。

## 最小验证

- 运行项目已有 scene reference check 或 smoke test。
- 扫描 Godot 输出中的 `ERROR`、`SCRIPT ERROR`、`PARSE ERROR`、`push_error`。
- 给 manual retest：打开哪个 scene、执行什么动作、期望看到什么。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
