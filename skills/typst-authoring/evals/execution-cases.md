# Execution Cases

## 场景 1：修 Typst 编译错误

- 输入：一份不能编译的 `.typ` 文件
- 预期：走 diagnostics → fix → compile 循环，并给出修复建议

## 场景 2：实现 Touying slides

- 输入：已有演示结构和页面需求
- 预期：完成 Touying 层的技术实现，而不是改写叙事

## 场景 3：图形方案选择

- 输入：需要在 Typst 中表达的流程图 / 架构图 / sequence
- 预期：在 `diagraph` / `D2` / `oxdraw` 之间做合理选择
