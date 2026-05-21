---
name: godot-game-dev-workflow
description: Use when Codex needs the Godot game workflow for project intake, docs routing, gameplay planning, implementation contracts, validation, closeout, MCP/editor boundaries, external reference intake, or Chinese-first project documentation. 用于 Godot 项目管理、中文文档规范、玩法计划、验证收尾、MCP/editor 协作和交接。
---

# Godot Game Dev Workflow

## 概览

把本 skill 当作 Godot 项目管理、gameplay 开发、验证和交接的操作流程。目标是让 AI agent 通过权威文档、最小上下文、implementation contracts、系统边界、MCP/editor 协作规则、high-quality gameplay code standards 和验证流程稳定推进项目。

核心规则：先检查真实项目状态，用项目 `docs/INDEX.md` 找权威上下文；正式计划前由 agent 自行选择快速档 / 标准档 / 严格档并记录理由，高风险、范围不清或需要人工取舍时才询问用户；计划 Boss、movement feel、camera/readability、route pacing、UI flow 等玩家可见设计或主观体验时，先联网查找同类成功游戏或开源实现的设计/技术参考；本地 bug、save/load、验证脚本和代码事实审查可写明 `Reference research: not needed`；按档位选择 Patch Plan / Task Plan / Milestone Plan；改代码前确认系统关系和扩展点；验证后同步文档和历史。

低 token 不是少读关键文件，而是用 hot context、routed references、current code、closeout docs 避免重复发现。不要因为低上下文而跳过 scene tree、script pseudocode、signal contract、resource dependency、InputMap、Autoload、ownership 或 verification requirement。

默认推荐 2DA-style indexed docs：每类文档一个目录和一个 `INDEX.md` 路由，active GDD 放 `docs/plans/gdd/`，completed / abandoned GDD 的唯一详细文件放 `docs/history/gdd/`，每次提交批次写入 `docs/history/commits/`。新 Godot 项目没有文档规范时建议初始化这套结构；已有项目规范时先按项目 docs。组织效率审查要同时看 active docs 是否吸收历史，以及主场景脚本、scene、smoke test 是否成为 owner 不清的大文件。

`SKILL.md` 是路由器，详细规则放在 `references/`。新增或更新文档、docs sync、commit message 和面向人查看的说明默认中文；路径、命令、API、Godot 标识符、GDD 编号、文件名和专有名词保持英文。

用户可主动调用 `/godot-workflow` 总代理和 5 个明确子命令；命令表面、安装规则和旧 wrapper 清理策略见 `references/slash-command-surface.md`。AI 内部仍通过 canonical references 细分调度，不暴露更多 slash wrapper。

## AI Failure Prevention Gate

- 写代码前先说明 assumption、scope、success criteria；不确定时读 source 或 reference，不用模型猜。
- 简单优先：最少可行改动，不为未来灵活性新增未用抽象。
- 外科手术式修改：只改 owned files；side issue 先分类，非阻塞问题不混入当前任务。
- 确定性任务交给脚本或命令：routing、error scan、doc audit、scene reference check、Git status/diff、validation output scan 不靠模型记忆判断。
- 冲突必须暴露：docs、source、archive、reference 不一致时，列出冲突、选择的 source of truth 和需要同步的文件，不折中混合。
- 测试验证意图：验证项要对应 user intent、visible runtime route 和 failure feedback，不能只证明函数被调用。
- 失败大声报告：Godot output、manual acceptance、MCP/editor 证据和未执行项分开写，不声称未发生的通过。

## 计划档位

- 快速档：小 bug、小参数、小文案、one-file fix。只读入口文档和相关文件；给 3-5 行 Patch Plan；跑窄验证或相关 smoke。
- 标准档：单个 GDD gameplay slice 或有限 scene/script change。读 `STATUS`、`NEXT-STEPS`、相关 plan、真实 scene/script；写 Task Plan；执行后同步必要 docs。
- 严格档：跨系统、多 agent、架构变更、提交前收尾或高风险修复。写完整 contract、ownership、验证计划、docs/history closeout；收尾跑完整 validation。
- 正式计划前由 agent 选择 selected tier，记录 reason、主要风险和不用更轻/更重档位的 tradeoff。只有 scope 不清、高风险、需要人工取舍或 `escalated` 时才询问用户。

## 任务分流与收尾原则

- 默认先判断任务类型，再走最小必要流程；one-file patch 不加载大计划、完整 history 或 closeout references。
- 客观且自动验证可证明的修复可由 agent 完成 docs sync / commit；主观体验、UI、路线可读性、Boss pacing、movement feel 等必须等待 manual acceptance。
- 玩家可见高风险设计按风险触发 `web-gameplay-reference-research.md`；小型可见修复可写 `Reference research: not needed` 和具体理由。
- 自动提交细节归 `session-closeout-sync.md`；执行节奏、暂停点和 docs rhythm 归 `agent-execution-discipline.md`。

