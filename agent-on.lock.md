<!-- instantiated-from kit/agent-on-lock-template.md @ v0.18.0 -->
# agent-on.lock

## pin
agent-on @ v0.18.0 (adee1198cf57b954d5fe44a418f7c89d7919e4a5)   <!-- 只有口令「agent-on 升级」允许改这一行 -->
本地路径：/Users/chao/Projects/Agent-On
model：claude-opus-5 / 保费档位：高

## last_settlement
<!-- 每次结账追加一行：<YYYY-MM-DD> → intake/<文件名>；首次为空 -->

## local_deviations（脚手架不合身登记簿）
| 日期 | 偏离了哪条规则/模板 | 为什么 | 状态 |
|---|---|---|---|
| 2026-08-19 | BOOTSTRAP §1.5 规划链：M 档「MRD 必 / PRD 必 / 技术方案必」全跳过 | 本项目是个人**学习仓**（学 AI video + 记笔记 + 写实验代码），没有市场、没有用户、没有产品范围可写。硬套 MRD/PRD 是高射炮打蚊子。改用 phase 卡承载「学习里程碑」 | 生效中 |
| 2026-08-19 | BOOTSTRAP §2 第 1 步目录：另加 `docs/notes/` 与 `docs/experiments/` | 学习仓的主产物是笔记与实验，不是 src/。骨架目录需为学习型项目留位置 | 生效中 |
| 2026-08-19 | AGENTS §2 铁律 L1 TDD 按车道分级（Explore 不强制测试，进 `tools/` 才转 Ship） | 学习实验本就是「错误不算错误的域」，对试模型/试 prompt 强制 TDD 会杀掉学习速度；但复用工具必须补测试 | 生效中 |
| 2026-08-19 | 新增本项目特有硬约束「笔记真实性红线」（agent-on 无对应条款） | 学习型项目的头号事故不是代码 bug，是 **AI 凭记忆写笔记 → 用户学到假知识**。AI video 领域半年换代，模型名/价格/参数极易过时。这条可能值得回流 agent-on（学习型项目模板缺口） | **候选回流** |
