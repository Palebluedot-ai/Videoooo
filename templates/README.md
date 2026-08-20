# templates —— L0 前期设定的可填模板

规范正文见 [`docs/notes/05-industrial-sop.md`](../docs/notes/05-industrial-sop.md)。

| 文件 | 干什么 | 对应 SOP |
|---|---|---|
| [beat-map.md](beat-map.md) | 剧本层：Hook → Escalation → Reveal → Landing | 第二节 |
| [shots.example.yaml](shots.example.yaml) | 分镜层：5-Aspect Shot Breakdown（S01 是填满的示例） | 第三节 |
| [character-sheet.md](character-sheet.md) | 设定集六件套 + turnaround 五视图 | 第四节 |

## 开工三步

```
mkdir -p docs/preproduction
cp templates/beat-map.md templates/character-sheet.md docs/preproduction/
cp templates/shots.example.yaml docs/preproduction/shots.yaml
```

填完分镜表后校验（**L0 的硬门**，退出码必须是 0）：

```
uv run --with pyyaml tools/check_shotlist.py docs/preproduction/shots.yaml
```

## 校验器查什么

| 检查 | hero 镜头 | 普通镜头 |
|---|---|---|
| 五维（subject / subject_motion / scene / spatial_framing / camera）完整 | ✗ 错误 | ⚠ 警告 |
| `scene.overlays` 键存在 | ✗ 错误 | ✗ 错误 |
| overlays 混进 `spatial_framing` 景深轴 | ✗ 错误 | ✗ 错误 |
| camera 七项书写顺序 | ✗ 错误 | ✗ 错误 |
| 空泛词（电影感 / 4K / 高细节…） | ⚠ 警告 | ⚠ 警告 |
| FG / MG / BG 三层齐 | ⚠ 警告 | ⚠ 警告 |

反向验证已跑过：故意把 camera 顺序颠倒 + 把字幕塞进景深轴 → 退出码 1，两条都报出来。
