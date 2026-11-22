# Switch-on checklist: tonight (Tue Nov 17) and Wednesday (Nov 18) (Design-Agent, 17:00 UTC)

All times UTC. Every flip uses the flags workflow (`flags set <key> true`). Tell Growth the exact minute of every flip. Only Derek starts a restart.

## Already on today (no action)
rankUpRightAway 12:22, storeRework and fxAfterLoad 14:01, parkRingEarly 15:05, parkGateTrail and parkTrailBack 15:06, tier3Path and tomorrowCard 15:07, areaOnly 15:21, cannonCue 15:43.

## Tonight, Tue Nov 17: Better on Every Device
| Time | Who | Step |
|---|---|---|
| by 18:00 | GE | All of tonight's PRs merged, publish green, new place version (coordinator checks at 18:00 and 19:00). |
| by 18:00 | GE, Sync | Streaming radius 384: ships tonight only if Sync's pop-in check passed by 18:00 (it is a place setting, so it takes the restart). Otherwise it waits for Wednesday's restart. |
| 18:00 | GE | Run `flags show` and post the state of `padControls` and `deviceFixes` (the update's controller and phone/tablet parts). |
| 19:55 | Growth | Confirm live, then the @everyone group post. |
| 20:00 | Derek | Starts the restart. |
| 20:00 + 1 min | GE | `padControls` and `deviceFixes` on, if either is still off. Then the admin events (Cat Storm, then Bowl Frenzy). |
| 20:00 to 21:00 | Growth | CCU at 19:50, 20:30 and 21:00. Description edit at 20:05. |
| 21:10 | Growth | Christmas Event page (retry after the 403), then send the id to GE for Config.UpdateEvents (startsAt 1797105600). |

## Wednesday Nov 18
| Time | Who | Step |
|---|---|---|
| 12:05 | GE | `cafeGrows` on, only once Model-Agent's wall fit at four sizes and Sync's look have passed. If either is missing, it waits until after the 20:00 restart. Then close nothing (#4543 is already closed) and tell Growth, Design and Model. |
| (done) | GE | Harvest merged Tue 16:27 UTC (#4382, switch off). No Wednesday fold. Only #5126 (save version 51) is left: it ships on a restart before Nov 25 (Wednesday's 20:00 restart if it is ready by 18:30). |
| 19:49 | GE | CCU. |
| 20:00 | Derek | Starts the restart. |
| 20:00 + 1 min | GE | `palDay` on (Pal Day, #4913). Tell Growth, whose baseline is Nov 15 to 18. Then the admin events. |
| after review | GE | `goalToAlley` (tap "Catch 1 more cat" opens the Cannon on the Alleyway) and `stationCut` (#5112), each as soon as it passes Review-QA. |

## Stays off (do not flip)
storeGuard (Derek decides), backdropsNear (not the same week as the streaming radius change), introSplit and noIntro (tests), harvestPieLow (Harvest week only), fusion, ticketBooth, dragonKeep and tier8 to tier10 (check they are already on; they are listed off by default only).

## Next after Wednesday
Thu Nov 19 about 06:00: Model-Agent arms #4763 (tables spread, #3867). Close #3867 when it merges.


Update 2026-11-18 04:22 UTC: already ON per the flags store: parkRingEarly, parkGateTrail, parkTrailBack (their Nov 19 and Nov 23 flips are dropped); also ON tonight: spinCat 02:42, nightSpread 03:10, netTiers 03:37, catFollower 03:51, parkRankPoint 04:17, parkFirstEasy 04:18, tradeSpot 04:21. The Nov 20 parkRingEarly read still stands.
