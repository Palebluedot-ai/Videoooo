<!-- instantiated-from kit/phase-card-template.md @ v0.18.0 -->
---
phase: "L0"
self_contained: true
required_context:
  - domain: "docs/notes/05-industrial-sop.md（SOP 正文·本卡主要依据）；docs/notes/04-capability-ladder.md（阶梯与判据）；templates/ 三个模板"
pointer_format: "file:line-line"
max_feedback_loop_min: 30
setpoint: "交付一套角色 turnaround（五视图 + HEX 色标）与一张 5-Aspect 分镜表，且分镜表能通过 check_shotlist.py 校验"
disturbance: "本卡不生成任何视频（L1 才生成）；不装 ComfyUI、不下本地模型（L4/L6 才碰）；不把 Mx-Shell 原始提示词文件拷进本仓（P5 版权禁令，本仓 public）；不追长片——先做 3-5 个镜头的量"
---

# Phase L0 — 前期设定

> **这一级是方法，不是测试。** 原 L0「拉片找 12 破绽」是诊断，已降级为 L1 起每级都过的验收 QC 门。
> **为什么在最底层**：原文「**Vague hero-frame specs are the single most common failure mode**」——后面每一级都在消费这一级的产出。

## 0. 前置检查

- [ ] 已读 `docs/notes/05-industrial-sop.md` 第三节（5-Aspect）与第四节（三视图）
- [ ] 已定题材与角色（**优先选无真人脸的角色**——一致性问题在选题时绕开，比在提示词层硬扛便宜十倍）
- [ ] 已确认角色里哪些元素会踩模型崩溃维度（动态空间关系 19–21% / 动态属性变化 8–24% / 复杂情节 9–11%）

## 1. 验收标准

- [ ] **beat map 就位**：`docs/preproduction/beat-map.md` 填完，Hook / Escalation / Reveal / Landing 四段齐，且 **`silence_windows` 非空**（沉默是必填设计对象，不是「没声音的地方」）
- [ ] **turnaround 五视图产出**：正面 / 3⁄4 前 / 侧面 / 3⁄4 后 / 背面。用规范 prompt（`turnaround` 这个词不能改），白灰背景
- [ ] **五视图比例一致**：对着同一条基准线检查头顶 / 肩 / 腰 / 脚——贴对比图作证
- [ ] **色标带代码**：Color Palette 每一块标了 HEX，不是只贴色块
- [ ] **规避方案写下来了**：character-sheet 的「一致性自检」四问全部作答，尤其「有没有在设计层绕开」
- [ ] **5-Aspect 分镜表 ≥3 个镜头**，其中 ≥1 个标 `hero: true` 且五维全填
- [ ] **机器校验通过**（这条是硬门，v2 起用 --strict）：
      ```
      uv run --with pyyaml tools/check_shotlist.py --strict docs/preproduction/shots.yaml
      bash tools/run_fixtures.sh
      ```
      两条都退出码 0，贴完整输出。第二条确认尺子本身没坏（8 个 fixture 全符合预期）
- [ ] **一帧视频都没生成**（本卡的纪律；生成是 L1 的事）

## 2. 内联要点

- **参考模式指针**：照 `templates/shots.example.yaml` 里 S01 那个填满的示例写，不要另创格式
- **camera 顺序不能乱**：`playback_speed → lens_distortion → height → angle → focus_dof → steadiness → movement`，校验器会红
- **overlays 单列**：字幕/图形写进 `scene.overlays`，**绝不**写进 `spatial_framing` 的 FG/MG/BG——混进去模型会试着把字幕当场景里的实物渲染
- **别写「电影感 / 4K / 高细节」**：AI 锚不住，写具体器材型号（`IMAX胶片摄影机 + Panavision C系列 35mm f4`）。校验器有空泛词黑名单
- **五段式先别写**：5-Aspect 是规划层，五段式是表达层。想清楚了再翻译
- **turnaround 是 L3 的资产源头**：这里做的五视图，L3 拿去当参考图条件化的输入。⚠️「turnaround 优于单张参考图」是推论无实证——**L3 第一件事就是亲手验它**

## 2b. Loop 台账

| 日期 | Loop# | 目标（一句话） | 验收命令 | 结果 |
|---|---|---|---|---|
| 2026-08-19 | 0 | 骨架初始化 | `ls docs/phases/` | 卡已建 |
| 2026-08-19 | 1 | deep-research 摸版图 | 105 agent / 验 25 条 | 确认 14 · 否 11 |
| 2026-08-19 | 2 | 定向调研：五段式方法论 | 见 notes/02 | 方法论落盘 |
| 2026-08-20 | 3 | deep-research 打能力阶梯 | 107 agent / 验 25 条 | 确认 10 · 否 14；**阶梯不存在**，自建 L0-L6 |
| 2026-08-20 | 4 | 补 SOP 缺口 | 见 notes/05 | 流水线/分镜/三视图 SOP 落盘 |
| 2026-08-20 | 5 | L0 工作包 | check_shotlist v1 | ⚠ 后发现 v1 有两个静默放行洞 |
| 2026-08-20 | 6 | 修尺子 v2 + 15 节排程 | `bash tools/run_fixtures.sh` | 8/8 符合预期，每条报错指名道姓；排程落 notes/07 |