## 不适用 / 边界

- 不把本 skill 当最终美术、音频、动画生产流程；相关方向先写入项目文档，除非用户明确要求实现资产。
- 不把自动化检查当作 movement feel、camera readability、route clarity、Boss pacing 或 fun 的验收；这些需要 editor/user manual playtest。
- 确认为 Godot 后，不再走旧 Unity 假设；先找 `project.godot`。Do not infer the engine from parent folder names。
- 不改无关系统，不 broad-refactor，不清理其他 agent 或用户改动，除非任务范围明确包含。
- multi-agent 计划不能绕过 owned-file boundaries；需要 non-owned file 时停止并报告。
- 不把低 token 路由当作跳过 docs/source evidence 的理由。
- 不照搬外部 AI 方法论；只把有用部分转成 Godot-specific checks、scripts、templates 或 references。
- 不把 MCP/editor 输出当作唯一真相；它可以辅助确认版本、项目信息和运行输出，但不能替代 `.tscn`、`.gd`、项目 docs 或人工验收。

## 工作流

1. 先找 `project.godot`，确认真实项目根。Do not infer the engine from parent folder names。
2. 判断 task shape：bug fix、player-visible polish、system slice、docs closeout、skill maintenance、side issue。
3. 按 task shape 和档位只加载 focused references；不要默认读完整 `references/`、history 或 reference project。
4. 改文件前写相应深度计划：Compact Patch Plan、Task Plan 或 Milestone Plan。
5. 使用 node path、signal、resource、InputMap、Autoload 前读真实 `.tscn` 和 `.gd`。
6. 玩家可见高风险设计先做 reference research；纯本地 bug / docs / validation 修复可写免除理由。
7. 自动验证和 manual playtest 分开报告；Godot output error scan 不能只看 exit code。
8. behavior、docs、plans、verification evidence 变化后按 closeout policy 同步 designated docs。
9. 客观修复按自动验证和项目 policy 收尾；主观体验先给 manual acceptance pack，用户确认后再 docs/history/archive/commit。

## Task Routing

| 任务类型 | 加载内容 | 意图 |
| --- | --- | --- |
| 已有项目进入 | quick context / identity、`docs/INDEX.md`、status、next steps | 识别身份和当前状态 |
| 文档路由/清理 | `references/project-doc-workflow.md` | 确认 source of truth，避免重复事实 |
| 组织效率审查 | `references/project-organization-health.md` | 检查 current/plans 是否吸历史、主场景脚本和 smoke 是否过大 |
| 新项目 docs / low-token handoff | `references/game-project-doc-structure.md`、`references/context-memory-strategy.md` | 建立 AI-readable docs 和 context tiers |
| gameplay 计划 | `references/gameplay-implementation-plan-template.md`，必要时 `references/implementation-contracts.md` | 写可执行 contract |
| 玩家可见玩法/关卡/Boss/UI flow 计划 | `references/web-gameplay-reference-research.md` | 联网查同类成功例子，提炼可本地化的 design / implementation pattern |
| 执行纪律 / 流程复盘 / 减少返工 | `references/agent-execution-discipline.md` | 区分 task shape、最小闭环、暂停点、验证节奏和文档时机 |
| scene/signal/resource/node path | `references/scene-signal-resource-checklist.md` | 防 node path、signal、resource 误判 |
| GDScript 编写/审查 | `references/godot-4-gdscript-rules.md` | 保持 Godot 4 兼容 |
| MCP/editor 协作 | `references/mcp-and-editor-workflow.md` | 区分 tool evidence、file evidence 和 manual acceptance |
| 会影响代码形态的计划 | 需要时加载 `references/godot-4-gdscript-rules.md` | 计划阶段就避开 API/script 约束错误 |
| 可复用系统/架构风险 | `references/extensible-gameplay-architecture.md` | 保留 ownership 和 extension points |
| reference-backed feature planning | 项目 `docs/reference/INDEX.md`，再读 selected reference files | 不扫描完整参考项目 |
| vague/large/milestone/multi-session | `references/large-project-planning.md`、`references/planning-readiness-and-traceability.md`，需求不稳时加 `references/spec-driven-gameplay-workflow.md` | 拆 scope，避免 premature implementation |
| 已有 plan 准备实现 | `references/planning-readiness-and-traceability.md`，再读任务 checklist | 确认 readiness 和 allowed scope |
| multi-agent | `references/multi-agent-gameplay-plan.md` | 只在边界能减少冲突时并行 |
| 行为没变或验证失败 | `references/common-failure-modes.md` | 修 visible runtime path；current behavior did not change |
| 完成前 | `references/validation-and-playtest.md`、`references/session-closeout-sync.md` | 验证、manual playtest、文档收尾 |
| 维护本 skill | `references/skill-quality-gate.md`、`references/external-repositories.md`，运行 `scripts/skill_self_check.py <skill-root>` | 保持 concise、可验证、来源可追踪 |
| 安装主动调用小技能 | `references/slash-command-surface.md`、`assets/slash-skill-wrappers/manifest.json`、`scripts/install_slash_skills.py` | 生成 `/godot-workflow` + 5 个用户子命令；AI 内部细分仍引用 canonical references |

