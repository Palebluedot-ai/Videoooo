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

## 校验器查什么（v2）

| 检查 | hero 镜头 | 普通镜头 |
|---|---|---|
| 五维完整 | ✗ 错误 | ⚠ 警告 |
| `scene.overlays` 键存在 | ✗ | ✗ |
| overlays 混进景深轴（**字符串或字典写法都查**） | ✗ | ✗ |
| camera 七项书写顺序（**字符串或字典写法都查**） | ✗ | ✗ |
| **模板残留**（「示例项目」等指纹没换掉） | ✗ | ✗ |
| **无任何 hero 镜头** | ✗ 整表 | — |
| 空泛词 / FG-MG-BG 三层 | ⚠ | ⚠ |

`--strict`：警告也算失败（L0 收口用它）。

**尺子自己的测试**：`tools/fixtures/` 8 个例子（1 好 7 坏，每个坏例子只坏一处、文件名即坏处）。

```
bash tools/run_fixtures.sh
```

全部符合预期才退出 0。⚠️ 注意：**示例模板本身会被模板残留检测拦下**——这是特性，抄完必须换成你自己的内容才可能过门。

> v1 有两个静默放行洞（模板逐字副本可全绿过门；camera 写成 YAML 字典时检查整段跳过），
> 2026-08-20 修复，经 fixtures 正反验证。教训见 `docs/notes/07-study-runway.md` 第零节。
