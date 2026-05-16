# MCP 与 Editor 协作

需要使用 Godot MCP、editor、headless runner 或 debug output 时加载。目标是把 tool evidence、file evidence 和 manual acceptance 分开，避免把工具输出误当最终验收。

## 可用场景

- 用 MCP 确认 Godot version、project info、当前 debug output、scene run result。
- 用 editor 或运行日志观察 parser、autoload、scene load、signal route、runtime error。
- 用 MCP/editor 辅助定位 played scene、attached script、main scene route 或 visible runtime path。

## 证据优先级

1. File evidence：`project.godot`、`.tscn`、`.gd`、`.tres`、项目 docs 和验证脚本。
2. Tool evidence：来自 MCP project info、Godot debug output、headless run logs 和 editor 状态的工具证据。
3. Human evidence：用户 manual playtest、可见行为反馈、验收结论。

tool evidence 可以帮助发现问题，但不能覆盖 file evidence；manual acceptance 只能来自真实 editor/user playtest，不能由 headless smoke 或 MCP 状态代替。

## 使用规则

- 先确认真实项目根，再调用 MCP 或运行项目；不要让父目录名决定项目身份。
- 报告 MCP/editor 结果时写明来源，例如 `MCP get_project_info`、`Godot debug output`、`editor manual playtest`。
- 如果 MCP 与文件冲突，以当前文件为准，并把冲突写入 plan 或 closeout。
- 如果 headless output 出现 `ERROR`、`SCRIPT ERROR`、`PARSE ERROR`、`push_error`，判定自动验证失败。
- 不关闭用户正在使用的 Godot editor；清理进程只针对本项目 headless smoke。

## Handoff 写法

- Automated checks：命令、exit code、是否扫描 Godot output error text。
- MCP/editor evidence：调用了什么工具，确认了什么，未确认什么。
- Manual playtest：scene、action、expected result、failure feedback；未执行时明确写未执行。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
