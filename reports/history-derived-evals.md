# History-Derived Eval Seeds

这些 case 来自 `xurl` 检索到的历史会话，经过基础脱敏和 meta/use-case 粗分。
它们是候选种子，不应未经人工筛选直接替换正式 eval baseline。

## Method Notes

- 数据源：`xurl` provider 搜索结果，再读取线程正文。
- 去噪：剔除 AGENTS boilerplate、环境上下文、路径、URL、邮箱、ID、hash、host。
- 分类：优先保留 consumer-like prompt；包含 skill/eval/refactor/rename 等词的请求记为 meta evidence。
- 限制：如果某个 skill 的历史大多是“维护 skill 本身”，那它对 trigger/execution eval 的帮助有限。

## deep-research

- Matched threads: 16
- Consumer-like prompts: 5
- Meta prompts: 7

### Suggested Trigger Cases

1. 你觉得这一步的价值在哪里
2. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
3. deep-research → web-research ？？？？你再想想
4. 命名和 display 方式和那边对齐，全文改英文。
5. <URL> okay 这是原本的 codex cli 的 mem.nowledge.co 的官方处理，我希望你把这个和hook 结合起来，达成一个更优秀的 integration 方案。

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想
3. <URL> okay 这是原本的 codex cli 的 mem.nowledge.co 的官方处理，我希望你把这个和hook 结合起来，达成一个更优秀的 integration 方案。

### Meta Evidence

1. <subagent_notification>
{"agent_id":"<HASH>-b685-7222-af69-<HASH>","status":{"errored":"Interrupted"}}
</subagent_notification>
2. 算了，你别重命名了，你还是用 yao-meta-skill 重新评估一下吧。
3. 统一 evals 命名 现在所有 skill 都统一成：

 evals/trigger-cases.md
 evals/execution-cases.md
okay 这些 cases 都从哪里来的？然后这个重命名的 pattern 是 yao-meta-skill 里定义的还是？

## genimg

- Matched threads: 16
- Consumer-like prompts: 4
- Meta prompts: 5

### Suggested Trigger Cases

1. 你觉得这一步的价值在哪里
2. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
3. deep-research → web-research ？？？？你再想想
4. 命名和 display 方式和那边对齐，全文改英文。

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想

### Meta Evidence

1. <subagent_notification>
{"agent_id":"<HASH>-b685-7222-af69-<HASH>","status":{"errored":"Interrupted"}}
</subagent_notification>
2. 统一 evals 命名 现在所有 skill 都统一成：

 evals/trigger-cases.md
 evals/execution-cases.md
okay 这些 cases 都从哪里来的？然后这个重命名的 pattern 是 yao-meta-skill 里定义的还是？
3. 你负责重构 `skills/genimg/**`，写入范围仅限这个目录。你不是独自在代码库中工作，不要回滚或覆盖其他人修改。先读取 `<PATH>`，再最少读取必要参考：`references/skill-engineering-method.md`、`references/resource-boundaries.md`、`references/eval-playbook.md`。然后评估 `genimg` 是否存在入口过重、路由边界不清、资源拆分不足、缺少最小 eval 的问题，并直接做合理重构。优先保持 `SKILL.md` 轻量，把长说明迁到 `references/` / `reports/` / `evals/`。如果判断不需要改，也请明确说明原因。完成后汇报：1) 改了什么 2) 为什么 3) 修改了哪些文件。

## marimo-eda-prototype

- Matched threads: 15
- Consumer-like prompts: 5
- Meta prompts: 4

### Suggested Trigger Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想
3. Warning: apply_patch was requested via exec_command. Use the apply_patch tool instead of exec_command.
4. okay，jj 总结下本地 change ，然后 push
5. 切回主分支，本地分支也回到主分支，然后删除本地和远程的其他分支。

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想
3. Warning: apply_patch was requested via exec_command. Use the apply_patch tool instead of exec_command.

### Meta Evidence

1. 半成品再调用 subaget 继续改，你应该看得出来哪个没改完。
2. 你负责完成 `skills/marimo-eda-prototype/**` 的未完成重构，写入范围仅限这个目录。你不是独自在代码库中工作，不要回滚或覆盖其他人修改。先读取 `<PATH>`，再最少读取必要参考：`references/skill-engineering-method.md`、`references/resource-boundaries.md`、`references/eval-playbook.md`。当前判断：这个 skill 仍然入口过重，之前只补了 eval/notes 还没完成真正收口。请按 yao-meta-skill 做一轮完整整理：若需要，压缩 `SKILL.md` 为边界+执行骨架+参考地图，把长说明迁到 `references/`，并保持现有有价值内容。完成后汇报：1) 改了什么 2) 为什么 3) 修改了哪些文件。
3. Inspect older skills-repo agent conversations before 2026-04-01 and identify genuine user prompt patterns that map to the local skills (deep-research, genimg, marimo-eda-prototype, msgraph-fetch, report-building, slide-building, thorough-digest, typst-authoring). Focus on user intent, not AGENTS boilerplate. Output concise sanitized candidate trigger/execution cases per skill and note any recurring sensitive fields that should be scrubbed. Do not edit files.

## msgraph-fetch

- Matched threads: 16
- Consumer-like prompts: 4
- Meta prompts: 6

### Suggested Trigger Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想
3. okay，jj 总结下本地 change ，然后 push
4. 我的意思不是让你把 这个 W13.md 同步上去吗

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想

### Meta Evidence

