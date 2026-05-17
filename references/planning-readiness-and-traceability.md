# 计划就绪度与追踪

Readiness states：pending、ready、escalated。每个 task 必须能追溯到 requirement、design item、GDD ID 或 user-accepted scope。

## 什么时候读

- vague / large / milestone / multi-session work。
- 已有 plan 准备进入 implementation。
- 用户要求多 agent、任务拆分、先计划、按计划执行。
- 自动验证缺口、manual playtest 缺口会影响能否开始实现。

## 档位选择记录

正式计划前记录档位选择，避免小任务过度计划或大任务验证不足。

- Recommended tier：agent 推荐的 `快速档` / `标准档` / `严格档`。
- Reason：推荐理由，至少覆盖 scope、风险、验证成本和是否涉及 gameplay-visible behavior。
- Selected tier：用户确认的档位；如果用户已明确指定档位，记录该选择并跳过重复询问。
- Tier tradeoff：一句话说明为什么不用更轻或更重的档位。

## Readiness 判定

- `pending`：目标、owned files、依赖、验证、manual acceptance 任一关键项缺失。只能补计划、查证据、拆任务，不直接改 gameplay code。
- `ready`：需求来源明确，当前代码和 docs 已核对，owned/prohibited files 明确，验证方式可执行，manual gap 已记录且不阻塞实现。
- `escalated`：范围或风险需要用户接受，例如必须改 non-owned files、架构取舍会影响后续、缺少可运行验证、manual acceptance 是唯一验收。用户接受后才能执行。

## Traceability 最小字段

- Task ID 或短名。
- Requirement/design source：用户原话、GDD、active plan、bug report 或 reference file。
- Current evidence：读过的 docs、scene、script、test 或 log。
- Tier：recommended tier、selected tier、reason。
- Owned files / prohibited files。
- Verification：自动命令、Godot scene、log scan、manual playtest。
- Status：`pending` / `ready` / `escalated`。

## Coverage 检查

- 每个 requirement 至少有一个 task 或明确 non-goal。
- 每个 task 至少指向一个 requirement/design source。
- 每个 gameplay-visible change 必须有 manual acceptance 步骤，除非任务明确是 docs/script/tooling。
- 每个 verification gap 必须写成风险，不用“后续再看”代替。

## 执行规则

- `pending` task：只能继续调查、补 plan、缩小 scope。
- `ready` task：按 owned files 实现。
- `escalated` task：先报告原因、影响、建议选项，等用户接受。
- 如果实现中发现 plan 错误，暂停并更新 readiness，不强行继续。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
