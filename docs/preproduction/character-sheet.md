<!-- instantiated-from templates/character-sheet.md @ v0.18.0 · 内容由 anchor-design-pack 工作流合成（3 视角设计 × 3 证伪 × 1 合成，2026-08-21）-->
# 角色设定集 · 加密晨报 AI 动画主播（合成定稿 v1.0）

> 结构依 `templates/character-sheet.md` 六件套。生成目标：Seedream / Nano Banana 级图像模型（描述式否定可用）。竖屏 9:16 走**生成参数**设置，不靠 prompt 文字（prompt 里只写构图提示）。
> 本版合成自 safety / brand / pipeline 三版：吸收全部被点名 strengths，逐条修掉 violations 与 weak（修复对照见各节内注）。

---

## 1. 角色名与一句话人设

| 位次 | 名 | 理由 |
|---|---|---|
| **主推** | **知早**（英文 Zoe，观众昵称「早早」） | 「早」绑定晨报场景——开场白「早！我是知早」天然成型；谐音「知道得早」直指加密晨报的信息差卖点；Zoe 音近好传播；查无知名 VTuber/动画角色撞名。⚠️ 罗马字**不用全大写 ZHIZAO**（易读成「制造」），对外统一用 **Zoe / 知早**；prompt 内角色锚词用 `ZOE` |
| 备选 1 | 晓晨（Xiaochen） | 双圆音节亲和、低撞名；缺点是不带「知」的信息差含义 |
| 备选 2 | 知晨（Zhichen） | 保「知」字品牌；若日后不止做早报，不被「早」字锁死时段 |
| 弃用 | 晨曦 | 通用词，VTuber/游戏角色/主播圈大量在用，搜索辨识度与品牌独占性弱 |

**一句话人设**：每天早上 60 秒、比你早一步把加密行情讲成人话的漫画晨报主播——永远同一张脸，永远准时。「早！我是知早。」

📋 **启用前动作**（进 M1 清单）：正式公开前对「知早 / Zoe」做一次商标 + B站/YouTube 现役 VTuber 名快查（约 10 分钟）。

---

## 2. 设计定稿

### 2.1 剪影三特征（纯黑剪影可辨，且要实证——见第 7 节）

1. **头顶正中一根折线呆毛**——锯齿状、末端上扬，形状就是一条上行趋势线。这是全角色唯一的币圈符号，藏在发型里，不堆币标。**居中**而非偏侧——对称特征在 turnaround 镜像时不会左右打架
2. **齐下巴钝剪 bob + 大号包耳耳机的双圆头部轮廓**——耳机是大体积对称几何体（模型最稳形状类），天然回答「为什么这个主播是虚拟的」，且是剪影第二锚点
3. **尖翻领西装的梯形上身 + 及膝 A 字裙**

**全设计零飘动元素、全特征对称/居中/可数**：一根居中呆毛、双侧对称琥珀发梢、每眼一个高光点、每耳罩一圈琥珀环、一枚居中六边形胸针。可数即可验收（挑片逐项点数），对称即镜像安全（turnaround 转侧背面不存在「单侧特征换边」漂移源）。无耳钉、无项链、无麦克风杆——饰品做减法，每少一件小物 = 少一个漂移变量。

> 修复注：胸针从 safety 版的「左襟」（镜像必翻车、只能靠 QC 兜底）改为 pipeline 版的**领结正中**——把问题消灭在设计层而非检查层。耳麦从 brand 版的「右耳单侧」改为 safety 版的**双耳对称包耳耳机**，同理。

### 2.2 发

深藏青钝剪短 bob（`#22335C`），齐下巴一刀切，平直刘海；头顶正中一根琥珀色折线呆毛（趋势线形状，全图唯一一根）；前侧两缕发梢**左右对称**染琥珀（`#F5A623`）。锁死 no flying hair strands——不许碎发、渐变、飘动发丝，发丝复杂度这个崩溃维度整个删除。

> 修复注：brand 版「dark navy-teal」色名与 `#263C5C` 打架（teal 会把发色往绿拉）——本版色名统一为 **dark navy**，与 `#22335C` 对齐。brand 版「发内层 underlights」是模型最易吃掉的细节，弃用；改用 safety 版可数的「两缕对称发梢」。

### 2.3 眼 / 嘴 / 手

