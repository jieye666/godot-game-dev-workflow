---
name: godot-game-dev-workflow
description: Use when managing, initializing, planning, auditing, implementing, validating, or documenting Godot game projects with AI-readable project management, high-quality gameplay code standards, low-token context routing, authoritative docs, Chinese-first documentation, task breakdowns, readiness gates, implementation contracts, scene/script/signal/resource discipline, MCP/editor collaboration rules, architecture decisions, external reference intake, single-source documentation cleanup, session closeout sync, multi-agent plans, or playtest-driven fixes in existing or newly created Godot game projects. 用于 Godot 项目管理、中文文档规范、玩法开发、计划、审计、验证、MCP/editor 协作和交接。
---

# Godot Game Dev Workflow

## 概览

把本 skill 当作 Godot 项目管理、gameplay 开发、验证和交接的操作流程。目标是让 AI agent 通过权威文档、最小上下文、implementation contracts、系统边界、MCP/editor 协作规则和验证流程稳定推进项目。

核心规则：先检查真实项目状态，用项目 `docs/INDEX.md` 找权威上下文；正式计划前给出快速档 / 标准档 / 严格档的推荐和理由，由用户确认档位；按档位选择 Patch Plan / Task Plan / Milestone Plan；改代码前确认系统关系和扩展点；验证后同步文档和历史。

低 token 不是少读关键文件，而是用 hot context、routed references、current code、closeout docs 避免重复发现。不要因为低上下文而跳过 scene tree、script pseudocode、signal contract、resource dependency、InputMap、Autoload、ownership 或 verification requirement。

`SKILL.md` 是路由器，详细规则放在 `references/`。新增或更新文档、docs sync、commit message 和面向人查看的说明默认中文；路径、命令、API、Godot 标识符、GDD 编号、文件名和专有名词保持英文。

## 计划档位

- 快速档：小 bug、小参数、小文案、one-file fix。只读入口文档和相关文件；给 3-5 行 Patch Plan；跑窄验证或相关 smoke。
- 标准档：单个 GDD gameplay slice 或有限 scene/script change。读 `STATUS`、`NEXT-STEPS`、相关 plan、真实 scene/script；写 Task Plan；执行后同步必要 docs。
- 严格档：跨系统、多 agent、架构变更、提交前收尾或高风险修复。写完整 contract、ownership、验证计划、docs/history closeout；收尾跑完整 validation。
- 正式计划前先给 recommended tier、reason 和主要风险；用户确认 selected tier 后再写对应深度计划。用户已明确指定档位时，不重复询问，只记录选择并执行。

## 自动提交规则

- 用户已授权提交、项目 policy 要求提交，或 bug 修复可由自动验证充分证明且不需要人工审查时，完成验证和必要 docs sync 后直接 commit。
- 不需要人工审查的 bug 修复：parser/test/smoke 失败、路径/引用错误、明确 runtime error、文档审计失败、验证脚本问题、非主观数值或代码缺陷，且有自动验证能覆盖修复结果。
- 仍需等待人工验收：movement feel、Boss pacing、route readability、camera/UI 观感、玩法节奏、manual-only behavior，或用户明确要求先不要提交。
- 直接提交前仍要检查 `git status` 和 diff，只加入本任务 owned files；提交后报告 commit id、验证命令和未执行的 manual acceptance。

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

