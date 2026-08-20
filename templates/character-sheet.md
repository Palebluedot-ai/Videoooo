# Character Sheet —— 角色设定集模板（六件套）

> 规范来源：传统动画产业通行规范（多来源一致）
> **这是沟通契约，不是画着好看。** 产出于前期，贯穿 concept → final frame。
> 在 AI 视频里它还有第二个身份：**参考图条件化的资产源头**（见 L3）。

角色名：
一句话定位：

---

## 1. Turnaround（五视图）

| 视图 | 文件 | 状态 |
|---|---|---|
| 正面 front | | ☐ |
| 3⁄4 前 | | ☐ |
| 侧面 profile | | ☐ |
| 3⁄4 后 | | ☐ |
| 背面 back | | ☐ |

**生成 prompt**（原样，`turnaround` 这个词不能改——它是行业标准正投影术语，模型认它）：

```
Create a four-panel turnaround for this <subject> to show his frontal,
his right side, his left side and his back, in a white and grey background.
```

- [ ] 白灰背景（制作友好，后续抠图/参考都方便）
- [ ] 每一个视图都明确列出，没指望模型自己补
- [ ] 五视图之间比例一致（对着同一条基准线检查头顶/肩/腰/脚）

## 2. Expression Sheet（表情表）
喜 / 怒 / 哀 / 惊 / 惧 + 本片特有的：

## 3. Pose Sheet（姿态表）
T-pose · 关键动作姿态 · 剪影视图（剪影认得出 = 设计立住了）

## 4. Props（道具）

## 5. Color Palette（色彩方案）
> **每一块必须标代码**（HEX / RGB / Pantone），不许只贴色块

| 部位 | 颜色 | HEX |
|---|---|---|
| | | `#` |

## 6. Annotations（注释）
比例关系 · 独特特征 · 设计要点 · **哪些细节绝不能被 AI 美化掉**

---

## 🔑 一致性自检（AI 视频专用）
- [ ] 这个角色的**哪些元素落在模型崩溃维度**？（动态属性变化 8–24% / 动态空间关系 19–21%）
- [ ] 有没有在**设计层**绕开？（例：真人脸 → 机器人 + 表情屏）
- [ ] 每条 prompt 是否**逐字重复**了角色描述？
- [ ] 参考图喂的是 **turnaround** 而不是随手一张图？
