# 03 · 四个工作流产品（一手页面实读）

> **日期：2026-08-19**｜方法：直接 curl 域名 + 抓取产品官网首页。**这是补上一轮调研的洞**——TapNow / Musein / LibTV 上轮全部零确认结论。
> ⚠️ 状态：**本文为一手页面快照，尚未做对抗验证**；第二轮 deep-research 结论回来后合并。定价与模型清单以官网当日为准。

---

## 域名与归属（curl 实测 302/308 链）

| 域名 | 实际落点 | 服务器 | 归属结论 |
|---|---|---|---|
| `tapnow.ai` | → `www.tapnow.ai` | **Vercel** | 独立产品 |
| `musein.ai` | 直达 | **Cloudflare** | 独立产品 |
| `libtv.ai` | **→ `www.liblib.tv`** | istio-envoy | ✅ **LibTV = LiblibAI（哩布哩布）出品** |
| `flora.ai` | 直达（`florafauna.ai` 301 过来） | **Framer** | 改名，同一产品 |

> 📌 **纠正上一轮**：「LibTV = LiblibAI 出品」上轮被 3 票否掉（0-3）。**域名 308 跳转是定义性一手证据**——归属属实。上轮被否的应是那串具体模型清单（Seedance 2.0 / Kling 3.0 / Wan 2.6），不是归属本身。**这是「对抗验证也会误杀」的一个实例，记下来。**

---

## 一、TapNow（tapnow.ai）

- **定位（官网原文）**：*"TapNow is the best way to create with AI Agents. Orchestrate text, image, audio, and video models."*
- **形态**：**白盒节点工作流**——页面有节点编辑器的键盘无障碍提示（*"Press enter or space to select a node…use arrow keys to move the node around"*）
- **面向**：专业创作团队。首页打*"Trusted by the world's leading creative teams"*，客户墙列 Google、TikTok、YouTube
- **定价**：有免费入口（"Get started for free"）+ Enterprise + Pricing 页；**首页未列具体档位**
- **底层模型**：**未披露**
- **API / MCP**：首页**未提及**

## 二、Musein（musein.ai）

- **定位**：**「下一代 AI 视觉创作引擎」**，覆盖从电商广告到电影短片
- **面向**：商业企业 + 内容创作者，主打「任何人都能创作专业级视觉」
- **功能模块**：`Workspace`、`TV`
- **定价**：有 pricing 链接，**首页未展示档位**
- **底层模型**：**未披露**（只写「高级 AI 模型」）
- **API / MCP**：**未提及**
- 有 Discord 社区

## 三、LibTV（libtv.ai → liblib.tv）⭐ 对学习最相关

- **出品**：LiblibAI（哩布哩布）
- **定位**：专业视频创作工具，主打**「音视频直出」**
- **底层模型（页面出现的）**：**Seedance 2.5**、**MiniMax H3**
- **定价（首个可引用的真实单价）**：**Seedance 2.5 低至 ¥0.4/秒**；年会员最低 4 折
  > 📌 换算：一条 5 秒片段 ≈ **¥2**。抽 20 次 ≈ **¥40**。
  > ⚠️ 这是**厂商挂牌价**、当日快照，且「低至」= 最低档；实际按分辨率/模式浮动。**别当固定价用。**
- **Agent 接入**：页面有 **「LibTV Agent」** 与 **「查看全部 skills」**
  > ⚠️ 但其官方 skill 仓 [libtv-labs/libtv-skills](https://github.com/libtv-labs/libtv-skills)（994★）**已停更 5 个月**（见 00 号笔记）——**产品在动，开源 skill 没在动**，别指望那个仓
- **两个对「渐进式学习」直接有用的功能**：
  | 功能 | 是什么 | 为什么对学习有用 |
  |---|---|---|
  | **逐帧拉片** | 对**参考视频**逐帧分析 | 「拉片」是影视学院的经典训练法——把好片子拆开看它每一帧怎么做的。**这是把专业训练法产品化了**，属于「看懂」这一级的工具 |
  | **导演台** | 虚拟 3D 场景，空间精准控制 | 把运镜从「写词碰运气」变成「在 3D 空间里摆机位」，属于「控制」这一级的工具 |
- 其他功能：新建画布创作、TV Show 分类

## 四、Flora（flora.ai，原 florafauna.ai）

已在 [00-landscape.md](00-landscape.md) 第三节详查（经 3 票对抗验证），要点：
- 节点式 AI 创意画布，Free $0 / **Starter $18** / Pro $50 / Max $200（每席/月，最多 8 席），共享美元额度池
- **免费档没有视频模型**（总用量封顶 $2.50）→ 试水最低 $18
- **从 $18 档起含 API & MCP**，endpoint `https://agents.flora.ai/mcp`，官方给了 Claude Code 一行安装命令
- ⏰ 翻倍额度促销 **2026-08-31 到期**

---

## 五、初步分类（⚠️ 我的判断，非引文）

| 产品 | 白盒/黑盒 | 开发者接入 | 疑似适合的学习阶段 |
|---|---|---|---|
| **LibTV** | 偏黑盒 + Agent | LibTV Agent / skills（开源仓已停更） | **看懂**（逐帧拉片）与**控制**（导演台） |
| **Flora** | **白盒节点** | ✅ **MCP，$18 起** | **编排**——且是唯一确认能被 Claude Code 直接驱动的云产品 |
| **TapNow** | **白盒节点** | 未披露 | 编排（但模型与价格不透明，评估成本高） |
| **Musein** | 未知 | 未提及 | 信息太少，暂不建议投入 |

---

## 六、这一节的证据等级

- 域名跳转：`curl -sIL` 实测，**定义性证据**
- 产品描述与定价：**厂商官网首页当日快照**，未经第三方交叉验证，**未做对抗验证**
- 「适合哪个学习阶段」：**我的判断**，等能力阶梯调研结论回来后重估
- ⚠️ 四个产品的首页都**没有**披露完整定价档位与模型清单（除 LibTV 的 ¥0.4/秒 与 Flora 的四档），要准确数字须登录后台或找定价页
