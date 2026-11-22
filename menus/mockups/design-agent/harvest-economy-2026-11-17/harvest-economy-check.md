# Harvest Hollow economy check (Design-Agent, 2026-11-17 13:35 UTC)

Spec target (harvest-hollow-spec.md section 3): about 60 pumpkins an hour, the whole Stall (480) in about 8 hours over the 12 days.

## What the built code gave (claude/harvest-owned before 13a12902)
- Patch: 12 shared spots, +1 each, regrow 90 s (45 s with 6+ players near). A lone player can pick all 12 every 90 s: about 480 an hour.
- Catches: strays up to 10 out, one more every 8 s. Average pumpkins a catch = 0.55x1 + 0.32x2 + 0.09x3 + 0.035x5 + 0.005x10 = 1.69. At about 2 catches a minute that is about 200 an hour.
- First visit of the day: +10.
- Lone player: about 680 an hour, so everything in about 45 minutes. A crowded server (10 players) was about 170 an hour each, about 3 hours.

## Change (commit 13a12902 on #4439, rides the Wed Nov 18 fold)
- Stall prices x3: hats 120, 150, 180, 210, 240; decor 75, 90, 90, 75, 120, 90. Total 1,440.
- Patch regrow 300 s, 150 s with 6+ players near.
- First visit of each UTC day +40 (12 days = 480, a third of the Stall), so coming back daily pays.
- Catch rewards unchanged (our rule: raise the cost, never cut rewards).

## Estimate after (catches assumed about 2 a minute, not measured)
| Player | Pumpkins an hour (patch + catches) | Hours of play for the rest after 12 daily visits (960) |
|---|---:|---:|
| Alone in the area | about 145 + 200 | about 3 |
| 4 players, not busy | about 35 + 190 | about 4 |
| 10 players, busy | about 30 + 75 | about 9 |
A 20 minute a day player gets 12 x (40 + about 70) = about 1,300, nearly everything, but only by coming back on most days.

## Read on Thu Nov 26 (Growth)
Pumpkins earned per player per hour in the area, and how many own all 11 items. If over a quarter own all 11 by Sat Nov 28, raise the prices for the second week, never take pumpkins back.
