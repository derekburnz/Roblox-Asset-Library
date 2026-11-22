# Tier ladder plan, draft 1 (#4192). Design-Agent, 2026-11-15 13:40 UTC

Status: draft. The numbers to ship come from Growth's Nov 17 05:00 UTC rerun, the first read with 3 days of rows after #4320.

## 1. What Growth's first read can and cannot tell us
- Its rows are Nov 8 to 14. #4320 (Nov 14 21:41 UTC) halved Tiers 3 to 7 again and cut kinds about 25%, so almost every row in it was played on the old, harder ladder. It shows where players stalled, not whether the current ladder still stalls them.
- Correction to point 4 of the read: full slots do not cap kinds. "Different cats" counts the collection, which is every cat ever had (`Economy.distinctCats`). `slots_full` only means a caught cat went to the cat room because every role slot was taken (CafeService). Selling is never needed for a kinds need. What full slots can cost is income, since the extra cat earns nothing.
- What holds: the stall is the next tier's bill after the area's first catch, Tiers 3 and 4 by kinds, Tiers 5 to 7 by coins and rarity.

## 2. The ladder live now (main 44eddd9c)
| Tier | Area | Coins | Kinds | Rarity need | Slots |
|---|---|---:|---:|---|---:|
| 2 | Park | 1,500 | 3 | | 4 |
| 3 | Neighbourhood | 110,000 | 6 | 1 Epic | 6 |
| 4 | Woods | 2.6M | 13 | 1 Mythical | 8 |
| 5 | Sewer | 45M | 14 | 2 Legendary | 10 |
| 6 | Desert | 625M | 21 | 2 Mythical | 12 |
| 7 | Ruins | 6.25B | 27 | 3 Mythical | 14 |
| 8 | Snowy | 21B | 36 | 4 Mythical | 16 |
| 9 | Water Park | 250B | 45 | 5 Mythical | 18 |
| 10 | Castle | 1.5T | 54 | 6 Mythical | 20 |

Two odd steps to look at: Tier 4 asks for 7 more kinds than Tier 3 and a Mythical in one go, then Tier 5 asks for 1 more kind. Tier 4's step is where the read lost 54%.

## 3. Targets
- Tier 7 reached within about 3 hours of play for a focused player (Growth's proposal); the few who got there took about an hour, so this is not the limit.
- The real target is reach: Tier 7 from 2.4% of Tier 2 players to 10% or more, and no single step losing more than 40%.

## 4. Decision table for the Nov 17 read
For each step, the leavers' first missing need (`quit_have`) decides the cut:
| If most leavers at the step are short of | Change |
|---|---|
| kinds | lower that tier's kinds to what Pace's focused player owns 10 minutes after the area's first catch; smooth Tier 4 (13 to about 10, Tier 5 to about 13) |
| rarity | keep the rarity, move the Mythical need of Tier 4 to Tier 5 if Tier 4 still loses over 40% (Legendary at Tier 4) |
| coins | lower the coin bill so Pace's gap after the area's first catch is under 25 minutes at Tiers 3 to 5 and under 45 at Tiers 6 and 7 |
| ready (had everything) | not a ladder problem: the rank up prompt (#3555) |

Economy rule kept: if a tier comes too fast, raise its cost, never cut rewards. Same rarity odds everywhere.

## 5. Still to settle in the final plan
- Passes and potions: Pace times with 2x, 3x and 4x Money. The old 4x Money 2 hour floor was dropped in #4189; recommend no new floor.
- Offline and AFK pay between sessions for returning players.
- Tiers 8 to 10 once they are live tonight: keep the 9-kind and 1-Mythical step unless the Water Park and Castle rows say otherwise.
- Phones and tablets lose more from Tier 2 to Tier 7 (tablet 173 to 1); #4307 covers the device side.

## 6. Next steps
1. Nov 17 05:00 UTC: Growth reruns the inputs (3 days after #4320).
2. Design runs Pace on the current ladder, fills section 4 and opens the Catalog PR (GE's file area, Design's numbers) with the decision in `docs/decisions.md`.

## 7. Days 2 to 7 and days 8 to 28 (added 2026-11-17 01:40 UTC, Growth's note on #4192)
Home now ranks on three return windows (day 1, days 2 to 7, days 8 to 28), counting players from Recommended For You. So the ladder plan also has to keep pulling players back after week 1, not just get them to Tier 7.

What already pulls players back, by window (live or built):
- Day 1: free daily spin, Daily Treat stamp, away pay and away notifications (awayNotes on), returnHookEarly line (off, waits on the Nov 17 read), Pal Day (#4913, off until Growth's baseline).
- Days 2 to 7: daily and weekly quests, the 7-stamp Daily Treat card, weekly leaderboards, admin events after restarts, Today's Deal.
- Days 8 to 28: Tiers 8 to 10 (Snowy, Water Park, Castle), Dragon Keep, Fusion, Ticket Booth weekly Water Park shelf, Harvest Hollow (Nov 25 to Dec 6), the Secret Cats.

Gaps:
1. Days 8 to 28 rest almost entirely on players who are already at Tier 7 or above. Players stalled at Tiers 3 to 6 get nothing new after the weekly quests repeat.
2. No goal is longer than a week. Nothing says "in 2 weeks you can have X".
3. Harvest Hollow is the only dated limited thing in the window.

Proposals for the final plan (numbers after the Nov 17 rerun):
- **Tier pace:** set the ladder so a typical daily player (about 20 minutes a day) reaches Tier 7 around day 10 to 14, not in one sitting. That puts Tiers 8 to 10 inside days 8 to 28. The Pace target becomes minutes of play per tier, plus "sessions to reach", not only total hours.
- **A 2 week collection goal:** an Index page reward at 50%, 75% and 100% of each area's cats, shown on the goal card once Tier 3 is reached. It reuses IndexRewards. No new save field if the claims already cover areas.
- **One dated thing every week:** a weekly rotating "featured area" that gives +25% rare odds there for 7 days. The Ticket Booth's weekly shelf is the model. It needs a small shared rule on the server clock and no save.
- **Week 2 return line:** the exit recap's "tomorrow" line (ReturnGoals) names the next dated thing ("Harvest Hollow opens in 3 days") when a player is past day 7.

Read to check them: D7 and D14 return by tier reached on day 1, from Growth's dashboard, after Harvest Hollow ends.

## 8. Shipped and the one item left (2026-11-17 08:55 UTC)
- Shipped in #5056, live 06:27 UTC Nov 17:
  - Tier 4 needs 10 kinds (was 13).
  - Tier 5 needs 13 kinds and 12M coins (was 14 and 17M).
  - Tier 6 needs 150M coins (was 312.5M).
  - Tier 3 is handled by `tier3Path` (#5038, PR #5049), which goes on Fri Nov 20.
- Left: Tier 6 to 7, now a 20x coin step (150M to 3.125B), on n of 17. Growth's Nov 18 read, with the after window from 07:27 UTC Nov 17, decides it. If Tier 6 to 7 loses over 40% and its leavers are short of coins first, cut Tier 7 to 2.5B. Check that Pace keeps Tier 8 in band, since a cut there moved Tier 8's wait in an earlier run.
