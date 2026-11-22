# Teaching players without a pushy tutorial (casual, mobile, children's games and Roblox)

Researched 2026-11-20. Source quality is marked where it matters: "primary" means a talk write-up, a peer-reviewed paper, official Roblox documentation or a first-hand developer post; "secondary" means an aggregator or a blog that does not show its data.

## 1. What are the named techniques for "invisible" or "learn by doing" onboarding, with examples?

### Takeaway
The best documented playbook is George Fan's ten rules from Plants vs. Zombies (GDC 2012) plus Roblox's own three techniques (in-world visual cues, contextual "just in time" tutorials, timed hints). Both say the same thing: never label a tutorial, make the player do the action once, keep words to a handful, and only help the players who are actually stuck.

### Cited Findings
- George Fan, GDC 2012, "How I Got My Mom to Play Through Plants vs. Zombies", ten tips (write-up by Tom Curtis, 2012-03-09) — [Game Developer](https://gamedeveloper.com/design/gdc-2012-10-tutorial-tips-from-i-plants-vs-zombies-i-creator-george-fan):
  1. Blend the tutorial into the game. No section is ever labelled "the tutorial"; players should learn without noticing they are taught.
  2. "Do" rather than "read". Level 1 shows that plants shoot right and zombies walk left with no explanation.
  3. Spread mechanics out. Money does not appear until the player has finished 10 levels; the Zen Garden comes near the end. Players are more willing to learn as they invest more.
  4. Get the player to do it once. One action is usually enough to understand a mechanic. Fan used a coin with a big arrow and blinking icons, crediting Fisher Price toy design (people respond to bright, shiny objects).
  5. Use fewer words. Maximum of eight words on screen at once (he admits breaking it sometimes). Example: "Click on a seed packet to pick it up." Write like an "eloquent caveman".
  6. Unobtrusive messaging. Text shown mid-game is passive; the player never has to stop playing to dismiss it.
  7. Adaptive messaging. Tips are shown only to players "doing the wrong thing" (for example planting on the wrong side), so skilled players are not patronised.
  8. Don't create noise. Irrelevant messages teach players to ignore all messages ("the boy who cried wolf").
  9. Use visuals to teach. Character design signals function: Peashooter has a big mouth, Screen-Door Zombie is visibly shielded.
  10. Leverage what people already know. Coins and diamonds were used as currency instead of brains because their value is understood instantly.
- Roblox official docs name three onboarding techniques: Visual Elements, Contextual Tutorials and Timed Hints — [Roblox Creator Docs, Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
  - Visual elements are temporary, in the world or over the UI, and "should disappear once they've served their purpose": bouncing arrows, particles, glowing trails, in-world signs showing the core loop.
  - Prominence example: in Color or Die a sign explaining the core survival mechanic sits in the player's line of sight at the first paint bucket and does not block the start of play.
  - Hints example: in Jailbreak, footprints suggest escape routes and imply objects are interactive, so players solve the problem themselves.
  - Immersion example: Hello Kitty Cafe uses directional trails that guide without forcing, so players keep freedom to explore. Creatures of Sonaria and Winds of Fortune use directional arrows and icons.
  - Visuals work across languages, avoid translation layout problems, help younger or pre-reader players and stay readable on small phone screens.
  - Contextual ("just in time") tutorials trigger during normal play (entering a new zone, picking up a new item). Claimed benefits: better retention of the lesson because the player practises right away, faster "speed to fun", lower cognitive load. Fixed tutorial sequences "can feel restrictive or boring".
  - Squishmallows example: the combine station tutorial appears only when the player is holding two identical Squishmallows; the marketplace is explained only when the player finds it. Putting either in onboarding "would make it too long and irrelevant".
- Roblox's three goals of onboarding: teach the essentials (controls and core loop, what to do and why), get to the fun quickly (players often decide within minutes), leave players wanting more (show short, mid and long term goals; end onboarding on a deliberate moment of joy) — [Roblox Creator Docs, Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)
- NPC framing beats a bare instruction: a character saying "Help me rebuild my house, it got destroyed!" engages more than an instruction to tap a house (Supersonic, Sari Berkovich, 2025-03-03) — [Supersonic](https://supersonic.com/learn/blog/optimizing-ftue/)
- Pokemon GO's catch tutorial is two lines of text and a static "Catch a Pokemon" message; three Pokemon appear on the map with no pointing fingers and the player experiments to learn the throw. Gyms are never explained (Steffie Garcia, 2016-07-25) — [Game Developer](https://gamedeveloper.com/business/is-pok-mon-go-s-ux-intentionally-obtuse-)
- Clash Royale splits onboarding into five short tutorials, one concept each; Call of Duty Mobile fills early lobbies with bots so new players win; Carcassonne offers "Go ahead" or "Later" for guidance (secondary, Adrian Crook, 2026-04-08) — [Adrian Crook + Associates](https://adriancrook.com/?p=8151)
- A Roblox-focused blog lists: constrain the first area so only the core mechanic is present, respond to every early action within about half a second, make early failure instructive (short respawn, no lost progress), one mechanic at a time. It cites Natural Disaster Survival as teaching its loop with no text box. Its numbers are unsourced design guidance, not data (Maya Osei, 2026-06-25) — [RoWatcher](https://rowatcher.com/news/onboarding-without-tutorials-teaching-through-play-in-roblox)

### Inferences
- A reusable checklist falls out of Fan plus Roblox: (a) no screen called "Tutorial"; (b) first action available in the world within seconds; (c) eight words or fewer per message; (d) messages never pause play; (e) each later system is introduced by a trigger in play (first time holding X, first time near Y), not by a step number; (f) help is conditional on the player stalling or doing the wrong thing.
- Fan's "money after 10 levels" is the precedent for hiding shops, tiers, rebirth and codes until the player has caught and placed a few cats. A HUD that grows as features unlock is itself a teaching device.
- Fan's own example uses a giant arrow over a coin. The lesson is not "never use arrows"; it is "point at a thing in the world the player wants, once, then stop".

### Gaps
- I could not open the GDC Vault video itself or Celia Hodent's onboarding material; the Hodent page I fetched ([designative.info](https://designative.info/2019/03/28/the-ux-of-fortnite-celia-hodent)) only describes her two pillars (usability and "engage-ability") and has no onboarding detail. Her well-known points (learning by doing in context, form follows function, an onboarding plan that ranks what to teach by importance and difficulty) are not sourced here.
- Classic level-design examples (Super Mario Bros 1-1, Half-Life 2, Portal) are not sourced in this session.
- No King or Supercell first-hand talk was retrieved. A GDC Vault talk titled "Staying in Top Eleven: Improving Retention Through the Tutorial" exists ([GDC Vault](https://gdcvault.com/play/1019300/contactUs)) but was not read.

## 2. What does the evidence say about forced tutorials, and what numbers exist?

### Takeaway
The strongest study (45,000 players, CHI 2012) found tutorials only helped the one complex, unconventional game; in the two simple games they did nothing or slightly reduced return rate, and restricting player freedom gave little benefit. Developer data from Roblox and mobile agrees: the biggest loss is at the first step, and click-and-read chains lose roughly half of new players.

### Cited Findings
- Andersen et al., "The Impact of Tutorials on Games of Varying Complexity", CHI 2012. Eight tutorial designs, three games, over 45,000 players (Foldit 9,743; Refraction 13,158; Hello Worlds 22,417) — [University of Washington project page](https://grail.cs.washington.edu/projects/game-abtesting/chi2012/), [paper PDF](https://grail.cs.washington.edu/projects/game-abtesting/chi2012/chi2012.pdf)
  - Foldit (most complex): context-sensitive tutorials gave 75% more levels completed (7 vs 4) and 29% more time played (660 s vs 510 s) than no tutorial. Context-insensitive gave 25% more levels and 12% more time.
  - Refraction: no significant effect of any tutorial (levels 15 vs 16, time 990 s vs 1050 s, return about 28.5% either way).
  - Hello Worlds: no effect on levels or time; return rate was lower with context-sensitive tutorials (17.96% vs 21.60% with none).
  - Forcing the player (blocking "stencils" vs non-blocking): little benefit; no significant effect in Refraction or Hello Worlds.
  - A help button on demand: in Refraction, players with the button completed 12% fewer levels and played 15% less; only 31% of players with access used it. In Hello Worlds the return rate was about 3 points lower. (The paper's text and table disagree on one aggregated help figure.)
  - Authors' conclusion: "investment in tutorials may not be justified for games with mechanics that can be discovered through experimentation"; design early levels to encourage experimentation.
- Roblox staff example funnel (Plant, by BreakfastCandy, 2024-07-12): 100% enter the farm, only 29.52% plant a seed (a 70.48% loss at the first real step), under 3% finish step 9. The fix that worked was an icon over the pots showing where seeds go — [Roblox DevForum](https://devforum.roblox.com/t/improving-onboarding-through-funnel-events/3064458)
  - Listed causes of drop-off: boredom (weak goal, unclear payoff), confusion (do not know what or how, cannot find location), frustration or blockage (economy too hard), bugs, and unrecoverable edge cases (selling the only rod before being able to afford another).
  - Advice: "Tackle the largest and earliest drop-offs first"; ship cheap fixes fast; prioritise drop-off fixes over content. No universal completion target exists; compare Day 1 retention with similar games.
  - The same post's Feline Fishing Fun example flags: selling (unclear where the shack is, confusing sell UI), first upgrade (unclear benefit, too expensive), and a first rare target too advanced for onboarding.
- Roblox developer Askavix (2025-07-14): a 5 minute, 16 step story tutorial that auto-starts; 41% quit at step 1 (about 20 seconds, heavily guided), only 30% finish. Crash rate under 1 in 200. The tutorial dims other buttons and walks through clicks and text — [Roblox DevForum](https://devforum.roblox.com/t/41-of-players-leaving-game-within-30-seconds-of-tutorial/3814365)
  - Reply (GamEditoPro): a click-and-read tutorial in their game lost about 50% of users.
  - Reply (ZurichBT, 2025-12-23): teach only the basics, minimal text, let players move first, teach each feature when it becomes relevant (equipment at the first enemy, stats at the first level up); a click-through chain before spawning makes players click past text without reading.
  - Reply (ZINTICK): dumping everything at once means players forget most of it. Others suggested a skip option with replay later.
- Supersonic (2025-03-03): in Trash Tycoon 60% of players churned during the tutorial when it jumped too quickly between mechanics. An earlier version that gave up to 1 minute with no instructions also caused confusion and churn because players did not understand the goal. Removing a single step or a single click in A/B tests can move retention — [Supersonic](https://supersonic.com/learn/blog/optimizing-ftue/)
- Secondary, aggregated mobile statistics (Adrian Crook, 2026-04-08; original studies not shown): 20% of players abandon a game within the first two minutes; 73% leave within 24 hours; average mobile Day 1 retention 26.48% to 27.69%; sessions over nine minutes go with 31% Day 1 retention vs 20% for shorter; 60% quit if a game gets too hard too quickly; Marvel Snap cut its tutorial to under four minutes — [Adrian Crook + Associates](https://adriancrook.com/?p=8151)
- Conflict worth noting: Roblox's own docs present "spotlight the target and dim the rest of the screen" with an arrow (Hello Kitty Cafe) as a clarity technique, and argue pointing is clearer than text such as "open your inventory by clicking the backpack button" — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques). The same page says fixed sequences can feel restrictive or boring and recommends contextual tutorials and timed hints instead.

### Inferences
- The two failure modes are opposite and both are documented: too much forcing (41% and about 50% losses on click-and-read chains) and no goal at all (Trash Tycoon's free minute). The target is a clear, visible goal with no lock on the player.
- A catch-a-cat game has mechanics "discoverable through experimentation" in Andersen's sense (walk up, tap, get a result), which is the class of game where tutorials showed no benefit and sometimes a small cost.
- Dimming and arrows are not harmful because of the visual itself; they hurt when they are chained into many steps, block other input and appear before the player wants the thing. One highlight on one button at the moment the player has a reason to press it is consistent with both Fan and Roblox.
- The first step carries the largest loss in every funnel found (70%, 41%), so the first step should be the fun verb itself, not a menu or a dialogue.

### Gaps
- No controlled A/B result was found for a Roblox game that removed its tutorial and reported before and after retention. The RoWatcher articles titled "Fewer Tutorials, Better Day 3" and "Onboarding in 90 Seconds" appeared in search but the one I read contains no sourced data.
- No per-technique numbers were found for screen dimming, arrows, or unskippable steps in isolation.
- The DevForum threads "A growing problem with tutorials" ([link](https://devforum.roblox.com/t/a-growing-problem-with-tutorials/2582978)) and "How do I make a tutorial feel less intrusive?" ([link](https://devforum.roblox.com/t/how-do-i-make-a-tutorial-feel-less-intrusive/172674)) could not be read (the forum returned a maintenance redirect and an empty page).
- Andersen's games were web games played by a general audience in 2011 and 2012, not children on phones.

## 3. What works for children roughly 8 to 13 on phones?

### Takeaway
Nielsen Norman Group's studies of 125 children aged 3 to 12 show children skip instruction paragraphs (observed on Roblox itself in 2018), want instant gratification, and explore by tapping everything rather than following a main path. By about 9 to 11 their motor skills are near adult level, but targets should still be generous and anything that looks like a small close button is a trap.

### Cited Findings
- Three study rounds (2001, 2010, 2018), 125 children aged 3 to 12; the 2018 round covered 39 websites and 36 apps with 35 children in the US and Beijing (Katie Sherwin and Jakob Nielsen, 2019-01-13) — [NN/g](https://nngroup.com/articles/childrens-websites-usability-issues)
  - Children skipped long instruction paragraphs on the U.S. Mint Kids site in 2010, "and the same behavior appeared on Roblox eight years later". Instructions must be brief.
  - Youngest children do not read, young children read tentatively, older children scan. Recommended 14 pt type for young children, 12 pt for older.
  - Children want instant gratification and get frustrated by slow designs; given a choice they switch to something else. They try a few quick fixes then give up.
  - Children "mine-sweep" the screen and like trying many options; adults stick to the main path.
  - Children reacted negatively to content pitched one school grade above or below them; design for narrow bands (3 to 5, 6 to 8, 9 to 12).
  - Children cannot reliably tell advertising from content.
  - Until about age 9 children preferred touchscreens to mouse and keyboard.
- Physical development (Feifei Liu, 2018-07-08) — [NN/g](https://www.nngroup.com/articles/children-ux-physical-development/)
  - Around 9, more advanced interactions become possible; around 11, children can use the same range of physical interactions as adults.
  - Recommended minimum touch target for young children is 2 cm by 2 cm (adult guideline 1 cm by 1 cm). A 5 mm close button was too small for 7 year olds to hit, and two 7 year olds left the app out of annoyance.
  - Ages 3 to 5 manage tap, swipe and drag on touchscreens; avoid demands for quick reactions and two-handed use for the youngest.
  - 7 to 9 year olds had no trouble when given "clear instructions with images".
  - Two 8 year olds abandoned a game when the dragging control was awkward.
- Visual cues help younger and pre-reader players and avoid translation problems — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)

### Inferences
- For 8 to 13 on phones: assume nobody reads a sentence. Use a picture or icon plus at most a few words (Fan's eight word limit fits the NN/g finding).
- "Mine-sweeping" means every visible button will be tapped in the first minute. Either every button does something safe and pleasant, or it is not shown yet. A locked or dimmed button that does nothing is read as "broken".
- Pitching tone slightly young is a real risk for 11 to 13 year olds (the "one grade below" reaction). A guide character should be funny or cool rather than babyish, and should never talk down.
- Instant gratification plus low patience argues against any wait before the first catch (no cutscene, no long loading tips, no timers in minute one).
- Targets around 1 cm are acceptable for 9 and up, but larger is safer for the younger end; close buttons need the same size as action buttons.

### Gaps
- No source was found that measures how children react to being told what to do (reactance) in games, or attention span in seconds for this age band.
- NN/g studied 3 to 12; nothing here covers 13 specifically (NN/g has a separate teen study that was not read).
- No reading-speed or words-per-screen data for this age on phones was found beyond the type sizes above.

## 4. How do good casual and idle games structure the first 60 seconds and first 3 minutes?

### Takeaway
Documented guidance agrees on the shape more than on exact seconds: core action inside the first minute, a rewarded early win with celebration, one mechanic at a time, fast early levels, and a glimpse of long term goals plus a "moment of joy" at the end of onboarding. Hard second-by-second benchmarks from named idle games were not found.

### Cited Findings
- A strong first-time experience gets players "engaged within their first minute", teaches through play and builds in early "aha" moments (secondary summary; full report is paywalled) — [Liquid & Grit](https://www.liquidandgrit.com/designing-streamlined-ftues-to-maximize-early-retention/)
- Roblox: players often decide whether they like a game within minutes; use low early XP thresholds so players level quickly; give starter items or soft currency (but do not overgive); by the end of onboarding show the full range of content and short, mid and long term goals; end with rewards, animations or celebration so players come back — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding)
- Supersonic (hybrid-casual, 2025-03-03): show the core mechanic quickly instead of front-loading rules; reward early wins with confetti so "each tap feels satisfying"; master one loop before the next system (Trash Tycoon: trash cycle first, then trucks, dumpyards, incinerators, each with its own short tutorial at unlock); make early levels achievable with mild friction; tease upcoming upgrades; delay ads; track time to first engagement with each mechanic and next-session return — [Supersonic](https://supersonic.com/learn/blog/optimizing-ftue/)
- Plants vs. Zombies delays its currency until after 10 levels and its biggest side mode until near the end — [Game Developer](https://gamedeveloper.com/design/gdc-2012-10-tutorial-tips-from-i-plants-vs-zombies-i-creator-george-fan)
- Secondary: front-load rewards tied to learning a mechanic, then move to variable rewards after the first session; show locked advanced rewards to build anticipation; 20% of players leave within two minutes; sessions over nine minutes go with higher Day 1 retention (31% vs 20%) — [Adrian Crook + Associates](https://adriancrook.com/?p=8151)
- Roblox suggests testing starting currency and hint delays with Experiments and setting winners live with Configs, without a server restart — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)

### Inferences
- A defensible target schedule built from these sources (my synthesis, not a published benchmark):
  - 0 to 10 s: player has control and can see the thing to interact with.
  - By about 30 s: first core action done and first reward with celebration.
  - By about 60 s: the loop has closed once (action, reward, the reward visibly does something).
  - By about 2 to 3 min: first upgrade or first goal completed, first level up, and a look at something desirable that is not yet affordable.
  - End of onboarding (about 3 to 5 min): a set-piece moment of joy and a visible next goal.
- Because the nine minute session figure is correlational, aim to give a reason to stay past minute five (a second goal already in progress) rather than treating nine minutes as a cause.
- Low early thresholds mean the first rank-up or tier should cost roughly what the first one or two loops earn.

### Gaps
- No primary source gave measured time-to-first-action or time-to-first-reward for named idle games (AdVenture Capitalist, Egg Inc., Idle Miner) or named Roblox simulators (Pet Simulator, Grow a Garden, Steal a Brainrot). Deconstructor of Fun and GameAnalytics articles were not retrieved.
- The Liquid & Grit data behind its recommendations is paywalled.

## 5. How do games give guidance that feels like help, not pressure?

### Takeaway
Guidance feels like help when it is conditional, passive and in the world: it appears only for players who stall, never stops play, and points at something the player already wants. Roblox documents the exact pattern, including a worked 10 second example.

### Cited Findings
- Timed hints: show a hint only after most players would already have done the step. Worked example: playtests show most players find the "PLANT CABBAGE SEED" button within 10 seconds, so highlight it at 11 seconds; this helps the rest "without bothering everyone else". Hints should need to be shown only once, and only the first time the task appears. Roblox suggests A/B testing a 5 second vs 10 second delay — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- Timed hints protect player agency: experienced players are not annoyed and newer ones get room to work it out. Hints can also surface a neglected feature later (highlight the trade button if unused after two sessions) — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- Second worked example: after harvesting, an arrow over the correct one of three market stalls appears only after the player has had time to explore — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- Trails and footprints guide without forcing (Hello Kitty Cafe trails, Jailbreak footprints) — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- Fan: passive text that never stops play; adaptive tips only for players doing the wrong thing; no noise, or players learn to ignore everything — [Game Developer](https://gamedeveloper.com/design/gdc-2012-10-tutorial-tips-from-i-plants-vs-zombies-i-creator-george-fan)
- Feedback must confirm every action or players assume the action did nothing or the game is bugged. Winds of Fortune example: hit flash, damage numbers, coins flying out, quest counter ticking on each defeat — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- An in-world icon over the target (icon over pots in Plant) fixed a 70% first-step loss; Roblox lists on-screen text, in-world visuals, NPC dialogue or quests as ways to make the goal clear — [Roblox DevForum](https://devforum.roblox.com/t/improving-onboarding-through-funnel-events/3064458)
- Motivation in a character's voice outperforms a bare instruction ("Help me rebuild my house") — [Supersonic](https://supersonic.com/learn/blog/optimizing-ftue/)
- Pokemon GO spends its little tutorial text on motivation rather than instruction, and asks for a nickname right after the first catch, when the player feels good (the author notes it is unclear whether the light touch was deliberate, and that some players were confused) — [Game Developer](https://gamedeveloper.com/business/is-pok-mon-go-s-ux-intentionally-obtuse-)
- Optional guidance: Carcassonne's "Go ahead" or "Later"; DevForum repliers ask for a skip with replay later — [Adrian Crook + Associates](https://adriancrook.com/?p=8151), [Roblox DevForum](https://devforum.roblox.com/t/41-of-players-leaving-game-within-30-seconds-of-tutorial/3814365)
- Caution on help buttons: a help-on-demand button lowered levels completed by 12% in one game and only 31% of players used it — [Andersen et al. 2012](https://grail.cs.washington.edu/projects/game-abtesting/chi2012/chi2012.pdf)

### Inferences
- A layered "help ladder" matches the evidence: (1) the world itself (the target is the brightest, nearest, moving thing); (2) one small goal chip of eight words or fewer that never blocks input and ticks when progress is made; (3) after about 10 seconds without progress, a glow or trail on the target; (4) only after a longer stall, a pointing hand or a line from the guide character. Each rung fires once per task.
- Measure the stall delay per step from playtests (time by which most players have done it, plus a second), as Roblox's 10 and 11 second example does, rather than using one global number.
- The goal chip doubles as feedback: a counter that ticks on each catch is the same device as Winds of Fortune's quest counter.
- Do not rely on a "?" help button as the safety net; proactive conditional hints are better supported than on-demand help.
- Ask for anything optional (name a cat, follow, favourite) right after a win, never before the first one.

### Gaps
- No measured comparison of "ignorable goal chip" versus "forced step" was found.
- No source measured the best stall delay for children; the 10 second figure is Roblox's illustrative example.

## 6. What makes a collection or catching game fun in the first minute?

### Takeaway
Direct evidence here is thin. What was found: Pokemon GO opens with three catchable creatures and almost no instruction, then asks for investment straight after the catch; Roblox's fishing example warns that selling, the first upgrade price and a too-advanced rare target are where catching games leak players; and strong, layered feedback on every action is treated as essential.

### Cited Findings
- Pokemon GO: three Pokemon appear on the map at the start, no pointing fingers, the player experiments with the throw; a nickname prompt follows immediately after the first catch. Hidden systems (gyms, the Pikachu starter trick) became shareable "lore" that drove word of mouth. The game reached over 21 million US daily users in July 2016 — [Game Developer](https://gamedeveloper.com/business/is-pok-mon-go-s-ux-intentionally-obtuse-)
- Feline Fishing Fun funnel (Roblox staff example): players drop at "sell fish" (do not know where or how), drop hard at "upgrade rod" (unclear benefit, too expensive, confusing shop), and at "catch shark" (unclear location, low spawn rate, high escape odds, target too advanced for onboarding). An unrecoverable state (selling the rod) is called out as an edge case to design out — [Roblox DevForum](https://devforum.roblox.com/t/improving-onboarding-through-funnel-events/3064458)
- Layered feedback per action (flash, numbers, coins flying, counter ticking) so the player never wonders whether it worked — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- Squishmallows teaches combining only once the player holds two identical ones — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design/onboarding-techniques)
- Early wins are engineered in other genres (bot lobbies in Call of Duty Mobile); 60% of players are reported to quit if a game gets too hard too quickly (secondary) — [Adrian Crook + Associates](https://adriancrook.com/?p=8151)
- Reward and celebrate early wins with confetti; create a visible low-currency moment only after the loop is understood — [Supersonic](https://supersonic.com/learn/blog/optimizing-ftue/)
- Fan: character visuals should signal function at a glance, which applies to reading a creature's rarity or behaviour from its look — [Game Developer](https://gamedeveloper.com/design/gdc-2012-10-tutorial-tips-from-i-plants-vs-zombies-i-creator-george-fan)

### Inferences
- First catch should be impossible to fail: several easy creatures in view at spawn (Pokemon GO's three), no escape chance, short catch time. Save escape odds and near misses for after the loop has closed once; the fishing example lists "high escape odds" as an onboarding leak.
- Put the rarity reveal on catch one or two as a celebration, and make one early catch noticeably better than expected so the player learns rarity exists by feeling it.
- The sell and upgrade steps are where catching games lose people. Make the first conversion to coins automatic or one tap at the place the player already is, and price the first upgrade at one or two catches.
- Keep a few systems unexplained on purpose (a rare night cat, a secret spot) as discoverable lore, which is cheap word of mouth for a young audience.
- Make it impossible to reach a dead end in minute one (no way to spend or lose the only bait or tool).

### Gaps
- No sourced data was found on guaranteed first catch, near-miss effects, hatch or reveal animation length, or sound design for catch moments in Pokemon GO, Roblox pet simulators or fishing games (Fisch, Pet Simulator 99, Adopt Me, Grow a Garden). The search returned only player guides.
- Near misses are also a gambling-adjacent mechanic; no source here addresses their suitability for a young audience, so this needs a policy check before use.
