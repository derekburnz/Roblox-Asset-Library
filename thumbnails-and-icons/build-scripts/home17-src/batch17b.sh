#!/bin/bash
PY=/tmp/claude-0/-home-claude/ce1429cf-f5fc-5c68-88c3-6f1c25722a5e/scratchpad/bpyenv/bin/python
cd "$(dirname "$0")"
for c in "$@"; do
  env CUT_AZ=16 CUT_EL=3 CUT_S=48 CUT_GLOSS=0.3 CUT_RIM=0.4 CUT_LENS=40 $PY cut.py cut17/big_$c.png 1500 "CatCafe_Cat_$c@0,0,0,0,1" > cut17/logb_$c.txt 2>&1 && echo ok $c || echo FAIL $c
done
