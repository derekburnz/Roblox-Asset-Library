# Catch a Cat Cafe: full audit from the owner's seat

Design-Agent, Nov 19 2026. Written as if the game were mine.

**How I did it.** I read Growth's Nov 19 numbers (Creator Hub to Nov 16, funnel onboarding_v9 for the last day, issue #5496), the design docs, the decisions log and the code on main (400c8495d). I did not play on a phone today, so anything about feel is marked "to check". Money numbers stay in this file and out of the repo.

## The short version

The game is not failing because it lacks features. It has 105 server systems and 104 screens. It is failing in the first five minutes, on touch screens, and at giving anyone a reason to come back. Nine in ten new players never see anything past the Park.

| Number | Ours | What it means |
|---|---|---|
| Still playing at 2 min / 5 min / 10 min / 30 min | 53% / 25% / 12% / 3% | Half are gone before the game starts |
| Reach first net catch / Tier 2 / Park catch / Tier 3 / Tier 4 | 53% / 42% / 20% / 9.5% / 5% | Everything built past Tier 3 is seen by 1 in 10 |
| D1 / D7 | 2.8% newest, 4.0% week / 0.59% | 16th percentile. Nobody comes back |
| Playtime per player | 9.2 min (was 12 to 21 before the ad push) | Ad players play shorter |
| Touch players | 86% (phone 57%, tablet 29%) | The game must be a phone game first |
| First Park catch lost, phone / PC | 36% / 12% | The core verb fails on touch |
| Players from ads | 84% | Organic reach is tiny and falling |
| Home impressions a day | 10,962 down to 3,406 in four days | Roblox is pulling back |
| Payer conversion / Robux per payer | 0.68% (good) / 36 (low) | People will pay, but only small amounts |

## Ranked problems and what I would do

Ranked by how much retention or revenue each one is worth.

### 1. The first minute does not match the name (retention, highest)
The game is called Catch a Cat. A new player watches an 8 shot intro, puts kibble in a bowl, waits, tames the cat, finds the cannon, flies and walks to a stray. Only then do they swing a net. 47% never get that far, and half of all players are gone by minute 2. The bowl hint and the cannon each lose 8 to 10% on every device, PC included, so these are not bugs. They are steps that should not be there yet.

**Do:** test catch first on half of new players. Spawn them a few steps from a stray with the net in hand, first catch inside 20 seconds, with the big first catch moment. The bowl, the cannon and the intro come later, each when it is needed. You chose bowl first on Nov 16, so this is a split test and not a flip: half and half, read on bounce under 60 s, reach of first catch and D1.

### 2. We change too much to learn anything (retention, highest)
About 170 switches exist. Dozens went on in the last two days, tier costs changed three times in three days, and D1 takes two days to read. Every read is a mix of ten changes, so we can't tell what worked. The numbers above have not moved in a week of very hard work, which is the proof.

**Do:** keep a holdout. One in ten new players gets a frozen set of switches for a week. Every big bet goes to a split by player and is read against the holdout. Fewer, bigger bets, each with a clean answer.

### 3. The catch fails on touch (retention, high)
86% of players are on touch. A phone player who starts the first Park catch fails to finish it three times as often as a PC player. The catch is a timing game judged on the server with a window of about a tenth of a second. Ping and touch delay eat most of that on a phone on mobile data. Wider windows have been tried several times (the Alleyway, early catches, the first Park catch, touch) and phones still lose 36%.

**Do:** #5497 (the cat stays put after a touch miss) is the right next step. Past that I would stop tuning windows and change the rule: a failed catch on a Common never moves the cat and never makes the player wait, on any device, in any area. They try again at once. A miss costs the bonus and never the cat. Timing skill then only matters for Rares and up, where players have already chosen to stay. Also to check on a phone: whether another player or the night sweep takes the cat mid catch, because the funnel can't tell those from a miss.

### 4. There is no reason to come back tomorrow (retention, high)
D1 is 3 to 4% and D7 is under 1%. The climb is very fast to Tier 3 (4 to 8 minutes in the pace sim), then Tier 4 costs 25 times more and Tier 5 20 times more again. The session ends on a wall, with nothing started that finishes tomorrow. The hooks we have (Daily Treat, tomorrow board, away money) all say "claim a thing". None is something the player began.

**Do:** wait for the tomorrowBoard read on Sat Nov 21 before adding more. Then make the bowl the overnight hook: at the end of a first session the bowl shows the shape of one new kind that will be sitting there tomorrow. For December, see problem 8.

### 5. Ads are buying players who leave (revenue and reach, high)
84% of players come from ads, they play 9 minutes, and Roblox's own Home signal for us is in the 5th percentile. Home impressions fell by two thirds in four days. Paying for players who leave teaches Roblox the game is weak, which cuts the free reach. The ads also target adult women while the game is built and ruled for young players.

