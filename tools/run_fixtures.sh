#!/bin/bash
# 尺子的回归测试：good 必须绿，6 个 bad 必须红且报对原因。
# 用法：bash tools/run_fixtures.sh    （全对 → 退出 0）
cd "$(dirname "$0")/.."
fail=0
printf "%-28s %-8s %-8s %s\n" "fixture" "期望" "实际" "判定"
for f in tools/fixtures/*.yaml; do
  name=$(basename "$f")
  case "$name" in good*) want=0 ;; *) want=1 ;; esac
  uv run --quiet --with pyyaml tools/check_shotlist.py "$f" >/tmp/fixture-out.txt 2>&1
  got=$?
  if [ "$got" -eq "$want" ]; then verdict="✓"; else verdict="✗ 不符"; fail=1; fi
  printf "%-28s exit=%-3s exit=%-3s %s\n" "$name" "$want" "$got" "$verdict"
done
[ $fail -eq 0 ] && echo "—— 全部符合预期 ——" || echo "—— 有 fixture 不符，尺子坏了 ——"
exit $fail
