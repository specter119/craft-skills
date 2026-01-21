# Deep Research Examples

## Example 1: Technology Research with Parallel Tasks

**Query**: "调研 Claude Code Skills 系统"

### Phase 0: Decomposition

```plain
Claude Code Skills 深度调研 (Technology Template)
├── D1. 是什么: Skill 定义, 与 MCP/Tool 的区别, 架构设计
├── D2. 为什么: 解决什么问题, 设计理念, vs 传统工具
├── D3. 怎么用: 创建 skill, SKILL.md 结构, 调试技巧
├── D4. 生态系统: 官方 skills, 社区资源, 插件市场
├── D5. 最佳实践: 设计原则, 常见模式, 反模式
├── D6. 高级特性: Task 集成, allowed-tools, model override
└── D7. 限制与未来: 当前限制, roadmap, 社区反馈
```

### Phase 1: Parallel Tasks

```plain
启动 3 个并行 Task:

**Task 1: 核心概念 (D1-D2)**
- 搜索: "Claude Code Skills official documentation"
- 搜索: "Claude Skills vs MCP vs Tools difference"
- 抓取: docs.anthropic.com/skills
- 输出: scratch/research-d1-d2.md

**Task 2: 使用方法 (D3-D4)**
- 搜索: "Claude Code Skills tutorial 2025"
- 搜索: "Claude Skills ecosystem community"
- Context7: get-library-docs for claude-code
- 输出: scratch/research-d3-d4.md

**Task 3: 高级实践 (D5-D7)**
- 搜索: "Claude Skills best practices"
- 搜索: "Claude Skills limitations roadmap"
- 抓取: github.com/anthropics/skills
- 输出: scratch/research-d5-d7.md
```

### Phase 2: Synthesis

```markdown
## 完整度评估

| 维度 | 覆盖度 | 可信度 | 缺口 |
|------|--------|--------|------|
| D1 | 90% | High | 无 |
| D2 | 85% | High | 无 |
| D3 | 80% | High | 代码示例需补充 |
| D4 | 70% | Medium | 社区资源不完整 |
| D5 | 75% | Medium | 反模式案例少 |
| D6 | 65% | Medium | model override 文档少 |
| D7 | 50% | Low | roadmap 信息有限 |

总体: 74% → 需要迭代 D6, D7
```

### Phase 3: Iteration

```plain
补充 Task: D6-D7 深入研究
- 搜索: "Claude Skills advanced features model"
- 搜索: "Claude Code roadmap 2025"
- 抓取: anthropic.com/engineering 相关文章
```

**Expected Output**: Comprehensive 15-page report with architecture diagrams, code examples, and actionable recommendations.

---

## Example 2: Comparison Research

**Query**: "Tokio vs async-std vs smol 对比分析"

### Decomposition (Comparison Template)

```plain
Rust 异步运行时对比分析
├── D1. 定位差异: 各自设计目标和理念
├── D2. 架构对比: 核心实现差异 (executor, reactor)
├── D3. 性能对比: 基准测试, 内存占用, 延迟
├── D4. 开发体验: API 设计, 文档, 错误处理
├── D5. 生态对比: 库支持, 社区规模
├── D6. 适用场景: 各自最佳用例
└── D7. 迁移考虑: 互操作性, 迁移成本
```

### Parallel Tasks

```plain
Task 1: 基础对比 (D1-D2)
- 搜索: "Tokio vs async-std design philosophy"
- Context7: Tokio docs, async-std docs

Task 2: 性能与体验 (D3-D4)
- 搜索: "Rust async runtime benchmark 2025"
- 搜索: "async-std vs tokio developer experience"

Task 3: 生态与场景 (D5-D7)
- 搜索: "Tokio ecosystem libraries"
- 搜索: "when to use smol vs tokio"
```

### Expected Output

```markdown
## 对比矩阵

| 特性 | Tokio | async-std | smol | 结论 |
|------|-------|-----------|------|------|
| 设计理念 | 性能优先 | 兼容 std | 极简 | 按需选择 |
| 性能 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Tokio 略优 |
| 学习曲线 | 中等 | 低 | 低 | async-std 最友好 |
| 生态系统 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Tokio 最丰富 |
| 适合场景 | 高性能服务 | 简单应用 | 嵌入式/小型 | - |
```

---

## Example 3: Problem-Solving Research

**Query**: "如何解决 Rust async 生态碎片化问题"

### Decomposition (Problem Template)

```plain
Rust 异步生态碎片化问题解决方案
├── D1. 问题定义: 什么是碎片化, 症状表现
├── D2. 根因分析: 为什么会碎片化
├── D3. 方案枚举: 有哪些解决方案
├── D4. 方案对比: 各方案优劣
├── D5. 推荐方案: 最佳实践
├── D6. 实施步骤: 如何落地
└── D7. 风险预案: 可能问题
```

### Key Findings

