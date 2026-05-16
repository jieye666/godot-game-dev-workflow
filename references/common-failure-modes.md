# 常见失败模式

验证失败或用户说行为没变时，优先检查 played scene、script attachment、input mapping、signal route、resource instance、main scene route。

## 行为没变

症状：测试通过、脚本改了、日志正常，但用户在游戏里看不到变化。

优先排查顺序：

1. Played scene：用户实际运行的是 `project.godot` main scene、测试 scene、还是 editor 中另一个 scene。
2. Attached script：改到的 `.gd` 是否真的挂在 player-facing scene 的 node 上。
3. Node path：运行时节点名、unique name、instance override 是否和代码路径一致。
4. InputMap：玩家按的 action 是否存在、绑定是否冲突、代码是否监听同一个 action。
5. Signal route：sender / receiver / payload 是否在 player-facing scene 中连接，不只是在测试 scene 连接。
6. Resource instance：改的是共享 `.tres`、scene-local override、还是未被引用的 duplicate resource。
7. Main route：bootstrap、room flow、save/load、checkpoint、reward route 是否绕过了被修改 scene。
8. Visibility feedback：状态变了但 UI、whitebox label、animation、collision 或 camera feedback 没有表现出来。

修复要求：

- 先证明当前可见路径在哪里，再改代码。
- 如果只改测试路径，要补 player-facing path 或把 task 降级为 test-only。
- final report 必须说明实际修到的 runtime path 和 manual retest steps。

## 验证流程失败

- Godot path 找不到：先读项目 quick context / `AGENTS.md` / validation scripts；不要猜 `C:\Program Files\...`。确认真实路径后同步必读文档。
- 中文审计失败：新增或更新文档标题和正文默认中文；路径、命令、API 和 GDD 编号保留英文即可。
- 完整验证长时间停顿：检查 `.tmp/smoke-tests/summary.txt` 和 scene logs；如果 smoke 已完成，清理本项目 `--headless --path <project-root>` 残留进程，并加固 runner 的 per-scene timeout/cleanup。
- 连续修验证脚本仍失败：停止 patch，通读脚本全文和最近日志，先用单个 scene 验证 runner 的进程等待、exit code 和日志扫描，再恢复全量验证。

## 计划执行失败

- `pending` task 被直接实现：停止，补 requirement、owned files、verification、manual acceptance 后再继续。
- `ready` task 实现中需要 non-owned file：改为 `escalated`，报告影响和选项。
- 参考项目方案复制失败：回到本地 owner、scene route、InputMap、resource contract，按本地结构复刻行为。
- docs 写了但代码没连：以 current scene/script 为准，更新 docs 或补 runtime integration。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
