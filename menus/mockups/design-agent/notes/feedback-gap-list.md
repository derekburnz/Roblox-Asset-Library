# Game Ideas feedback: what is built and what is queued

Checked 2026-10-28 01:17 UTC against main at b588892 (code in games/cat-cafe/src) and each thread's queue. Sources: the four saved rounds in docs/design/cat-cafe/feedback/ (round 1 2026-10-26, round 2, round 3 Q1 to Q6 and round 4, all 2026-10-27). Set 4 (10 questions) is still unanswered in the Google Doc, so it adds nothing yet. Answers that changed nothing ("good for now") are left out. Themed cats and the town layout were skipped on purpose, because they are already in flight.

## Counts

62 agreed items.

- 40 are built or done (4 of these needed no build: no manager avatar, the name, the audience, the paid items policy).
- 3 were replaced by a later decision.
- 3 are in flight and skipped (the area sets, themed cats, the later area cats).
- 1 is a backlog idea, not a build ask.
- 2 wait on something outside the game: milestone codes and passes.
- 13 are not built yet:
  - 6 were already fully queued at Gameplay-Engineer.
  - 6 were queued at Gameplay-Engineer but had no UI or model work queued; those parts went out at 01:17.
  - 1 (F70 Daily Treat) was not queued anywhere and went to Gameplay-Engineer, UI-Engineer and Sound-Agent.

Messages sent: Gameplay-Engineer (F70), UI-Engineer (F57, F59, F60, F61, F63, F70), Model-Agent (F63, F64 models and potion icons), Sound-Agent (F70). VFX-Agent, Animation-Engineer and Tutorial-Agent have nothing new: their effects and sounds for these rows are already on main.

## The list