```markdown
## 方案对比

| 方案 | 复杂度 | 风险 | 成本 | 推荐度 |
|------|--------|------|------|--------|
| 统一使用 Tokio | Low | Low | Low | ⭐⭐⭐⭐⭐ |
| 使用 async-compat | Medium | Low | Low | ⭐⭐⭐⭐ |
| 自建抽象层 | High | High | High | ⭐⭐ |
| 等待标准化 | N/A | N/A | Time | ⭐⭐⭐ |
```

---

## Example 4: Trend Research

**Query**: "AI Agent 框架 2025 现状与趋势"

### Decomposition (Trend Template)

```plain
AI Agent 框架现状与趋势
├── D1. 当前状态: 成熟度, 采用率
├── D2. 关键玩家: LangChain, AutoGPT, CrewAI, Claude Code
├── D3. 最新进展: 近期发布, 重大更新
├── D4. 发展方向: 多 Agent, 工具使用, 记忆系统
├── D5. 竞争格局: 开源 vs 闭源
├── D6. 采用建议: 是否值得入场
└── D7. 风险因素: 技术/生态/商业风险
```

### Parallel Tasks with Different Focus

```plain
Task 1: 市场概览 (D1-D2)
- Exa Search: "AI agent frameworks comparison 2025"
- 抓取: state of AI agents report

Task 2: 技术动态 (D3-D4)
- WebSearch: "LangChain updates 2025"
- WebSearch: "AI agent memory systems research"

Task 3: 评估建议 (D5-D7)
- WebSearch: "AI agent framework production experience"
- WebSearch: "AI agent framework risks"
```

---

## Search Query Patterns

### For Different Research Types

**Technology**

```plain
"[tech] official documentation"
"[tech] architecture design"
"[tech] getting started tutorial 2025"
"[tech] vs [alternative] comparison"
"[tech] production case study"
```

**Comparison**

```plain
"[A] vs [B] benchmark 2025"
"[A] vs [B] which is better for [use case]"
"migrate from [A] to [B]"
"[A] [B] feature comparison"
```

**Concept**

```plain
"what is [concept] explained simply"
"[concept] how it works internally"
"[concept] real world examples"
"[concept] common misconceptions"
```

**Problem**

```plain
"[problem] solution best practices"
"how to solve [problem] in [context]"
"[problem] root cause analysis"
"[problem] prevention strategies"
```

**Trend**

```plain
"[topic] state of 2025"
"[topic] market trends"
"[topic] future predictions"
"[topic] adoption statistics"
```

---

## Tool Selection Guide

| 场景 | 推荐工具 | 原因 |
|------|----------|------|
| 广泛发现 | WebSearch, Exa Search | 覆盖面广 |
| 官方文档 | Context7, WebFetch | 精确内容 |
| 代码示例 | Exa Code Context | 代码专用 |
| 最新动态 | Exa Search (livecrawl) | 实时抓取 |
| 深度内容 | WebFetch, Exa Crawl | 完整页面 |
| 并行加速 | Task Agents | 节省时间 |

---

## Quality Assurance Checklist

每次研究完成前检查:

- [ ] 所有维度覆盖度 > 50%
- [ ] 关键发现有 2+ 来源验证
- [ ] 信息时效性满足要求
- [ ] 冲突信息已标注
- [ ] 信息缺口已记录
- [ ] 报告结构完整
- [ ] 建议具体可执行

---

## Quick Start: Full Workflow Demo

Shows the complete user-facing interaction flow.

```plain
User: "调研 A2A 协议的商业落地案例"
Current working directory: /path/to/project

→ Phase 1: Scope

  [Internal decomposition]
  Subtopics: saas-integration, cross-org-collaboration, platform-orchestration

  [Generate brief - internal]
  Topic: A2A Protocol Commercial Deployments
  Goal: Identify real production cases, not demos
  ...

  [Inform user and proceed - NO confirmation needed]
  "开始研究 A2A 商业案例

   输出目录: ./research/a2a-commercial-cases/

   研究方向:
   1. SaaS 产品互联案例
   2. 跨组织协作案例
   3. 平台编排案例

   预计 5-8 分钟，开始..."

→ Phase 2: Research (autonomous)

  - Launch 3 parallel sub-agents
  - Each archives sources to _sources/
  - Each writes {subtopic}/findings.md
  - Supervisor reviews, no critical gaps → proceed

→ Phase 3: Write

  - One-shot report from all findings
  - Output: ./research/a2a-commercial-cases/report.md

→ Done

  "研究完成

   报告: ./research/a2a-commercial-cases/report.md
   来源: 12 个文档存档在 _sources/

   主要发现:
   1. [Key finding 1]
   2. [Key finding 2]
   3. [Key finding 3]"
```

**Example with user-specified directory:**

```plain
User: "调研 A2A，存到 docs 目录"

→ Double confirm:
  "确认将研究结果存到 ./docs/research/a2a-xxx/ ？"

User: "好"

→ Proceed as above...
```
