# Nov 17 read plan (Design-Agent, prepared 2026-11-16 23:30 UTC)

**Source:** the scheduled analytics run (analytics.yml, about 10:17 UTC on Nov 17), which covers Nov 15 and Nov 16. If it hasn't run, start it by hand with `days=2`. Every section named below is already in that report. No new queries are needed.

**Baseline:** run 43908628570 (Nov 14 to 15). That was before tonight's first-5-minute fixes: #4779 cannon dim and arrow, #4928 strip, #4949 asks after 5 min, #4950 no admin UI in the walk-through, #4953 pop-up pacing if merged, #4920 quick first flight.

## 1. Where new phone players leave
Section: "New players leaving: by device and furthest clean step".

Baseline on phone, top 6:

| Furthest step | Players |
|---|---:|
| first_bait_resolved | 171 |
| first_move | 119 |
| near_stray | 102 |
| loaded | 92 |
| first_role_assigned | 78 |
| tier_2 | 75 |
| joined | 67 |

Then read "by furthest step and bounce window" for the same steps. Baseline for first_bait_resolved: 61-180s 194, 3-10m 186.

What each one decides:
- **first_bait_resolved** (bowl cat tamed, never flew to the Alleyway). If it is still the top phone step, the next fix is the cannon step. Auto-open the cannon picker on the Alleyway once after the bowl cat is tamed, behind a new switch, off.
- **near_stray** (stood by a stray, never started a catch). If phone is still over 60, the next fix is the NET button. Pulse it with the tutorial ring whenever a stray is in reach during the walk-through, plus "Tap NET!" over the stray, behind a switch.
- **loaded and joined** (left during loading). Compare against "client_load" and "boot_ui" (Custom events), and against loading_seen. If loaded plus joined is more than 25% of phone leavers, the work is load time (#4788 streaming), not design.
- **first_move**. Read "Stalls by device, awaited step and last hint". A stall at the bowl step with no hint means the bowl ring isn't showing.

## 2. First 60 seconds (spec first-60-seconds/spec-2026-11-16.md)
- "first_cat_owned" (Custom events): median seconds by device. The target is 30 s or less on phone.
- "First bait cutscene: players by device and outcome": a skipped share over 50% means the cut is too long.
- "First bait: players by device and choice": there should be no "let go" rows, since #4863 removed Let go.

## 3. Tier 2 and Rank Up (#4920 item 7, #3951)
- "First rank up ready" against "First rank up pressed", by device. Nov 15 baseline: 431 ready, 283 pressed. Target: 80% or more pressed.
- "Leavers before Tier 2, ready to rank up or not": if "ready" leavers are still over 100, make the Rank Up ring louder (it already self-opens via autoRankUp).
- Day 1 return (Players and sessions per day, plus Growth's D1). If it is under 6%, switch on returnHookEarly copy tweaks for #3951. It is already ON, so read its "return_hook_early" rows: shown but no D1 lift means the line needs a reason, not just a reminder.

## 4. Other open items that wait on this read
- #4192 tier ladder: quit_have by tier on the post #4320 ladder.
- #3867 tables: arm PR #4763 only if Tier 2 to 3 is not stalling on coins.
- #4438 part 2: robux_purchase against the group sale log (Growth).
- #2912: the 2 to 5 minute stretch, which is the same rows as section 1.

## Output
One short reply to Derek with the top phone leaver step, what changed since Nov 15, and the one fix that ships next behind a switch.
