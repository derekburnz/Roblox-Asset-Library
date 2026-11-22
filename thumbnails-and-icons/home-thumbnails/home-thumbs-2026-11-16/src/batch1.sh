#!/bin/bash
PY=/tmp/claude-0/-home-claude/ce1429cf-f5fc-5c68-88c3-6f1c25722a5e/scratchpad/bpyenv/bin/python
cd "$(dirname "$0")"
r(){ out=$1; size=$2; spec=$3; shift 3; env "$@" $PY cut.py cut/$out.png $size "$spec" > log_$out.txt 2>&1 && echo ok $out || echo FAIL $out; }
for c in Tabby Ginger Tortie Calico Taxi Duckling Void Blossom Neon Balloon Comet Tuxedo; do
  r cat_$c 900 "CatCafe_Cat_$c@0,0,0,0,1" CUT_AZ=28 CUT_EL=10 CUT_S=48
done
for c in Tabby Ginger Tuxedo; do r work_$c 900 "CatCafe_Cat_${c}_Work@0,0,0,0,1" CUT_AZ=25 CUT_EL=10 CUT_S=48; done
r cannon 1200 "CatCafe_Square_Cannon@0,0,0,0,1" CUT_AZ=35 CUT_EL=14 CUT_S=48
