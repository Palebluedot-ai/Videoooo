# 04 · 能力阶梯（自建 —— 因为公开资料里不存在）

> **日期：2026-08-20**｜第二轮 deep-research：107 agent / 抓 25 源 / 抽 125 条声称 / 验 25 条 / 3 票对抗验证 → **确认 10 条、否掉 14 条**。
> 本文是**你要的那份「一点一点学」的文档**的正文。

---

## 零、本轮最重要的结果是一个**否定结论**

**你要的那种「能力阶梯」，公开资料里不存在。**

证据不是「没搜到」，而是**这类主张被系统性否决**——本轮被 0-3 / 1-2 否掉的 14 条里，有 7 条恰好全是「某机构课程发布了能力判据 / 硬门禁 / 能力分解」这一类：

| 被否的主张 | 票 |
|---|---|
| Comfy Compositing 三层硬门禁能力阶梯 | 0-3 |
| 每层有行为化 exit criterion | 1-2 |
| Studio Arts 定义了「意图性导演 / 视觉连续性 / 剪辑纪律」三项非生成技能 | 0-3 |
| Studio Arts 把资产库作为硬前置 | 0-3 |
| Curious Refuge 九阶段课程结构 | 0-3 |
| NYU Tisch 三能力域 | 0-3 |
| Full Sail 三模块分解 | 0-3 ×3 |

**多个独立验证者对同一类主张一致否决 = 这类主张普遍缺乏可核实依据。**