- **眼**：大圆琥珀眼（`#F5A623`，与呆毛/发梢/耳机环同一个 HEX——琥珀色全设计只有一个值），每眼**一个**白色高光点（可数、可复述），细简眉。双眼同色，不搞异色瞳
- **嘴**：简化漫画嘴，扁平色块形状——no realistic lips, no teeth detail。这是口型同步（brief 命中 #6 绕法 A）与防写实化的双保险，为后续简化口型动画留路
- **手**：默认腰部以上构图、手出画（below the desk edge）；必须入画时逐字用 `simplified rounded cartoon hands with minimal finger detail`。**手锁写进每一条手会入画的 prompt，包括 turnaround**——不靠图生图继承，不靠人记得加

### 2.4 服装

万寿菊黄西装外套（`#F2A33C`）尖翻领——深蓝演播室里主体极跳，竖屏手机优化；白衬衫（`#FFFFFF`）；领口藏青丝带结（`#1E2A4A`）**正中**钉一枚金色六边形胸针（`#D9A441`）——几何形状承载区块链意象，同时规避真实 logo 与字符两个雷区。头戴哑光白包耳耳机（`#F4F4F2`），每耳罩一圈平面琥珀环（`#F5A623`），无麦克风杆。下身及膝藏青 A 字裙 + 藏青平底鞋（`#1E2A4A`，全身图必须锁死）。约 6.5 头身。

> 修复注：safety 版发色 `#1F2A44` 与西装 `#22304A` 几乎同色、彩色画面里头发会融进肩线——本版西装改万寿菊黄，发与衣彻底拉开。随之而来的「琥珀瞳色 vs 万寿菊外套近色」风险（pipeline weak，评级低）：两者空间分离（脸内 vs 躯干）、瞳的验收锚是**白高光点 + 圆形**而非色相，已列入 P0 抽卡检查项（第 7 节 Step 1）。

### 2.5 色彩方案表（每块 HEX，硬约束 7）

| 部位 | 颜色 | HEX |
|---|---|---|
| 头发主色 | 深藏青 | `#22335C` |
| 呆毛 / 发梢挑染 / 眼睛 / 耳机环 | 琥珀（全设计唯一琥珀值） | `#F5A623` |
| 皮肤 | 暖浅肤 | `#FFE3CE` |
| 耳机 | 哑光白 | `#F4F4F2` |
| 西装外套 | 万寿菊黄 | `#F2A33C` |
| 衬衫 | 白 | `#FFFFFF` |
| 丝带结 / A 字裙 / 平底鞋 | 藏青 | `#1E2A4A` |
| 六边形胸针 | 金 | `#D9A441` |
| 主播台 | 深藏蓝 | `#16223F` |
| 演播室背景 | 深蓝 | `#101B33` |
| 大屏底色（空白） | 暗蓝 | `#0E1A33` |
| 大屏边缘光 | 青色（与角色色域刻意分离，避开涨跌红绿语义） | `#35E0E0` |

> 修复注：brand 版三个几乎不可辨的琥珀 HEX 已统一为一个 `#F5A623`。嘴部颜色**不进色板**（safety 版把 `#D96A5E` 列进色板但 prompt 里从未出现，设定集与 prompt 脱节）——嘴色降为备注：后期口型资产制作时参考暖红 `#D96A5E`，生成阶段只写形状不写色。

### 2.6 杜绝写实化注释（Annotations）

1. **风格锁**（焊死在角色块内，逐字复用自动携带）：`Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render`
2. **嘴部锁**：flat shapes、no realistic lips、no teeth detail；禁止 lips / lipstick / realistic mouth 等词出现
3. **文字锁**（也在角色块内）：`No text, letters, numbers or logos anywhere in the image`——连同大屏一起锁空白，数据全部后期代码 overlay
4. **手部锁**：默认出画；入画必须逐字带 `simplified rounded cartoon hand`（机器检查不变式：手入画的 prompt 必含该子串）
5. **平涂锁 + 例外条款**：角色本体禁 airbrush 渐变软阴影；**渐变仅限背景天空等场景元素，且用「平涂色带（flat color bands）」实现**——修掉 pipeline 版 S3 渐变天空与平涂锁自相矛盾的挑片判据
6. **可数特征不许被美化合并/删除**：一根居中折线呆毛（锯齿+上扬，绝不许被顺滑化成普通呆毛）、双侧琥珀发梢、每眼一个高光点、一枚居中六边形胸针、每耳罩一圈琥珀环——挑片逐项点数，少一样即废片
7. **场景锁**：matte surfaces only, no mirrors, no reflective glass；天际线用平涂背板不用玻璃窗（五问 #5）
8. **可移植条款**：本包按 Seedream / Nano Banana 写，描述式否定可用；**若日后迁 Runway Gen-4，删除所有 no- 句式改纯正向描述**（02 号笔记坑表：Runway 负向有害）

