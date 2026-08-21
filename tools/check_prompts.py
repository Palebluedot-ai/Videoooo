#!/usr/bin/env python3
"""M1 Step 0：出图前的 prompt 逐字校验（角色块字节级一致性）。

规则来自 docs/preproduction/character-sheet.md 第 7 节 Step 0：
  ① 角色块在 P0-P6 中逐字节出现（P7 无角色，豁免）
  ② 全身块在 P0/P1/P2/P6 逐字出现，且不出现在 P3/P4/P5
  ③ 手入画的 prompt（P0/P1/P2/P5/P6）必含 'simplified rounded cartoon hand'
  ④ 'lips' 只许以 'no realistic lips' 出现；'photoreal' 只许以 'no photorealism' 出现
用法：uv run tools/check_prompts.py     退出码 0=可出图
"""
import sys, re
from pathlib import Path

D = Path(__file__).parent.parent / "docs/preproduction/prompts"
CHAR = (D / "_char-block.txt").read_text().strip()
FULL = (D / "_fullbody-block.txt").read_text().strip()

CHAR_IN = ["P0-base", "P1-turnaround-4panel", "P2-turnaround-3q", "P3-expressions",
           "P4-studio-desk", "P5-studio-greeting", "P6-poses"]
FULL_IN = ["P0-base", "P1-turnaround-4panel", "P2-turnaround-3q", "P6-poses"]
FULL_OUT = ["P3-expressions", "P4-studio-desk", "P5-studio-greeting"]
HAND_IN = ["P0-base", "P1-turnaround-4panel", "P2-turnaround-3q", "P5-studio-greeting", "P6-poses"]
HAND = "simplified rounded cartoon hand"

errs = []
prompts = {p.stem: p.read_text() for p in sorted(D.glob("P*.txt"))}

for n in CHAR_IN:
    if CHAR not in prompts.get(n, ""):
        errs.append(f"{n}: 角色块未逐字出现（一个字节都不许动）")
for n in FULL_IN:
    if FULL not in prompts.get(n, ""):
        errs.append(f"{n}: 全身块缺失")
for n in FULL_OUT:
    if FULL in prompts.get(n, ""):
        errs.append(f"{n}: 半身构图却带了全身块（构图与描述打架）")
for n in HAND_IN:
    if HAND not in prompts.get(n, ""):
        errs.append(f"{n}: 手入画但缺手锁 '{HAND}'")
for n, t in prompts.items():
    for bad in re.findall(r'.{0,14}lips', t):
        if "no realistic lips" not in bad:
            errs.append(f"{n}: 'lips' 未以 'no realistic lips' 形式出现：…{bad}")
    for bad in re.findall(r'.{0,6}photoreal\w*', t):
        if "no photorealism" not in bad:
            errs.append(f"{n}: 'photoreal' 未以 'no photorealism' 形式出现：…{bad}")

print(f"prompt 文件 {len(prompts)} 个")
for e in errs:
    print(f"  ✗ {e}")
print("✗ 不可出图" if errs else "✓ 全部通过，可出图")
sys.exit(1 if errs else 0)
