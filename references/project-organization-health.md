# 项目组织健康

审查 Godot 项目的文档、主场景脚本、scene 和 smoke test 是否开始降低组织效率时加载。目标是发现上下文膨胀和 owner 变模糊的趋势，不把行数阈值当作机械重构命令。

## 文档健康

Active docs 只保存当前真相和下一步：

- `docs/current/STATUS.md`：当前系统状态、当前验收状态、验证命令、当前风险；不写 completed GDD 时间线。
- `docs/current/PROJECT-SNAPSHOT.md`：scene/script/test 索引和 owner 摘要；不写长篇测试叙事。
- `docs/plans/GAMEPLAY-EXPANSION-ROADMAP.md`：当前和未来方向；已完成或废弃路线进 `docs/history/gdd/INDEX.md`。
- `docs/plans/NEXT-STEPS.md`：当前下一步和少量长期约束；不复制 roadmap 或历史。
- `docs/history/gdd/INDEX.md`：超过约 50 条后按阶段分组，再链接具体 GDD 文件。

失败信号：

- active docs 出现大量 `2026-.. 完成`、`completed` / `abandoned` 时间线。
- `STATUS.md` 需要读很久才能找到当前风险或 pending acceptance。
- roadmap 大部分内容已经 completed / abandoned，但仍在 plans 入口。
- snapshot 把 smoke test 细节写成单个超长段落。

## 代码和测试健康

大文件默认是 warning，不是立刻拆分命令。只有触碰相关功能时，才按 owner / route / assertion family 顺手拆：

- `main_game.gd` 超过约 800-1000 行：新增 route helper、debug snapshot、save bridge、UI layout 时优先拆 owner helper。
- smoke test 超过约 600-800 行：新增断言时优先放入独立 smoke scene 或 assertion family。
- `Main.tscn` 可以作为白盒集成入口变大，但新增路线段必须有清晰 node group、owner script、test route 和文档索引。
- `PROJECT-SNAPSHOT.md` 只记录大文件风险和索引，不复制每个断言细节。

## 处理规则

- 先标记组织健康风险，再决定是否纳入当前任务。
- 如果用户要求“组织效率”或“项目结构审查”，可以写文档/skill 规则和自检 warning。
- 如果用户要求 gameplay bug fix，不因为大文件 warning 顺手重构。
- 拆分必须保持 visible runtime route 和 smoke coverage 不变。

## 自检输出

- Active docs 历史堆积、缺少索引、GDD 重复存储：fail。
- 超大 script / scene / smoke：warn，除非项目明确启用严格组织门。
- Warning 要给出路径、行数和推荐下一步，不阻止 docs-only / skill-only 提交。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
