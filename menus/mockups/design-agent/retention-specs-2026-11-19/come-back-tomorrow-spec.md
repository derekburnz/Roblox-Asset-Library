# Spec: come back tomorrow, on away money and days played (#5505)

Design-Agent, Nov 19 2026. Goal: D1 from about 3% to 6%, then to the 7.9% median. Derek: away money and daily reward milestones are the focus. Switch `awayPromise`, off by default.

## 1. The away line (client only)
- From minute 4 of an account's play, one small line under the money counter: "Away: about $X by tomorrow".
- X = the cafe's day rate times Config.OfflineRate times Config.OfflineCapSeconds (the pass values when the Long Nap pass is owned), through ShortNumber. It updates when the rate changes.
- If X plus the coins held covers the next rank up's cost, the line reads "Away: $X by tomorrow. Pays for Tier N!" in the gold text colour.
- Tap: opens the tomorrow card (the Daily Treat Board's card), which now leads with the same number, then tomorrow's Daily Treat prize, then the next days played milestone.
- Hidden at night's dusk warning, in cutscenes and while any window is open on a phone.

## 2. The return moment
On a join 4 hours or more after the last leave, in this order, one at a time:
1. The away money card that exists today, with the amount counting up over 1.5 s and a short coin sound.
2. The Daily Treat stamp, if one is due.
3. A days played milestone, if one was reached today.
4. One strip line with an arrow: "You can Rank Up!" when Economy.rankUpBlocker is nil, else the best upgrade in reach (UpgradePace's pick), else nothing.

Nothing else may open on top until these are closed (the Popups queue already orders cards).

## 3. Days played milestones
Total UTC days on which the account played, never a streak and never lost. It reads from a new counter `stats.daysPlayed` with `stats.lastPlayDay` (version bump, so on after a restart Derek calls). Existing players start at 1 on their next join.

| Days | Prize |
|---:|---|
| 2 | fish 100, spins 3 |
| 3 | A kept cat: Rare from the player's newest area, of a kind they don't own if one exists |
| 5 | crates: classic_golden_crate 1, potions: lucky_potion 1 |
| 7 | A kept cat: Epic from the newest area, new kind first |
| 14 | fish 500, crates: classic_golden_crate 2 |
| 30 | A kept cat: Legendary from the newest area, new kind first |

- The cats are picked by rule, not rolled, so nothing is random and nothing is for Robux.
- The Daily Treat Board gets a second row: "Day 2 of 3: a Rare cat" with a small bar. The tomorrow card shows the same row.
- After day 30 the row reads "All milestones done" and hides a week later.

## Rules
No streak, no countdown clock, no pop-up in the first 4 minutes, every prize shown before it is earned, no Robux.

## Telemetry
- `away_line`: shown once a session, tapped; field whether it said "Pays for Tier N".
- `return_card`: value hours away; fields rank up in reach yes or no, device.
- `days_played`: on each milestone claim, value the day number.

## Read
D1 and D7 by cohort, two days before and after the on-minute, and against the holdout (#5499) once it exists.

## Test plan
- Spec: the away number for a rate, with and without the pass; the "pays for Tier N" test against tier needs under each tier switch; the days counter across UTC day edges; milestone order and the cat pick rule.
- In game: fresh account to minute 4 shows the line; set the last leave back 5 hours and rejoin to see the four steps in order on a phone and a PC.
