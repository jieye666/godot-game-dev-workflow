# 可扩展玩法架构

保持首版小而清晰，同时不压扁后续一定会需要的系统边界。检查 owner、related systems、extension points 和 coupling risks。

## 什么时候读

- 新 gameplay system、Boss/敌人/奖励/房间流/存档/UI runtime path。
- 第二种 variant 很可能出现，例如第二个 Boss、第二类机关、第二种奖励。
- 需求看似小，但会碰 shared state、scene route、save flag、signal bus、resource config。

## Architecture Check

- Owner：哪个 node/script/resource 拥有状态和决策。
- Boundary：这个系统负责什么，不负责什么。
- Related systems：读写哪些外部系统，是否只通过稳定接口通信。
- Data/config：硬编码、export var、resource、save data 分别放什么。
- Communication：direct call、signal、group、resource reference、manager method 的选择理由。
- Extension points：新增 variant 时改哪里，不改哪里。
- Coupling risk：哪些 shortcut 会导致后续重写。
- Not over-engineered：为什么当前抽象够用，不提前做过大框架。

## 默认取舍

- 首版可以小，但 owner 必须清楚。
- 同类玩法的第二个实例不能要求复制整套 scene/script 再手改路径。
- UI feedback、save flag、reward route 这类 player-visible state 不能各自维护一份真相。
- `Autoload` 只用于跨 scene 生命周期确实需要的状态；scene-local prototype 优先 scene-local manager。

## Godot System Boundaries

| 系统 | 默认 owner | 推荐边界 |
| --- | --- | --- |
| Player ability | ability script / component | 输入、状态消耗、动作触发清楚分层；不要把所有能力塞回 Player 主脚本 |
| Enemy / Boss phase | enemy scene root 或 phase controller | phase state、telegraph、damage window、reward trigger 分离 |
| Level object | object scene root | 机关只暴露稳定 signal / method，不直接改玩家内部状态 |
| HUD / UI feedback | UI scene 或 presenter | 显示状态来自单一 gameplay source，不维护第二份真相 |
| Progress / reward | route manager、checkpoint、save owner | player-visible completion、unlock、reward 只能有一个权威来源 |

## Composition Rules

- 优先组合 scene/script/resource，小系统先有清晰 owner，再考虑抽象 base class。
- 重复出现第二个 variant 时，抽出 config/resource 或 shared component；不要先建大框架。
- signal 用于跨边界事件；direct call 用于 owner 内部或稳定邻接关系；group 用于动态集合。
- export var 适合 scene-local tuning；`.tres` resource 适合可复用配置；save data 只放需要跨 session 存活的状态。
- runtime path 必须能从 main scene / played scene 走到改动脚本，避免只改测试场景。

## Acceptance Checks

- 新增第二个实例时，不需要复制后再手改 node path。
- 改一处 tuning 不会让 docs、HUD、reward flag 或 save state 各自不同步。
- 删除或替换一个 scene-local prototype 不会破坏全局状态。
- manual playtest 能观察到关键 state transition 或白盒反馈。

## 输出要求

在计划或实现说明里写 3-6 行 architecture note：owner、boundary、extension point、coupling risk、验证方式。小 bug 可以更短，但不能省掉 owner 和 runtime path。

## 中文规范

本 reference 的说明文字使用中文。路径、命令、GDD 编号、Godot API、类名、函数名、signal、InputMap action 保持英文。