唯一被逐字核实的机构大纲（[Studio Arts](https://studioarts.com/ai-for-filmmaking/)，洛杉矶，8 周 30 小时 $1,000，7 阶段）是**生产流程顺序**，不是能力难度阶梯——**零能力判据、零关卡考核、零卡点数据**。

> 📌 **所以这份阶梯是我构造的。** 地基是三块经过对抗验证的学术证据（下一节），构造过程是我的推论，**已逐处标注**。你可以推翻任何一级。

---

## 一、先分清两条轴（混淆这两条 = 第一个弯路）

| | **生产流程轴** | **能力难度轴** |
|---|---|---|
| 回答什么 | 做一部片**按什么顺序做** | **先练什么后练什么** |
| 公开资料 | ✅ 有（Studio Arts 七段） | ❌ **不存在** |
| 例子 | 概念脚本 → 视觉开发 → hero frames → 图生视频 → 画质增强 → 声音配乐 → 终混交付 | 本文第三节 |

**为什么必须分开**：按生产流程学，你第一天就要同时面对分镜、生成、调色、混音——每一样都不会，每一样都在拖后腿。按能力难度学，你一次只练一件事。

---

## 二、地基：三块可引用的证据

### 2.1 ⭐ 决定学习顺序的那条线：superficial vs intrinsic faithfulness

[VBench-2.0](https://arxiv.org/abs/2503.21755)（preprint，v1 2025-03 / v2 2025-08）明确区分两层，原文逐字：

> superficial faithfulness（逐帧美感、时序一致、基本 prompt 遵循）—— **"many aspects of superficial faithfulness are now approaching saturation"**
> intrinsic faithfulness —— **"physical laws, commonsense reasoning, anatomical correctness, and compositional integrity"**
> **"the new frontier shifts from merely appearing real to being intrinsically real."**

**关键：intrinsic 不是全面失败，是「特定维度崩溃」**（Table II，⚠️ 2025-03 那批模型 Sora/Kling/HunyuanVideo/CogVideoX，**不可当当前值**）：

| 维度 | 得分 | 对你意味着 |
|---|---|---|
| Commonsense / Instance Preservation | **92–94%** | 🟢 模型已包办，**不是你的学习内容** |
| Human Anatomy | **86–88%** | 🟡 大体可以，但手仍是经典破绽 |
| Dynamic Attribute Change | **8–24%** | 🔴 **崩** |
| Dynamic Spatial Relationship | **~19–21%** | 🔴 **崩** |
| Complex Plot | **9–11%** | 🔴 **崩得最狠** |

> **这张表就是学习路线图。**
> 模型已饱和的维度 → 别花时间。
> 模型崩溃的维度 → **这才是你的手艺所在，而且必须靠「改设计绕开」，不是靠「把 prompt 写得更好」。**

### 2.2 质量的可测量分解（两套 rubric）

| rubric | 结构 | 覆盖 |
|---|---|---|
| [AesRM](https://arxiv.org/abs/2604.28078)（preprint 2026-04-30） | **3 维 × 15 细则**：Visual Aesthetics（色彩/光照/影调）· Visual Fidelity（结构稳定/纹理连续/锐度/伪影）· Visual Plausibility（构图/焦距/运镜/画面丰富度/专业电影语言） | 与六位美院背景专家共同设计；每条打分 ∈ {−1,0,1} |
| [VBench-2.0](https://arxiv.org/abs/2503.21755) | **5 维 × 18 子能力**：Human Fidelity 3 / Creativity 2 / Controllability 7（含 Camera Motion）/ Physics 4 / Commonsense 2 | 18 名标注者 284 小时人工对齐 |

**🚨 必须知道的范围警告**：两套 rubric **只覆盖单镜头视觉子集**——
**完全不含剪辑节奏、色彩管理/LUT、声音设计/混音、叙事结构、表演。**
VBench-2.0 作者自陈只评 5–10 秒片段，「insufficient for complex narratives」。
→ 你的手艺有一半，学术界还没给出可测量分解（见 L6）。

### 2.3 「一眼假」的实操检查表：12 个破绽

学术表述是 superficial/intrinsic 之分；**实操版**来自 [opus.pro 的 12 tells](https://www.opus.pro/blog/ai-slop-aesthetic-12-tells)（blog，非学术）：

| # | 破绽 | 怎么查 | 怎么绕 |
|---|---|---|---|
| 1 | **手部变形** | 暂停数手指（4/6 根或帧间变化） | 选不露手的镜头 / 构图让手出画 |
| 2 | **切镜后背景物理不一致** | 云位置、阴影、光向在两镜间是否守恒 | 需人工控制多镜背景一致 |
| 3 | **平板恐怖谷打光** | 各环境镜头是否都是「晴朗午后」扩散光、无硬阴影 | 显式给光位与硬阴影 |
| 4 | **过饱和合成色** | 草太绿 / 肤色偏橙 / 天空均匀饱和无渐变 | 后期把饱和度压到真实传感器水平 |
| 5 | **运动过于顺滑（无微抖）** | 像飞行模拟器一样线性稳定 | **加微抖**（= 五段式的「呼吸感」行）/ 避免长焦推进 |
| 6 | **口型音画不同步** | 看 p/b/m 双唇音时嘴有没有闭合 | 调优的语音克隆 |
| 7 | **镜面反射崩坏** | 反射物错位/角度错/消失 | 画面里别放镜面 |
| 8 | **画面内文字变乱码** | 路牌书封是否帧间一致可读 | 场景里最小化文字 |
| 9 | **背景群演单腿走路** | 步态是否真的左-右-左 | 剔除背景密集的镜头 |
| 10 | **纹理重复平铺** | 草地砖墙沙滩有无可见重复块 | 手动处理 |
| 11 | **克隆声无呼吸** | 真人每 5–10 秒换气一次，AI 常不换 | 带韵律模型的 TTS |
| 12 | **TTS 平台调** | 有无重音起伏、列举加速、停顿 | 同上 |

> 📌 注意 1、2、7、9 全部落在学术上的 intrinsic 一侧（物理/解剖），3、4、5 落在 superficial 一侧——**两套框架对得上，互为印证。**

---

## 三、能力阶梯（⚠️ 我构造的，非引文）

**构造原则**（这一条是全文的方法核心）：
> **模型饱和的维度不学；模型崩溃的维度重点学，而且学的是「怎么绕开」不是「怎么写更好的 prompt」。**

---

### L0 · 看懂 —— 先长眼睛
**为什么在最底层**：看不出破绽，后面每一级的自检都是假的。

| | |
|---|---|
| **判据** | 给你一条 AI 片，能指出 **≥5 个**破绽并说出成因（对照 12 tells） |
| **练习** | 找 3 条 AI 短片 + 1 条专业实拍片，**逐条对照 12 tells 打分**，做成表格 |
| **工具** | LibTV「**逐帧拉片**」（把影视学院的拉片训练法产品化了）；或任何播放器逐帧 |
| **典型卡点** | 觉得「都挺好啊」——说明还没过关，回去对着 12 tells 再看一遍 |
| **投入** | 3–5 小时 |

### L1 · 单镜头出片 —— 手感
| | |
|---|---|
| **判据** | 一条 5–10 秒片段，**12 tells 里 0 命中** |
| **练习** | 同一条 prompt 抽 **10 次**，逐条标注命中了哪几个 tell，做成表 |
| **工具** | Seedance（BytePlus / 即梦 / LibTV ¥0.4 秒起）· 五段式提示词 · `/shortfilm-prompt` skill |
| **典型卡点** | 以为是 prompt 写得不好，**其实是选题落在了模型崩溃维度**（比如让主角边走边变色 = dynamic attribute change 8–24%） |
| **投入** | 1–2 天 |

### L2 · ⭐ 规避设计 —— 全篇最值钱的一级
**这一级是分水岭。**《丧尸清道夫》把主角设计成「机器人 + 像素表情屏」，不是美术偏好，是**在模型崩溃维度上改需求**——它是这一级的一个示例，不是这一级本身。

| | |
|---|---|
| **判据** | 给定任一模型崩溃维度（复杂情节 / 动态空间关系 / 动态属性变化 / 手），能提出 **≥2 种**美术或叙事上绕开它的方案 |
| **练习** | 写一份**约束清单**：你想做的题材里哪些元素会踩崩溃维度？每条给一个绕开方案。<br>例：想要「两人对话走位」→ 动态空间关系仅 ~19–21% → 绕法 a) 改成静止对峙 b) 改成单人 + 画外音 |
| **工具** | 就是纸笔。**这一级没有工具能替你做** |
| **典型卡点** | 习惯性想「再调调 prompt」。**记住：崩溃维度不是 prompt 能救的**（模型级得分 9–21% 意味着换谁写都一样） |
| **投入** | 半天想清楚，之后一直用 |

### L3 · 一致性工程
| | |
|---|---|
| **判据** | 3+ 个镜头里同一角色/场景，**人眼一眼认得出是同一个** |
| **练习** | 做一个 3 镜头连续片段，对比「只靠文字描述」vs「参考图条件化」的一致性差距 |
| **工具** | 参考图条件化（ingredients）· 每条 prompt **逐字重复**角色描述 · 角色资产库 |
| **典型卡点** | 参考图质量不够——**「图片质量不高就别喂参考图」**，AI 会模仿画风而不是模仿设计 |
| **⚠️ 证据等级** | **这一级是我的类比**（context engineering ↔ 资产工程）。两轮研究对这一轴**零存活证据**；唯一的机构级线索因验证器报错未能定论 |
| **投入** | 3–5 天 |

### L4 · 管线与批量 —— Claude Code 主场
| | |
|---|---|
| **判据** | 一条命令从 `shots.yaml` 跑到粗剪成片；某镜头失败能断点续跑 |
| **练习** | 批量出 20 条 + 每条自动落台账（prompt/模型/参数/seed/抽第几次/花费/**选没选中**） |
| **工具** | **OpenMontage**（48.9k★）· **ViMax**（12k★）· comfy-mcp · 自己写 |
| **典型卡点** | 照记忆写 SDK 调用。**先 `print(resp)` dump 真实响应再写解析** |
| **⚠️ 证据等级** | harness 类比同样**零存活证据**——但 OpenMontage / ViMax 的存在是工程事实（我已逐个核验） |
| **投入** | 3–5 天 |

### L5 · 自动筛选 —— 全网空白，最值钱的自研点
| | |
|---|---|
| **判据** | 机器排出的 top 3 里，**≥1 条**是你人眼也会选的 |
| **练习** | 拿 L4 攒的台账（尤其「选没选中」那一列）训一个筛选器 |
| **工具** | [VBench](https://github.com/Vchitect/VBench)（1.7k★ Apache-2.0，pushed 2026-03）· VLM-as-judge 自己搭 |
| **🚨 最重要的警告** | **模型级 eval ≠ 镜头级筛选。** VBench-2.0 / AesRM 是给**生成器排名**的基准，拿来「筛我今天抽的 20 条」是**超出设计意图的外推**。<br>而且 **FVD / CLIPScore 当筛选器在方法论上不成立**——FVD 是分布级指标，对单条视频**根本没有定义**（属范畴不适用，不是「不准」） |
| **可引的替代方向** | NeuS-V（把 prompt 转成时序逻辑规范做形式化验证，**与人类评估相关性高出既有启发式 5 倍以上**）· FiVE-Acc（VLM 做 Yes/No 语义询问）· Video-Bench 的 Chain-of-Query |
| **已被坐实的只有训练闭环** | AesRM 已用于对齐 Wan2.2-**TI2V-5B**（消费级小模型，非旗舰），**「评估→选片」那一半没被证明** |
| **投入** | 这是长期项目 |

### L6 · 非视觉维度 —— 学术界还没给出可测量分解
剪辑节奏 · 色彩管理/LUT · 声音设计/拟音/混音 · 叙事结构 · 表演

| | |
|---|---|
| **⚠️ 状态** | 两套 rubric **完全不覆盖**这些，本轮**零结论** |
| **只能怎么办** | **回传统影视教材**。AI 没有改变这一半的学习方式 |
| **实操锚点** | 12 tells 里的 #3/#4（打光、调色）、#6/#11/#12（声音）就是这一级的入口检查表 |

---

## 四、方法论映射表（诚实版）

| 编程范式 | AI 视频对应物 | 证据等级 |
|---|---|---|
| **eval** | **AIGVE**（AI-Generated Video Evaluation）| ✅ **唯一被证实已系统论述的一轴**：有专名、三范式分类法（metric-based / human-involved / model-centered）、五条研究线、三个演进阶段，**CVPR 2026 设 VGBE workshop** |
| prompt engineering | 视频提示词结构化（五段式等） | ⚠️ **我的类比**。本轮零存活证据（社区实践大量存在，但达不到对抗验证门槛） |
| context engineering | story bible / 角色库 / 风格锁 / 资产库 | ⚠️ **我的类比**。零存活证据；唯一机构线索验证器报错，未证实也未证伪 |
| harness | 工作流编排 / 批量管线 | ⚠️ **我的类比**。零存活证据（但 OpenMontage / ViMax 是工程事实） |
| graph engineering | ComfyUI 节点图设计模式 | ⚠️ **我的类比**。零存活证据 |

> **这张表是本轮最诚实的产出。** 10 条存活结论 **10/10 落在 eval 轴**——这个分布本身就是证据。
> **不等于**另外四轴不存在，等于**它们还没被人当成学科系统论述过**。
> 换句话说：**你在做的这件事（把 AI 视频当工程学）本身还没有教科书。**

---

## 五、工具与开源资源（全部当日 GitHub API 自核）

### 🥇 直接把 Claude Code 变成视频工作室
| 仓库 | 数据 | 判断 |
|---|---|---|
| **[calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)** | **48,916★** / 6,126 fork / **AGPL-3.0** / created 2026-03-29 / **pushed 2026-08-18** / 38 贡献者 | 🟢 **本轮头号发现**。2,104 文件、**138 个 SKILL.md**、**12 条生产管线**（cinematic / animation / documentary-montage / talking-head / clip-factory / explainer / localization-dub / podcast-repurpose / screen-demo / avatar-spokesperson / character-animation / hybrid）、同时带 `.claude` `.cursor` `.codex`。**两天前刚合并外部贡献的 Seedance 2.5 skill**。⚠️ **AGPL-3.0 是传染性 copyleft**，商用前看清楚 |
| **[HKUDS/ViMax](https://github.com/HKUDS/ViMax)** | **12,032★** / 1,801 fork / **MIT** / pushed 2026-07-29 | 🟢 Agentic 视频生成：Director / Screenwriter / Producer / Generator 一体 |
| [jnMetaCode/ai-shortfilm-prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) | 359★ / MIT / pushed 2026-08-18 | 🟢 五段式 → Claude Code Skill，21 题材模板（见 [02 号笔记](02-shortfilm-method.md)） |

### 评估与筛选（L5）
| 仓库 | 数据 | 判断 |
|---|---|---|
| [Vchitect/VBench](https://github.com/Vchitect/VBench) | 1,741★ / Apache-2.0 / pushed **2026-03-23** | 🟢 维护中。CVPR2024 Highlight |
| [zai-org/VisionReward](https://github.com/zai-org/VisionReward) | 423★ / Apache-2.0 / pushed **2025-03-26** | 🟡 **停更 17 个月**。AAAI 2026 论文，细粒度多维人类偏好 |
| [OpenGVLab/PhyGenBench](https://github.com/OpenGVLab/PhyGenBench) | 165★ / **无 License** / pushed **2024-10-25** | 🔴 **停更近 2 年 + 无 License**。ICML2025 物理常识基准，只当论文附件看 |
| AesVideo-Bench（AesRM 的基准） | — | 🔴 **未确认公开发布**，找不到 GitHub/HF 制品，**不能写进「今天可用」清单** |

### ComfyUI 侧
[Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp)（82★，官方公测，日更）· [ComfyUI Subgraph 官方发布](https://blog.comfy.org/p/subgraph-official-release)

---

## 六、证据等级与缺口（必须随本文一起看）

### 强度
- **preprint 警告**：AesRM 与 VBench-2.0 **均未经同行评审**。只有 CVPRW 2026 那篇综述过了评审（**workshop 级，门槛低于主会**）
- **自报警告**：AesRM「打赢既有奖励模型」是作者自报，且作者名单含 Wan 的所有者阿里；效果温和（1.2k 视频用户研究**仅 45% 样本改善**，未报变差比例）。VBench-2.0 的 95–99% 人类一致率也是自报，无独立复现
- **vintage 警告**：TC-Bench 的「SOTA <20%」是 **2024-06** 数字从未修订；VBench-2.0 Table II 是 **2025-03** 那批模型。**都不能当当前值**
- **检索限制**：多名验证者 WebSearch 配额耗尽（200/200），部分条目「未找到反证」是**弱陈述**

### 两轮研究连续没答上的
1. **四个产品的完整定位与定价** —— 我已用[一手页面实读补上](03-workflow-products.md)，但**未经对抗验证**
2. **L6 非视觉维度**（剪辑/色彩/声音/叙事）的可测量分解 —— 零结论
3. **模型级 eval 怎么降维成镜头级筛选** —— 只坐实训练闭环，选片闭环没证明
4. **context engineering 轴是否真有系统论述** —— 唯一线索验证器报错

### 一条元教训（值得回流 agent-on）
上一轮「LibTV = LiblibAI 出品」被 **3 票全否**，但本轮 `curl -sIL libtv.ai` 显示 **308 跳转到 www.liblib.tv**——归属属实。
**对抗验证会误杀**：验证者否掉的是那条声称里的模型清单细节，连带把正确的归属一起否了。
→ **教训：被否的结论不等于假，要看它被否在哪一部分。**
