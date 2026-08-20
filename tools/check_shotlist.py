#!/usr/bin/env python3
"""5-Aspect 分镜表校验器 —— 让 L0 的判据机器可验，而不是「我觉得填完了」。

规范来源：OpenMontage cinematic pipeline / scene-director.md（逐字读取）
用法：uv run --with pyyaml tools/check_shotlist.py [--strict] <shots.yaml>
  --strict  警告也算失败（L0 收口用这个）
退出码：0 = 全过；1 = 有问题（可直接接进 CI 或 pre-commit）

v2（2026-08-20）修复两个静默放行洞（tools/fixtures/ 有对应坏例子）：
  - camera / spatial_framing 写成 YAML 字典时整段检查被跳过 → 现在字典也查
  - 模板逐字副本可以全绿通过 → 现在有模板残留检测
"""
import sys
import yaml

# scene-director 规定的相机参数书写顺序，一个字都不能乱
CAMERA_ORDER = [
    "playback_speed", "lens_distortion", "height",
    "angle", "focus_dof", "steadiness", "movement",
]
SCENE_KEYS = ["overlays", "pov", "setting", "time_of_day", "dynamics"]
ASPECTS = ["subject", "subject_motion", "scene", "spatial_framing", "camera"]

# 空泛词黑名单：AI 锚不住，必须换成具体器材型号
VAGUE = ["电影感", "高细节", "4K", "8K", "cinematic", "high detail", "超清", "精美", "大片感"]
# 叠加元素关键词：出现在景深轴里 = 违反 overlays 单列规则
OVERLAY_WORDS = ("字幕", "overlay", "标题卡", "logo", "水印")
# 模板残留指纹：抄了 templates/shots.example.yaml 没改成自己的内容
TEMPLATE_MARKS = ("示例项目", "单个机器人清道夫")


def _is_empty(v):
    return v is None or (isinstance(v, str) and not v.strip()) or (
        isinstance(v, (dict, list)) and not v)


def _dict_text(d):
    """把字典的键值摊平成一段文本，供关键词类检查使用。"""
    return " ".join(f"{k} {v}" for k, v in d.items() if v is not None)


def check_camera(cam, hero, tag, errs, warns):
    """camera 支持两种写法：有序字符串（推荐）或字典（键序即书写序）。"""
    if _is_empty(cam):
        return  # 缺失由五维完整性检查负责
    if isinstance(cam, dict):
        keys = [k for k in cam.keys() if k in CAMERA_ORDER]
        unknown = [k for k in cam.keys() if k not in CAMERA_ORDER]
        if unknown:
            warns.append(f"{tag}: camera 有未知键 {unknown} —— 规范七项是 {', '.join(CAMERA_ORDER)}")
        missing = [k for k in CAMERA_ORDER if k not in cam]
        if missing:
            (errs if hero else warns).append(f"{tag}: camera 缺 {', '.join(missing)}")
        expect = [k for k in CAMERA_ORDER if k in keys]
        if keys != expect:
            errs.append(f"{tag}: camera 书写顺序错（字典键序即书写序）—— 规范是 {' → '.join(CAMERA_ORDER)}")
        for k, v in cam.items():
            if _is_empty(v):
                warns.append(f"{tag}: camera.{k} 是空的")
    elif isinstance(cam, str):
        found = [(cam.find(k), k) for k in CAMERA_ORDER if k in cam]
        missing = [k for k in CAMERA_ORDER if k not in cam]
        if missing:
            (errs if hero else warns).append(f"{tag}: camera 缺 {', '.join(missing)}")
        seq = [k for _, k in sorted(found)]
        expect = [k for k in CAMERA_ORDER if k in cam]
        if seq != expect:
            errs.append(f"{tag}: camera 书写顺序错 —— 规范是 {' → '.join(CAMERA_ORDER)}")
    else:
        errs.append(f"{tag}: camera 类型不对（{type(cam).__name__}）—— 写成有序字符串或字典")


