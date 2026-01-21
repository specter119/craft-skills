# Topic Decomposition Guide

## Quick Reference

| Research Type | Trigger Keywords | Template | Typical Dimensions |
|---------------|------------------|----------|-------------------|
| Technology | 调研, 了解, 学习 [X] | [Technology](#technology) | 7 |
| Comparison | X vs Y, 区别, 对比 | [Comparison](#comparison) | 7 |
| Concept | 什么是, 原理, 理解 | [Concept](#concept) | 7 |
| Problem | 如何解决, 方案, 问题 | [Problem](#problem) | 7 |
| Trend | 现状, 趋势, 发展 | [Trend](#trend) | 7 |

---

## Dynamic Adjustment Principles

### When to Add Dimensions

- Topic spans multiple domains → Add cross-domain dimension
- User mentions specific concerns → Add targeted dimension
- Initial search reveals unexpected complexity → Split dimension

### When to Remove Dimensions

- Topic is narrow/focused → Merge related dimensions
- Time constraints → Prioritize core dimensions (D1-D4)
- Information scarcity → Skip dimensions with no sources

### Dimension Prioritization

```plain
优先级 1 (必须): D1-D2 核心概念
优先级 2 (重要): D3-D4 实践应用
优先级 3 (补充): D5-D7 高级/未来
```

---

## Technology

**Use when**: "调研 X", "了解 X 框架", "学习 X"

```plain
[Technology] 深度调研
├── D1. 是什么 (What) [必须]
│   ├── 核心定义与一句话解释
│   ├── 设计理念/哲学
│   ├── 关键概念术语
│   └── 与相似技术的本质区别
│
├── D2. 为什么 (Why) [必须]
│   ├── 解决什么问题
│   ├── 历史背景与演进
│   ├── vs 现有方案的优势
│   └── 为什么选择它而非替代品
│
├── D3. 怎么用 (How) [重要]
│   ├── 安装/配置步骤
│   ├── 核心 API/接口
│   ├── Hello World 示例
│   ├── 常见用例代码
│   └── 调试技巧
│
├── D4. 生态系统 (Ecosystem) [重要]
│   ├── 官方工具链
│   ├── 社区库/插件
│   ├── IDE/编辑器支持
│   ├── 社区活跃度指标
│   └── 学习资源质量
│
├── D5. 优劣势 (Pros/Cons) [补充]
│   ├── 主要优点（具体量化）
│   ├── 主要缺点（真实痛点）
│   ├── 适用场景
│   └── 不适用场景
│
├── D6. 生产实践 (Production) [补充]
│   ├── 性能基准数据
│   ├── 稳定性评估
│   ├── 大厂/知名项目案例
│   ├── 踩坑经验与解决方案
│   └── 运维注意事项
│
└── D7. 未来趋势 (Future) [补充]
    ├── 官方路线图
    ├── 版本计划
    ├── 社区讨论热点
    └── 潜在风险与不确定性
```

**Example Queries per Dimension**:

```bash
# D1: 核心概念
"[Tech] 是什么? 核心概念和设计理念? 一句话解释"
"[Tech] vs [Similar] 本质区别是什么?"

# D2: 为什么
"为什么需要 [Tech]? 它解决什么问题? 历史背景"
"[Tech] 相比 [Alternative] 的优势是什么?"

# D3: 怎么用
"[Tech] 快速上手指南 getting started"
"[Tech] 核心 API 示例代码"
"[Tech] 常见用法 common patterns"

# D4: 生态系统
"[Tech] 生态系统 主流库和工具 2025"
"[Tech] 社区活跃度 GitHub stars contributors"
"[Tech] 学习资源 教程 文档质量"

# D5: 优劣势
"[Tech] 优缺点分析 pros cons"
"[Tech] 适用场景 use cases"
"[Tech] 什么时候不应该使用"

# D6: 生产实践
"[Tech] 生产环境经验 production"
"[Tech] 性能基准 benchmark"
"[Tech] 大厂案例 [Company] uses [Tech]"

# D7: 未来趋势
"[Tech] 路线图 roadmap 2025"
"[Tech] 未来计划 what's next"
"[Tech] 社区讨论 RFC proposal"
```

---

## Comparison

**Use when**: "X vs Y", "X 和 Y 的区别", "选择 X 还是 Y"

```plain
[A] vs [B] 对比分析
├── D1. 定位差异 [必须]
│   ├── A 的设计目标与理念
│   ├── B 的设计目标与理念
│   ├── 根本理念差异
│   └── 各自的 "Why" 故事
│
├── D2. 架构对比 [必须]
│   ├── 核心实现差异
│   ├── 技术栈差异
│   ├── 依赖/运行时要求
│   └── 内部工作原理对比
│
├── D3. 性能对比 [重要]
│   ├── 官方基准测试数据
│   ├── 社区基准测试数据
│   ├── 内存占用
│   ├── 启动时间
│   ├── 实际场景性能
│   └── 可扩展性
│
├── D4. 开发体验 [重要]
│   ├── 学习曲线
│   ├── 文档质量
│   ├── 调试工具
│   ├── 错误信息可读性
│   ├── IDE 支持
│   └── 开发效率
│
├── D5. 生态对比 [补充]
│   ├── 社区规模
│   ├── 库/插件丰富度
│   ├── 企业支持
│   ├── 就业市场
│   └── 长期维护前景
│
├── D6. 适用场景 [补充]
│   ├── A 最佳用例
│   ├── B 最佳用例
│   ├── 两者都不适合的场景
│   └── 决策树/选择指南
│
└── D7. 迁移考虑 [补充]
    ├── A→B 迁移成本
    ├── B→A 迁移成本
    ├── 互操作性
    ├── 渐进式迁移方案
    └── 迁移风险评估
```

**Comparison Matrix Template**:

```markdown
| 维度 | [A] | [B] | 结论 |
|------|-----|-----|------|
| 设计理念 | | | |
| 性能 | | | |
| 学习曲线 | | | |
| 生态系统 | | | |
| 社区活跃度 | | | |
| 企业采用 | | | |
| 适合场景 | | | |
```

---

## Concept

**Use when**: "什么是 X", "X 的原理", "理解 X"

```plain
[Concept] 深度理解
├── D1. 定义 (Definition) [必须]
│   ├── 一句话定义
│   ├── 正式/学术定义
│   ├── 通俗类比解释
│   └── 常见误解澄清
│
├── D2. 背景 (Context) [必须]
│   ├── 历史起源
│   ├── 解决什么问题
│   ├── 在更大体系中的位置
│   └── 相关领域
│
├── D3. 原理 (Mechanism) [重要]
│   ├── 工作原理
│   ├── 核心算法/机制
│   ├── 关键组件
│   └── 数据/控制流
│
├── D4. 示例 (Examples) [重要]
│   ├── 最简单示例
│   ├── 实际应用案例
│   ├── 代码实现
│   └── 可视化/图解
│
├── D5. 变体 (Variants) [补充]
│   ├── 不同实现方式
│   ├── 相关概念对比
│   ├── 演化历史
│   └── 领域特定变体
│
├── D6. 权衡 (Tradeoffs) [补充]
│   ├── 优点
│   ├── 缺点/限制
│   ├── 适用边界
│   └── 复杂度分析
│
└── D7. 实践 (Practice) [补充]
    ├── 使用建议
    ├── 常见误区
    ├── 调试技巧
    └── 深入学习资源
```

---

## Problem

**Use when**: "如何解决 X", "X 问题的方案", "处理 X"

```plain
[Problem] 解决方案调研
├── D1. 问题定义 [必须]
│   ├── 问题描述
│   ├── 症状表现
│   ├── 影响范围
│   ├── 复现条件
│   └── 严重程度评估
│
├── D2. 根因分析 [必须]
│   ├── 直接原因
│   ├── 深层原因
│   ├── 相关因素
│   └── 5 Whys 分析
│
├── D3. 方案枚举 [重要]
│   ├── 方案 A: [描述]
│   ├── 方案 B: [描述]
│   ├── 方案 C: [描述]
│   └── 其他可能方案
│
├── D4. 方案对比 [重要]
│   ├── 实现复杂度
│   ├── 性能影响
│   ├── 维护成本
│   ├── 风险评估
│   └── 所需资源
│
├── D5. 推荐方案 [补充]
│   ├── 首选方案
│   ├── 选择理由
│   ├── 备选方案
│   └── 方案组合
│
├── D6. 实施步骤 [补充]
│   ├── 前置准备
│   ├── 详细步骤
│   ├── 验证方法
│   ├── 回滚计划
│   └── 时间估算
│
└── D7. 风险预案 [补充]
    ├── 潜在问题
    ├── 应对措施
    ├── 监控指标
    └── 升级路径
```

**Solution Comparison Template**:

```markdown
| 方案 | 复杂度 | 风险 | 成本 | 推荐度 |
|------|--------|------|------|--------|
| A    | Low    | Low  | Low  | ⭐⭐⭐⭐ |
| B    | Medium | Med  | Med  | ⭐⭐⭐ |
| C    | High   | High | High | ⭐⭐ |
```

---

## Trend

**Use when**: "X 的现状", "X 发展趋势", "X 的未来"

```plain
[Topic] 现状与趋势
├── D1. 当前状态 [必须]
│   ├── 成熟度评估
│   ├── 市场采用率
│   ├── 标准化程度
│   └── 当前版本/状态
│
├── D2. 关键玩家 [必须]
│   ├── 主要项目/产品
│   ├── 核心公司/组织
│   ├── 关键贡献者
│   └── 投资/资金情况
│
├── D3. 最新进展 [重要]
│   ├── 近期重要发布
│   ├── 重大更新
│   ├── 行业事件
│   └── 媒体报道
│
├── D4. 发展方向 [重要]
│   ├── 官方路线图
│   ├── 社区讨论热点
│   ├── 技术演进方向
│   └── 研究前沿
│
├── D5. 竞争格局 [补充]
│   ├── 主要竞品
│   ├── 差异化定位
│   ├── 市场份额
│   └── 竞争态势变化
│
├── D6. 采用建议 [补充]
│   ├── 现在是否值得采用
│   ├── 适合什么团队/场景
│   ├── 学习投资回报
│   └── 观望 vs 入场时机
│
└── D7. 风险因素 [补充]
    ├── 技术风险
    ├── 生态风险
    ├── 商业风险
    └── 法规/合规风险
```

---

## How to Use

### Step-by-Step Process

1. **识别类型**: 根据用户问题选择合适的模板
2. **定制维度**: 根据具体主题调整 D1-D7
   - 添加话题特定的子维度
   - 移除不相关的子维度
   - 调整优先级
3. **生成计划**: 为每个维度制定具体问题和信息源
4. **执行调研**: 按维度逐个收集信息（或并行）
5. **评估完整度**: 检查每个维度的覆盖率
6. **迭代深入**: 对覆盖不足的维度补充研究
7. **综合报告**: 汇总各维度发现

### Dimension Quality Checklist

每个维度应满足:

- [ ] 有明确的研究问题
- [ ] 有 2+ 个独立来源
- [ ] 信息时效性 < 1 年（技术类）
- [ ] 标注了可信度等级
- [ ] 记录了信息缺口

### Coverage Assessment

```markdown
| 维度 | 覆盖度 | 质量 | 状态 |
|------|--------|------|------|
| D1 | 90% | High | ✅ |
| D2 | 75% | Medium | ⚠️ 需补充 |
| D3 | 60% | Low | ❌ 迭代 |
| ... | ... | ... | ... |

总体: 73% → 目标 80%
```

---

## Parallel Research Assignment

将维度分配给 Task agents:

```plain
默认分配策略:

Task 1 (基础): D1-D2 → 核心概念和背景
Task 2 (应用): D3-D4 → 实践和生态
Task 3 (高级): D5-D7 → 权衡和趋势

时间紧迫时:

Task 1: D1-D3 (必须)
Task 2: D4-D7 (补充)

深度研究时:

Task 1: D1
Task 2: D2
Task 3: D3-D4
Task 4: D5-D7
```

---

## Source Quality Reference

### 来源可信度评级

| 等级 | 来源类型 | 例子 |
|------|----------|------|
| **High** | 官方文档 | docs.*, github.com/[org] |
| **High** | 权威组织 | IETF, W3C, CNCF |
| **High** | 核心维护者 | 项目作者的博客/演讲 |
| **Medium** | 知名技术博客 | engineering.*, InfoQ |
| **Medium** | Stack Overflow | 高票答案, 验证的回答 |
| **Low** | 个人博客 | 需交叉验证 |
| **Low** | 论坛讨论 | Reddit, HN 评论 |
| **Verify** | AI 生成内容 | 必须与其他来源交叉验证 |

### 时效性要求

| 话题类型 | 最大信息年龄 |
|----------|--------------|
| 安全漏洞 | 1 个月 |
| 库版本 | 3 个月 |
| 最佳实践 | 1 年 |
| 架构模式 | 2-3 年 |
| 基础概念 | 5+ 年 OK |
