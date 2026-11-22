# Switch and build timeline for funnel reads (Design-Agent, 2026-11-17 14:50 UTC)

Cut hour buckets at these minutes. When an hour holds a change, drop that hour from both before and after.

| UTC | Change | Funnel steps it can move |
|---|---|---|
| Nov 13 05:39 | newKindTag on | catch choice |
| Nov 13 06:05 | come back tomorrow gift on (#3772) | D1 |
| Nov 16 03:30 | Secret Cats restart (v718) | all, mixed servers before |
| Nov 16 04:58 | minute 6 return line on (#4626) | D1 |
| Nov 17 06:27 | Tier ladder #5056 live (T4 to T6 needs) | tier_4 to tier_7 |
| Nov 17 09:30 | fxOneAdded on | Park landing, load |
| Nov 17 12:22 | rankUpRightAway on | v8 steps 7 to 16 |
| Nov 17 about 13:15 | v8 steps 9 to 14 from real moments (2773551e) | v8 steps 8 to 14 (counting changes, not players) |
| Nov 17 14:01 | storeRework on, fxAfterLoad on | store_v1, load time |
| Nov 18 20:00 | Harvest fold, Better on Every Device restart; palDay on after it | all |
| Thu Nov 19 12:05 | parkRingEarly (planned) | v8 steps 18 to 19 |
| Sat Nov 21 12:05 | tier3Path (planned) | Park to Tier 3 |
| Sun Nov 22 12:05 | tomorrowCard (planned) | D1 |
| Mon Nov 23 12:05 | parkTrailBack + parkGateTrail (planned) | v8 steps 17 to 18 |
| Wed Nov 25 20:00 | Harvest Hollow opens | Tier 2 play time |

Hour read rules:
- An hour bucket needs at least 30 players entering the step before we read its rate. With fewer, merge neighbouring hours on the same side of a change.
- Compare the same UTC hours on different days, not morning against evening, because the mix of devices and ages changes through the day.
- Day reads stay the decision tool. Hour reads only show whether a change took effect at its minute.
- Steps 8 to 14 before about 13:15 UTC Nov 17 are not comparable with after.

- Growth 14:52 UTC: park_left #5078 live 13:18 UTC (place v865). Real v8 steps 9 and 11 to 14 #5082 live 13:24 UTC (place v866). storeRework and fxAfterLoad on 14:01 UTC.

Added 15:20 UTC (Derek's ASAP override): parkRingEarly 15:05, parkGateTrail 15:06, parkTrailBack 15:06, tier3Path 15:07, tomorrowCard 15:07 UTC Nov 17. Strip RANK UP button removed in #5108 (minute on publish). cannonCue next. Read them together: 14:00 to 15:00 before, from 16:00 after.

## Switches waiting to go on (issues closed under Derek's 15:45 UTC rule, code in game, switch off)
- palDay (#4913): after the Wed Nov 18 20:00 UTC restart.
- cafeGrows (#4543): after Model-Agent's wall fit at four sizes and Sync's look, planned Wed Nov 18.
- tables spread (#3867, PR #4763): Thu Nov 19 about 06:00 UTC, if it merges behind a switch today.
- stationCut (#5112): after Review-QA passes #5116 and GE's trigger.
- goalToAlley: after Review-QA passes.
- cannonCue (#5097): next, via Motion-FX's LiveFlags PR.
