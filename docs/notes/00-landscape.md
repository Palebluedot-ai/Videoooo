# 00 · AI 视频工具与方法论版图（第一次调研）

> **调研日期：2026-08-19**｜方法：5 角度并行检索 → 抓 23 个源 → 抽 115 条声称、验 25 条、每条 3 票对抗验证（需 2/3 反驳才判死）→ 确认 14 条、否掉 11 条。
> **本文纪律**（AGENTS §1 笔记真实性红线）：每条结论标来源与日期；推论与引文分开写；**被否的说法单列一节，防止日后自己捡回来当真**。
> ⚠️ AI 视频半年换代，本文所有数字是 **2026-08-19 快照**。

---

## 一、结论先说：三个直接答案

### Q：AI 视频有没有像 prompt engineering 那样的方法论体系？
**有，但它分散在三处，且没有任何一处自称「AI video engineering」。** 别去找一本圣经，要分别去这三个地方取：

| 来源 | 它给什么 | 它不给什么 |
|---|---|---|
| **厂商侧**（Google Veo 官方指南） | 可直接照抄的 prompt 结构 + 受控术语表 | 跨厂商通用性（是 Veo 的口径） |
| **学术侧**（可控视频生成综述） | 按「控制信号」组织的完整分类学，274 篇论文书单 | 创作工作流（它不按工作流组织） |
| **实践侧**（agent skill 仓库） | 已被机读化的分镜→关键帧→i2v 流程 | 厂商中立（多绑死某家 CLI） |

### Q：Claude / Cursor 在 AI 视频里是不是完全没用？
**不是。但适用面明确在「编排层 + 后处理层」，不在「创作决策层」。** 详见第四节——有第一方证据的能做事项 4 类，明确做不了的 3 类。

### Q：那几个工作流产品选哪个？
**本轮只有 FLORA 拿到扎实结论。TapNow、Musein 零确认结论；LibTV 只确认了它的官方 skill 仓已停更 5 个月，产品定位的说法被 3 票全否。** 所以下面不对这三个给选型建议——这是**调研缺口，不是「它们不行」**。

---

## 二、方法论：具体能抄的东西

### 2.1 Google Veo 官方 prompt 公式（可直接抄）

五槽公式：`[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`
配套受控词表：
- **运镜**：dolly, tracking, crane, aerial view, slow pan, POV
- **构图**：wide shot, close-up, extreme close-up, low angle, two-shot
- **镜头/焦点**：shallow depth of field, wide-angle, soft focus, macro, deep focus

来源：[Google Cloud Blog · Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)（发布 2025-10-16，2026-08 仍为现行口径，未见 Veo 4 发布）

**三条必须同时知道的限定**：
1. Google 自己**还有另一套**元素划分（[Cloud docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) 的 Subject / Context / Action / Style / Camera motion / Composition / Ambiance）。所以这是「一套官方公式」，不是唯一正典，原文也没给它起名。
2. **「模型会听这套词表」是厂商口径，实践有反证**：从业者报告 Veo 3.1 会**静默降权运镜指令**（写了 dolly in / slow push 却返回基本静止的片段）；遇到互相矛盾的运镜指令倾向选最小运动；叠加 dolly + pan + tilt 不稳定。
3. → **实操铁律：一个 clip 只给一个运镜。**

### 2.2 首尾帧与一致性：是官方功能，不是社区偏方

