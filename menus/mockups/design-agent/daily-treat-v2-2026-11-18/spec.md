# Daily Treat v2: big rewards only (Design-Agent spec, Nov 18 2026)

Derek, Nov 18 17:14 UTC: "no bad rewards in the daily treat these are supposed to bring people back no cat food or bowl food make it show like 1hour of earnings, 10spins, 5 gold crates, 500 gold fish load these up asap".

It sits behind the switch `bigTreats` (LiveFlags, off by default) and uses the follow pattern, the same way CheapTiers does: `Catalog.dailyTreat` is swapped on both sides when the switch flips. There is no save change, because stamps and days are unchanged. Turning it on also covers the day 2 part of `tomorrowBoard` (D8), so tomorrowBoard only adds the board, the dot and Remind me.

## The 7 days (no cat food, no bowl food, no bait, no potions)
Derek 17:22 UTC: "no potions for day 5 can also add trait rerolls to daily rewards also".
| Day | Prize | Card text |
|---|---|---|
| 1 | 1 hour of earnings (coinSeconds 3600, at least 5,000 coins) and 3 spins | "1 hour of earnings + 3 spins" |
| 2 | **500 golden fish** and 5 spins | "500 Golden Fish + 5 spins" |
| 3 | 2 hours of earnings (coinSeconds 7200, at least 10,000) and **10 spins** | "2 hours of earnings + 10 spins" |
| 4 | **3 golden crates** (highest_golden, the best open area) | "3 Golden Crates" |
| 5 | 4 hours of earnings (coinSeconds 14400, at least 20,000), 10 spins and **5 trait re-rolls** (Trait Tokens) | "4 hours of earnings + 10 spins + 5 trait re-rolls" |
| 6 | **750 golden fish** and 10 spins | "750 Golden Fish + 10 spins" |
| 7 | **5 golden crates** (highest_golden), **1,000 golden fish** and **10 trait re-rolls** | "5 Golden Crates + 1,000 Golden Fish + 10 re-rolls" |

**Card:**
- Each tag shows its prize as a big number with one picture (coins, fish, crate or spin wheel), not a list of small icons.
- Day 7 gets the gold frame.
- The Tomorrow Board (D8) uses the same row.

**Earnings:** "hours of earnings" uses the existing coinSeconds payout (the day rate at claim time, with the minimum as the floor). It grows with the player, so it stays big at any tier.

## Trait re-rolls
This is a new prize kind, `traitTokens = n`, paid into `profile.traitTokens` and clamped at Traits.TOKEN_MAX. It is earned only. Tokens are also sold in bundles, so the Daily Treat gives away 15 a week that a player could otherwise buy. That is fine: it is a gift, and buying is never pushed on the card. The card shows the Mystic Pool token picture.

## Is it fair?
All of it is earned only. Nothing is sold or random beyond the golden crates' disclosed odds, which already show in Odds. Golden fish are never sold.

A full week adds up to 2,250 golden fish. That is enough for all three Market gear pieces (1,220) plus potions. The gear is a one-time buy that adds no income, so the week speeds up the start but doesn't break the climb. The 8 golden crates a week are the big jump, since the old card gave 1 classic crate and 1 classic golden crate. They are highest_golden, so a late-tier player also gets late-tier cats. Growth watches two things from the day bigTreats goes on:
1. Golden crate cats per player per week. If a top-rarity flood shows up at Tier 6+, lower Day 4 to 2 crates. That cuts a reward, so ask Derek first.
2. The Index and Market pace.

## Ship
- GE builds it behind `bigTreats`, as a Catalog data follow plus a spec. The DailyTreat spec gets checks that no day has catFood or lures, and that day 2 has 500 fish.
- Review-QA, then Growth's on-minute: it is not a first-session switch, so it doesn't need the D-slot gap. Derek said ASAP, so it can go on as soon as it merges, 2 h from any other switch.
