# External Reference Repositories

维护本 skill 或刷新外部 workflow idea 时读本文件。这里记录来源和用途，不把完整外部仓库 vendor 进 skill；除非未来确实需要某个可复用资产，且 license 允许复制。

## AI Workflow and Memory References

| Repository | Local snapshot used | Purpose in this skill |
| --- | --- | --- |
| `https://github.com/oguzbilgic/agent-kernel.git` | `agent-kernel` at `c58a49b` | Agent identity and compact operating rules. |
| `https://github.com/axiomhq/agent-memory.git` | `agent-memory` at `7207541` | Memory layering, consolidation, and handoff ideas. |
| `https://github.com/jayzeng/agentmemory.git` | `agentmemory` at `b7267bb` | Alternative memory and docs organization patterns. |
| `https://github.com/trailofbits/claude-code-config.git` | `claude-code-config` at local `main` snapshot | Practical AI coding workspace conventions. |
| `https://github.com/peterkrueck/Claude-Code-Development-Kit.git` | `Claude-Code-Development-Kit` at `df9bd95` | Development-kit organization and command patterns. |
| `https://github.com/cloudnative-co/claude-code-starter-kit.git` | `claude-code-starter-kit` at `b1be790` | Starter-kit structure and onboarding patterns. |
| `https://github.com/shinpr/claude-code-workflows.git` | `claude-code-workflows` at `c371835` | Workflow decomposition and task-flow examples. |
| `https://github.com/github/spec-kit.git` | `spec-kit` at `6322a4d` | Spec-driven planning, task traceability, and verification gates. |

## Local-Only Reference

`vibe-coding-cn-develop` 曾作为本地外部 workflow material 审查，但 packaging 时可用 snapshot 没有 Git metadata。把它当作 local reference source，不当作 vendored dependency。可借鉴点是小而可审计的 quality mechanics：explicit boundaries、reproducible examples、maintenance/source tracking、compact quality gate。

## Refresh Rules

- 优先更新本 manifest 的 upstream URL 和 commit snapshot，不复制完整仓库。
- 把外部 idea 转成 Godot-specific checks、scripts、references 或 templates。
- `SKILL.md` 保持 router；详细导入指导放进 focused reference files。
- 引入任何外部工具或 Godot 行为前，先验证该 claim，再写入 core workflow。
