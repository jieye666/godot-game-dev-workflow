# 玩法实现计划模板

改 gameplay code 或 scene 前写计划。小修使用 Compact Patch Plan；涉及 `.tscn`、signals、resources、InputMap、Autoload、多个 subsystem 或 shared ownership 时升级 Task Plan。

## Compact Patch Plan

用于 one-file fix、tuning、小 bug、docs sync。

```text
Goal:
Current evidence:
Reference research:
Owned files:
Prohibited files:
Risk:
Verification:
Manual check:
Doc sync:
Readiness:
```

`Readiness` 只能是 `ready`，否则不要进入实现；缺字段就先补计划。

## Task Plan

用于 gameplay slice、scene/script contract、visible runtime behavior。

```text
Task ID:
User intent:
Non-goals:
Requirement/design source:
Current evidence:
Reference research:
  - Sources checked:
  - Adopted patterns:
  - Rejected patterns:
  - Local mapping:
  - Open questions:
Owned files:
Prohibited files:
System owner:
Related systems:
Extension points:
Scene tree changes:
Script plan:
Signals:
Resources/scenes:
InputMap:
Autoload decision:
Verification:
Manual acceptance:
  - Scene path:
  - Start state:
  - Exact controls / actions:
  - Visible expected results:
  - Save/load steps if relevant:
  - Failure feedback to report:
Doc sync targets:
Implementation Readiness:
```

## Readiness Quick Check

- `pending`：目标、owned files、evidence、verification、manual acceptance 有缺口。
- `ready`：scope 可执行，文件边界清楚，验证路径可运行，manual gap 已记录；玩家可见系统已有 `Reference research` 或明确免除理由。
- `escalated`：需要用户接受 non-owned files、架构取舍、验证不可用或 manual-only 验收。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