**Do:** your call, since you run the ads. In your seat I would hold spend at the low test level until 5 minute retention is above 35%, then spend. I would also decide who the game is for. A cozy cat cafe for older players is a real niche and they spend more, but it would be a slower, deeper game than the fast simulator we have.

### 6. Too many systems, seen by almost nobody (retention and speed, medium)
Eight or more shops, five or more currencies, cards, traits, fusion, potions, a wheel, quests, a pass, a lawn, an arcade, trading. 90% of players never reach Tier 3 where most of it opens. Each system adds buttons, bugs and memory (phones run at 1.06 GB).

**Do:** no new systems until D1 is above 8%. All work goes to the first ten minutes, touch and coming back. The 25 day pace of new features is what I would spend differently.

### 7. The Tier 3 to 4 step is now the wall (retention, medium)
Tier 3 is now 10,000 coins. Tier 4 is 250,000. Only 55% of Tier 3 players reach Tier 4. Cutting prices again just moves the wall up one tier.

**Do:** put three small named goals between Tier 3 and Tier 4, each with a reward and a visible bar, so there is always a next thing within five minutes.

### 8. Christmas has no daily pull and nothing to sell (both, medium)
Snowglobe Village runs Dec 1 to Jan 3. It gives 40 Snowflakes for the day's first visit and has a stall of 8 items, with nothing for Robux. It is the biggest traffic moment we will have and it earns nothing and asks nobody to return.

**Do:** an advent calendar. One door a day from Dec 1 to 24, a small gift behind each, a Christmas cat on the 24th, and missed doors can be opened late so nobody is punished. Add one paid item with fixed contents (a Christmas cat and a cafe look), no timer and no pop-up.

### 9. The store sells too cheap and at the wrong moment (revenue, medium)
10% of players open the Store. In the last day 18 pressed Buy and 1 finished (small sample, Growth is reading it). The strongest item in the game, 2x Money, is the cheapest thing on the shelf, so everything else looks dear beside it.

**Do:** wait for the store read. Then show one offer where the need is: the 2x Money card on the Rank Up window's coins line when coins are the only thing missing. A card in place, never a pop-up.

### 10. Night still shuts the areas (retention, medium to low)
Every cycle the areas close for 90 seconds and send players home. The older leave read had night as 18% of the clock and 30% of leaves. New players are protected only until their first catches.

**Do:** split test keeping the areas open at night up to Tier 3. Night stays as a look and a fresh wave of cats.

## By area

| Area | Main problem | What I would do |
|---|---|---|
| First session and tutorial | Seven steps before the first net catch. Bowl hint and cannon lose 8 to 10% each on every device | Catch first split (1). Teach the rest on triggers |
| Catching | Fails on touch. Losing a Common to a missed tap feels unfair | A missed Common stays put (3) |
| Park and areas | Tier 2 to Park loses 17% on touch and 3% on PC. Ten areas, and 9 in 10 players see two | Fix the touch leaks in #5496 before any new area |
| Cafe | The cafe plays itself. In a first session the player does almost nothing there | One clear job on each visit: collect, place the new cat, see the number go up. No new system |
| Cats menu and index | Many overlapping boosts (traits, companion, cards, potions, passes, decor) that a child can't add up | One line: "Your cafe earns X. Best next step: Y" |
| Companion | Opens at Tier 2 with a boost of a few percent. Nice, but not a reason to stay | Leave it. It is done |
| Store and money | Problem 9 | Offer at the moment of need. One Christmas item |
| Events | Problem 8 | Advent calendar |
| Social | Friends brought 112 players on the best day and are the best players we get. Servers are near empty (6 playing at the read) | Read the palDay split on Nov 20. Put the invite reward on the first session recap |
| UI on each device | Tablets lose 11 to 17% at the Rank Up card and no other device does. That looks like a layout fault | Sync checks that card on a tablet (already asked in #5496) |

## What I would not do
- Cut tier prices again.
- Add another shop, currency or station.
- Raise ad spend.
- Polish menus that 5% of players open. I spent today on some of those myself.

## What I am unsure of
- Whether catch first beats bowl first. That is why it is a test.
- The store finish rate. 18 presses is too few.
- Any feel claim about phones, until Sync or you check it on a device.

## Issues opened from this audit (Nov 19)
- #5498 Split test: half of new players catch a cat in their first 20 seconds (problem 1). Built with the switch off, on only with Derek's OK.
- #5499 Holdout group: 1 in 10 new players keeps a frozen set of switches for a week (problem 2).
- #5500 A missed catch on a Common never moves the cat or makes the player wait (problem 3, with #5496 and #5497).
- #5501 Three named goals between Tier 3 and Tier 4 (problem 7).
- #5502 Christmas advent calendar, one door a day from Dec 1 to 24 (problem 8).
- #5503 Split test: areas stay open at night up to Tier 3 (problem 10).

Not opened, because they are Derek's calls: ad spend (5), a freeze on new systems (6), a paid Christmas item (8) and the Store offer (9, after Growth's store read).
