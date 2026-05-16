# 多 Agent 玩法计划

用户明确允许多 agent、任务可独立、owned files 清晰、final integration 可验证时使用。并行的目的不是更快写更多代码，而是降低冲突和缩短可验证 slice。

## 启动条件

必须同时满足：

- 用户明确要求或接受多 agent / parallel work。
- 每个 worker 有唯一 owned files 或 owned responsibility。
- tasks 不依赖同一段 scene tree、同一 signal connection 或同一 resource owner 的即时结果。
- final integration owner 明确，且有一条完整验证命令或 scene smoke。
- shared docs / plans 有唯一 owner，避免多个 agent 同时改同一事实。

不满足时，使用单 agent 顺序执行。

## Owned Files 划分

每个 worker brief 必须包含：

- Task ID 和目标。
- Owned files：允许编辑的具体文件或目录。
- Prohibited files：不得编辑的共享文件、其他 worker 文件、用户改动文件。
- Read-only context：可以读取但不能改的 scene/script/reference。
- Integration contract：暴露给其他 worker 的 signal、method、resource、InputMap action 或 docs entry。
- Verification：该 worker 自己能运行的最小验证。
- Stop rule：需要改 non-owned file、发现 plan 错、发现 shared owner 冲突时暂停报告。

## 常见切分方式

| 切分方式 | 适用 | 风险 |
| --- | --- | --- |
| Script owner | movement、combat、save、UI controller 各自独立 | scene signal connection 仍需 integration owner |
| Scene owner | 一个 worker 只改 test scene，另一个只改 player-facing scene | 容易出现测试通过但玩家路径没变 |
| Docs owner | 一个 worker 同步 current/status/history，代码 worker 不碰 docs | docs 可能落后，需要 final closeout |
| Validation owner | 一个 worker 只加 smoke/test runner | runner 不能替代 gameplay fix |

## Integration Owner

多 agent 计划必须指定一个 integration owner，负责：

- 汇总 workers 的 changed files 和 verification evidence。
- 检查 overlapping edits 和 unexpected dirty files。
- 读最终 `.tscn` / `.gd`，确认 scene route、signals、InputMap、resources 真的连到 player-facing path。
- 运行完整验证并扫描 Godot output error text。
- 同步 docs/current、history、next steps。

## Brief 模板

```text
Agent N - <task id / title>
Owned files:
Prohibited files:
Read-only context:
Goal:
Current evidence:
Implementation contract:
Verification:
Manual acceptance:
Stop and report if:
```

## 禁止项

- 多个 worker 同时改同一个 `.tscn`、same signal connection、same resource default、same docs fact。
- worker 为了通过测试改 non-owned integration path。
- integration owner 只看 exit code，不读 logs / scene route。
- 发现冲突后直接回滚其他 agent 或用户改动。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
