# First 15 minutes: stall fixes (#5285 E, from Sync's fresh-account log, 2026-11-18)

Source: Sync's 15-minute run on main 423c4356e with the live switches. T2 at 1.1 min, T3 at 7.7, no T4 by 15. Three stalls of 45 s or more with no goal step. Both items ship behind their own off switch.

## 1. nightLine (stalls at 3.4 to 4.0 and 9.8 to 10.5 min)
While the areas are closed at night and the player is Tier 4 or under, the hint strip shows one line:
"Areas open at sunrise in 0:42. Upgrade your cafe while you wait" with a small arrow to the Upgrades button.
- The timer counts down each second from the real sunrise time.
- A tap on the line opens nothing. The player taps Upgrades themselves (tutorial rule).
- The line hides at sunrise and when any menu is open.
- No change to night length for now. If the stall still shows in the next Sync run, Design will spec a shorter first night.

## 2. goalNeedLine (stalls at 5.0 to 7.7 and 7.8 to 15+ min)
The goal card shows the biggest missing Rank Up need under the tier name, with progress:
- Coins short: "Coins 194K / 250K" and a thin bar.
- Kinds short: "Kinds 9 / 12".
- Rarity short: "Need 1 Epic or better".
Biggest means the need furthest from done, as a share. Ties go coins, then kinds, then rarity.
When every need is met the line reads "Ready to Rank Up!" (the existing Rank Up pointer still does the pointing).
It reuses the Rank Up window's need data, so it follows cheapTiers and tier4Easy with no extra work.

## Order and checks
GE builds both, Review-QA passes, Sync takes a phone look. Each goes on at its own clear minute, 2 h from other switches, after tier4Easy. Success: the next Sync fresh-account run has no stall over 45 s before minute 12, and T4 lands by minute 13.

## Update 18:40 UTC (after GE's check)
The goal card already shows need rows from RankUpNeeds. They hide when the card is folded to the touch chip or when a takeover goal owns it. Sync's run was on touch, so goalNeedLine means: the folded chip shows the biggest need ("Famous Cafe: Coins 194K/250K"), and a takeover goal keeps the biggest need as one small line under it.