| # | item | source round | feature id | thread | status |
|---|---|---|---|---|---|
| 1 | 5 minute day and 5 minute night | R1 Q1 | F23, F66 | Gameplay-Engineer | Replaced: Derek set the night to 90 s (F66); the day stays 300 s |
| 2 | Leftover strays catchable by day until the next night | R1 Q2 | F23, F66 | Gameplay-Engineer | Replaced: areas close at night and a fresh wave comes at sunrise (F66, R3 Q3) |
| 3 | 10 strays per area each wave | R1 Q3 | F23 | Gameplay-Engineer | Built |
| 4 | Five areas: Park, Woods, Neighbourhood, Alleyway, Sewer | R1 Q4 | F23, F51 | Gameplay-Engineer, Model-Agent | Built as grayboxes; the real area sets are being placed now (in flight, skipped) |
| 5 | 10 cats per area across five rarities, Legendary and Mythical in every area | R1 Q5 | F22 | Gameplay-Engineer | Built |
| 6 | Net as closing circles, a better net is easier, all Perfect is a sure catch | R1 Q6 | F26, F34 | Gameplay-Engineer, UI-Engineer | Built |
| 7 | Bait any time, a cat after 10 minutes, Tame or Let go, food used either way | R1 Q7 | F28 | Gameplay-Engineer, UI-Engineer | Built |
| 8 | Rescue traps by area, harder for rarer cats, better gold chance | R1 Q8 | F27, F51 | Gameplay-Engineer, UI-Engineer | Built (the later areas' traps use stand-in props until the sets land) |
| 9 | Interrupt a carrier on the way home; one cat carried at a time | R1 Q9 | F29, F41, F74 | Gameplay-Engineer | Built (now the Tackle) |
| 10 | Money keeps flowing at night, plus offline income | R1 Q10 | F31 | Gameplay-Engineer | Built (night pays 60% today; row 37 raises it) |
| 11 | Rich day customers with big tips | R1 Q10 | F31 | Gameplay-Engineer | Built (made bigger in row 40) |
| 12 | Night food dealer selling rare food | R1 Q10 | F32, F43 | Gameplay-Engineer, UI-Engineer | Built |
| 13 | No manager on screen; the player is the manager | R1 Q11 | none | none | Done, nothing to build |
| 14 | Cat roles with a boost for the right role | R1 Q12 | F25 | Gameplay-Engineer | Built (favourite role pays 1.5x) |
| 15 | Patio, second floor, toys, outfits, daily special customer | R1 Q13 | features section 9 | none | Backlog: Gavin called them content ideas, not a build ask |
| 16 | Strays on all fours, working cats upright in their role outfit | R1 Q15 | F25 | Model-Agent, Gameplay-Engineer | Built |
| 17 | Players name their cats | R1 Q16 | F33 | Gameplay-Engineer, UI-Engineer | Built |
| 18 | A gold version of every cat, no merging | R1 Q16 | F30, F42 | Model-Agent, Gameplay-Engineer | Built |
| 19 | Tiers with prerequisites in place of rebirth | R1 Q18 | F24 | Gameplay-Engineer, UI-Engineer | Built |
| 20 | "Cat Cafe" as the name for now | R1 Q19, R2 Q11 | none | none | Done |
| 21 | Made for everyone | R1 Q20 | rules | none | Done (young audience rules) |
| 22 | A miss ends the catch, the cat sprints off, unlimited tries | R2 Q2 | F40 | Gameplay-Engineer | Built |
| 23 | Shove other players in catching areas | R2 Q3 | F41, F74 | Gameplay-Engineer | Built (now the Tackle, Derek 22:31) |
| 24 | Bait bowl outside the cafe, timer runs offline | R2 Q4 | F44 | Gameplay-Engineer | Built (back step) |
| 25 | Gold cats have their own colouring, 5% from net and bait | R2 Q5, R3 Q4 | F42 | Model-Agent, Gameplay-Engineer | Built |
| 26 | Ranking up spends the coins | R2 Q6 | F24 | Gameplay-Engineer | Built |
| 27 | Cats earn 60% at night | R2 Q8 | F44 | Gameplay-Engineer | Replaced by R3 Q6 (night pays the same, row 37) |
| 28 | One dealer stock on every server | R2 Q9 | F43 | Gameplay-Engineer | Built (amounts per player come in row 36) |
| 29 | Cats only spawn in their own area | R2 Q10 | F22, F23 | Gameplay-Engineer | Built |
| 30 | Getaway after a catch: others pushed back, catcher speeds off | R3 Q1 | F55 | Gameplay-Engineer, VFX-Agent, Sound-Agent | Built (#392, live in version 20) |
| 31 | A shove drops the cat and anyone picks it up with E | R3 Q2 | F56 | Gameplay-Engineer | Built (#357), kept by the Tackle |
| 32 | Chase distances doubled (24 to 64 studs) | R3 Q3 | F57 | Gameplay-Engineer | Queued (main still runs 12 to 32) |
| 33 | A miss costs the player who missed: a wait of 3, 6 then 10 s and a short slow | R3 Q3 | F57 | Gameplay-Engineer, UI-Engineer | Server queued; UI "Catch your breath" wait sent now; the Startled effect is on main |
| 34 | Announce a Mythical in a new wave | R3 Q3 | F58 | Gameplay-Engineer | Queued (the Mythical sting is on main) |
| 35 | Wipe the cats at night and refresh | R3 Q3 | F66 | Gameplay-Engineer | Built |
| 36 | Dealer: amounts per food rolled the same on every server, per player, every 5 minutes | R3 Q5 | F59 | Gameplay-Engineer, UI-Engineer | Server queued; UI half sent now |
| 37 | Night pays the same as day | R3 Q6 | F60 | Gameplay-Engineer | Queued (main still pays 60%) |
| 38 | Bait set at night is ready in half the time | R3 Q6 | F60 | Gameplay-Engineer, UI-Engineer | Server queued; UI moon countdown and dusk reminder sent now |
| 39 | Day customers leave tip piles worth a share of income | R3 Q6 | F61 | Gameplay-Engineer, UI-Engineer | Server queued; UI Collect on the till sent now (the pile model and sound are on main) |
| 40 | Rich visitors pay a good chunk | R3 Q6 | F61 | Gameplay-Engineer | Queued (main still pays 45 s of rate) |
| 41 | Cat Collector offers rewards for one of your resting cats | R3 Q6 | F63 | Gameplay-Engineer, UI-Engineer, Model-Agent | Server queued; UI offer card and the Collector model sent now (sounds on main) |
| 42 | Cat lock so the Collector never takes a favourite | R3 Q6 | F62 | Gameplay-Engineer | Queued (the UI lock is on main) |
| 43 | Mystery Visitor leaves potions and gifts | R3 Q6 | F64 | Gameplay-Engineer, UI-Engineer, Model-Agent | Server and UI queued and moved up (Derek 00:51); visitor, gift box, four potion bottles and potion icons sent to Model-Agent now (effects and sounds on main) |
| 44 | Hold E to start a catch | R4 Q1 | F45 | Gameplay-Engineer | Built |
| 45 | One miss ends the catch | R4 Q2 | F40 | Gameplay-Engineer | Built |
| 46 | 1 to 5 circles by rarity | R4 Q3 | F22, F26 | Gameplay-Engineer | Built |
| 47 | A dropped cat walks back to its spot and can be picked up on the way | R4 Q4 | F67 | Gameplay-Engineer | Queued (the UI is on main) |
| 48 | Safe zone starts at the stripes | R4 Q5 | F45 | Gameplay-Engineer | Built |
| 49 | Themed cats with one or two props, ideas for the later areas | R4 Q6 | F46, F51, F78 | Model-Agent | In flight (skipped); second props wait on Set 4 Q2 (F71) |
| 50 | Every working cat shows a sign of its role | R4 Q7 | F46, F71 | Model-Agent, Gameplay-Engineer | Built for one-prop cats; the two-prop Entertainer rule waits on F71 (Set 4 Q2) |
| 51 | Gold Legendary and Mythical cats keep their effects, in gold | R4 Q8 | v0.10 effects | VFX-Agent | Built |
| 52 | Daily Treat: good days 2 and 4, a really good day 7 | R4 Q9 | F70 | Gameplay-Engineer, UI-Engineer, Sound-Agent | Sent now (was not built or queued); Set 4 Q5 may tune the prizes, which are data only |
| 53 | Tip Jar: a good 60 minute gift and a really good 120 minute one | R4 Q10 | F68 | Gameplay-Engineer | Built (#351); the 120 minute Tip Potion arrives with F64 |
| 54 | Food rarity badges | R4 Q11 | F69 | UI-Engineer | Built |
| 55 | Spin wheel odds button | R4 Q11 | F69 | UI-Engineer | Built (UI-Engineer is restyling odds rows, Derek 01:08) |
| 56 | A different forever bonus per Index track, big milestone prizes | R4 Q12 | F54 | Gameplay-Engineer | Built |
| 57 | `launch` code at release | R4 Q13 | F65 | Gameplay-Engineer | Built, off until the game goes public |
| 58 | Codes for player count and like milestones | R4 Q13 | none yet | none | Waiting on the milestones |
| 59 | Group code for group members | R4 Q13 | F65 | Gameplay-Engineer | Built, off until the game moves to Derek's group (Set 4 Q8 open) |
| 60 | Passes picked by a monetization agent | R4 Q14 | none yet | none | Waiting (Set 4 Q10 asks when it starts) |
| 61 | Paid items may help a player if everything is earnable in game | R4 Q15 | policy | none | Done (decisions) |
| 62 | The 18 later-area cats stand | R4 Q16 | data-model 3c, F51, F78 | Model-Agent | In flight (skipped; F78 replaced some) |
