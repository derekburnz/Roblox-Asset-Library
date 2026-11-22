# Bowl tame to Rank Up on phones (Design-Agent, 2026-11-17 14:35 UTC)

Growth: on phones about 1 in 3 players leave between onboarding_v8 step 7 (bowl_cat_tamed) and step 15 (rank_up_ready_shown).

## What that stretch is
At the tame a bowl-first player has 2 cats (starter + bowl cat) and the 1,500 coins. Tier 2 needs any 3 cats. So steps 7 to 15 are the whole first hand catch:
8 in_cannon, 9 alley_picked, 10 alley_arrived, 11 near_stray, 12 catch_started, 13 first_catch, 14 first_checkin, 15 rank_up_ready_shown.

## What rankUpRightAway (on since 12:22 UTC Nov 17) covers
- The goal card reads "Catch 1 more cat" right after the tame (catsShort reads the ledger first_checkin, which the tame passes).
- A stray waits near the Alleyway landing until the third cat is in.
- After the check-in: the Rank Up window opens by itself (autoRankUp, 1.5 s calm) and opens again on landing if closed, up to 2 times.

It does NOT cover the trip itself: opening the cannon, the launch, finding the stray, the touch catch and the carry home. If phones leak there, rankUpRightAway will not fix it.

## Why we cannot tell yet
Steps 9 to 14 were ledger based until 2773551e (merged 12:54 UTC Nov 17), so bowl-first saves passed them within seconds of the tame. Clean per-step data starts with that publish (about 13:15 UTC). Wed Nov 18 is the first clean UTC day with rankUpRightAway on.

## Read (Growth, Thu Nov 19 noon UTC read, Nov 18 data)
Phone vs computer vs tablet conversion for each of steps 7 to 8, 8 to 10, 10 to 12, 12 to 13, 13 to 14, 14 to 15. Also time between steps for leavers.

## Fix per leaking step (pick the one or two biggest; each behind its own switch, on one UTC day each)
- 7 to 8 (never open the cannon): tapping the goal card's "Catch 1 more cat" opens the cannon with the Alleyway picked; Motion-FX pulse on the cannon button after the tame.
- 8 to 10 (open it, never launch): the cannon window on a phone shows the Alleyway as the only big choice at Tier 1.
- 10 to 12 (land, no swing): the waiting stray placed in view of the landing with a ground arrow.
- 12 to 13 (swing, no catch): the first hand catch on touch is 1 circle with the widest Good window; no chase on the first miss.
- 13 to 14 (catch, no check-in): auto carry home after the first hand catch (cloud hop straight to camp).
- 14 to 15 (check in, no Rank Up shown): already rankUpRightAway; check rank_up_window outcomes by device.

Target: phones within 5 points of computers on steps 7 to 15.
