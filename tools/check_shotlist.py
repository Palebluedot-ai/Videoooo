#!/usr/bin/env python3
"""5-Aspect 分镜表校验器 —— 让 L0 的判据机器可验，而不是「我觉得填完了」。

规范来源：OpenMontage cinematic pipeline / scene-director.md（逐字读取）
用法：uv run --with pyyaml tools/check_shotlist.py <shots.yaml>
退出码：0 = 全过；1 = 有问题（可直接接进 CI 或 pre-commit）
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


def check_shot(shot, idx):
    """返回 (errors, warnings)。errors 会让整体判定失败。"""
    errs, warns = [], []
    sid = shot.get("id") or f"#{idx + 1}"
    hero = bool(shot.get("hero"))
    tag = f"{sid}{' [hero]' if hero else ''}"

    # ── 五维完整性 ──
    for a in ASPECTS:
        v = shot.get(a)
        empty = v is None or (isinstance(v, str) and not v.strip()) or (isinstance(v, dict) and not v)
        if empty:
            (errs if hero else warns).append(f"{tag}: 缺 {a}")

    # ── scene 子字段 ──
    scene = shot.get("scene")
    if isinstance(scene, dict):
        for k in SCENE_KEYS:
            if k not in scene:
                warns.append(f"{tag}: scene 缺子字段 {k}")
            elif k != "overlays":
                v = scene.get(k)
                if v is None or (isinstance(v, str) and not v.strip()):
                    warns.append(f"{tag}: scene.{k} 是空的")
        # overlays 必须存在（可以是空列表，但不能没有这个键）
        if "overlays" not in scene:
            errs.append(f"{tag}: scene.overlays 缺失 —— overlays 必须单列，不进景深轴")
    elif scene is not None:
        warns.append(f"{tag}: scene 建议写成带 overlays/pov/setting/time_of_day/dynamics 的结构")

    # ── overlays 混进景深轴 ──
    sf = shot.get("spatial_framing")
    if isinstance(sf, str) and any(w in sf for w in ("字幕", "overlay", "标题卡", "logo", "水印")):
        errs.append(f"{tag}: spatial_framing 里出现了叠加元素 —— overlays 不属于 FG/MG/BG 景深轴")

    # ── camera 书写顺序 ──
    cam = shot.get("camera")
    if isinstance(cam, str) and cam.strip():
        found = [(cam.find(k), k) for k in CAMERA_ORDER if k in cam]
        missing = [k for k in CAMERA_ORDER if k not in cam]
        if missing:
            (errs if hero else warns).append(f"{tag}: camera 缺 {', '.join(missing)}")
        seq = [k for _, k in sorted(found)]
        expect = [k for k in CAMERA_ORDER if k in cam]
        if seq != expect:
            errs.append(f"{tag}: camera 书写顺序错 —— 规范是 {' → '.join(CAMERA_ORDER)}")

    # ── 空泛词 ──
    blob = " ".join(str(shot.get(a, "")) for a in ASPECTS)
    hit = [w for w in VAGUE if w.lower() in blob.lower()]
    if hit:
        warns.append(f"{tag}: 出现空泛词 {hit} —— AI 锚不住，换成具体器材型号")

    # ── 景深三层 ──
    if isinstance(sf, str) and sf.strip() and not all(x in sf for x in ("FG", "MG", "BG")):
        warns.append(f"{tag}: spatial_framing 建议写全 FG / MG / BG 三层")

    return errs, warns


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    shots = (doc or {}).get("shots") or []
    if not shots:
        print("✗ 没有找到 shots")
        return 1

    all_errs, all_warns = [], []
    for i, s in enumerate(shots):
        e, w = check_shot(s, i)
        all_errs += e
        all_warns += w

    heroes = sum(1 for s in shots if s.get("hero"))
    print(f"镜头 {len(shots)} 个（hero {heroes} 个）\n")
    for w in all_warns:
        print(f"  ⚠  {w}")
    for e in all_errs:
        print(f"  ✗  {e}")

    if all_errs:
        print(f"\n✗ 不通过：{len(all_errs)} 个错误，{len(all_warns)} 个警告")
        return 1
    print(f"\n✓ 通过（{len(all_warns)} 个警告）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
