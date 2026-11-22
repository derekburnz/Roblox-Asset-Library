# Spec: daily playtime gifts (#5506)

Design-Agent, Nov 19 2026. Goal: more players still in the game at 5, 10 and 15 minutes. Switch `dailyGifts`, off by default. Builds on shared/PlaytimeGifts and Config.PlaytimeGiftSteps.

## The ladder
Minutes are minutes played today (UTC day, the same day as the free spin, Spin.day). Prizes use the IndexPrize fields that Payout already pays.

| Step | Minute | Prize | Why here |
|---|---:|---|---|
| d1 | 1 | coinSeconds 60 | A win before the 2 minute drop |
| d3 | 3 | lures: tuna 1 | Half of players are gone by 2 to 3 minutes |
| d5 | 5 | spins 1 | 25% are left at 5 |
| d8 | 8 | coinSeconds 180 | |
| d12 | 12 | fish 5 | 12% are left at 10 |
| d16 | 16 | potions: swift_potion 1 | |
| d20 | 20 | spins 2 | |
| d30 | 30 | crates: classic_crate 1 | |
| d45 | 45 | fish 15, coinSeconds 300 | |
| d60 | 60 | crates: classic_golden_crate 1 | |

A full day pays 9 minutes of income in coins, so it can't replace playing. Later tiers earn more a second, so the coin steps grow with the player.

## Rules
- Time counts only while the player is in the game. It carries across rejoins on the same UTC day and starts again at 0 on a new day.
- One gift at a time, in order. A gift that is ready waits until claimed. Gifts not claimed by the day's end are lost without a message.
- While the switch is on, the old once-per-account small steps (m2, m4, m6, m15, m20) stop paying. The like card (10 min) and favourite card (30 min) are unchanged.
- No Robux skip, no streak, no pop-up. The claim is a tap on the chip.

## Save
`profile.dailyGifts = { day: number, seconds: number, claimed: number }`: the UTC day, seconds played that day, and the last step claimed. This needs a version bump, so the switch goes on only after a restart Derek calls. No migration: a missing field reads as a fresh day.

## HUD chip
- Sits by the existing gift icon. It shows a small gift and "1:20" counting down to the next step. When ready it reads "Open!" and pulses gently (no flashing).
- Hidden until the tutorial strip's first minute has passed, and hidden in a cutscene.
- Tap when ready: the gift pays with the normal prize toast. Tap when not ready: a small card lists all ten steps with each prize and a tick on claimed ones.
- Phone: the chip is at least 44 px tall and sits clear of the jump button and the thumbstick. Follow the ui-review checklist.

## Server
- PlaytimeGiftService tracks seconds for the day and answers a ClaimDailyGift remote: checks the day, the step order and the seconds on the server, rate limited to one call a second. The client's timer is display only.

## Telemetry
- `daily_gift` on claim: value the minutes played today; fields step, device, first day or later day.
- `daily_gift_chip` once a session when the list card is opened.

## Read
Share still playing at 5, 10 and 15 minutes (playtime_v1) and playtime per player, one UTC day before and after. Targets: 35% at 5 minutes, 20% at 10.

## Test plan
- Spec: the due step for any (day, seconds, claimed), the day rollover, order can't be skipped, and the totals in the table.
- In game on a fresh account: gifts at 1, 3 and 5 minutes, rejoin keeps the minutes, a new UTC day resets.