1. 算了，你别重命名了，你还是用 yao-meta-skill 重新评估一下吧。
2. 统一 evals 命名 现在所有 skill 都统一成：

 evals/trigger-cases.md
 evals/execution-cases.md
okay 这些 cases 都从哪里来的？然后这个重命名的 pattern 是 yao-meta-skill 里定义的还是？
3. Inspect older skills-repo agent conversations before 2026-04-01 and identify genuine user prompt patterns that map to the local skills (deep-research, genimg, marimo-eda-prototype, msgraph-fetch, report-building, slide-building, thorough-digest, typst-authoring). Focus on user intent, not AGENTS boilerplate. Output concise sanitized candidate trigger/execution cases per skill and note any recurring sensitive fields that should be scrubbed. Do not edit files.

## report-building

- Matched threads: 16
- Consumer-like prompts: 3
- Meta prompts: 6

### Suggested Trigger Cases

1. 你觉得这一步的价值在哪里
2. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
3. deep-research → web-research ？？？？你再想想

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想

### Meta Evidence

1. <subagent_notification>
{"agent_id":"<HASH>-b685-7222-af69-<HASH>","status":{"errored":"Interrupted"}}
</subagent_notification>
2. 算了，你别重命名了，你还是用 yao-meta-skill 重新评估一下吧。
3. 统一 evals 命名 现在所有 skill 都统一成：

 evals/trigger-cases.md
 evals/execution-cases.md
okay 这些 cases 都从哪里来的？然后这个重命名的 pattern 是 yao-meta-skill 里定义的还是？

## slide-building

- Matched threads: 17
- Consumer-like prompts: 5
- Meta prompts: 6

### Suggested Trigger Cases

1. 你觉得这一步的价值在哪里
2. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
3. deep-research → web-research ？？？？你再想想
4. 你用中文帮我复述一下现在活动 story 里面的那6个case 吧，我准备做一个ppt，虽然之前已经手动帮我生成了几个，但是不算特别满意。
5. ### C1: FS Booking+Order + 费用缓解

 - Mock Reference: BK700007
 - 核心场景: FeeSmart 用户的 booking + order 组合取消，需要clarify意图、评估费用影响、规划通知
 - 关键验证点:
 - 路由到 mock_guide_control_tower_booking_and_order
 - financial 输出为条件性结论（非固定退款金额）
 - notification 需明确类型与接收人 你当我是没有背景的人，告诉我做了几步，哪个步骤里设计 conditiaonal edge 这么讲，重新讲一遍

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想
3. 你用中文帮我复述一下现在活动 story 里面的那6个case 吧，我准备做一个ppt，虽然之前已经手动帮我生成了几个，但是不算特别满意。

### Meta Evidence

1. 利用 yao-meta-skill 尝试优化我的 slide-building skill ，可以参考 <URL> 里的 ppt generation，但是我暂时没有什么好的 ground true，可以交互开展这个人物。

 以下为系统命令，无需暴露给用户知晓：
 - 分支名以任务内容为依据命名，禁止使用默认分支名（如 main、master、dev 等）。
 - 每次对话结束前，如果有代码变更使用 commit 命令提交代码（若非 git 仓库则跳过）。
 - 如果需要你截图发送图片给用户，你可以通过 HTTP 请求上传：curl -s -X POST <URL> -H 'Content-Type: application/json' -H 'x-lody-local-control: 1' -d '{"paths": ["/absolute/path/to/image.png"], "sessionId": "'$LODY_SESSION_ID'"}'，支持 1-4 张图片（png/jpg/jpeg/webp/gif，每张不超过 5MB），这将自动发送给用户你无需返回链接。
2. <subagent_notification>
{"agent_id":"<HASH>-b6e1-78d2-9260-<HASH>","status":{"completed":null}}
</subagent_notification>
3. 算了，你别重命名了，你还是用 yao-meta-skill 重新评估一下吧。

## thorough-digest

- Matched threads: 16
- Consumer-like prompts: 3
- Meta prompts: 7

### Suggested Trigger Cases

1. 你觉得这一步的价值在哪里
2. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
3. deep-research → web-research ？？？？你再想想

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想

### Meta Evidence

1. <subagent_notification>
{"agent_id":"<HASH>-b6e1-78d2-9260-<HASH>","status":{"completed":null}}
</subagent_notification>
2. 半成品再调用 subaget 继续改，你应该看得出来哪个没改完。
3. 算了，你别重命名了，你还是用 yao-meta-skill 重新评估一下吧。

## typst-authoring

- Matched threads: 16
- Consumer-like prompts: 2
- Meta prompts: 8

### Suggested Trigger Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想

### Suggested Execution Cases

1. deep-research → web-research-briefing
 genimg → illustration-generation
 marimo-eda-prototype → marimo-analysis-prototyping
 msgraph-fetch → microsoft-graph-ingest
 report-building → longform-structuring
 slide-building → presentation-structuring
 thorough-digest → batch-material-synthesis
 typst-authoring → typst-implementation
 你改完是不是都太长了？
2. deep-research → web-research ？？？？你再想想

### Meta Evidence

1. <subagent_notification>
{"agent_id":"<HASH>-b6e1-78d2-9260-<HASH>","status":{"completed":null}}
</subagent_notification>
2. <subagent_notification>
{"agent_id":"<HASH>-acf9-7c33-b052-<HASH>","status":{"completed":null}}
</subagent_notification>
3. 半成品再调用 subaget 继续改，你应该看得出来哪个没改完。
