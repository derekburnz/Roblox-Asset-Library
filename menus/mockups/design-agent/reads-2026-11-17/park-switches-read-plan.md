# Read plan: parkRingEarly, tier3Path, parkTrailBack and parkGateTrail (Design-Agent, 2026-11-17 13:05 UTC)

## Why the dates move
Our funnel reads (Creator Hub onboarding_v8 and the analytics workflow) split by UTC day, not by hour. With the switches 24 h apart at 12:05, no switch gets a single full day to itself. All three touch the Park part of the funnel:
- parkRingEarly: Park landing to first Park catch.
- tier3Path: a waiting stray near the Park landing at Tier 2 (also Park landing to catch), then Park catch to Tier 3.
- parkTrailBack plus parkGateTrail: the Park trail, which also feeds the Park catch.
Stacked a day apart, we could not tell which one moved a number. Spacing them two days apart gives each a full clean UTC day.

## New switch dates (all 12:05 UTC, Gameplay-Engineer flips, tells Growth and Design the minute)
| Switch | Was | Now | Clean day to read | Read after the refresh on |
|---|---|---|---|---|
| rankUpRightAway (on 12:22 Nov 17) | | | Wed Nov 18 | Thu Nov 19 |
| cafeGrows | Wed Nov 18 | Wed Nov 18 (no change, not a Park step) | | |
| parkRingEarly | Thu Nov 19 | Thu Nov 19 (no change) | Fri Nov 20 | Sat Nov 21 |
| tier3Path | Fri Nov 20 | **Sat Nov 21** | Sun Nov 22 | Mon Nov 23 |
| parkTrailBack plus parkGateTrail | Sat Nov 21 | **Mon Nov 23** | Tue Nov 24 | Wed Nov 25 |
| tomorrowCard (#5079) | | Sun Nov 22 | D1 only, read inside the day (shown vs not) | from Nov 24 |

Harvest Hollow opens Wed Nov 25, a new area that pulls players away from the Park, so every Park read must finish on days before Nov 25.

## Before and after per switch (Growth reads, by device: Phone, Tablet, Computer)
Rule for every switch: if its step gets more than 5 points worse on any device in its clean day, turn it off that day and tell Design.

### parkRingEarly (#5034, PR #5035)
- Step: park_arrived to park_catch churn. Before: Wed Nov 18 (full day with rankUpRightAway). The 7-day figure today is Phone 35.9%, Tablet 29.3%, Computer 14.2%.
- After: Fri Nov 20. Target: Phone under 25%, Tablet under 22%, Computer unchanged.
- Also: average seconds from Park landing to first Park catch (step_gap), and park_trail rows.
- Guard: park_catch to tier_3 is not worse.

### tier3Path (#5038, PR #5049)
- Step: park_catch to tier_3 churn. Before: Fri Nov 20 (parkRingEarly on all day). The 7-day figure today is Phone 41.7%, Tablet 51.6%, Computer 22.9%, all 40.2%.
- After: Sun Nov 22. Target: under 20% on all devices (spec park-to-tier3.md).
- Also: quit_have at Tier 2, the share whose first need missing is kinds (before 346 of 449). Seconds from Tier 2 to Tier 3 (before about 400 s). tier3_path rows by field (kind, rare). tier3_topup count and average amount (cap 15,000).
- Guard: tier_3 to tier_4 churn not worse. If Tier 3 starts to feel free (Tier 2 to 3 under 120 s), lower the gift cap to 10,000.

### parkTrailBack plus parkGateTrail (#5045, PR #5047)
- Step: park_arrived to park_catch again, plus park_trail shown, entered and caught. Before: Sun Nov 22. After: Tue Nov 24.
- Target: park_trail entered to caught up, and no rise in Park landing to catch.

## Not changed
rankUpRightAway's baseline is bowl_cat_tamed to rank_up_ready_shown (Growth's new baseline, 32.1% all, Phone 35.1%, Tablet 33.4%), because the Alley steps log at the bowl tame. GE's #5082 changes steps 9 to 14 from its publish minute, so read rankUpRightAway on step 7 to 15 only.
