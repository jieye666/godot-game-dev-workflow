# 项目 AI 规则

## 入口

先通过 `project.godot` 确认项目根，再读 `docs/current/AGENT-QUICK-CONTEXT.md` 和 `docs/INDEX.md`。

## 工作规则

- 源码和 scene 是最终事实；docs 负责路由和当前状态。
- 使用 MCP/editor 时，把 tool evidence、file evidence、manual acceptance 分开记录。
- 验证不能只看 exit code；Godot 输出出现 `ERROR`、`SCRIPT ERROR`、`PARSE ERROR`、`push_error` 时判定失败。

## 文档语言

新增和更新文档默认中文。路径、命令、GDD 编号、Godot 标识符不翻译。