1. 找到 `project.godot`，确认 Godot 项目根。
2. 需要 MCP/editor 时加载 `mcp-and-editor-workflow.md`，先把 tool evidence 和 file evidence 分开。
3. 正式计划前判断档位并给推荐理由；用户确认后再进入对应 plan depth。
4. 判断 plan depth：Patch Plan 用于快速档；Task Plan 用于标准档 gameplay slice 或 scene/script change；Milestone Plan 用于严格档 vague/multi-system/multi-agent/multi-session work。
5. 大任务先更新 planning artifacts：brief、requirements、design、task breakdown、verification plan、progress log；加载 `large-project-planning.md` 和 `planning-readiness-and-traceability.md`。
6. gameplay system 或大功能要加载 `extensible-gameplay-architecture.md`，先做 architecture check。
7. documented project 先读 quick context / identity，再读 `docs/INDEX.md`，然后读 index 指向的 status 和 next-step files。docs 冲突时更新 designated source of truth，不新增重复事实。
8. 改文件前写相应深度计划。Patch Plan 保持紧凑：goal、owned files、current evidence、risk、verification、manual acceptance。Task Plan 涉及 scenes/scripts/signals/resources/InputMap/Autoload/ownership 时必须写完整 contract。
9. 使用 node path 前检查真实 `.tscn` 和 `.gd`；不要猜 node name 或 signal connection。
10. planned work 只有 traceable 且 Implementation Readiness 为 `ready` 时执行；`escalated` 需要用户接受。
11. implementation agent 可以补 risk notes 和 verification checks，但不能推翻已接受 scope；计划明显错误时暂停报告。
12. 自动验证和 manual playtest 分开报告；Godot executable 先读项目 quick context / 验证脚本 / `GODOT_EXE`，不要猜系统路径。
13. manual acceptance 需要给 scene、action、expected result、failure feedback。
14. behavior、nodes、signals、resources、tuning、task status、architecture decision 或 verification evidence 变化后，同步项目 docs。
15. 完成 implementation、doc cleanup 或 milestone handoff 后，按 `session-closeout-sync.md` 收尾。用户手动验收通过时，docs sync 属于同一执行单元；无需人工审查的 bug 修复在验证和必要 docs sync 后直接 commit。

## Task Routing

| 任务类型 | 加载内容 | 意图 |
| --- | --- | --- |
| 已有项目进入 | quick context / identity、`docs/INDEX.md`、status、next steps | 识别身份和当前状态 |
| 文档路由/清理 | `references/project-doc-workflow.md` | 确认 source of truth，避免重复事实 |
| 新项目 docs / low-token handoff | `references/game-project-doc-structure.md`、`references/context-memory-strategy.md` | 建立 AI-readable docs 和 context tiers |
| gameplay 计划 | `references/gameplay-implementation-plan-template.md`，必要时 `references/implementation-contracts.md` | 写可执行 contract |
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

## 强制质量门

| 场景 | 必须确认 | 不允许 |
| --- | --- | --- |
| 正式计划前 | 推荐档位、理由、用户确认的 selected tier | 未确认档位就写过重或过轻的计划 |
| 改 gameplay code | task 可追踪且 readiness 为 `ready`；必要时加载 `implementation-contracts.md` | 从 `pending` 计划直接实现 |
| 改 `.tscn` / signal / resource | 读真实 scene/script；加载 `scene-signal-resource-checklist.md` | 猜 node path、signal、resource 实例 |
| 大功能或可复用系统 | 写 architecture check；加载 `extensible-gameplay-architecture.md` | 为首版方便牺牲明显扩展点 |
| 验证通过但行为没变 | 检查 played scene、attached script、main route、resource instance | 只补测试，不修 visible runtime path |
| 引入外部参考 | 先读 manifest / selected files；转成 Godot-specific gate | 复制大段外部 theory 或不明来源规则 |
| 完成前 | 扫描 Godot 输出错误文本；同步必要 docs/history | 只看 exit code 或声称未做的 manual acceptance |

## 上下文预算规则

- 始终先找 `project.godot`。
- 有 quick context / identity 时先读它，再读 `docs/INDEX.md`；随后只读 index 指向的 current/status/next-step files。
- `docs/INDEX.md` 是 router；不要默认加载全部 docs、全部 plans 或 full history。
- 按档位控制读取深度：快速档不读完整 history；标准档只读相关 plan/source；严格档才加载完整 contract、history 和 closeout references。
- 不在已有 accepted active plan 时重写计划；先读它，再补必要 risk / verification notes。
- 不默认扫描完整 reference projects；先读项目 `docs/reference/INDEX.md`，再读 selected files。
- identity facts 放在项目指定 source of truth；其他文档链接过去。
- 需要降低 token 成本时，使用 `context-memory-strategy.md` 的 hot/warm/cold layering。
- archived plans 和 history 是证据，不是当前真相；行动前要与当前文件核对。
- final handoff 要列出 key project docs and reference files used。
- 用户说行为没变时，默认 visible runtime path 仍错；检查 played scene、script attachment、input mapping、signal route、resource instance。

## Two-Stage Records

- Planning stage：记录 user intent、confirmed decisions、solution tradeoffs、current executable plan、rough next direction。当前计划和未来方向分开。
- Implementation / acceptance stage：记录改动文件、自动验证、手动测试步骤、用户验收结果和后续失败反馈。
- 两个阶段可能由不同 agent 或不同 conversation 完成；保留足够 routing/evidence，避免把完整历史复制进 active docs。