---

## 3. 角色描述块（所有 prompt 逐字复用这段）

**复用规则（双块结构）**：

- **【角色块】**：**每一条**出角色的 prompt 逐字嵌入，一个字节不许动。手、下装、构图**不在块内**——brand 版把 `simplified cartoon hands` 写进块里、又在两条 prompt 里手工裁掉，破了自己立的逐字规矩；本版从结构上消灭这个诱惑：块内只放「任何景别都可见」的内容
- **【全身块】**：仅全身图（P0/P1/P2/P6）逐字追加——修掉 pipeline 版「表情表半身构图 vs 块内全身描述打架」的固有冲突
- 出图前跑逐字校验脚本（第 7 节 Step 0）

**【角色块】CHAR_BLOCK：**

```
ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image.
```

**【全身块】FULLBODY_BLOCK（仅 P0/P1/P2/P6 追加）：**

```
Below the waist she wears a knee-length navy A-line skirt (#1E2A4A) and simple flat navy shoes (#1E2A4A). Slim build, youthful proportions, about 6.5 heads tall.
```

---

## 4. P0–P3 提示词（基准图 → turnaround 两段式 → 表情表）

> 两段式原因（硬约束 2）：引文 turnaround prompt 是 four-panel（frontal/right/left/back），不含 3⁄4 视图，而设定集判据要五视图——P1 保留引文原结构出四视图，P2 补 3⁄4 前后，并集六视图凑满判据还多一个侧面冗余。`turnaround` 一词全程未动。
> **P1 与 P2 的图生图输入都是 P0 定稿图**（修掉 safety 版 P2 输入悬空的问题）；两段措辞对称，都写 `identical to the reference image`，都带地线对齐、都带手锁（修掉 safety/pipeline 版 turnaround 缺手锁、P1/P2 措辞不对称的问题）。

### P0 · 基准图 —— **文生图**，无输入

呆毛折线形状在这一步靠抽卡锁死（预算见第 7 节），之后一律图生图传递、文字仅兜底——这是 05 号笔记「参考图条件化」的正确用法，修掉 brand 版呆毛只靠每次文字重造的机制缺口。

```
Character design reference sheet, single full-body figure standing straight facing the viewer in a relaxed neutral A-pose, arms slightly away from her body, friendly closed-mouth smile, hands drawn as simplified rounded cartoon hands with minimal finger detail, plain white and grey studio background, flat even lighting, character-sheet quality. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image. Below the waist she wears a knee-length navy A-line skirt (#1E2A4A) and simple flat navy shoes (#1E2A4A). Slim build, youthful proportions, about 6.5 heads tall. Entire figure visible from the top of her head to her shoes, centered composition, no cropping.
```

### P1 · Turnaround 第一段（四视图）—— **图生图，输入 = P0 定稿图**

引文句式原样保留（仅 subject/代词替换）：

```
Create a four-panel turnaround for this anime virtual news anchor to show her frontal, her right side, her left side and her back, in a white and grey background. Keep her strictly identical to the reference image in every panel: same height, same proportions, same outfit, same colors. Full body in every panel, neutral A-pose, arms slightly away from her body, hands drawn as simplified rounded cartoon hands with minimal finger detail, all four figures aligned on a common ground line so the top of the head, shoulders, waist and feet line up across panels, flat even lighting, no labels. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image. Below the waist she wears a knee-length navy A-line skirt (#1E2A4A) and simple flat navy shoes (#1E2A4A). Slim build, youthful proportions, about 6.5 heads tall.
```

### P2 · Turnaround 第二段（3⁄4 前 + 3⁄4 后）—— **图生图，输入 = P0 定稿图（与 P1 同源）**

```
Create a two-panel turnaround for this anime virtual news anchor to show her three-quarter front view and her three-quarter back view, in a white and grey background. Keep her strictly identical to the reference image in both panels: same height, same proportions, same outfit, same colors. Full body in both panels, neutral A-pose, arms slightly away from her body, hands drawn as simplified rounded cartoon hands with minimal finger detail, both figures aligned on a common ground line so the top of the head, shoulders, waist and feet line up across panels, flat even lighting, no labels. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image. Below the waist she wears a knee-length navy A-line skirt (#1E2A4A) and simple flat navy shoes (#1E2A4A). Slim build, youthful proportions, about 6.5 heads tall.
```

