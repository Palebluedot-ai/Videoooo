# 05 · 工业级 SOP：流水线 / 分镜 / 三视图 / 设定集

> **日期：2026-08-20**｜**这是「方法」那一半**，补 04 号笔记（能力阶梯）的缺口。
> **来源等级**：主体来自 [OpenMontage](https://github.com/calesthio/OpenMontage) 的 cinematic 流水线源文件**逐字读取**（48.9k★，10 个 director 角色文件）+ 传统动画产业的 character sheet 规范。**不是我编的流程**。

---

## 零、为什么先给流水线，再给单项手艺

工业级的意思不是「画得好」，是**每个环节有交付物、有验收、有闸**。
OpenMontage 把它编码成 8 个阶段 + 10 个 director 角色——这是目前能拿到的、最接近「AI 视频工业 SOP」的东西。

---

## 一、主流水线：8 阶段 · 2 道人工闸 · 4 条硬限制

```
research → proposal → script → scene_plan → assets → edit → compose → publish → Final QA
```

| 阶段 | 产出物 | 说明 |
|---|---|---|
| research | `artifacts.research` | 调研简报，后面所有事实性主张都要能追溯到它 |
| **proposal** | `artifacts.proposal` + **delivery_promise、renderer_family 锁定** | 🚧 **人工闸 G1** |
| script | `artifacts.script` | beat map（见第二节） |
| **scene_plan** | `artifacts.scene_plan` + **hero_moments 定义** | 分镜（见第三节） |
| assets | `artifacts.assets` | 资产（见第五节） |
| edit | `artifacts.edit` | 剪辑决策 |
| compose | `artifacts.compose` | 合成与调色（见第六节） |
| publish | `artifacts.publish` | 交付 |

### 两道人工闸（原文 `human_approval_default: true`）
1. **proposal 之后** —— "Has the user approved the proposal?"
2. **任何昂贵/不可逆步骤之前** —— 必须 "present [decision] whether the run is a sample or batch"，切换 provider/model 需用户同意

> 每个 director 文件末尾都有同一句硬规则：checkpoint 到 `status="awaiting_human"` 然后 **END YOUR TURN**——不许在同一次回复里往下推进。

### 四条硬限制
| 项 | 值 |
|---|---|
| 每阶段最多返工 | **3 次** |
| 每对阶段最多回退 | **1 次** |
| 全流程最多回退 | **3 次** |
| 最大墙钟时间 | **12 分钟** |
| 预算告警线 | **90%** |

### ⛔ 静默降级禁令（原文逐字）
> "If Remotion or clip generation breaks a motion-led brief, **stop and bubble the issue to the user instead of quietly switching mediums**."

**这条直接对应我们 AGENTS.md 的「完成 = 贴证据」纪律。** 工具跑不动就上报，不许偷偷换个便宜路子交差。

---

## 二、剧本层 SOP：beat map 四件套

**强制结构**：
```
Hook → Escalation → Reveal → Landing
```
长片可加 **一个** midpoint turn，但 "should not become essay-like in complexity"。

**必填字段**：
`beat_map` · `dialogue_selects` · `title_card_copy` · `music_turns` · `silence_windows`

> 📌 注意 `silence_windows` 是**必填字段**——沉默是被当作设计对象管理的，不是「没声音的地方」。

**台词开采的四类目标**（从素材语音里挖）：
strong standalone lines · emotional phrases · concise declarations · reveal phrases
没有可用台词时：走 title-led 或 narration-led，**并在 metadata 里写明**。

**标题卡标准**（原文）：
> "fewer words, more contrast, more whitespace, more timing precision" —— 预告片式的感觉

**验收四条**：beat map 干净地递进 · 台词与标题卡不重复 · reveal 落得清楚 · landing 给出"final feeling or action"

**事实核查协议**：不确定的主张用 `web_search` 查，记为 `category="visual_accuracy_check"`，所有事实性主张必须能追溯到 research brief。

---

## 三、⭐ 分镜层 SOP：5-Aspect Shot Breakdown（强制）

> scene director 的职责原文：决定 "how each cinematic beat will look and transition. **This is where mood becomes a visual plan.**"

**每一个 beat——尤其 hero frames——必须五个维度全部写明：**

| # | 维度 | 要写什么（原文） |
|---|---|---|
| 1 | **Subject** | "type + key visual attributes; **if multiple, how to disambiguate**" |
| 2 | **Subject Motion** | "actions in **temporal order**; subject↔object / subject↔subject interactions" |
| 3 | **Scene** | "overlays (**separately!**) + POV + setting + time of day + scene dynamics" |
| 4 | **Spatial Framing** | "shot size + position-in-frame + **depth (FG/MG/BG)** + camera-height-relative" |
| 5 | **Camera** | **书写顺序被规定死**：<br>"playback speed → lens distortion → height → angle → focus/DoF → steadiness → movement" |

### 三条硬规则

1. **Overlays 规则**：叠加元素 "**NOT** part of the scene's foreground/midground/background depth axis. List them separately in scene metadata."
   → 字幕/图形不进景深轴，单列进 metadata。混进去 = 模型会试着把字幕当场景里的物体渲染。

2. **Hero frame 规则**（原文，值得贴墙上）：
   > **"Vague hero-frame specs are the single most common failure mode"**

3. **转场克制**：只用一个 "small set"——hard cut、fade、dissolve、restrained push/punch-in。

### 验收清单
每个 beat 都有 treatment · hero frames 五维全写明 · support inserts 有理由 · overlays 在 metadata 里而不在景深描述里 · 视觉语言一致

### 📐 5-Aspect 与五段式的关系（重要，别混）

| | **5-Aspect Shot Breakdown** | **五段式提示词** |
|---|---|---|
| 是什么 | **规划层**——想清楚这个镜头是什么 | **表达层**——把它翻译给模型 |
| 产出 | scene_plan（人读的分镜表） | prompt 文本（模型读的） |
| 何时用 | 写 prompt **之前** | 规划完之后 |
| 来源 | OpenMontage cinematic pipeline | Mx-Shell |

**映射关系**（⚠️ 我的对照，非引文）：

| 5-Aspect | → 五段式的哪一段 |
|---|---|
| Subject | ② 人物与基础设定 |
| Subject Motion | ⑤ 分镜时间轴的「动作」 |
| Scene | ② 的场景行 + ① 核心主题 |
| Spatial Framing | ④ 运镜规则的景别/角度 |
| Camera | ③ 氛围画质（器材）+ ④ 运镜 + ⑤ 的「镜头」 |

> **弯路警告**：直接上五段式写 prompt = 跳过规划层。5-Aspect 才是「想清楚」的地方，五段式只是把想清楚的东西翻译出去。想都没想清楚，翻译得再漂亮也是空的。

---

## 四、⭐ 三视图 / 角色设定集 SOP

### 完整 character sheet 六件套

| 件 | 内容 |
|---|---|
| **Character Turnaround** | 360° 转身图（下详） |
| **Expression Sheet** | 表情表——喜/怒/哀/惊/惧等 |
| **Pose Sheet** | 姿态表——"how a character moves and behaves in different situations"，含 T-pose、关键动作姿态、剪影视图 |
| **Props** | 道具 |
| **Color Palette** | 色彩方案，**每个色块必须标名称或代码（RGB / HEX / Pantone）** |
| **Annotations** | 注释——比例关系、独特特征、设计要点 |

### Turnaround 的标准角度

**正面（front）· 3/4 前 · 侧面（profile）· 3/4 后 · 背面（back）**

（部分规范简化为四视图：frontal / right side / left side / back）

### 产线位置与使用者
前期设定阶段产出，**贯穿 concept → final frame 全流程**；使用者是 storyboard artists、animators、character designers、directors——它是**沟通契约**，不是画着好看。

### 🤖 AI 时代怎么做三视图

拿一张角色参考图，用这条 prompt（**原样引用**）：

```
Create a four-panel turnaround for this man to show his frontal,
his right side, his left side and his back, in a white and grey background.
```

**为什么这么写有效**：
- **必须用 "turnaround" 这个词**——它是行业标准的正投影术语，模型认这个词
- **明确列出每一个视图**，别指望模型自己补全
- **白灰背景**——制作友好，后续抠图/参考都方便
- 输入单张图即可（正面或带角度都行）

### 💡 这一节和 L3 一致性的关系（关键）

> **参考图条件化，喂进去的应该是 turnaround，不是随手一张图。**

第 02 号笔记里那条「图片质量不高就别喂参考图」讲的是**质量**；这里讲的是**形态**——一张正面照只锁住了正面，模型转到侧面时就自由发挥了。turnaround 锁的是 360°。

这就是**「角色一致性」从玄学变成工程**的地方：不是反复调 prompt 求模型别变脸，是**先把设定集做出来当契约**。

---

## 五、资产层 SOP：三条防烧钱规则

1. **Sample-before-batch**（原文）：
   > "Before batch-generating support assets, produce **one sample of each expensive generated type** and show the user."

2. **Provider disclosure**（原文）：出样之前就要告诉用户 —— "exactly which generation path will be used: **tool, provider, model or variant, generation mode, why it was selected**"

3. **Rights notes**：metadata 必须含 `rights_notes` 做出处留痕
   → 你的仓是 public 的，这条对你是硬需求（AGENTS §1 版权禁令）

**motion 检查**：若 `proposal_packet.metadata.motion_required = true`，必须有真实运动素材或生成的视频片段——静帧糊弄不过去。

---

## 六、合成层 SOP

**runtime 锁定**，三选一：Remotion（视频主导）/ Hyperframes（动态字幕、HTML/GSAP/Three.js）/ FFmpeg（**仅**源素材拼接，不做合成）

> ⛔ **"Silent swap to another runtime (including FFmpeg Ken Burns) is a CRITICAL governance violation."**

**保护项**：
- 音频——"Allow quiet moments, impact moments, clear dialogue or narration, controlled music swells"
- 调色/锐化——**不能伤脸和字**（"must not damage faces or text"）
- letterbox、24fps 意图、重调色——**只在真的对片子有帮助时才用**

**验收四点**：opening frame · reveal beat · final landing · subtitle readability

**要避开的坑**：音频压平、乱加信箱式黑边、伤脸伤字、未批准就换 runtime

---

## 七、把 SOP 接回能力阶梯

**04 号笔记的 L0 已改。** 原来的 L0（拉片找 12 个破绽）是**测试**不是**方法**——测试不该单独占一级。

| 改动 | 内容 |
|---|---|
| **新 L0 = 前期设定** | 做设定集 + 写 5-Aspect 分镜表。**这是方法** |
| **12 个破绽降级为验收检查表** | 不再是一级，而是 **L1 起每一级交付时都要过的 QC 清单**——工业界的 QC gate 本来就贯穿全程，不是入门考试 |

---

## 八、证据等级

| 内容 | 等级 |
|---|---|
| 8 阶段流水线、5-Aspect、beat map、资产三规则、合成规范 | ✅ **OpenMontage 源文件逐字读取**（48.9k★，38 贡献者，2 天前活跃）。⚠️ 但这是**一个开源项目的实现**，不是行业标准委员会发布的规范 |
| character sheet 六件套、turnaround 标准角度 | ✅ 传统动画产业通行规范，多来源一致 |
| turnaround 生成 prompt | ✅ 原样引用，✅ 但单一来源 |
| 5-Aspect ↔ 五段式映射表 | ⚠️ **我的对照，非引文** |
| 「turnaround 优于单张参考图」 | ⚠️ **我的推论**——逻辑成立（锁 360° vs 锁一个面），但**没找到直接实证**。这是你 L3 该亲手验的第一件事 |
