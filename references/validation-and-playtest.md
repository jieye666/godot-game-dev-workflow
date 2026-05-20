# 验证与游玩验收

自动验证证明结构、脚本和 smoke route；人工验收证明 feel、readability、pacing、fun。两者必须分开报告。

## 验证分层和时间成本

- Godot headless 启动、全量 smoke、完整 validation 和失败后定位通常是主要耗时点；不要在每个小步骤都默认跑完整验证。
- implementation 中的验证节奏先服从 `agent-execution-discipline.md`：开发中跑窄验证，用户验收 closeout、最终收尾或提交前再跑完整 validation。
- 快速档：开发中跑相关 parser、unit、单 scene smoke 或最小命令；收尾报告说明未跑完整 validation 的原因。
- 标准档：实现中跑相关 smoke 或聚焦测试；影响 gameplay-visible behavior 时给 manual playtest 步骤；收尾按项目风险决定是否跑完整 validation。
- 严格档：跨系统、架构变更、multi-agent integration、提交前收尾或用户手动验收 closeout，必须跑项目完整 validation，例如 `scripts\validate-project.ps1`。
- 无论档位，Godot 输出出现 `ERROR`、`SCRIPT ERROR`、`PARSE ERROR`、`push_error` 时都判定失败；自动验证不能替代 manual playtest。

## Godot 启动路径

- 先读项目 quick context、`AGENTS.md` 或验证脚本中的 Godot executable；其次使用 `GODOT_EXE`。
- 不要猜 `C:\Program Files\...` 或其他系统路径。
- 如果路径缺失，先定位真实路径并写回项目必读文档，再运行验证。

## 修改验证链路前

- 先通读验证脚本全文，再改动；不要凭局部片段连续 patch。
- 把问题拆成单独假设：Godot path、runner timeout、exit code、输出扫描、headless 残留、测试脚本真实失败、文档审计失败分别验证。
- 先用单个 smoke scene 证明 runner 可以退出、拿到 exit code、写入日志且无错误文本，再跑全量 smoke 和完整 validation。
- 如果需要改 runner，先保留或新增最小回归方式，确认 timeout 真的能结束并清理本项目 headless 进程。
- `check_scene_references.py` 只应扫描当前项目源码；`.tmp`、`.git`、`.godot`、`reference` 等临时目录或参考项目目录必须跳过，避免把外部参考代码噪声当作当前项目缺口。

## Smoke Test 进程清理

- 优先使用项目的 `scripts\run-smoke-tests.ps1` 或等价脚本，不要手写一串 Godot scene 命令。
- smoke runner 应逐 scene 设置 timeout，保存 scene log，并在每个 scene 前后清理本项目 `--headless --path <project-root>` 的 Godot 残留进程。
- 完整验证长时间停顿时，先读 smoke summary/log 判断是否已经完成，再只清理本项目 headless smoke 进程；不要关闭 Godot editor。
- Godot 输出出现 `ERROR`、`SCRIPT ERROR`、`PARSE ERROR`、`push_error` 时判定失败，即使 exit code 为 0。

## 完成前验证门

- 不能只报告 exit code；必须说明是否扫描 Godot output error text。
- 自动验证适合证明 parse、scene load、unit/smoke route、doc audit、script runner。
- manual playtest 适合证明 movement feel、camera readability、route clarity、Boss pacing、UI feedback、fun。
- 如果 manual playtest 未执行，最终报告必须写清 scene、exact controls、操作、期望结果、失败反馈，不声称已验收。
- Manual acceptance steps 必须能让用户照做：写出 scene path、起点、路线、具体按键或输入、可见 UI 文案/状态、保存读取步骤和失败时应反馈什么。涉及 Boss/debug route/save-load/gated progression 时，必须写清类似 `F6` 造成白盒伤害、`F5` 保存、`F9` 读取这类 exact controls；不要只写“击败 Boss”“确认路线打开”。
- 如果用户已经手动接受，把 acceptance result 写进 closeout docs。

## 失败处理

- exit code 0 但输出有错误文本：失败，先修错误文本。
- 测试通过但用户说行为没变：加载 `common-failure-modes.md`，检查 played scene、attached script、input map、signal route、resource instance、main scene route。
- 验证脚本自身失败：先最小复现 runner，再改验证链路。
- Godot editor 手动验收不能被 headless smoke 替代；两者结论分开写。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
