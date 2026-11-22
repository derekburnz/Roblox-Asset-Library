# First 15 minutes: where the minute 5 to 10 wall is (Design-Agent, Nov 18 2026, #5285 part E)

**Method.** I used the Pace sim (tests/specs/Pace.spec.luau, the real shared economy code), run on main with cheapTiers on, as live. It played 20 seeded fresh accounts per case for 30 minutes. There were two players:
- **casual:** 4 catch trips a day, the sim's model player.
- **active:** 12 trips.

The sim leaves out spins, fish, crates, quests and the Daily Treat, so real players run a little faster. Sync's real timed run (E4) should confirm.

## What a new player sees (median runs, cheapTiers on)
| | Tier 2 | Tier 3 | Tier 4 (median) | Not at Tier 4 by 30 min |
|---|---|---|---|---|
| Casual | 0:51 | 7:53 | 22:34 | 5 of 20 |
| Active | 1:50 | 3:37 | 15:10 | 2 of 20 |

- **Up to Tier 3 it's busy:** a buy or a new cat about every 30 to 60 s, all the way to Tier 3 at 4 to 8 minutes.
- **After Tier 3 it goes quiet.** The casual player gets a new cat every 1 to 2 minutes, plus a few upgrade buys. Then there are gaps of 2.5 minutes or more with nothing to do, and the next real step, Tier 4, is 15 to 22 minutes in. **That is the minute 8 to 20 wall.** The video's wall was minute 5 to 10, and ours shows up just after Tier 3.

## What actually blocks Tier 4 (400k coins, 10 kinds, 1 Legendary)
I changed one gate at a time and kept everything else the same:
| Change | Casual median | Active median | Never reach by 30 min |
|---|---|---|---|
| Today (400k, Legendary) | 22:34 | 15:10 | 5 / 2 |
| Legendary to **Epic** | 22:34 | 15:10 | 3 / 0 |
| Kinds 10 to 8 | 22:34 | 15:10 | 3 / 0 |
| Epic **and 250k coins** | **18:02** | **11:24** | **1 / 0** |

- **Coins are the main wall** for the typical player. The kinds and the rarity only matter in the tail.
- **The Legendary need is a luck wall.** In 5 of 20 casual runs no Legendary came in 30 minutes at all, and those players can't rank up however hard they play. That is the worst kind of wall for D1, because the player can't see a way past it.

## Recommendation (two changes on the cheapTiers row, one switch, `tier4Easy`, off by default)
1. **Tier 4 needs an Epic or better, not a Legendary.** Tier 5 keeps its Legendary, so the rarity steps up one tier at a time: Rare at 3, Epic at 4, Legendary at 5.
2. **Tier 4 costs 250,000, not 400,000.** That is the CheapTiers row [4], and Tier 3 stays 25,000.

Together these move Tier 4 from about 22 to 18 minutes (casual) and from 15 to 11 (active), and almost nobody is stuck by luck. Both are cost cuts. Derek asked twice today for easier tiers and for "at least half" on 3 to 4, so this follows his ask, but he can say no.

Then the E1 contextual tips (needTips) fill the 8 to 18 minute stretch: "You can afford an upgrade", "Cafe full", "Fill your bowl", "New best cat" and "Catch more to earn the rest" on the Rank Up's coins line.

## Build note for GE
`Catalog.setTierNeeds` needs to take `needsRarity` as well as cost, distinctCats and needsRarityCount. The PLAIN_TIER_NEEDS row gets `needsRarity` for the switch off. The RankUpCount and LateTierGoals specs read the tier rows, so they follow.
