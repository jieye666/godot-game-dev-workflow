# Agent 执行纪律

计划前、玩家可见改动、文档收尾、流程复盘或提交前使用。目标是在写计划前先定 task shape、最小闭环、暂停点和验证节奏，避免边做边扩大 scope、过早写文档、重复验证、把中途异常无说明混入主任务。

## 强制执行循环

1. Task shape：正式计划前先把任务归类为 bug fix、player-visible polish、system slice、docs closeout、unexpected warning / side issue。不同 shape 分开决策，不把 warning、审美调整、文档收尾混成一个无边界任务。
2. Minimal loop：写计划前说清最小可接受闭环：要改到什么可见结果、哪些文件/系统属于 owned scope、哪些明确不做。用户没有要求扩大时，不主动顺手做下一阶段。
3. Player-visible pause：UI、camera、route readability、movement feel、Boss pacing 等主观内容采用两阶段：先做可看版本和窄验证，给 manual acceptance pack；用户确认后再做 docs/history/archive/commit。
4. Verification rhythm：开发中优先相关 smoke、单 scene 或最小命令；最终收尾、提交前或用户验收 closeout 才跑完整 validation。不要每个小 patch 后都跑全量验证。
5. Docs rhythm：未验收前只记录必要临时状态或待验收项，不反复改 current/history/archive。验收通过后一次性同步 designated docs、history 和 next steps。
6. Side issue handling：中途发现额外问题先分类。阻塞当前验收的错误必须修并说明；非阻塞问题记录或单独报告；只有用户同意或任务 policy 要求时才纳入本次 scope。
7. Deterministic work：确定性检查交给脚本或命令。文件路由、Git status/diff、文档语言审计、scene reference 检查、Godot output error scan、验证结果汇总等不靠模型记忆或肉眼猜测。
8. Conflict exposure：current docs、source、archive plan、reference 或 MCP/editor evidence 冲突时，先列出冲突和采用的 source of truth；不能把两种模式折中混合后继续实现。

## 暂停点

- 计划或实现开始前：先完成 task shape 和最小闭环判断；如果任务是玩家可见或主观体验，再确认 manual acceptance 口径。
- 第一版可运行后：只做窄验证和人工验收包，不急着归档、写已验收历史或提交。
- 用户反馈“还不对”时：先复盘判断错误属于 scope、设计意图、runtime path、debug 泄漏、验证不足，更新最小闭环后再改。
- 用户确认通过后：再进入 closeout，同步 docs/history/archive，跑完整 validation，并按项目 policy commit。

## 异常分类

| 类型 | 处理 |
| --- | --- |
| 阻塞错误 | runtime error、Godot warning 影响验收、scene 无法启动、smoke 失败；本次修复并补最小验证。 |
| 非阻塞风险 | 代码异味、未来 polish、debug 信息过多但不影响当前验收；记录为后续或请求用户确认后再做。 |
| 文档异常 | current truth 已损坏或审计会失败时修；先说明恢复范围，不借机重写无关文档。 |
| Scope creep | 新功能、新系统、新路线内容；停止并转成下一步计划，不混入当前 closeout。 |

## 输出要求

- 中间更新要说明当前处于哪个阶段：实现第一版、等待人工验收、验收后 closeout、提交前验证。
- 最终交接要分开写自动验证、人工验收、文档同步和提交结果。
- 如果完整 validation 被推迟，要说明原因和后续触发点。
- 如果修了 side issue，要说明为什么它阻塞当前任务；否则列为未纳入 scope。
- 如果发现 source 冲突，要写清采用哪个 owner 文件、哪些文档需要后续同步、哪些历史证据只作为参考。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
