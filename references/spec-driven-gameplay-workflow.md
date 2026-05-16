# 规格驱动玩法流程

模糊、跨系统或多会话请求先拆为 Requirement、Design、Plan、Task 四层，避免 task plan 同时承担需求澄清、方案设计和执行细节。

## 四层职责

- Requirement：玩家目标、用户意图、成功标准、in/out of scope、人工验收口径。
- Design：系统关系、场景流、输入/输出、UI/feedback、风险和 tradeoff。
- Plan：拆出 milestone、task list、owned files、verification strategy 和 docs sync targets。
- Task：可执行 slice，必须有 Implementation Readiness、allowed files、manual check。

## 最小字段

Requirement：
- Goal
- Success criteria
- Audience / player-facing result
- Out of scope

Design：
- Systems touched
- Runtime route / scene route
- Data or resource contract
- Manual playtest expectation

Plan：
- Task ID
- Dependencies
- Verification gates
- Docs sync targets

Task：
- Owned files / prohibited files
- Implementation Readiness：`pending` / `ready` / `escalated`
- Automated checks
- Manual check

## Readiness 输出格式

只允许 `ready` task 进入实现：

```text
Task ID:
Status: pending | ready | escalated
Why:
Owned files:
Blocked by:
Automated checks:
Manual check:
Docs sync:
```

`pending` 说明缺少需求、文件证据或验证路径；`escalated` 说明需要用户接受 tradeoff、scope change 或 non-owned file；`ready` 说明实现者不需要再做产品决策。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
