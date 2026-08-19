<!-- instantiated-from kit/phase-card-template.md @ v0.18.0 -->
---
phase: "S0.1"
self_contained: true
required_context:
  - domain: "AGENTS.md §1 笔记真实性红线 / 代码即证据 / 密钥红线；docs/requirements.md 待拍板区 Q1（第一条主线工具）"
pointer_format: "file:line-line"
max_feedback_loop_min: 30
setpoint: "本机能用一条命令，从一句文字提示生成出一个真实视频文件；并留下一篇全部结论都有实跑或官方文档背书的笔记"
disturbance: "禁碰：不搭 Web 界面、不做产品化（暂停项 P1）；不自动调付费 API（P2，每次调用前先报预估花费问一句）；生成的视频不入 git（大文件红线）；不引入 Docker/训练管线（P4）"
---

# Phase S0.1 — 环境就绪 + 第一条 AI video 链路

> 学习仓约定：一张 phase 卡 = 一个**学习里程碑**，不是功能切片。「做到」的标准是「跑通了并且真的搞懂了」，证据是命令输出 + 笔记里那条「我原以为 X，实际是 Y」。

## 0. 前置检查

- [ ] **用户已拍板第一条主线工具**（docs/requirements.md 待拍板区 Q1）——没拍板不开工，别自己替用户选一个模型就冲

## 1. 验收标准

- [ ] **环境就绪**：`uv --version` 与 `ffmpeg -version` 各有输出（贴出来）；`requirements.txt` 存在且 `uv pip list` 里能看到所选 SDK
- [ ] **工具版图笔记**：`docs/notes/00-landscape.md` 写成——至少 4 个主流 AI video 工具/模型，每个含「能力边界 / 计价 / 拿什么接口调」，**每条带官方文档链接 + 查阅日期**（凭记忆写 = 违反 §1 头号红线）
- [ ] **选型理由落盘**：为什么选这条主线（而不是另外三条），一句话写进 `docs/notes/00-landscape.md` 末尾，并同步进 `docs/requirements.md` 已确认区
- [ ] **实验可跑**：`docs/experiments/e01-first-clip/run.py` 存在，从 `.env` 读 key（不硬编码），一条命令能跑：贴出实际命令 + 完整输出
- [ ] **真的产出了视频**：`ffprobe` 对产出文件的输出贴进笔记（时长/分辨率/帧率/编码），并留一张首帧截图（≤200KB）作为证据
- [ ] **认知差记录**：`docs/notes/01-first-clip.md` 至少一条「我原以为 X，实际是 Y」——没有认知差就说明没真学到，回去多试两个参数
- [ ] **花费记录**：本次实验实际消耗（credits / 美元 / 本地跑则记耗时+显存）写进笔记；付费调用前是否问过用户，也记一行
- [ ] **密钥没泄**：`git check-ignore -v .env` 有输出，且 `git log -p | grep -iE '(api[_-]?key|token).{0,4}=.{12}'` 无命中（贴命令与结果）
- [ ] **收口**：`docs/state/progress.yaml` 状态更新 + `dashboard.html` 重绘 + 一个中文语义化 commit

## 2. 内联要点

- **先小后大**：第一次跑用最短提示、最低分辨率、最短时长——把链路跑通比把画面跑好重要十倍。画质调优是 S0.2 的事
- **集成探针**（接新外部服务必做）：真调 API 前先 dump 一次真实响应（`print(resp)` 原样打出来），跟你以为的字段形状对账，再写解析——**别照着记忆里的 SDK 签名写**，AI video 各家 API 半年一变
- **异步是常态**：视频生成基本都是「提交任务 → 轮询 → 拿 URL」，不是同步返回。第一版就把轮询和超时写对，别写成阻塞死等
- **ffmpeg 是底座**：不管用哪家，最后拼接/转码/抽帧都靠它。这一卡顺手把 `ffprobe` 看信息、`ffmpeg -ss` 抽帧两条命令记进笔记
- **扫坑指针**：对照 agent-on `bench/cases/README.md` 使用时机表的「接外部服务」一节，动手前先认一遍别人踩过的坑

## 2b. Loop 台账（跨会话续跑读这里）

| 日期 | Loop# | 目标（一句话） | 验收命令 | 结果 |
|---|---|---|---|---|
| 2026-08-19 | 0 | 骨架初始化，卡就位待拍板 | `ls docs/phases/` | 卡已建，等 Q1 拍板 |