def check_spatial(sf, tag, errs, warns):
    if _is_empty(sf):
        return
    text = sf if isinstance(sf, str) else _dict_text(sf) if isinstance(sf, dict) else str(sf)
    if any(w in text for w in OVERLAY_WORDS):
        errs.append(f"{tag}: spatial_framing 里出现了叠加元素 —— overlays 不属于 FG/MG/BG 景深轴，单列进 scene.overlays")
    if not all(x in text for x in ("FG", "MG", "BG")):
        warns.append(f"{tag}: spatial_framing 建议写全 FG / MG / BG 三层")


def check_shot(shot, idx):
    """返回 (errors, warnings)。errors 会让整体判定失败。"""
    errs, warns = [], []
    sid = shot.get("id") or f"#{idx + 1}"
    hero = bool(shot.get("hero"))
    tag = f"{sid}{' [hero]' if hero else ''}"

    # ── 五维完整性 ──
    for a in ASPECTS:
        if _is_empty(shot.get(a)):
            (errs if hero else warns).append(f"{tag}: 缺 {a}")

    # ── scene 子字段 ──
    scene = shot.get("scene")
    if isinstance(scene, dict):
        for k in SCENE_KEYS:
            if k not in scene:
                warns.append(f"{tag}: scene 缺子字段 {k}")
            elif k != "overlays" and _is_empty(scene.get(k)):
                warns.append(f"{tag}: scene.{k} 是空的")
        if "overlays" not in scene:
            errs.append(f"{tag}: scene.overlays 缺失 —— overlays 必须单列，不进景深轴")
    elif scene is not None and not _is_empty(scene):
        warns.append(f"{tag}: scene 建议写成带 overlays/pov/setting/time_of_day/dynamics 的结构")

    check_spatial(shot.get("spatial_framing"), tag, errs, warns)
    check_camera(shot.get("camera"), hero, tag, errs, warns)

    # ── 空泛词 ──
    blob = " ".join(
        (a_v if isinstance(a_v := shot.get(a, ""), str) else
         _dict_text(a_v) if isinstance(a_v, dict) else str(a_v))
        for a in ASPECTS)
    hit = [w for w in VAGUE if w.lower() in blob.lower()]
    if hit:
        warns.append(f"{tag}: 出现空泛词 {hit} —— AI 锚不住，换成具体器材型号")

    return errs, warns


def main():
    args = [a for a in sys.argv[1:] if a != "--strict"]
    strict = "--strict" in sys.argv[1:]
    if len(args) != 1:
        print(__doc__)
        return 2
    raw = open(args[0], encoding="utf-8").read()
    doc = yaml.safe_load(raw)

    all_errs, all_warns = [], []
    shots = (doc or {}).get("shots") or []
    if not shots:
        print("✗ 没有找到 shots")
        return 1

    # ── 模板残留检测（防「零工作量过硬门」）──
    for mark in TEMPLATE_MARKS:
        if mark in raw:
            all_errs.append(f"模板残留：文件里还有「{mark}」—— 抄完模板必须换成你自己的内容")

    heroes = sum(1 for s in shots if s.get("hero"))
    if heroes < 1:
        all_errs.append("没有任何镜头标 hero: true —— 至少一个重点镜头必须五维全填")

    for i, s in enumerate(shots):
        e, w = check_shot(s, i)
        all_errs += e
        all_warns += w

    print(f"镜头 {len(shots)} 个（hero {heroes} 个）{' [--strict]' if strict else ''}\n")
    for w in all_warns:
        print(f"  ⚠  {w}")
    for e in all_errs:
        print(f"  ✗  {e}")

    failed = bool(all_errs) or (strict and bool(all_warns))
    if failed:
        print(f"\n✗ 不通过：{len(all_errs)} 个错误，{len(all_warns)} 个警告" +
              ("（--strict 下警告也算失败）" if strict and not all_errs else ""))
        return 1
    print(f"\n✓ 通过（{len(all_warns)} 个警告）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
