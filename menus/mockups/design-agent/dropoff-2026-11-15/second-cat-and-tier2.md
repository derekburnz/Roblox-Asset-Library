# Second cat and Tier 2 drop-off: causes and fixes

Design-Agent, 2026-11-15 02:40 UTC, for Derek's 02:01 UTC ask ("still the drop off at second cat and tier 2 upgrade seems to be huge ... see what the cause could be").

## Short answer

1. **Most of the numbers you are looking at are still the old game.** Easier Tier 2 (3 kinds and $1,500, #4199) reached every server only at the 22:00 UTC Nov 14 restart, and Roblox fills a day about a day late. The last full day in the data (Nov 13) had Tier 2 at 5 kinds and $13,500. The first clean read of the new Tier 2 is Nov 15's data, ready about 10:17 UTC Nov 16. Growth has two analytics runs queued for Nov 14 (GitHub's queue is about 60 runs deep tonight).
2. **Even with the new rules, the game points players away from Rank Up at the exact moment it opens.** For 2 minutes after the bait cat, the goal card says "Free a stuck cat" and the strip says "Hop in the cannon", while Tier 2 is already affordable. The rank up spotlight only shows outside catching areas, so anyone who follows the stuck cat pointer never sees it.
3. **On phones, one touch puts the rank up spotlight away for good.** After 2 seconds on screen, any tap or thumbstick touch outside the goal card closes it forever (RankSpot.putsAway). Phones touch the screen all the time to walk. Phone Tier 2 reach was 37% against 51% on PC (Nov 13).
4. **The second cat step has three pulls at once.** Right after the first check-in at the Alleyway camp: the strip asks for Kibble in the bowl at home, a waiting stray glows and calls right next to the player, and two toasts, the catch card and a Grand Opening prize toast all land within seconds (the Grand Opening strip itself never shows in a real client, #4162). Half of the second-cat leavers go within 60 s of their first job, with no window open and no hint shown.

I am building fixes 2 and 3 tonight behind a switch (section 4). Fix 4 is an issue for the morning.

## 1. What the data says (and what it cannot say yet)

Baseline Nov 13 (onboarding_v7, 1,074 new players, old rules; Growth-Agent/tier-baseline and daily-2026-11-14):

| Step | Reached | Lost at the step | Phone | PC |
|---|---:|---:|---:|---:|
| first job to second cat | 683 (63%) | 160 (18%) | 59% reach | 70% reach |
| bait cat done to Tier 2 | 454 (42%) | 209 (31%) | 37% reach | 51% reach |

Leavers (Gameplay-Engineer/onboarding, Nov 13):
- 118 left with the first job as furthest step: 96 had never put food in the bowl, none were carrying a cat, 105 had no window open, half left within 60 s of the job. Of the stalls waiting for the second cat, 206 had seen no hint at all.
- Second cat trail on phone: shown 238, followed 34 (14%), caught 13. PC: 129 shown, 44 followed (34%).
- Leavers before Tier 2: 531 not ready, 13 ready; 418 of 546 had under 25% of the old $13,500. That cause (coins too far) is what #4199 fixed, so it should mostly disappear in the Nov 15 read.

Changes that split the reads: Tier 2 to 4 kinds and $7,500 (04:45 UTC Nov 14), bowl and Kibble at start (09:35), Tier 2 at 3 kinds and $1,500 (new servers 17:19, every server 22:00 UTC Nov 14). Ads started 18:00 UTC Nov 14 and bring a different crowd.

## 2. Walk of the first 10 minutes (current main, from the code)

Pace (the cloud sim) has a focused player with Tier 2 ready about 30 s after the bait cat (Tier 2 at 1 min median in tonight's run). What the player sees on the way:

| Time | Where | Strip (bottom) | Goal card (top right) | Other |
|---|---|---|---|---|
| 0:00 to 0:50 | cafe, cannon, Alleyway | "Go out ... tap as each circle closes" | tier goal | short intro |
| about 0:50 first check-in | Alleyway camp | "Tap the Bait bowl and put Kibble in it" (phone) | "2nd cat: your Bait bowl 1/2" | toasts "New cat! ... (+$50, fish)" and "Your first cat! ... is your Barista", catch card, Grand Opening prize toast, a waiting stray next to the camp glows (gold paw through walls), hops and meows |
| about 1:30 bait cat | home | "A cat is on its way to your bowl", then "Tame it" | same | bait cutscene and card |
| about 2:00 tutorial done | home | "A cat is stuck in the Alleyway! Hop in the cannon" for 120 s | "Free a stuck cat" | whole HUD opens with red badges (Index, Quests 4, Rewards, Decor), Grand Opening pays 2 milestones, Tier 2 already affordable |
| next free 2 s at home | home | same | spotlight "You can rank up!" over a card that reads "Free a stuck cat" | a tap anywhere after 2 s closes it for good |

## 3. Causes, ranked

### Tier 2

1. **Stuck cat goal outranks Rank Up** (strong, code fact). `StuckGoal.waiting` stays true until Tier 2 is reached, and `UIController.refreshTutorial` shows it before anything else after the tutorial. With Tier 2 now ready at the tutorial's end, the pointer sends players to the Alleyway, where `RankSpot.due` is false (catching area), so the rank up spotlight never shows there. Under the old 9 minute Tier 2 this was filler; now it is a detour away from the next area.
2. **The spotlight closes for good on any touch** (strong, code fact; size unknown until the rank_spot "closed" count by device is read). SpotlightGuide fires `onOutside` on every Touch or left click outside the goal card; after KEEP_SECONDS (2 s) RankSpot.putsAway saves it as seen. A phone player walking with the thumbstick dismisses it in the first step they take.
3. **Mixed words when it does show**: the dim says "You can rank up!" on a card whose title reads "Free a stuck cat".
4. **Noise at the moment of readiness**: the tutorial's end opens the full HUD with four red badges and two Grand Opening prize toasts, all inside the same seconds the spotlight waits for 2 free seconds.
5. Coins (weak now): $1,500 matches Pace's focused player; real players who buy upgrades first may be short. Check quit_have's coin share in the Nov 15 read before touching the price.

### Second cat

1. **Three directions at the first check-in** (medium, code fact plus Nov 13 leaver read): the strip and card ask for the bowl (at home), the waiting stray beacon and call pull toward a catch right there, and the check-in brings two toasts, the catch card and a Grand Opening prize toast at once. The leavers had no window open and no hint shown, which fits "lost, not stuck on a menu".
2. **Phones do not follow world pointers** (medium): 14% trail follow on phone against 34% on PC. The phone line now uses the HUD's Bowl tile ("Tap the Bait bowl"), which needs no walking; the wording names the 3D bowl and the tile the same way, so a phone player may look for the bowl in the world.
3. **Fast exits**: half leave within 60 s of the first job. That is the first quiet moment after the first catch; the bait cat (cutscene, new kind) is the hook, so the sooner it plays the better.

## 4. Fixes

| # | Fix | Switch | Who | When |
|---|---|---|---|---|
| A | Rank up first: while a Tier 1 cafe can rank up, the stuck cat goal and pointer wait; the card shows the tier goal with "Rank up!", the strip says "Rank up! Tap YOUR GOAL" | `rankFirst` (on unless switched off) | Design-Agent | #4388, passed review, armed |
| B | The spotlight is never put away for good by a stray touch: a press hides it for 20 s, and only the third press puts it away | `rankFirst` | Design-Agent | #4388 |
| C | One ask at a time at the first check-in (#4384): the waiting stray's beacon and call wait while the bowl step is on (Motion-FX); the Grand Opening prize toasts wait for the tutorial's end, and the strip too should #4162 ever wire it (Design-Agent #4389); the two check-in toasts become one (Gameplay-Engineer #4385) | `checkInCalm` (on unless switched off) | three threads | PRs up |
| D | Phone bowl line names the button: "Tap Bowl, then Use on Kibble" | none (words) | Design-Agent | #4389 |
| E | Read after the restart: rank_spot shown and closed by device, rank_up_ready_first to rank_up_pressed_first seconds, quit_have at Tier 2 (coin share, kinds), first job to second cat by route (bowl or hand) | none | Growth-Agent | Nov 16 10:17 UTC run |

Expected effect: A and B act on the 31% bait-to-Tier 2 loss directly for every player who is ready but never presses; the Nov 13 split (13 ready leavers) cannot show their size because readiness used to come late. The Nov 16 read is the check.

## 5. Nov 14 read (Growth, 03:45 UTC Nov 15; mixed day)

Source: Growth-Agent/funnel-2026-11-15/second-cat-tier2.md. Easier Tier 2 was on new servers from 17:19 UTC and on all servers from 22:00, and ads ran from 18:00. Treat it as a warning, not a verdict.

- Second cat: 787 to 597 (24% lost, Nov 13 18%). Trail shown 514, followed 49 (10%). The ad crowd is likely part of the rise.
- Tier 2: 574 finished the bait cat, 249 reached Tier 2 (56% lost, Nov 13 31%). Phone 209 to 68 (67% lost), PC 80 to 51 (36% lost).
- Ready but never pressed: rank_up_ready_first 225, rank_up_pressed_first 124, and the spotlight showed for only 65 players. That is about 100 players a day, the #4388 target, and it matches causes 1 and 2.
- Leavers with 3 or more kinds (about the bait-cat group): 343. Only 50 of all leavers were ready, and 169 had 75%+ of the coins. So most bait-cat leavers had the kinds but not the coins. Part of the day still had the $7,500 price, so the Nov 15 read decides.

**Next lever if the Nov 15 read agrees** (3+ kinds, not ready, coin-short leavers above 100 a day after 22:00 UTC Nov 14): make Tier 2 ready the moment the bait cat is tamed. Either the bait cat's welcome pays the gap up to $1,500, or Tier 2 drops to $1,000. I recommend the gap top-up, because it keeps the price players see on the card, needs no other tier change and only fires once. It would sit behind its own switch.

## 6. Nov 16 read plan (written 11:55 UTC Nov 15)

What each day holds:
- Nov 15 UTC: easier Tier 2 ($1,500, 3 kinds) on every server all day. `rankFirst` and `checkInCalm` only on servers started after 07:14 UTC (no restart), so split Nov 15 at 07:14 by server start if the data allows, else treat it as about two thirds "after".
- Nov 16 UTC: everything above on every server from the 20:00 UTC Nov 15 restart. The first fully clean day, read on Nov 17.

Cuts to ask Growth for (Nov 16 10:17 UTC run, Nov 15 data):
1. bait cat tamed -> Tier 2, by device (phone, tablet, PC, console). Baseline Nov 13: 31% lost, Nov 14: 56% lost.
2. rank_up_ready_first -> rank_up_pressed_first count and median seconds; rank_spot shown and closed by device.
3. Tier 1 leavers after the bait cat: kinds held (3+ or fewer), coins held as a share of $1,500, ready or not.
4. first job -> second cat by route (bowl, hand), and the trail shown -> followed rate.
5. starter_suggest shown counts (falls to near zero for Tier 1 once #4438 part 2 ships; a baseline for that change).

Decision rule (from the Nov 15 data, confirmed on Nov 16 data on Nov 17):
| What the read shows | Do |
|---|---|
| Coin-short leavers with 3+ kinds above 100 a day | Build the bait cat top-up: the bait cat's welcome pays the gap to Tier 2's price once, behind its own switch (Gameplay-Engineer server, Design-Agent toast words "Your cafe is ready to rank up!") |
| Coin-short leavers 50 to 100 a day | Keep the price, add the coin bar to the goal card ("$1,240 of $1,500") so the gap reads as close (Design-Agent, client only) |
| Ready but not pressed still above 60 a day | The spotlight is still missed: look at where those players are (zone) and make the rank up toast tappable |
| Phone loss still twice the PC loss | Phone-only pass: goal card size and position on small screens, the bowl step on touch (#4307) |
| Tier 2 loss at or under 30% on every device | Done here; move to the second cat (trail followed 10%) |
