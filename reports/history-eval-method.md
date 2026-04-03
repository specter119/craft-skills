# History Eval Method

用 `xurl` 先按 skill 名称搜索 agent history，再解析对应 session 文件，提取可复用的历史 prompt 证据。

## Why

- 现有 `evals/trigger-cases.md` 和 `evals/execution-cases.md` 目前大多是 seed evals。
- 真正有价值的下一步不是继续拍脑袋补 case，而是先把历史调用记录变成可审阅的候选集。
- 但 repo 内历史会混入大量“维护 skill 本身”的对话，这类记录不能直接当公开 skill 的 runtime eval。

## Workflow

1. 用 `xurl '<provider>?q=<skill>&limit=N'` 或 `xurl 'agents://<repo-root>?q=<skill>&limit=N'` 找到候选 threads。
2. 收集 `thread_source`，解析原始 session jsonl。
3. 抽取两类文本：
   - user prompts
   - delegated subagent task messages
4. 执行脱敏：
   - 去掉 AGENTS boilerplate
   - 替换绝对路径、URL、agent URI、邮箱、UUID、附件引用
5. 按 skill 聚类，并区分：
   - consumer evidence
   - maintenance evidence
6. 生成 markdown 报告，人工审阅后再决定是否提升为正式 eval。

## Command

```bash
uv run scripts/build_history_eval_report.py --global-history
```

如果 `xurl` 需要访问 provider 的本地数据库或 session 存储，可能需要在更高权限环境运行。

## Promotion Rule

- 有 2 条以上独立的 consumer evidence，才适合直接改写该 skill 的 trigger seeds。
- 只有 maintenance evidence 时，不应污染该 skill 的 runtime eval；这类记录更接近 `yao-meta-skill` 的执行证据。
- execution cases 仍应人工补上期望输出和 key checks，不建议从历史文本全自动生成。
