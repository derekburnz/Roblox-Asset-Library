# First check-in to Rank Up card drop (onboarding_v8 step 14 to 15)

Design-Agent, 2026-11-17 03:00 UTC. Derek's ask (02:22 UTC): "figure out what the huge drop off is" between first_checkin (48) and rank_up_ready_shown (35), 27% churn.

## What the player has at step 14

The starter Tabby, the tamed bowl cat and the first Alleyway cat make Tier 2's 3 cats (any cats since #4809, live 14:22 UTC Nov 16). The catch that completes them tops coins up to 1,500 (#4674, live 01:16 UTC Nov 16). So a player who tamed the bowl cat is ready for Tier 2 as soon as the first cat is checked in. Money is not the gate, as Derek said.

Step 15 logs only when the Rank Up window is reported open at Tier 1. The auto-open (#4924, live about 21:20 UTC Nov 16) opens it after 1.5 s of calm screen. Pressing RANK UP or reaching Tier 2 fills step 15 in too.

## What the data says (analytics run 44002569974, Nov 15 to 16 UTC, 883 joined)

- The drop was the same before the auto-open: 585 to 413 (29%). Phones are worst: 250 to 164 (34%). PC is 88 to 66 and tablet 161 to 114.
- 139 players left with first_checkin as their furthest step. They had played about 150 s on average. Most left 1 to 3 minutes after the check-in, with no window open and while still moving (idle under 15 s). 74 were in Town, 37 in the Alley and 20 in the cafe.
- None of them had a hint showing. In the first five minutes, 305 players stalled 30 s or more waiting on another cat with "last hint: none".
- 111 leavers had 2 kinds and 75%+ of the coins but were not ready. That is the repeated Tabby before the any-cats fix. 95 leavers had 3 cats and the coins, so they were ready, but never pressed.
- Derek's screenshot was taken at 02:21 UTC, so its 48 to 35 is mostly after all three fixes. The gap is still there.

## Cause

After the first check-in nothing reliably puts the Rank Up in front of the player:

1. **Ready, but the window is not counted or not seen.** The window's open is reported through the 5 s throttled screen report. A window closed with X inside 5 s is never logged. A player who closes it then has nothing pointing back at it, apart from the HUD button glow.
2. **Not ready, with no hint.** If the bowl cat was let go, the player is one cat short. The walk-through's second-cat help ended at the first hand catch (bowl cat counted as one), so no stray waits and the goal card does not say "1 more cat".

## Fix, switch `rankUpRightAway` (OFF by default, GE builds, Motion-FX cue)

1. **Measure it exactly.** This part needs no switch. The RankUp window opening at Tier 1 sends its own unthrottled report, so step 15 logs the moment it opens. A new event, rank_up_window, has the fields how (auto or button) and outcome (pressed, closed or left).
2. **Ready: open right after the check-in.** Open it straight after the check-in's card closes, with no once-a-session limit until it is pressed. If it is closed, it opens again the next time the player lands in Town or the cafe, at most twice. The goal card reads "Rank up now! Your cafe is ready" and the trail points to the RANK UP button.
3. **Not ready: say exactly what is missing.** The goal card says "Catch 1 more cat to rank up" and a stray waits near the camp landing, like SecondCat, until Tier 2's cat need is met. The top-up still pays the coin gap on that catch.
4. **Motion-FX** pulses the goal card and plays a soft chime when the last Tier 2 need is met, under the same switch.

## The read

Compare step 14 to 15, and 15 to 17, for one full UTC day before and after the switch goes on, by device. The goal is under 10% churn at 14 to 15.