### P3 · 表情表 —— **图生图，输入 = P0 定稿图**

覆盖模板要求的喜/怒/哀/惊/惧五基础 + 三个本片特有（晨间眨眼问好 / 播报严肃脸 / 行情下跌担忧脸——直接对应日更晨报的实际镜头需求）。半身构图，**只嵌角色块、不嵌全身块**——构图与描述不再打架。网格崩溃预案见第 7 节 Step 4。

```
Expression sheet: a 4x2 grid of eight head-and-shoulders portraits of the exact same character on a white and grey background, lower body out of frame, identical face shape, hair, headphones and colors in every cell, only the expression changes. Panel 1: joy, a bright open cheerful smile. Panel 2: anger, puffed cheeks and furrowed brows. Panel 3: sadness, downcast eyes and a tiny frown. Panel 4: surprise, wide eyes and a small round open mouth. Panel 5: fear, wide uneasy eyes and a small wavering mouth. Panel 6: signature morning greeting, a cheerful wink with an open-mouth smile. Panel 7: calm focused professional news-reading face. Panel 8: concerned market-watching face, a slight frown with one sweat drop. Every mouth drawn as a simple flat shape. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image.
```

### 补齐六件套：P6 姿态表 / 剪影验证 / P7 道具

> 修复注：三版都只落了四件，Pose Sheet 与 Props 缺失；「纯黑剪影认得出」是模板明文判据，要验不是宣称。

**剪影验证（不靠生成，客观免费）**：把 P0 定稿图人物填充纯黑（ImageMagick 阈值化或任意图像工具），检查三特征可辨：折线呆毛 / bob+耳机双圆轮廓 / 梯形肩线+A 字裙。生成式剪影不可靠，后期涂黑才是实证。

**P6 · 姿态表 —— 图生图，输入 = P0 定稿图**：

```
Pose sheet: a 2x2 grid of four full-body drawings of the exact same character on a white and grey background, identical design and colors in every cell, all four figures aligned on a common ground line. Panel 1: T-pose, arms straight out to the sides. Panel 2: seated news-reading pose behind a plain matte desk block, both hands resting on the desk. Panel 3: standing presenting pose, one arm extended to the side with an open palm. Panel 4: standing waving pose, one hand raised beside her face. All hands drawn as simplified rounded cartoon hands with minimal finger detail. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image. Below the waist she wears a knee-length navy A-line skirt (#1E2A4A) and simple flat navy shoes (#1E2A4A). Slim build, youthful proportions, about 6.5 heads tall.
```

**P7 · 道具表 —— 文生图**（无角色，不嵌角色块）：

```
Prop design sheet on a plain white and grey background, flat colors, clean bold lineart, 2D anime illustration style, no photorealism. Three props of a virtual news studio, each drawn separately with generous spacing: 1) large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone, shown in front view and three-quarter view; 2) one small gold hexagon brooch (#D9A441), enlarged detail view; 3) a sleek matte dark navy news anchor desk (#16223F), simple front view. No text, letters, numbers or logos anywhere in the image.
```

---

## 5. 演播室场景 P4–P5（大屏空白 · overlay 留位 · 固定机位）

> 两景都是**图生图，输入 = P1 四视图**（参考图喂 turnaround 不喂随手一张图——自检问 4 的落地）。机位统一 straight-on eye-level、固定居中构图——每天的 overlay 坐标模板可复用；空白大屏底色 `#0E1A33` + 青色边缘光 `#35E0E0` 为代码叠加的币价卡预留对比度，且与角色色域分离、避开涨跌红绿语义。9:16 与 1080×1920 在**生成参数**里设。

### P4 · 播报主景（坐姿台后，日更主力机位）

手在台面下出画——写进构图而非祈祷模型。

```
Vertical 9:16 composition. Waist-up medium shot, straight-on eye-level camera, fixed centered framing. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image. Scene: she sits centered behind a sleek matte dark navy anchor desk (#16223F), facing the viewer with a friendly closed-mouth smile, both hands out of frame below the desk edge. Behind her, one large completely blank rectangular broadcast screen filling the upper background, dark blue (#0E1A33) with a soft cyan edge glow (#35E0E0) — the screen surface is entirely empty, no charts, no icons, no symbols, no images on it. Deep blue studio background (#101B33), matte surfaces only, no mirrors, no reflective glass, soft even key light with a warm rim light on her hair and shoulders.
```

