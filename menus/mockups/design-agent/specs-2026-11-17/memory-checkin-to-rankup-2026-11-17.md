---
name: checkin-to-rankup-2026-11-17
description: Onboarding v8 step 14 to 15 drop (first_checkin to rank_up_ready_shown, about 27-34%): cause, switch rankUpRightAway fix with GE, Growth baseline split
metadata:
  type: project
  modified: 2026-11-17T02:44:04.094Z
---

Derek asked at 02:22 UTC on Nov 17 why players drop between first_checkin and rank_up_ready_shown. He said it is not money.

**Cause.** After the first Alley check-in most players are already ready for Tier 2. The starter Tabby, the bowl cat and the first Alley cat make 3, and the #4674 top-up brings coins to 1,500. Two things then go wrong:
- The RankUp window open is reported through the 5 s throttled screen report, so a window closed with X inside 5 s never logs. Nothing brings it back except the button glow.
- If the bowl cat was let go, the player is 1 cat short and no hint says so.

Leavers go 1 to 3 minutes after the check-in, with no window open and "last hint none". Phones churn 34% and PC 25% (Nov 15 to 16).

**Fix.** GE is building it behind the switch `rankUpRightAway`, OFF by default:
- An exact, unthrottled report of the window opening, plus a rank_up_window event.
- Reopen the window until it is pressed.
- Show "Catch 1 more cat to rank up" with a stray that waits.

Motion-FX adds a goal card pulse and chime under the same switch. The spec is at /mnt/project-files/Design-Agent/dropoff-2026-11-17/checkin-to-rankup.md.

**How to apply.** Growth records the baseline at the 10:30 and 12:00 UTC Nov 17 reads. Tell Growth the exact minute rankUpRightAway goes on, so they can split before and after. The target is under 10% churn at step 14 to 15.

Related, Nov 17: tier ladder #5056 went live at 06:27 UTC. Tier 4 needs 10 kinds, Tier 5 needs 13 kinds and 12M, Tier 6 needs 150M, Tier 7 unchanged. Growth's after window starts 07:27 UTC. Watch Tier 6 to 7 loss: it is now a 20x coin step. Park to Tier 3 is #5038, built as PR #5049 behind the switch tier3Path (off).
