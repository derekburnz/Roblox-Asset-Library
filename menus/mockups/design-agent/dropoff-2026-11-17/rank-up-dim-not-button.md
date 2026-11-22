# Rank Up pointer: dim and arrow, no extra button (Design-Agent, 2026-11-17 15:05 UTC)

Derek, 15:00 UTC: "put all the first 5 min/turorial step and tutorial changes into game asap also no need for extra rankup button above the bottom middle tutorial step its just ugly make I think a dim screen and arrow point to rank menu is fine then a dim and arrow to rankup button".

## 1. Remove the strip's RANK UP button
- HUD._renderStripBuy: a rank up line (RankFirst.isLine) no longer shows `_stripBuy` with RankFirst.BUTTON. The strip's Buy button keeps its other job (offers).
- HUD.goalButton falls back to the goal card, so every arrow and ring points at the goal card (the Rank menu).
- RankFirst.LINES name what the arrow points at now: touch "Rank up! Tap YOUR GOAL to open the Park", keyboard "Click YOUR GOAL", gamepad "Select YOUR GOAL". They must fit the strip on smallphone (uigate).

## 2. Dim and arrow, two steps (this is the RankSpot walk-through, live since launch week)
- Step 1 (RankSpot phase "button"): dim the screen, cut out the goal card, ring it and point the arrow at it. Words: "You can rank up!".
- Step 2 (phase "confirm", the Rank Up window open): dim around the window and point the arrow at its RANK UP button. Words: "Press to rank up". This replaces the Nov 16 noDim ring on the window's button. The window's X must stay visible and tappable, so the dim is drawn under the window, never over it.
- When rankUpRightAway opens the window by itself, go straight to step 2.
- Safe zones only (cafes, Town Square, area camps), as Derek set on Nov 12. In a catching area: no dim, only the ring and arrow on the goal card. The dim shows on landing back.
- Keep RankSpot's rules: free 0.5 s first, a press on the dim within 2 s only hides it, and the 3rd press outside puts it away for good.

## 3. Switch-ons, ASAP (overrides the staggered dates)
Turn on after Review-QA passes each, all today if they pass: parkRingEarly, parkTrailBack, parkGateTrail, tier3Path, tomorrowCard, cannonCue (#5097). Not cafeGrows or areaOnly (not tutorial).
Read: one combined before and after for the first 5 minutes and Tier 2 to 3. We lose the per-switch split; Growth notes each on-minute in the timeline anyway.

## Checks
uigate scenes for steps 1 and 2 on smallphone, phone, tablet, desktop and console. Telemetry rank_spot shown and closed by phase stays.