## 质量门路由

- 执行纪律、暂停点、scope creep、docs rhythm：读 `agent-execution-discipline.md`。
- Scene tree、signal、resource、InputMap、Autoload、ownership：读 `implementation-contracts.md` 和 `scene-signal-resource-checklist.md`。
- 验证分层、Godot output scan、manual acceptance：读 `validation-and-playtest.md`。
- 行为没变或验证失败：读 `common-failure-modes.md`，检查 played scene、attached script、main route、resource instance。
- 本 skill 维护和发布前 gate：读 `skill-quality-gate.md` 并运行 `scripts/skill_self_check.py <skill-root>`。

## 上下文预算规则

- 始终先找 `project.godot`。
- 如果会从 workspace parent 操作子项目，先切到子项目根或在所有 patch/file paths 中显式带子项目目录；不要混用父目录相对路径和项目根相对路径。
- 有 quick context / identity 时先读它，再读 `docs/INDEX.md`；随后只读 index 指向的 current/status/next-step files。
- `docs/INDEX.md` 是 router；不要默认加载全部 docs、全部 plans 或 full history。
- 按档位控制读取深度：快速档不读完整 history；标准档只读相关 plan/source；严格档才加载完整 contract、history 和 closeout references。
- 如果需要越过当前档位读取 archive、full history、完整 reference project 或大量工具输出，先说明原因、预期收益和如何避免污染当前上下文。
- 不在已有 accepted active plan 时重写计划；先读它，再补必要 risk / verification notes。
- 不默认扫描完整 reference projects；先读项目 `docs/reference/INDEX.md`，再读 selected files。没有本地参考或本地参考不足时，对玩家可见计划联网查找同类游戏/开源实现。
- identity facts 放在项目指定 source of truth；其他文档链接过去。
- 需要降低 token 成本时，使用 `context-memory-strategy.md` 的 hot/warm/cold layering。
- archived plans 和 history 是证据，不是当前真相；行动前要与当前文件核对。
- final handoff 要列出 key project docs and reference files used。
- quick context、`docs/INDEX.md` 和 `NEXT-STEPS.md` 不堆 completed GDD 长历史；历史通过 `docs/history/gdd/INDEX.md` 和按提交拆分的 `docs/history/commits/` 路由。completed / abandoned GDD 不同时保存在 `docs/plans/archive/` 和 `docs/history/gdd/`。
- `STATUS.md`、`PROJECT-SNAPSHOT.md` 和 roadmap 不堆完成时间线；大型 `main_game.gd`、`Main.tscn` 或 smoke test 先作为组织健康 warning，触碰相关 owner 时再按 route / assertion family 拆。
- 用户说行为没变时，默认 visible runtime path 仍错；检查 played scene、script attachment、input mapping、signal route、resource instance。

## Two-Stage Records

- Planning stage：记录 user intent、confirmed decisions、solution tradeoffs、current executable plan、rough next direction。当前计划和未来方向分开。
- Implementation / acceptance stage：记录改动文件、自动验证、手动测试步骤、用户验收结果和后续失败反馈。
- 两个阶段可能由不同 agent 或不同 conversation 完成；保留足够 routing/evidence，避免把完整历史复制进 active docs。

## Reference Loading

按需加载 references，不默认读完整目录；具体 owner 和读法以 `references/index.md` 为准。

