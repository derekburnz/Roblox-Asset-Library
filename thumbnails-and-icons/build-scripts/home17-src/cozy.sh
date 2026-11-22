#!/bin/bash
PY=/tmp/claude-0/-home-claude/ce1429cf-f5fc-5c68-88c3-6f1c25722a5e/scratchpad/bpyenv/bin/python
cd "$(dirname "$0")"
r() { env CUT_AZ=${3:-26} CUT_EL=${4:-14} CUT_S=40 CUT_GLOSS=0.3 CUT_RIM=0.4 CUT_LENS=50 $PY cut.py cozy/$1.png ${5:-1100} "$2" > cozy/log_$1.txt 2>&1 && echo ok $1 || echo FAIL $1; }
r bed "CatCafe_Furniture_CatBed@0,0,0,0,1" &
r tub "CatCafe_Decor_BathtubSofa@0,0,0,0,1" &
r cushion "CatCafe_Prop_GrandCushion@0,0,0,0,1" &
r seat "CatCafe_Furniture_WindowSeat@0,0,0,0,1" &
wait
r cafe "CatCafe_Plot_Cafe_Lilac@0,0,0,0,1" 30 18 1400 &
r pool "CatCafe_Camp_Park_MysticPool@0,0,0,0,1" 26 18 1400 &
r castle "CatCafe_Camp_Castle@0,0,0,0,1" 26 12 1400 &
r sit_Balloon "CatCafe_Cat_Balloon_Sit@0,0,0,0,1" 20 8 &
wait
r sit_Comet "CatCafe_Cat_Comet_Sit@0,0,0,0,1" 20 8 &
r sit_KingCroissant "CatCafe_Cat_KingCroissant_Sit@0,0,0,0,1" 20 8 &
r sit_Nebula "CatCafe_Cat_Nebula_Sit@0,0,0,0,1" 20 8 &
r sit_Moonstag "CatCafe_Cat_Moonstag_Sit@0,0,0,0,1" 20 8 &
wait
echo COZYDONE
