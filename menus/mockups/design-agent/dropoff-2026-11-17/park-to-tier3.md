# Park catch to Tier 3 drop (onboarding_v8 step 19 to 20)

Design-Agent, 2026-11-17 03:10 UTC, from the coordinator's idle push. Run 44002569974, Nov 15 to 16 UTC.

## The drop

park_catch 244 to tier_3 156, so 36% are lost. The players who do make it reach Tier 3 at about 560 s of play, roughly 400 s after Tier 2.

## What Tier 3 asks

- 50,000 coins
- 6 different kinds of cat (duplicates do not count)
- 2 Rares (the Bellhop Cat counts)

A new player at their first Park catch holds about 3 to 4 kinds: the Tabby, the bowl cat, the Alley cat (often a repeat) and one Park cat. They also hold a small share of the 50,000.

## Leavers at Tier 2: the first need missing (quit_have)

| First need missing | Players |
|---|---:|
| kinds | 346 |
| ready, never pressed | 44 |
| coins | 36 |
| rarity | 23 |

Kinds short:

| Kinds short | Players | Of those, under 25% of the coins |
|---|---:|---:|
| 1 to 2 | 248 | 112 |
| 3 to 5 | 234 | 148 |

Most leave still short of 3 or more new kinds, and with under 12,500 coins too. The goal card already says "Catch new kinds of cat x/6" and new kinds wear a tag. So the guidance is there, but the walk is long: several Park catches plus coins, with no single next thing in reach.

## Fix, switch `tier3Path` (OFF by default)

1. **A new kind waits near the Park landing.** This is the SecondCat stray again. At Tier 2, while the player is short of Tier 3's kinds, one free Park stray of a kind they do not own turns Curious near the Park camp landing and waits for that player (WaitsFor). It uses the first catch's slow circle. After each catch a new one waits, until the kinds need is met. Once the kinds are met but the Rares are not, the waiting stray is a Rare (Park odds still decide the rest). Each catch then takes about 20 s instead of a search.
2. **The goal card names one next thing.** Kinds first: "Catch 2 more new kinds", with the trail to the waiting stray. Then "Catch 1 more Rare". Then the coins line, which already exists.
3. **A Tier 3 welcome gift.** Once Tier 3's kinds and Rares are met at Tier 2, the coins are topped up once, by up to 15,000 and never past 50,000. The toast reads "Welcome gift: +$N toward Tier 3". It is shown as a gift and the price stays the real price, as Tier 2's top-up. The save gets stats.tier3TopUp.
4. **Telemetry.** A tier3_path event when a stray starts waiting, with the field kind or rare. A tier3_topup event with the amount.

## Read

For one full UTC day before and after the switch goes on, by device, check:
- step 19 to 20
- quit_have's t3_kinds share
- the seconds from Tier 2 to Tier 3

The target is under 20% lost at 19 to 20.

## Picks (settled under the sleep-mode OK, recommended)

- Gift cap 15,000, not a full top-up, so Tier 3 still takes some play.
- The waiting stray is per player, like SecondCat. The server's shared spawns are not changed.