- **首尾帧**：Veo 3.1 有正式 API 参数 `last_frame` / `lastFrame`（`GenerateVideosConfig`）。给起始图 + 结束图，生成中间过渡（含音频）。来源：[Gemini API · Veo docs](https://ai.google.dev/gemini-api/docs/veo)
- **跨镜头一致性**：官方方案叫 **ingredients to video**——用参考图（角色/物体/场景/风格）条件化，同一批参考图复用于多次生成。
- **官方推荐两段式**：先用 Gemini 2.5 Flash Image（Nano Banana）生成锚点帧/参考图 → 再交给 Veo。

**限定（都很实操）**：
- 首尾帧与 1–3 张 reference images（ingredients）**不能在同一请求里混用**
- 有 2026-01 论坛报告该路径要求 **8s 时长，4s 会报「Your use case is currently not supported」**
- 早期「last_frame not supported」报错，OP 自己复盘是 **SDK 版本过旧**
- 质量抱怨真实存在：开头卡在首图、中段畸变、末帧匹配偏松

**关于 seed（重要澄清）**：那篇官方指南**通篇没提 seed**。所以「Veo 靠参考图不靠 seed」只对**那套工作流**成立，**不能**外推成「Veo 没有 seed」——Vertex AI 的 Veo API **有**可选 uint32 seed（0–4294967295），同 seed + 同输入可得确定性输出，横跨 t2v / 图引导 / extend。
> 正确的心智模型：**参考图条件化 = 一致性主杠杆；seed = 可复现性控制。两者不互斥。**

2026-01 更新另加了竖屏 9:16、4K 上采样、循环角色身份一致性改进。

### 2.3 学术侧：按「控制信号」组织的分类学

论文：[Controllable Video Generation: A Survey](https://arxiv.org/abs/2507.16869)（Yue Ma 等 22 作者，HKUST/清华/腾讯/上交；v1 2025-07-22，**v3 更新至 2026-01-19**）
配套仓库：[Awesome-Controllable-Video-Generation](https://github.com/mayuelala/Awesome-Controllable-Video-Generation)（766 stars，官方配套，去重后 **274 篇** arXiv 论文）

综述核心论点：**纯文本 prompt 不足以表达复杂细粒度意图**，因此研究转向注入非文本条件（相机运动、深度图、人体姿态）。

目录可逐条映射到实践术语：

| 学术分类 | 对应实践术语 |
|---|---|
| Camera-Guided | 运镜控制 |
| Trajectory-Guided / Motion-Guided | motion brush 类轨迹控制 |
| ID Control（Person / Subject-Guided） | 角色一致性 |
| Image Control | i2v / 首帧驱动 |
| Structure Control（Pose / Depth / Sketch / BBox） | ControlNet 式结构控制 |

**⚠️ 措辞警告**：这篇综述**从未说过**「I2V 比 T2V 更可控」。那是合理推论（图像是非文本条件，信号多于纯文本），**不是引文**。而且这个推论只在**外观/构图/身份**维度成立——运动维度有反例：过度依赖条件图会**压制运动表现力**（ConsistI2V 有记录），部分 i2v 模型**不跟随文本条件**（DynamiCrafter 有记录）。
另注：README 里字面**没有** motion brush、first/last frame、character consistency、seed 这些词（各 0 次命中），只有 image-to-video（45 次）/ I2V（51 次）是原生用语。实践术语的对应是我做的桥接，不是原文标注。

### 2.4 实践侧：已被写成机器可读 skill 的工作流

[SamurAIGPT/Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)（4,092 stars，pushed 2026-08-15）

- `storyboard` skill：把 premise 拆成 **setup → inciting moment → escalation → climax → resolution** 的 beats，**只出图不出视频**
- `character-story-video` skill：先立角色图（nano-banana-pro）→ 用 image edit 以该图为参考跑所有场景 → 用 `kling-v3.0-pro-image-to-video` 或 `veo3.1-image-to-video` 逐帧动画化 → ffmpeg concat 合并
- **反漂移手法写死在 Notes 里**：*每条 prompt 逐字重复角色描述，别指望模型记住*

**限定（别当行业正典引用）**：
- 全流程**绑死 muapi.ai 的 CLI 与 API key**——这是**一家厂商的 cookbook**
- repo created_at 是 2023-05-25 却覆盖 2026 世代模型 → 是改名/复用仓，**4.1k stars 不构成对当前内容的背书**
- 两个 skill **并非一条链**：storyboard 明确把视频需求 handoff 给 music-video skill
- **覆盖范围**：只有分镜 / 一致性 / 逐字重复三件事。**没有**覆盖首尾帧、seed 固定、运镜/motion brush、curation 管线、降低抽卡成本

---

## 三、工作流产品：只有 FLORA 有结论

### FLORA（原 florafauna.ai，现已 301 跳转到 flora.ai）

**定价结构（2026-08-19 当天 curl 原始 HTML 核对 + 官方 docs 交叉验证）**

| 档 | 价格（每席/月，最多 8 席） | 视频模型 |
|---|---|---|
| Free | $0，总用量封顶 **$2.50** | ❌ **没有** |
| Starter | $18 | ✅ |
| Pro | $50 | ✅ |
| Max | $200 | ✅ |

来源：[flora.ai/pricing](https://flora.ai/pricing) · [docs.flora.ai/plans-and-billing/pricing](https://docs.flora.ai/plans-and-billing/pricing)

**关键机制**：席位费买的是一份工作区**共享美元额度池**，按各模型公布费率计量（官方举例 Nano Banana 2 $0.077/图）。

**四条容易搞错的地方**：
1. **免费档跑不了视频** → 试水成本不为零，跑第一条视频最低 **$18**（年付约省 20%）
2. **「超出即另计」不准确**——超额是**默认关闭、需管理员显式开启并设美元上限**的 opt-in；池子用完默认**停止生成**，无 auto-recharge，额度每周期重置不滚存
3. Free 卡上的「FAUNA (unlimited, free)」**不是免费生成额度**——FAUNA 是编排 agent，它提议要跑的节点照常计费
4. 全站文档 grep「trial」**零命中**，付费档无试用

**⏰ 时效警告**：翻倍额度（Starter +$12 / Pro +$50 / Max +$100 每席）是 launch promo，**2026-08-31 结束**（距本文 12 天）。之后 Pro 席位含的预算从约 $100 腰斩回 $50。
**已过时信息（网上还在流传，别信）**：「$0.90/1000 credits」「Starter/Studio/Scale 三档」「免费送 500 credits 含 2 次视频生成」——均为 2026-05 改制前的旧 credit 制。

**FLORA 有 MCP**（对你这个「想同时学写代码」的场景最相关）
- 从**最低付费档 $18 起**就含「API & MCP access」，官方文档明写 Free 无 API/MCP
- endpoint `https://agents.flora.ai/mcp`（OAuth 登录），官方给了 Claude Web/Desktop、**Claude Code（一行安装命令）**、Cursor 的安装路径，状态「已出公测」
- 暴露工具：list workspaces、search techniques、list models、upload assets、**generate（image/video/audio）**、run techniques、submit feedback
- 来源：[docs.flora.ai/more/mcp](https://docs.flora.ai/more/mcp) · [flora.ai/mcp](https://flora.ai/mcp)；第三方批评性佐证：[basedlabs.ai 评测](https://basedlabs.ai)（2026-06-11，题为「Flora AI API: What It Actually Does, and Where It Falls Short in 2026」，仍确认 MCP/API 自 Starter 起、无 waitlist）
- **收紧措辞**：FLORA 自己把 MCP 定位为「在 canvas 之外使用 FLORA」。**没有任何文档证明 MCP 的产物会落回可视画布节点**。准确说法是「让 Claude Code / Cursor 调用 FLORA 的模型与 techniques」，**不是**「接到 FLORA 画布上」。

### TapNow / Musein / LibTV：本轮没结论

- **TapNow**：零确认结论
- **Musein**：零确认结论
- **LibTV**：唯一硬事实是它的官方 skill 仓 [libtv-labs/libtv-skills](https://github.com/libtv-labs/libtv-skills) **已停更 5 个月**（见下节）。关于「LibTV = LiblibAI 出品的 Agent 编排平台、聚合 Seedance 2.0 / Kling 3.0 / Wan 2.6」的说法，**3 票全否**，未被证实。

→ 这三个需要**单独一轮针对产品本体（而非其 GitHub 仓）的调研**。

---

## 四、Claude / Cursor 的适用边界（核心问题）

### ✅ 有第一方或可运行代码支撑的「能做」

**1. 驱动本地 ComfyUI 的 workflow JSON 全链路** —— 第一方支持，不是社区野路子

[Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp)：**ComfyUI 官方组织自己发的 MCP server，标语直接点名 Claude Code、Claude Desktop、Cursor**。官方文档站有四语言专章，称其为「Comfy 的第一方本地 MCP server」。
39 个工具（源码 grep `@mcp.tool` 得 39，与 README 自称一致），覆盖：
`run_workflow`（提交 JSON，`wait=False` 异步返回 prompt_id）· `validate_workflow`（对 live object_info 预检）· `set_workflow_slot`（改 prompt/seed/steps/model，默认非破坏性）· `list_workflow_slots` · `search_templates` · `fetch_outputs` · `job`
→ **一个 Claude/Cursor 会话可以读取、参数化、校验、派发、收取工作流，无需在 GUI 里手改图。**

身份确认：Comfy-Org 拥有 ComfyUI 本体（**128,422 stars**）、ComfyUI-Manager（15,827）等 79 个公开仓，不是同名仿冒。

**六条限定**：
- **双方都自称 beta**（README「Status: beta」/ docs「Public beta… may change」）→ 引用时写「官方公测（截至 2026-08-19）」而非「稳定支持」
- 不是独立 API client——每个工具 shell out 到 `comfy-cli >= 1.14.0`，且需要 ComfyUI 在跑
- `list_workflow_slots` **只吃前端格式 JSON**，API-format 导出会被拒；参数化那步必须用 **UI 导出**的 JSON
- `set_workflow_slot` **只能改已存在的参数槽，不能增删节点或改连线** → **能「调图」不能「作图」**
- 178/205 commits 出自单一贡献者；许可 AGPL-3.0-or-later OR Commercial
- created 2026-07-01，79 stars，上线约 7 周 → 引用为「当前官方工具」，**不是**「经实战检验的社区标准」；39 这个数字会随日更漂移

视频能力确有覆盖：`search_templates` 支持 `type="video"`；`list_partner_models` 含 t2v / i2v / video-extend / lipsync 共 **52 个**合作模型（Kling、Veo、Seedance、MiniMax H3 等）。

**2. 通过 MCP 调用云端聚合平台的模型与 techniques** —— FLORA，$18/席/月起（见上节）

**3. 把工作流写成可复用的 agent skill 文本流程** —— Generative-Media-Skills（见 2.4，注意厂商绑定）

**4. TTS + 词级字幕对齐 + 音频驱动时间轴 + 程序化渲染**

[runesleo/claude-video-kit](https://github.com/runesleo/claude-video-kit)（115 stars，26 forks，MIT，TypeScript，created 2026-04-06，pushed 2026-08-18）
把 `script.json` 变成竖屏 1080×1920@30fps 解说视频：TTS（Fish Audio API 或本地 IndexTTS2）→ faster-whisper **词级**字幕对齐 → **由音频实际时长驱动**的元数据计时 → Remotion 渲染，带一道 pre-render review gate。README 明写目标用户是「已经在 Claude Code 或 Cursor 里写研究/技术解说的人」。
逐 stage 在**源码**里核对过（`scripts/tts.py` 打 api.fish.audio、`scripts/align.py` 调 `word_timestamps=True`、`remotion/` 工作区）。

**🚨 范围限定（很重要，别误用）**：它**不是生成式视频管线，不调用任何视频生成 API**——grep `render.sh` 里 veo|sora|runway|kling|wan|hunyuan|luma|pika|replicate|fal **零命中**；README 自陈「No B-roll / video clip support — slides are still-frame + audio + captions」，作者自己划清「不是一键 topic → AI b-roll Short 工厂，不是 generative video lottery」。
→ 它只能作为**字幕/配音/时间轴自动化**（+ 部分 ffmpeg 批处理）的证据，**不能**用于「调用视频生成 API 写管线」「ComfyUI JSON 自动化」「MCP 接视频生成服务」——那是范畴错误。
权威性限定：单一贡献者、115 stars、约 4 个月、RC 未 GA、README 嵌了 Fish Audio 推荐返利链接、端到端 Verified 证据只是一个 8 秒 442KB 演示 MP4，无第三方复现。IndexTTS2 分支 README 自标「a placeholder — CUDA wiring is left to the user」，**纯 macOS 用户尤其注意**。

### ❌ 本轮**没有**找到可引用公开实现的（= 缺口，不是「不可能」）

1. **批量生成后的自动打分与筛选（curation）管线** —— 14 条确认结论里**零命中**
2. **系统性降低抽卡次数的自动化脚本**
3. **多平台视频生成 API 的统一封装**

### 一句话边界

> **编排层 + 后处理层 = Claude/Cursor 的主场；创作决策层不是。**
> 补充：有个说法称「LibTV 官方 skill 把用户侧编程 AI 限定为只做上传/传话/轮询的搬运工」——**该说法 1-2 被否**，所以「托管平台会主动限制 Claude 角色」这一命题**未被证实**，别拿它当边界论据。

---

## 五、成本：本轮最大的空洞（必须诚实说）

**唯一通过对抗验证的价格锚**：[Replicate 定价页](https://replicate.com/pricing)（2026-08-19 直取）GPU 按秒费率——

| GPU | 每秒 | 每小时 |
|---|---|---|
| Nvidia T4 | $0.000225 | $0.81 |
| L40S | $0.000975 | $3.51 |
| A100 80GB | $0.001400 | $5.04 |
| H100 | $0.001525 | $5.49 |

（H200 与 H100 同价；多卡精确线性倍数，8×H100 = $0.012200/秒 = $43.92/时。小时价是页面自己印的，非换算推导，算术自洽。）

**这组费率只锚「租云 GPU 跑开源模型」这一条路。** 注意：Replicate 是托管 serverless GPU，不是自建机器；**私有/独占部署会为启动时间和空闲等待一并计费**，间歇使用的真实成本高于纯活跃秒费率；公开模型只按活跃处理时间计。同页明确另有**按产出计价**的模型。

**🕳️ 空洞**：关于「一条 5 秒片段多少钱 / 抽 10 次多少钱」，本轮**没有任何经过验证的可引用数字**——三条具体单价声称分别以 1-2、0-3、0-3 被否（见第六节）。
→ **待办：单起一轮只做核价的调研**，分别取 fal.ai / Replicate / Runway / Kling / Veo(Vertex) 官方定价页当日快照，**严格区分「按 GPU 秒」与「按输出秒」两种计价模型**。

---

## 六、⛔ 被对抗验证否掉的说法（存档防复发）

**这一节的存在意义**：这些说法在网上/初检里看起来都很像真的，几个月后我很可能又捡回来。**它们没通过验证，别用。**

| 被否说法 | 票数 |
|---|---|
| Veo 3.1 支持 "timestamp prompting"（`[00:00-00:02]` 式内联分镜，一次生成多镜头） | 被否 |
| 该综述是「单条件/多条件/通用可控」三层分类 | 0-3 |
| LibTV = LiblibAI 出品，聚合 Seedance 2.0 / Kling 3.0 / Wan 2.6…… | 0-3 |
| LibTV 官方 skill 把编程 AI 限定为搬运工角色 | 1-2 |
| fal.ai 视频模型按「输出单位」计费，页面给出每美元买多少秒 | 1-2 |
| Wan 2.5 $0.05/秒 vs Veo 3 $0.4/秒（约 8 倍差） | 0-3 |
| Replicate Wan 2.1 i2v $0.09/输出秒（480p）、$0.25（720p） | 0-3 |
| Generative-Media-Skills 有 41 个 recipe、一行 npx 装 | 1-2 |
| `muapi mcp serve` 暴露 19 个工具 | 0-3 |
| Comfy-Org 建议 Apple Silicon 别跑本地视频 → **因此排除本地路线** | 0-3 |
| claude-video-kit「刻意为 agent 操作而设计」的架构主张 | 被否 |

**关于 macOS 本地路线的正确表述**：Comfy 官方文档确实写了「For Mac users, if you plan to run open-source models, we recommend the cloud connection … will not run at a workable speed on the Apple GPU」——但从「官方建议走云」跳到「排除本地路线」属于过度推论，**被 3 票全否**。
→ 正确写法：**官方倾向建议 Mac 用户用云端连接跑开源模型；本轮未取得 Apple Silicon 上 Wan / HunyuanVideo / LTX-Video / Mochi 的任何实测数据点。**

---

## 七、开源资源清单

### 已验证

| 仓库 | star | 状态 | 用途 |
|---|---|---|---|
| [Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) | 79 | 官方公测，日更 | Claude/Cursor 驱动 ComfyUI |
| [SamurAIGPT/Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills) | 4,092 | pushed 2026-08-15 | 分镜/一致性 skill（绑 muapi） |
| [runesleo/claude-video-kit](https://github.com/runesleo/claude-video-kit) | 115 | RC 未 GA | 字幕/配音/时间轴自动化 |
| [mayuelala/Awesome-Controllable-Video-Generation](https://github.com/mayuelala/Awesome-Controllable-Video-Generation) | 766 | 配套综述 v3 2026-01 | 274 篇论文书单 |
| [libtv-labs/libtv-skills](https://github.com/libtv-labs/libtv-skills) | 994 | ⚠️ **停更 5 个月** | 反面样本，见下 |

### ⚠️ star 数不能当维护活跃度用（当轮实测反例）

libtv-skills：**994 stars / 102 forks，但全部 7 次提交挤在 2026-03-16 至 03-18 三天内**，单一作者，此后到 2026-08-19 **5 个月零提交**。watchers 仅 3。
堵死了「开发转移别处」的退路：只有 main 一个分支、0 release、0 tag、组织 libtv-labs 下**只有这一个仓库**。
反向佐证来自它自己的 issue 区：#8「更新频率能提高吗？」(2026-04-11)、#9「什么时候更新呢，现在太难用了啊」(2026-05-05)、#1「这技能真的可用吗？」(2026-03-18)，PR #5 挂了约 5 个月未合，**全部无人回应**。

### 已抓取但本轮**未做验证**（当线索用，别当结论）

因验证预算耗尽（7 条声称被 budget-dropped）未核实，仅记录指针：
[deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP) · [ATH-MaaS/Pixelle-Video](https://github.com/ATH-MaaS/Pixelle-Video) · [liusida/top-100-comfyui](https://github.com/liusida/top-100-comfyui) · [showlab/Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) · [Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates) · [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) · [wilwaldon/Claude-Code-Video-Toolkit](https://github.com/wilwaldon/Claude-Code-Video-Toolkit)

---

## 八、调研本身的可信度披露

1. **多位验证者的 WebSearch 配额本轮耗尽**（200/200），涉及 Replicate 定价、Generative-Media-Skills、comfy-mcp、claude-video-kit 四条 → **无第三方独立佐证或批评扫描**，全部依赖对一手产物（定价页、源码、SKILL.md）直读。对「文件里写了什么」这是最强证据；对「好不好用/有没有人成功用过」，本轮**没有独立复现证据**。
2. **Veo 3.1 发布日期两位验证者口径不一**：一位据 Google Developers Blog 记 2025-10-15/16 首发，另一位记 2026-01-13 出货。前者有可核对的博文时间戳，更可靠；后者可能对应 2026-01 功能更新。→ 本文写「2025-10 首发，2026-01 更新」。
3. **Google 相关三条结论全部以 Google 自家博客/文档为源**——对「厂商公布了什么」是理想一手源，但对「这套方法有效」带厂商利益。实践反证（运镜被降权）已并入正文。
4. **所有 GitHub 数字均为 2026-08-19 快照**，comfy-mcp 日更中，39 这个数字会漂移。

---

## 九、四个待查（下一轮调研的题目）

1. **一次「抽卡」到底多少钱**——按 GPU 秒 vs 按输出秒必须分开，取当日官方定价页快照，给可复算的每 5 秒片段成本区间
2. **批量生成后的自动打分筛选有没有公开实现**——这是「降低抽卡成本」最关键一环却零命中。是真没人做，还是检索没覆盖到（VBench 类自动评测、美学打分模型、CLIP/VLM 一致性打分接进筛选脚本）？
3. **Apple Silicon 上跑开源视频模型的实测边界**——生成一条 5 秒 480p 要多久、多少内存、有无 MPS 后端。这直接决定「本机 macOS 自用」这条路成不成立
4. **TapNow / Musein / LibTV 产品本体**——针对产品而非其 GitHub 仓