## Reference Loading

按需加载 references，不默认读完整目录：

- `references/large-project-planning.md`：大功能、原型、里程碑、多会话、任务拆分。
- `references/planning-readiness-and-traceability.md`：从 plan 实现前、审批大计划、拆 task、判断 verification gaps。
- `references/gameplay-implementation-plan-template.md`：写 gameplay task plan 的结构。
- `references/implementation-contracts.md`：scene tree、scripts、signals、resources、InputMap、Autoload、ownership 字段标准。
- `references/extensible-gameplay-architecture.md`：可复用系统、大功能、第二变体风险、coupling risk。
- `references/project-doc-workflow.md`：进入 documented project、降低交接 token、判断权威 docs。
- `references/mcp-and-editor-workflow.md`：MCP/editor 的使用边界、证据分层、报告规则。
- `references/context-memory-strategy.md`：面向 AI 的记忆分层、hot/warm/cold context、参考项目 intake。
- `references/session-closeout-sync.md`：implementation closeout、user acceptance closeout、milestone handoff。
- `references/spec-driven-gameplay-workflow.md`：需求/spec/plan/task 分层。
- `references/game-project-doc-structure.md`：Godot 项目 docs layout 审计或初始化。
- `references/multi-agent-gameplay-plan.md`：严格 owned-file boundaries 的并行计划。
- `references/godot-4-gdscript-rules.md`：写或审查 GDScript。
- `references/scene-signal-resource-checklist.md`：scene edits、node rename、signal/resource changes。
- `references/validation-and-playtest.md`：完成前验证和 handoff。
- `references/common-failure-modes.md`：debug、验证失败、runtime behavior 未变化。
- `references/skill-quality-gate.md`：维护本 skill、添加 reference/script、筛选外部 AI workflow idea。
- `references/external-repositories.md`：追踪塑造本 workflow 的外部参考源和 refresh rules。
- `references/index.md`：维护 skill 或判断新增内容归属时的地图。

## Examples

### Small Gameplay Bug Fix

Input: "敌人碰到玩家应该造成 1 点伤害，而不是直接杀死玩家。"

Steps: 定位项目根；推荐快速档并等用户确认；读 quick context / index 和相关 player/enemy/damage/health/respawn scripts/scenes；写 Compact Patch Plan；窄改；运行 parser/headless/tests；行为变化时同步 docs/history。

Expected output: changed files 限定在 damage/health path；final handoff 分开 automated checks 和 manual playtest needs。

### Large Feature Plan

Input: "分几个会话加入 checkpoint、hazard、HUD 和关卡目标改进。"

Steps: 推荐严格档并等用户确认；加载 large planning、readiness、architecture references；更新 requirements/design/task breakdown/verification plan/progress log；把 requirements/design 映射到 tasks，标记 `pending` / `ready` / `escalated`；只在 selected task ready 后实现。

Expected output: plan 含 task IDs、system ownership、verification gates、explicit gaps；不从 `pending` 计划直接实现。

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
- `scripts/skill_self_check.py <skill-root>`

script output 是 advisory；改动前仍要直接检查相关 scene 和 script。

## Completion Criteria

完成前说明 selected tier、changed files、automated checks、system boundaries、extension points、manual steps 或 user acceptance、docs sync、working basis、next recommended task。不要声称未实际发生的 editor/MCP/manual acceptance。

large task 要说明 task ID 或 planning artifact；manual validation 通过后，把 docs/history 更新放在同一执行单元。commit 只在用户要求或项目 policy 要求时做。

无需人工审查的 bug 修复属于自动提交场景：如果自动验证能证明修复结果，收尾后直接 commit；如果涉及 player-facing feel/readability/pacing 或 manual-only 验收，先给用户手动验收步骤，不提前提交。

## Maintenance

- Sources: 当前 Godot 项目实践、用户确认的 workflow、bundled references、Godot 4 constraints、MCP/editor 协作经验、经筛选的外部 AI workflow material。
- Last updated: 2026-05-16。
- Known limits: helper scripts 不能证明 gameplay feel；manual playtest 仍负责 player-facing feel、readability、pacing、route acceptance。
- Upgrade rule: 优先加小 reference、script、template，不拉长 `SKILL.md`；重大变更后运行 `scripts/skill_self_check.py <skill-root>` 和平台 validator。
