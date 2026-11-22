# The new start, version 2: play first, no tutorial steps

Design-Agent, Nov 20 2026. Replaces the tutorial part of new-start-spec.md, which Derek rejected at 11:44 UTC ("the steps right now are dull and hard to follow and feel pushy follow other games do deep research"). Coin-only tiers (`coinsOnly`) and the one tap Rank Up (`rankOneTap`, PR #5534) stand as they are.

Research: reports/Roblox first minute onboarding.md and the four note files under research_notes/.

## 1. What the research says

1. **The top games have no tutorial sequence.** Grow a Garden and Steal a Brainrot drop the player on an empty plot with a small wallet that buys exactly one obvious thing from a shop in view. Nobody is walked through steps. Tutorials only show up where the core input is a skill minigame (Fisch, Dig), and those are short.
2. **Income comes to the player.** In Restaurant Tycoon 2 customers arrive by themselves. In Steal a Brainrot the first buy pays itself back in 25 seconds. The player sees numbers go up before being asked to learn anything.
3. **One small goal, never a lock.** Bee Swarm has one bear with one quest. Pet Simulator 99 shows two goals at a time. They can be ignored. Roblox's own docs say fixed tutorial sequences "can lead to boredom or frustration due to restricting player choice".
4. **Hints only for players who stall.** Roblox's worked example: most players find the button within 10 seconds, so the hint shows at 11 seconds, once, only to those who have not acted.
5. **Kids skip text and tap everything** (Nielsen Norman, 125 children). Eight words on screen at most (Plants vs. Zombies rule). Never label a tutorial.
6. **Forced chains bleed at step 1.** A 16 step forced tutorial lost 41% at step 1 and 30% finished. A large study (45,000 players) found tutorials did nothing or hurt in simple games.
7. **Home recommendations read the first session**: play through rate, first play bounce under 60 seconds, playtime per user, play days. The first minute is the test.
8. **Nobody gates the first session on a collection.** Early progress is a single coin price ladder. That matches coin-only tiers.

Our start does the opposite on every point: about 20 forced steps, each with a dim, an arrow or a text strip, three windows, and nothing fun until step 8.

## 2. The idea

The start is a small playground, not a lesson. Cats are walking around the player the moment they load. The catch button works. Whatever they do first is right. The cafe earns by itself as soon as one cat is in it. One small goal chip shows the next good thing and pays a little when it happens. Nothing dims, nothing points, nothing opens, nothing blocks.

## 3. The first three minutes

| When | What the player sees | What they can do | What teaches it |
|---|---|---|---|
| 0 s | They stand on the street in front of their cafe, net in hand. Three cats wander within 15 studs. No intro, no strip, no dim. Goal chip: "Catch a cat +100". | Swing at any cat, or run about | The cats themselves. The catch button is the biggest button on screen |
| about 5 to 15 s | First catch. One slow ring, a miss costs nothing. The cat pops into their arms, its name and rarity flash, coins burst. | Catch | Doing it once |
| 15 to 25 s | The cafe door glows softly. Chip: "Take it home +100". Walk in and the cat hops onto a job. A customer walks in within 5 seconds and coins fly out. | Walk through the door | A glow on the door, no arrow |
| 25 to 60 s | Cats keep wandering by. Each one caught raises the coins per second shown by the counter. Chip: a coin bar to 1,500. A sleepy cat sits by the food bowl with a "Tame" bubble for anyone who wanders over. | Catch more, tame the bowl cat, or just watch coins tick | Numbers going up |
| about 60 to 90 s | The chip turns into the gold RANK UP button. One tap: the cafe grows, confetti. The Town Square cannon lights up with a PARK sign. | Tap. Walk into the cannon when they like | The cannon glows. No picker the first time |
| 90 s to 3 min | Park: cats are near the landing. Park cats pay clearly more. Chip: coin bar to Tier 3. | Catch, fly home, Rank Up again | Same loop, bigger numbers |

Words on screen in the first minute: under 15 in total. Forced steps: 0. Windows: 0.

## 4. Rules for the build

- **No dim, no TutorialArrow, no tutorial strip, no window** for a save on this start, until Tier 3. That removes tameCannonPoint, the rankSpot walk-through, parkLead, parkRankPoint, the bowl lines and the catch line for these saves.
- **The stall hint is the only pointer.** If the chip's goal has not moved for 11 seconds, the thing in the world glows (the nearest cat, the door, the cannon) for 6 seconds. Once per goal. Never on the screen itself.
- **The goal chip** is the existing goal card, folded size, at most five words plus the reward. It never blocks and can be ignored. Order: "Catch a cat +100", "Take it home +100", then the coin bar and RANK UP. After Tier 2: the coin bar only.
- **The first three catches cannot be lost**: one slow ring, a miss leaves the cat in place.
- **The first three Park catches cannot be lost either** (Growth, Nov 20: 37% of phone players who start their first Park catch never land it, 10% on PC). The cats near the Park landing are Commons and Uncommons, their rings keep the first catch's slow speed and wide bands on every device, and a miss leaves the cat in place with no wait. Not a one hit catch: the rings stay, the punishment goes. Switch `streetCats` covers it.
- **Cats are always in sight** for the first three minutes of a new save: three Commons kept within 20 studs of the cafe front, a new one walking in within 5 seconds of a catch.
- **The player is never moved or flown without their own action.** Walking into the lit cannon is the action; the first flight goes straight to the newest area with no picker. The picker is there from the second flight.
- **Bowl, Upgrades, Store, companions, daily gifts**: nothing about them in the first three minutes. Each is found by walking up to it, or by the existing contextual tip later.
- Young audience rules hold: no timers that pressure, no near miss tricks, no purchase prompts in the first session.

## 5. Pieces and switches (each off by default, each can go off alone)

| Switch | What it does | Owner |
|---|---|---|
| `coinsOnly` | Tiers ask coins only | GE, in progress |
| `rankOneTap` | Goal card becomes RANK UP, one tap | Design, PR #5534 |
| `noIntro` | Intro does not play by itself | on since 11:48 UTC Nov 20 |
| `freeStart` | New saves skip every tutorial step, dim, arrow and strip; spawn on the street in front of the cafe facing the cats | GE |
| `streetCats` | Three Commons kept near a new save's cafe front for its first three minutes; first three catches cannot be lost | GE |
| `goalChip` | The two first goals with their 100 coin rewards, then the coin bar | Design (UI), GE (rewards) |
| `stallGlow` | The 11 second world glow | Motion-FX, GE for the timer |
| `cannonGlow` | After a Rank Up that opens an area the cannon glows with the area's sign; the first walk in flies straight there | GE, Motion-FX |
| `onboarding_v10` | Milestones, not steps: first_catch, first_home, catches_3, rank_ready, tier_2, park_arrived, park_catch, tier_3, plus alive at 60 s, 3 min and 5 min, and seconds to first_catch | GE, Growth |

`freeStart` replaces the catch first and bowl first orders for new saves; saves already in an arm of orderSplit keep it.

## 6. What to read after 24 hours

First play bounce under 60 seconds, share alive at 3 and 5 minutes, median seconds to first catch (target under 15), share reaching tier_2 (v9 window A: 47%), playtime, D1. If players stall somewhere, add a glow there, not a step.

## 7. Honest limits

No public source gives stopwatch times for the top games' first minute, and no one publishes a before and after for removing a tutorial on Roblox. The plan follows the pattern those games share and Roblox's own written advice; our own funnel is the proof. Every piece is a switch, so any of them can come off the same hour.

## 8. Change after the engineer's check (Nov 20 12:10 UTC)

There is no catch area on the cafe streets; every stray lives in an area. Building one in front of each cafe is a new system and not safe by Friday. So the start is the Alleyway landing, with no flight: the player loads there facing three Commons 10 to 16 studs away. "Take it home" is the walk back onto the camp ring, which already hops the player home with the cat; the glow goes on that ring, not the door. The ring ignores a new save until its first catch. After the hop the player lands facing the cafe, the cat takes its job and a customer comes within 5 seconds. Everything else in sections 3 to 5 stands. Tier 2 costs 1,500 (a new save starts with 1,000, and the engineer's pace run puts Rank Up 1 at 55 seconds).

Correction (12:11 UTC): the Alleyway camp checks a carried cat in on the spot and the player stays in the Alleyway, so there is no hop. The second chip goal reads "Take it to camp +100" and pays at that check-in. Coins fly from the camp to the coin counter and the per second number pops, so the money link is seen without visiting the cafe. The player first sees the cafe when they tap Home or after the Rank Up.