### P5 · 开场问候 / 收尾挥手景

单手入画，手锁逐字在场；天际线用**平涂色带背板**——无玻璃窗（五问 #5），角色本体仍 flat（平涂锁例外条款只给背景天空）。修掉 safety 版 S3「让她指屏又要求双手出画」的自相矛盾——本景手势与手锁是一致的。

```
Vertical 9:16 composition. Chest-up shot, straight-on eye-level camera, fixed centered framing. ZOE, a 2D anime-style virtual news anchor girl. Flat cel shading, clean bold lineart, flat colors, 2D anime illustration style — no photorealism, no realistic skin texture, no 3D render. Chin-length blunt-cut dark navy bob hair (#22335C) with straight flat bangs, exactly one upright zigzag ahoge on the top center of her head shaped like a rising trendline (a jagged line pointing upward, amber #F5A623), and the two front hair strands symmetrically tipped in amber (#F5A623), no flying hair strands. Large round amber eyes (#F5A623), each eye with a single white highlight dot; thin simple eyebrows; small simplified anime mouth drawn as flat shapes, no realistic lips, no teeth detail. Light warm skin (#FFE3CE). Large matte white over-ear headphones (#F4F4F2) with one flat amber ring (#F5A623) on each ear cup, no microphone. She wears a marigold-yellow blazer (#F2A33C) with sharp lapels over a plain white collared shirt (#FFFFFF); at the collar, a navy ribbon bow (#1E2A4A) with one small gold hexagon brooch (#D9A441) pinned at its center; no earrings, no other jewelry, no patterns, no logos on her clothing. No text, letters, numbers or logos anywhere in the image. Scene: she faces the viewer with her signature cheerful wink and open-mouth smile, one hand raised beside her face in a friendly wave, the raised hand drawn as a simplified rounded cartoon hand with minimal finger detail, the other arm out of frame. Background: a flat matte-painted stylized morning city skyline backdrop panel in simple flat color bands of warm amber (#F2A33C) and deep blue (#101B33), no window glass, no reflections, no mirrors, and the edge of one completely blank glowing screen panel, dark blue (#0E1A33) with a soft cyan edge glow (#35E0E0), entirely empty, no charts, no icons, no symbols on it. Matte surfaces only, soft warm morning light.
```

---

## 6. 一致性自检四问（模板原题作答）

- [x] **哪些元素落在模型崩溃维度？** 逐项列出并处置：写实脸（→漫画风+反写实三连锁）、口型（→扁平简化嘴，无唇无牙）、手（→默认出画，入画简化漫画手，锁逐字进 prompt 含 turnaround）、画面文字（→文字锁进角色块，大屏穷举式空白，数据 overlay）、发丝复杂度（→钝剪 bob+禁飘发，维度整个删除）、小饰品漂移（→压到耳机+胸针两件，全对称/居中/可数）、镜像翻转（→零单侧特征，设计层消灭而非 QC 兜底）、镜面反射（→matte only，平涂背板替玻璃窗）
- [x] **有没有在设计层绕开？** 有，且是本设计的组织原则：对称化消灭镜像漂移、可数化让验收可执行、大件对称几何体（耳机）当身份锚、六边形几何承载币圈意象规避 logo/字符、空白屏升级为 overlay 落位区架构
- [x] **每条 prompt 是否逐字重复了角色描述？** 是——双块结构：角色块 8 条 prompt（P0–P6，P7 无角色除外）逐字嵌入，全身块仅全身图追加；手锁以固定子串形式出现在所有手入画的 prompt；出图前跑字节级校验（第 7 节 Step 0），逐字是机器可验的，不是纪律宣称
- [x] **参考图喂的是 turnaround 而不是随手一张图？** 是——P4/P5 及日后视频生成一律以 P1 四视图（必要时 P1+P2 合并板）为参考输入。⚠️ 诚实标注：「turnaround 优于单张参考图」是 05 号笔记标明的**未实证推论**，首次生产按 sample-before-batch 各出一张样片先验收再批量——这是 L3 该亲手验的第一件事

---

## 7. M1 验收流程（出图后 AI 怎么验、对照什么）

### Step 0 · 出图前：逐字校验（机器）