- 计划与执行：大任务读 `large-project-planning.md`、`planning-readiness-and-traceability.md`；实现、player-visible polish、docs closeout 或提交前读 `agent-execution-discipline.md`。
- Gameplay contract：task plan 读 `gameplay-implementation-plan-template.md`；玩家可见设计读 `web-gameplay-reference-research.md`；scene/script/signal/resource/API 风险读 `implementation-contracts.md`、`scene-signal-resource-checklist.md`、`godot-4-gdscript-rules.md`。
- 项目文档与协作：docs/layout/context/MCP/multi-agent 分别读 `project-doc-workflow.md`、`game-project-doc-structure.md`、`context-memory-strategy.md`、`mcp-and-editor-workflow.md`、`multi-agent-gameplay-plan.md`。
- 组织效率：审查 docs/current/plans、主场景脚本、scene 或 smoke test 体量时读 `project-organization-health.md`。
- 验证、失败与维护：完成前读 `validation-and-playtest.md`、`session-closeout-sync.md`；行为没变读 `common-failure-modes.md`；维护本 skill 读 `skill-quality-gate.md`、`external-repositories.md`；调整 slash 命令表面时读 `slash-command-surface.md`。

## Examples

### Small Gameplay Bug Fix

Input: "敌人碰到玩家应该造成 1 点伤害，而不是直接杀死玩家。"

Steps: 定位项目根；agent 选择快速档并记录理由；读 quick context / index 和相关 player/enemy/damage/health/respawn scripts/scenes；写 Compact Patch Plan；窄改；运行 parser/headless/tests；行为变化时同步 docs/history。

Expected output: changed files 限定在 damage/health path；final handoff 分开 automated checks 和 manual playtest needs。

### Large Feature Plan

Input: "分几个会话加入 checkpoint、hazard、HUD 和关卡目标改进。"

Steps: agent 选择严格档并记录理由；加载 execution discipline、large planning、readiness、architecture references；更新 requirements/design/task breakdown/verification plan/progress log；把 requirements/design 映射到 tasks，标记 `pending` / `ready` / `escalated`；只在 selected task ready 后实现。

Expected output: plan 含 task IDs、system ownership、verification gates、explicit gaps；不从 `pending` 计划直接实现。

### Reference-Backed Gameplay Plan

Input: "设计 Boss 二阶段和奖励路线。"

Steps: 推荐标准档或严格档；联网查 2-4 个相近 2D action/platformer 的 Boss phase、telegraph、reward pacing 或 debug-route 实现；记录 source、reference pattern、local mapping、rejected idea；再写 Task Plan / Milestone Plan。

Expected output: plan 说明借鉴了哪些成功例子、哪些不适合本项目、会落到哪些 scene/script/resource、如何自动验证和人工验收；不能只靠 agent 直觉写 Boss 方案。

### User Says Behavior Did Not Change

Input: "I tested it; the current state did not change."

Steps: 加载 common failures；检查 played scene、attached scripts、InputMap、signals、resource instances、main scene route；必要时更新 plan；修 visible runtime path；重新验证并给 manual retest steps。

Expected output: final report 说清实际改到的 runtime path；不能把 test-only change 当 gameplay fix。

## Optional Scripts

- `scripts/scan_godot_project.py <project-or-parent-dir>`
- `scripts/check_scene_references.py <godot-project-root>`
- `scripts/audit_godot_docs.py <godot-project-root>`
- `scripts/audit_doc_language.py <paths...>`
- `scripts/init_godot_ai_docs.py <godot-project-root> [--dry-run|--check]`
- `scripts/install_slash_skills.py [--dry-run|--check|--target <skills-dir>]`
- `scripts/skill_self_check.py <skill-root>`

script output 是 advisory；改动前仍要直接检查相关 scene 和 script。涉及安装或清理的脚本先运行 `--dry-run` 或 `--check`，确认 target 在预期 skills/project 目录内后再执行写入或清理。

## Completion Criteria

完成前说明 agent selected tier、changed files、automated checks、system boundaries、extension points、manual steps 或 user acceptance、docs sync、working basis、next recommended task。不要声称未实际发生的 editor/MCP/manual acceptance。

large task 要说明 task ID 或 planning artifact；manual validation 通过后，把 docs/history 更新放在同一执行单元。commit 只在用户要求或项目 policy 要求时做。

无需人工审查的 bug 修复属于自动提交场景：如果自动验证能证明修复结果，收尾后直接 commit；如果涉及 player-facing feel/readability/pacing 或 manual-only 验收，先给用户手动验收步骤，不提前提交。

## Maintenance

- Sources: 当前 Godot 项目实践、用户确认的 workflow、bundled references、Godot 4 constraints、MCP/editor 协作经验、经筛选的外部 AI workflow material。
- Last updated: 2026-05-21。
- Known limits: helper scripts 不能证明 gameplay feel；manual playtest 仍负责 player-facing feel、readability、pacing、route acceptance。
- Upgrade rule: 优先加小 reference、script、template，不拉长 `SKILL.md`；重大变更后运行 `scripts/skill_self_check.py <skill-root>` 和平台 validator。
