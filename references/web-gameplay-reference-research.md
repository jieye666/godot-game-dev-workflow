# 联网玩法参考调研

正式制定玩家可见 gameplay、关卡、Boss、UI flow、camera、combat、movement、save/load、unlock、checkpoint、collectible 或 route plan 前使用。目标是先看同类成功游戏和可靠开源实现怎么解决相同问题，再把可复刻部分转成本项目的计划约束。

## 触发条件

- 用户要求制定新玩法、新关卡、新 Boss、系统路线、UI flow、存档/解锁、移动能力、战斗反馈或 camera 方案。
- 计划会影响玩家体验、节奏、可读性、路线理解、操作手感或可见 progression。
- 当前项目 `docs/reference/INDEX.md` 没有足够例子，或本地 reference 只能覆盖代码结构，不能覆盖玩法设计取舍。

可免除的情况：

- 纯本地 bug、parser/test/smoke 修复、文档清理、路径引用错误、已有 accepted plan 的小补丁。
- 用户明确要求不要联网或只按指定本地参考执行。

免除时在计划里写：`Reference research: not needed`，并给一句具体理由。

## 调研步骤

1. 先定义当前问题：玩法类型、玩家目标、失败反馈、可见状态、系统约束和 Godot 落点。
2. 优先查 2-4 个对应游戏部分的成功例子；可以包含设计拆解、官方/开发者访谈、wiki 中的机制说明、开源 Godot/Unity 实现、postmortem 或高质量教程。
3. 每个来源只提炼可验证的机制，不复制大段文字。记录 source、feature、reference pattern、why it works、risk if copied blindly。
4. 把参考转成本地计划字段：scope、non-goals、scene/script/resource 落点、tuning variables、telegraph / feedback、validation、manual acceptance。
5. 如果参考之间冲突，选择最符合本项目当前 milestone 的最小可验证版本，并把更重方案列为 rejected / later。

## 搜索建议

- 查询组合：`<feature> <genre> game design`、`<feature> Godot implementation`、`<known game> <mechanic> breakdown`、`boss phase telegraph 2D platformer`、`checkpoint save unlock metroidvania implementation`。
- 优先来源：官方资料、开源仓库、Godot docs/demo、开发者 blog、GDC/技术文章、机制 wiki。普通论坛/视频评论只能当灵感，不能当事实来源。
- 搜不到完全一致例子时，选择同一玩家问题的近邻机制，例如 Boss 二阶段可参考 telegraph / escalation / reward pacing，而不强求同题材。

## 计划输出字段

在 Compact Patch Plan 或 Task Plan 中加入：

```text
Reference research:
  - Sources checked:
  - Adopted patterns:
  - Rejected patterns:
  - Local mapping:
  - Open questions:
```

标准档至少列 2 个来源或本地参考文件；严格档至少列 3 个来源，并说明为什么没有采用更复杂方案。快速档如果涉及玩家可见体验，也至少查 1 个针对性来源或说明免除理由。

## 本地化规则

- 参考是 blueprint，不是 source of truth；最终计划服从本项目 scene tree、InputMap、Autoload、资源命名、docs policy 和当前 milestone。
- 不为了模仿成功游戏而扩大 scope；先实现可验证的白盒版本，再把 polish、动画、音频、正式美术列入 later。
- 不把“某游戏这么做”当作充分理由；必须写清它解决的玩家问题，以及本项目如何验证同样问题被解决。
- 涉及 Boss、movement feel、route readability、camera 或 UI flow 时，manual acceptance 必须覆盖参考机制的可见结果。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、URL、游戏名、Godot API、类名、函数名、signal、InputMap action 保持英文。