脚本读取全部 prompt 文件，检查：① 角色块在 P0–P6 中逐字节一致（`str in prompt` 级比对）；② 全身块在 P0/P1/P2/P6 中逐字节一致且**不出现**在 P3/P4/P5；③ 手入画的 prompt（P0/P1/P2/P5/P6）必含子串 `simplified rounded cartoon hand`；④ 全部 prompt 不含 `lips`、`teeth detail` 以外的 teeth、`photoreal` 正向用法。任一失败不出图。

### Step 1 · P0 基准图（sample-before-batch，抽卡预算 5–10 张）

**这一步是锁死呆毛形状的唯一机会**——选定后 P1–P6 全部图生图传递，文字仅兜底。逐张对照可数清单（AI 验法：把 P0 与角色块喂给多模态模型，逐项问 yes/no）：

| # | 检查项 | 判据 |
|---|---|---|
| 1 | 呆毛 | 恰好一根、居中、锯齿折线、末端上扬（不是顺滑弧线）、琥珀色 |
| 2 | 发梢 | 前侧两缕、左右对称、琥珀色；无碎发飘发 |
| 3 | 眼 | 每眼恰好一个白高光点；瞳色为琥珀且**未被外套串成同一平涂色块**（近色风险检查点） |
| 4 | 嘴 | 扁平形状，无唇纹无牙 |
| 5 | 耳机 | 双耳对称包耳、每耳罩一圈琥珀环、无麦克风杆 |
| 6 | 胸针 | 一枚、六边形、居中于领结 |
| 7 | 下装 | 及膝 A 字裙 + 平底鞋、全身完整无裁切、约 6.5 头身 |
| 8 | 风格 | 平涂+清晰线稿，无写实皮肤质感、无 3D 渲染感 |
| 9 | 文字 | 全图无任何文字/字母/数字/logo |

选定 P0 后立即做**剪影验证**：人物填纯黑，三特征（呆毛/双圆头部/梯形肩+A 字裙）可辨才算设计立住；不可辨则回炉调整轮廓，不进入 P1。

### Step 2–3 · P1 / P2 turnaround（各先出一张样片验收再重抽）

- 视图齐全：P1 四视图（frontal/right/left/back）、P2 两视图（3⁄4 前/3⁄4 后），并集覆盖模板五视图判据
- **单图内**：四条水平基准线（头顶/肩/腰/脚）逐视图拉尺核对
- **跨图**：P1、P2 与 P0 三者对同一组基准线核对比例（修掉 safety/brand 版跨图比例无人管的缺口）
- 镜像检查（本设计全对称，剩余检查项）：双侧发梢在每个视图仍双侧、耳机环两侧仍在、胸针仍居中
- 逐视图点数可数清单（Step 1 表 1/2/5/6/7 项）；**脸部特征（高光点/嘴形）放宽为「放大后可辨」**——四格全身图脸部分辨率有限，是 turnaround 路线固有代价，不做像素级核对
- 手：每个视图手型为简化漫画手，无写实指节

### Step 4 · P3 表情表

八格齐全、无缺格串格；每格五官/发型/耳机/呆毛一致；所有嘴为扁平形状。**崩溃预案**：缺格或表情串格 → 拆两次 2×2 出图，或对废格单独补拍（同输入 P0，单表情 prompt）。

### Step 5 · P4 / P5 演播室 + P6 / P7

- 大屏**放大检查**无伪文字乱码，屏面纯空白；边缘光为青色非红/绿
- 机位 straight-on eye-level、构图居中——选定样片后**记录 overlay 落位区坐标**（屏面矩形四角），存成日更模板
- P4 双手确实出画；P5 仅一只简化漫画手入画
- 背景无镜面/玻璃反射；角色本体无渐变软阴影（渐变仅背景色带）
- 半身景**不查**头身比（waist-up 不可验）——分层验收：全身图查比例/下装/地线，半身图查呆毛/发梢/高光点/胸针/耳机环，表情表查五官一致

### 通用纪律

- 每类昂贵图先 1 张 sample 给人看再批量（OpenMontage 资产三规则）；出样前声明生成路径（工具/模型/模式/理由）
- 挑片判据 = 上表逐项点数，**少一样即废片**；「应该没问题」不算验收，验收 = 贴对照结果
- 平台迁移触发条款：迁 Runway Gen-4 前，全部 prompt 去 no- 句式改正向（见 2.6 第 8 条）