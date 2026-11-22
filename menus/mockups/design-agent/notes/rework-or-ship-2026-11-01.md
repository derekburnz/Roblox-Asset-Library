# Rework or ship: decision memo

Design-Agent, 2026-11-01. For Derek, from his message of 2026-10-31 19:47.

## Recommendation

Ship and learn. I agree with the lean toward a learning release. Before the ads, spend about five thread-days on three things. First, make the first ten minutes frictionless. Second, make rare cats and rare decor feel big when you get them. Third, add one visible Luck number built from luck pieces the game already has. Then run the ads week at about 20% of the budget and decide from the numbers, using the rules already written in docs/growth/comps.md section 8.

Park the Cat Cannon server build (F84) and the long areas (F85) until the ads week shows whether area travel is the problem. The cannon's UI, effects, sounds and animations are merged and switched off, so parking it loses nothing. Building it first would add about three days and a 3 second flight to every trip, and that flight is exactly the part you are unsure is fun.

A rework is not cheap. The smallest real one is about a week and the one you described is about two, and both throw away tested work before a single stranger has played. The ads week tells us which rework, if any, is worth it.

## The core loop in one sentence

Catch stray cats out in the areas, carry them home past the other players and give them jobs in your cafe so they earn coins that rank you up into areas with rarer cats.

## Why it feels like two games

Steal an Egg works because the base asks for nothing: you drop the pet and it earns, so all your attention goes to the run. Restaurant Tycoon works because the restaurant is the game: building and decorating are the fun. Ours asks for attention in both places at once. The areas have the catch circles, rescues, tackles, bait and the night clock. The cafe has tables, roles, decor, the tip jar, rich tips and bedtime. On top of that sit quests, the dealer, the Collector, the Fish Market, crates, potions, codes, the spin wheel and the daily treat. That is more than twenty systems with their own screens, and a new player meets most of them in the first session.

Every option below makes the same fix: one active loop (catching) and one passive earner (the cafe), with the extras arriving one at a time as you rank up.

## Options

| Option | What changes | Thread-days | What we risk |
|---|---|---|---|
| A. Ship and learn (recommended) | Today's town and travel buttons stay. A low-friction start with short tips at the moment each thing first matters, funnel events and a feedback button. Extras like the dealer, Collector, Fish Market, crates and potions open from Tier 2 instead of on day one. Big celebrations for Legendary and Mythical pulls. One Luck number and a free Lucky Day. Daily bug fixes in the ads week. | about 5 before the ads | Low. If the loop does not hold, we learn that for 20% of the budget. |
| B. One active loop | Catching is the only thing you do with your hands. The cafe runs itself: cats take orders, carry the food and collect tips with no clicks. Tables and decor stay as things you buy. Night, rescues and the tip jar are cut or folded into catching. The economy is retuned. | about 7 to 9 | Medium. Cuts tested systems and needs a full QA pass. Best done after the ads, if D1 says the cafe side is noise. |
| C. One straight world | Steal an Egg's shape: the town at one end and the areas in a line going out, each further zone rarer, with walk speed as the upgrade that opens the next zone. Carrying a cat always slows you to one fixed speed, so faster running shortens the trip out but never the trip home, and tackles stay possible. | about 10 to 14 | High. New world sets, travel, tackle tuning, economy and every QA script change, and most of the cannon work is thrown away. |

Your worry about C, that faster running makes tackling impossible, has a simple answer: the carry speed is fixed. Speed upgrades only make the empty run out faster. The walk home with a cat is always the slow, exposed part, and that is where the tackles happen.

If the ads week says travel is the problem, C is the rework I would pick. If it says the cafe side is noise, B is. If D1 is fine, neither.

## Where luck fits

The game already has luck, but it is hidden in five places a player never sees together: the bowl's level, Catnip, the Lucky Potion, the crates' lucky twentieth and the Index's gold luck. Most popular games show one Luck number that every source adds to. That is the fix. The way it fits a cat cafe is the Lucky Cat: the beckoning cat statue real shops keep by the door for luck. Every cafe gets one by its front door, you upgrade it with coins and other players see it from the street. The rolls already exist, so this is about a day and a half plus the statue model. Full spec: docs/design/cat-cafe/luck-and-rare-moments.md.

1. A Luck chip on the HUD, for example "Luck x1.3". It adds up your sources (the Lucky Cat's level, a Lucky Potion, a Lucky Day) and applies to your own rolls, bait results and crates. Wave strays are rolled once for the whole server, so they use the luckiest player there, the way gold luck already works. Tapping the chip shows what adds to it. This is the recommended piece for the ads week.
2. A Lucky Day, free and server-wide. Every fourth day, about every 26 minutes, a banner says "Lucky Day!" at sunrise and that wave rolls with rare cats twice as likely. The HUD clock counts down to the next one, so players stay for one and come back for one. Recommended for the ads week.
3. Lucky landings, only if the cannon is built later. Each flight rolls where you land, and Luck raises the chance of landing next to a rare stray. This turns the flight from a wait into a roll.
4. A Luck stat on cats, later. A cat you take with you on your shoulder adds its own Luck, more for rarer cats. It is a good long-term goal but a new system, so it waits.

None of these are sold for Robux in v1. Paid luck would make every roll it touches a paid random item under Roblox's May 2026 rules, which docs/growth/monetization.md keeps out of the first release.

## What has to be true before the ads

1. The low-friction start, specced next in this thread.
2. Funnel events at every step of the first session, so we can see where people quit, as your notes say.
3. A feedback button. The bug report screen and its upload already work, so this is a small change to it.
4. Celebrations for Legendary and Mythical cats and decor, specced in this thread after the start.
5. The Luck chip and Lucky Day.
6. The experience set to public and the maturity questionnaire filled in (Tools-Agent).
7. A daily bug fix and publish rhythm for the ads week.

After launch, one update a week on a fixed day, which is what the trending games do. The first two would be the cats making the orders (week one) and the front lawn decorations (week two). Both are specced in this thread, ready to build.

## How we decide after the ads week

These are the rules from comps.md section 8, and they need about 100 new players a day to read.

| What the numbers say | What we do |
|---|---|
| D1 at or above 12% and sessions of 10 minutes or more | Keep the game. Weekly updates, the next content layer. |
| D1 between 8% and 12% | Fix the worst step in the start funnel first. No new content. |
| D1 under 8% after two start fixes, or sessions under 6 minutes | The loop is not holding. Pick B or C from where players quit, or move on to the next game with what we learned, as you suggested. |
