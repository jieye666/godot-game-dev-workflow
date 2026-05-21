# Skill 质量门

维护 `godot-game-dev-workflow`、新增 reference/script/template、调整触发条件，或吸收外部 workflow idea 时使用。一个有用的 Godot skill 不是长提示词，而是可重复执行的 operator workflow：触发清楚、边界明确、reference 可路由、脚本可验证、例子可复现、来源可追踪。

## Merge Filter

外部材料或新规则必须同时通过：

- Godot relevance：会改变 agent 如何 plan、implement、validate、document 或 hand off Godot gameplay work。
- Operational form：能落成 step、checklist、template field、script check 或 example。
- No duplication：不重复已有 reference，除非能收紧行为。
- Low context cost：`SKILL.md` 保持 router；长细节进入 focused reference。
- Verification path：说明如何检查遵守情况，即使检查只能 manual。

拒收或只摘要：

- 没有 Godot 行动的 broad AI philosophy。
- core instructions 已覆盖的通用工程建议。
- 当前 Codex 或目标 Godot 项目不存在的 tool-specific workflow。
- 未验证的 Godot API、命令或行为 claim。

## Production Gate

发布 skill 变更前检查：

1. Activation：frontmatter `description` 能决定何时触发，不把完整 workflow 塞进描述。
2. Boundaries：`SKILL.md` 明确 not-for / misfire prevention。
3. Routing：新增 reference 出现在 Task Routing 或 Reference Loading。
4. Progressive disclosure：详细内容在 `references/`；`SKILL.md` 可扫描。
5. Examples：至少三个例子覆盖 small bug、large plan、behavior unchanged。
6. Maintenance：sources、last updated、known limits、validation commands 清楚。
7. Scriptability：便宜可检查的规则进入 `scripts/skill_self_check.py` 或 helper script。
8. Evidence：外部来源和不确定性记录在 `external-repositories.md` 或对应 reference。
9. Package hygiene：不保留 cache、temp logs、local run artifacts；根目录不放 helper `.py`，临时目录必须在仓库外或被 `.gitignore` 明确忽略。
10. Merge coverage：从旧 skill 或外部来源迁入时，确认每个高价值点落在 `SKILL.md`、focused reference、script、template 或明确拒收记录之一。
11. Failure prevention：新增规则能映射到 assumption、owned scope、source of truth、deterministic check、verification 或 manual acceptance；否则只保留为参考，不进 core workflow。
12. Context cost：新增内容不得让 `SKILL.md` 变成长文章；核心门靠短句，细节进入 focused reference，能脚本化的规则进入 helper script。

## Machine vs Manual Gates

| Rule type | Preferred gate |
| --- | --- |
| Required skill files and links | `scripts/skill_self_check.py` |
| Frontmatter shape | platform skill validator；Windows 中文内容必要时先设置 `$env:PYTHONUTF8='1'` |
| Reference link integrity | `scripts/skill_self_check.py` |
| Required sections | `scripts/skill_self_check.py` |
| Root package hygiene | `scripts/skill_self_check.py` 检查 `.tmp/`、根级异常文件和 cache |
| agent 自选档位和 selected tier 记录 | `scripts/skill_self_check.py` plus golden task review |
| 玩家可见计划的 reference research 字段 | `scripts/skill_self_check.py` plus golden task review |
| Golden task regressions | `scripts/skill_self_check.py` 检查小 bug、行为没变、玩家可见参考调研的关键流程词 |
| Generated cache/temp artifacts | `scripts/skill_self_check.py` 报告；显式 fix flag 才清理 |
| Godot node paths/signals | `scripts/check_scene_references.py` plus direct inspection |
| Project docs drift | `scripts/audit_godot_docs.py` plus current-file review |
| 中文文档规范 | `scripts/audit_doc_language.py` plus manual review |
| AI failure prevention fields | `scripts/skill_self_check.py` plus golden task review |
| Deterministic checks before judgement | helper script / command evidence plus manual review |

Manual gates 仍负责：

- examples 是否匹配用户期望 workflow。
- 新规则是降低返工，还是只增加仪式感。
- gameplay feel、readability、pacing、route flow 是否可接受。
- 外部 workflow idea 是否已转成 Godot-specific behavior。
- source 冲突是否被明确暴露，而不是折中混合。

## Scoring Rubric

重大变更用这个 quick score：

| Area | Pass condition |
| --- | --- |
| Activation | frontmatter 可判断 trigger 和 scope |
| Boundary | explicit not-for rules 防止误触发 |
| Usability | agent 不靠隐藏上下文也能跟随 examples |
| Evidence | sources 和 unknowns 被命名 |
| Maintainability | 新内容只有一个 owner file，没有 duplicate truth |
| Validation | 至少一个 command 或 checklist 能抓 regression |
| Merge fidelity | 旧 skill 的独特优点被保留、压缩或有理由拒收，没有只因瘦身而丢掉执行检查 |

任一 area fail 时，先保留为 proposal/reference note，不写成 core workflow。

## Golden Task Tests

维护本 skill 后，用这些任务心智检查输出是否退化；其中小 bug、行为没变、玩家可见参考调研已有轻量 `scripts/skill_self_check.py` 关键短语检查。需要独立验证时，可让另一个 agent 只读 skill 后回答流程。

- 小 bug：玩家受伤数值错误。期望：Compact Patch Plan、读相关 script/scene、自动验证、manual retest、必要 docs sync。
- 自动提交 bug 修复：文档审计失败、引用错误或 smoke 失败且无需人工审查。期望：定位根因、修复、验证、必要 docs sync 后直接 commit，并报告 commit id。
- 档位选择：用户只说“小参数调整”或“跨系统收尾”。期望：agent 自行选择快速档/严格档，记录理由和 tradeoff；只有 scope 不清、高风险或 `escalated` 才询问用户。
- scene/signal：按钮触发门打开。期望：加载 scene-signal-resource checklist，不猜 node path，写 sender/receiver/payload。
- 大任务：Boss 二阶段和奖励路线。期望：先联网查同类 Boss phase、telegraph、reward pacing 或开源实现，再做 task breakdown、readiness、architecture check；`pending` 不直接实现。
- reference-backed feature：参考项目有完整方案。期望：先读项目 `docs/reference/INDEX.md` 和 selected files，再本地化实现，不盲目复制。
- 行为没变：测试通过但游戏里没变化。期望：检查 played scene、attached script、main route、resource instance，而不是只补测试。
- 收尾：用户验收一个 prototype slice。期望：同步 current/status/history/next steps，报告 automated checks 和 manual acceptance。
- 流程复盘：用户说“刚才流程有问题，整理进 skill”。期望：先识别 task shape、scope creep、验证节奏、文档时机和暂停点等流程层级问题，不只补单点 UI 或测试规则。
- 玩家可见 polish：用户要求 UI、路线可读性、手感或 Boss 节奏“更像游戏”。期望：先声明最小可看闭环和 manual acceptance pack；第一版后跑窄验证并等待用户确认，确认后才 docs/history/archive/commit。
- 文档/源码冲突：`STATUS.md`、`NEXT-STEPS.md`、archived plan 和源码不一致。期望：列冲突、选 source of truth、同步 designated docs，不把旧事实和新源码混合。
- 确定性验证：用户问“现在是否通过”。期望：运行或引用脚本/命令结果和 Godot output scan，不凭模型回忆回答。
- 历史索引化：项目入口堆积 completed GDD 历史。期望：`docs/INDEX.md`、quick context、`NEXT-STEPS.md` 只保留当前状态和索引链接；GDD 历史进入 `docs/history/gdd/`，提交批次进入 `docs/history/commits/`。

## 轻量化边界

- `SKILL.md` 只放 routing、质量门和最小 examples。
- 可执行细节放 reference，reference 优先写 checklist/template，不写长文章。
- 脚本能检查的内容不要写成长流程。
- 删除内容前先确认是否被 quality gate、golden task 或 helper script 依赖。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
