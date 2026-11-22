# Ticket Booth (Water Park) and Dragon Keep (Castle): full draft

Status: draft 2 for Derek's OK, Design-Agent, 2026-11-13. Gameplay-Engineer's stacking and pace check is folded in (Gameplay-Engineer/notes/ticket-booth-dragon-keep-check-1.md). Nothing is built until he says yes.
Derek's picks (23:04 UTC Nov 13): station 3 Ticket Booth for the Water Park, station 4 Dragon Keep for the Castle, with his changes.
Picture: `Design-Agent/for-derek-2026-11-13/ticket-booth-dragon-keep-draft2.png`.
Helpers: Gameplay-Engineer (stacking and pace check), Model-Agent (booth, keep, five dragon looks), Motion-FX (rank-up cutscenes, card flips, VFX), sound (cues).

Rules both follow (same as every camp extra):
- Each sits in its area's camp, in the safe zone, uses the shared "!" and has one cannon picker line.
- Nothing is sold for Robux: no tickets, no warmth, no card rerolls. So neither is a paid random item.
- The Dragon's card pick is random but earned only. Its odds still show on the pick screen, so it reads honest and stays safe if anything here is ever sold.
- The 2x, 3x and 4x Money passes are never in the Ticket Booth or any golden fish shelf (#4055 rule).

---

## 1. Ticket Booth (Water Park camp)

### 1.1 What it does
Once the Water Park is unlocked, every cat caught anywhere drops tickets: nets, rescues, bait, the Mouse Dash prize cats. Tickets buy real prizes at a clean booth: golden fish, Trait Tokens, golden crates, Water Park decor and outfits, and a booth-only cat. No food bowl filler.

### 1.2 Tickets per catch
| Cat | Tickets | Gold coat (x2) | Rainbow coat (x5) |
|---|---|---|---|
| Common | 1 | 2 | 5 |
| Rare | 2 | 4 | 10 |
| Epic | 4 | 8 | 20 |
| Legendary | 10 | 20 | 50 |
| Mythical | 25 | 50 | 125 |
| Secret | 60 | 120 | 300 |

- A small "+2 🎟" pops off the cat on the catch, under the money pop.
- A repeat cat pays the same as a new one, so tickets are the late-game reason to keep catching after the Index is done.
- Event days stack in one place only: a Cafe Event's money boost does not touch tickets. A once-a-day "Ticket Rush" hour gives x2 tickets. The rush turns on at the first catch after the daily reset and shows in the event strip.
- Pace (GE check): a Tier 9 player catches about 40 to 60 cats an hour, mostly Common to Epic, so about 200 tickets an hour.

### 1.3 The shelf
Two tabs, 4 cards per row, the same layout as the Day Cart.

**Prizes (always there)**
| Prize | Tickets | Limit |
|---|---|---|
| 25 golden fish | 300 | 4 a day |
| Trait Token | 700 | 3 a week |
| Golden Crate | 900 | 2 a day |
| Big Gold Rush Potion (30 min) | 1,200 | none |
| Big Luck Potion (30 min) | 1,200 | none |
| Swift Paws (1 hour) | 800 | none |
| Booth Plush Cat (booth-only shop cat, Legendary, sits on a mini inner tube) | 8,000 | once |
| "Park Regular" chat title | after 10,000 tickets spent | once |

**This week (4 cards that change every Monday 00:00 UTC, countdown on the tab)**
Taken in turn from a pool of 12 Water Park items:
- Decor (+4% to +8% money each, so six of them stay under the Grand Cafe pass and an R$99 pack): Flamingo Float, Splash Fountain, Ticket Arch, Wave Pool Tiles, Lifeguard Chair, Snack Hut. 1,500 to 3,000 each.
- Wearables (+5% money, one worn at a time, head or face only, never the neck): Snorkel Mask, Swim Cap, Sun Visor, Starfish Shades. 1,200 to 2,000 each.
- Toys (fun only): Water Squirter (sprays a harmless splash at nearby players) and Pool Noodle (bonks with a squeak). 2,000 each.
- An item bought once stays owned. When it comes back on the shelf it shows "Owned".

### 1.4 The booth UI
- Header: the ticket count, big, with the ticket icon. Then "Ticket Rush ready" or its time left.
- Every card: a picture, name, what it does in one line ("+25% money" or "25 🐟"), the price, and BUY.
- A card you can't afford keeps BUY greyed and shows a thin bar: "1,240 / 3,000".
- Limits sit as a small chip on the card ("2 left today").
- No pop-up confirm under 1,000 tickets. At 1,000 and over, BUY turns into "Tap again" for 3 seconds, like Unequip All.
- Phone: 2 per row under 700 px wide, 4 per row on PC (GridFit). Cocoa menu colours.

### 1.5 Station and look (Model-Agent)
- `CatCafe_Camp_WaterPark_TicketBooth`: a striped red and white kiosk about 8 studs wide, with a round ticket window and a big spinning ticket wheel sign on top.
  - The sign spins for looks only. There is no wheel to play.
  - Prize plushies hang inside the window.
  - It has a PromptAnchor at the window and a BangAnchor over the sign.
- The "!" shows while any prize is affordable and not at its limit.
- Picker line: "Ticket Booth: 3,240 🎟 · 2 prizes ready !".
- Sound: a ticket printer "brrrt" on BUY and a carnival ding on a big prize.

### 1.6 Saves and contracts (GE)
- `tickets` (number), `ticketSpent` (lifetime), `ticketLimits` { [prizeId]: { day, n } }, `ticketRushDay`.
- Remote `BuyTicketPrize(prizeId)`: the server checks the price, the limit, this week's shelf and ownership. Rate limited.
- Config: `TicketsPerRarity`, `TicketCoatMult` { gold = 2, rainbow = 5 }, `TicketRushMult` 2, `TicketPrizes`, `TicketWeekPool`.
- Behind LiveFlags `ticketBooth`.

---

## 2. Dragon Keep (Castle camp)

### 2.1 What it does
The Castle has a baby dragon, Cinder. Spare cats move into the Keep to keep him company, which gives him Warmth.
- Warmth grows him through 5 stages. His look changes at each stage, for you only.
- Each stage up plays a short cutscene and deals 3 perk cards. You keep one, and it fills a slot.
- At stage 5 he has 5 slots. More Warmth keeps dealing "Rekindle" hands: pick 1 of 3 new cards, then pick which slot it replaces.

Wording note (young audience): the game never says sacrifice or eat. Cats "move into the Keep" and you can see them there, napping on the gold pile around Cinder.

### 2.2 Warmth per cat (Derek's numbers)
| Cat | Warmth | Gold coat (x2) | Rainbow coat (x5) |
|---|---|---|---|
| Common | 1 | 2 | 5 |
| Rare | 2 | 4 | 10 |
| Epic | 4 | 8 | 20 |
| Legendary | 6 | 12 | 30 |
| Mythical | 10 | 20 | 50 |
| Secret | 25 | 50 | 125 |

Plus a trait bonus: +1 for a Rare to Epic trait and +3 for a Legendary or Mythic trait. A cat that holds a trait is worth a little more, never less.

### 2.3 Giving cats (safety)
- Picker: a grid of your cats, sorted weakest first, with a running total ("+46 Warmth").
- "Add all Commons" and "Add all repeats" quick buttons.
  - Both skip locked, working, gold, rainbow, Legendary and better cats, and the last copy of any cat.
- These are never offered:
  - locked cats (the F62 rule);
  - cats at the spa or in a trade;
  - your last cat of all (the #3123 rule).
- A working cat leaves its role, and Equip Best refills the slot.
- A gold, rainbow, Legendary, Mythical or Secret cat in the picked set asks once: "This includes 2 gold cats. Send them to the Keep?"
- A cat that moves in leaves the save for good, like a Museum donation. The Index keeps it as found.

### 2.4 Stages
| Stage | Name | Warmth total | Slots | His look (Model-Agent) |
|---|---|---|---|---|
| 1 | Hatchling | 50 | 1 | Small and round, pastel scales, curled on a cushion, an egg shell cap on his head |
| 2 | Whelp | 300 | 2 | Stubby wings, little horns, sits on a small coin pile and blows smoke rings |
| 3 | Drake | 1,000 | 3 | Twice the size, real wings, perched on the keep's wall, a glowing chest |
| 4 | Elder | 2,500 | 4 | Long neck, crown of horns, a gold pile in a jewelled heap, wings half spread |
| 5 | Crowned | 5,000 | 5 | Huge, a small gold crown and gem studded scales, circles the castle every few minutes |

- At stage 3 you also pick his scale colour from Ruby, Sapphire, Emerald or Amethyst. It's a look only, and you can change it later for free.
- Pace (GE check): at 2 hours a day, stage 5 takes about a week (10,000 would have been about a month).
- After stage 5, every 1,500 Warmth fills a Rekindle hand. Up to 3 hands can wait, so a player is never forced to pick at once.

### 2.5 Rank-up cutscene (Motion-FX, sound)
- About 7 seconds, skippable after 1 second.
  - The camera swings to the Keep.
  - The cats in the Keep cheer and Cinder curls into a glowing ember ball.
  - The ball cracks with light and he unfurls in his new look.
  - He gives a happy roar (cute, not scary) and a burst of warm sparks and confetti flames fills the yard.
- Stage 5 gets a 12 second version: he flies one lap of the castle, then lands on the tower with the crown glinting.
- Reduce Motion plays a 2 second fade with the new look and the roar.
- Then the card deal.
- Sounds:
  - a rumble build;
  - a roar per stage that grows deeper;
  - a chime as each card flips;
  - a bigger fanfare when a Legendary or Mythic card shows.
- Other players see a short glow over the Keep and "Sam's dragon is now a Drake!" in the feed. The name comes from the player's own display, never written to the repo.

**Motion-FX notes (23:30 UTC):**
- Build it on Rift Run's cutscene shell: letterbox bars, and every window and pop-up held until the card deal (the food bowl too). A hard cap and a watchdog always give back the camera and controls.
- Shots: the camera swings to the Keep in about 1.2 s, holds low on the dragon for the curl and the crack, then makes one slow push in on the new look. No cut is faster than about 0.8 s.
- The crack is one bright flash, not a flicker. Nothing flashes more than about once a second.
- The effects grow with each stage, like Rift Run's gates:
  - Stage 1: small sparks.
  - Stage 2: sparks and smoke rings.
  - Stage 3: adds an ember ring and a light column.
  - Stage 4: adds gold coins in the column.
  - Stage 5: adds the castle lap, flame confetti and the biggest roar.
- The cards flip one at a time, about 0.4 s each, on the Legendary word-ladder timing with rarity rings. Legendary and Mythic reuse the Mystic Pool's top tier burst.
- New sound cues for the sound pass:
  - rumble build;
  - five stage roars (each deeper);
  - card flip;
  - rare card fanfare;
  - Rekindle whoosh;
  - Ticket Booth printer and carnival ding.

### 2.6 The card deal
- 3 cards face down, then flip one by one. The card's edge colour is its rarity: Common grey, Rare blue, Epic purple, Legendary gold, Mythic rainbow.
- Tap a card to read it, then "Take this card". You must take one (a stage-up always gives a perk).
- A Rekindle hand has "Keep my cards" too, which gives 25 golden fish instead.
- A Rekindle pick then shows your 5 slots: tap the one to replace, or "Put in my binder". The replaced card goes to the binder (section 2.7a), and the new card shows "Replaces: Fire Trail".
- A card you already own (in a slot or the binder) is never dealt, so every hand holds new cards and the binder grows toward all 54. When every card of the rolled rarity is owned, that card rolls again at the shown odds among the rarities with cards left. Once all 54 are owned, a Rekindle hand gives 50 golden fish instead.
- The 3 cards in a hand are always different.
- Odds (shown under the cards, "Card odds"):

| Dragon stage | Common | Rare | Epic | Legendary | Mythic |
|---|---|---|---|---|---|
| 1 to 2 | 45 | 30 | 16 | 7 | 2 |
| 3 to 4 | 35 | 30 | 20 | 11 | 4 |
| 5 and Rekindle | 25 | 30 | 24 | 15 | 6 |

- Pity: a hand at stage 4 or later with no Epic or better turns its third card into an Epic.

### 2.7a Card binder (Derek 2026-11-13 23:54: "let the card have an inventory since set bonuses")
- Every card you take is kept for good in the binder. A card that's swapped out of a slot goes back to the binder, never away. The two cards you didn't pick from a hand are gone.
- At the Keep you can swap freely and at any time: tap a slotted card and a binder card to switch them. There's no cost and no cooldown, so building a set is a choice and never a gamble.
- Set bonuses count slotted cards only. The binder shows which family each card is in and how close each set is ("Flame 2/3 slotted").
- The binder lists cards by family, then rarity, with a count ("38 / 54 cards"). Cards you don't own show as dark outlines with their rarity edge, so the full pool is visible.

### 2.7 Families and sets
Every card belongs to one of six families: Flame (money), Claw (catching), Wing (moving), Hoard (fish and loot), Heart (cats and XP) and Crown (Mythic only, big ones).
- Holding 3 cards of one family lights a set bonus: Flame +5% money, Claw +3% net reach, Wing +1 stud/s, Hoard +5 golden fish a day, Heart +10% XP.
- The slots glow in the family's colour, so building a set feels like a deck.

### 2.8 The cards (54)
GE's caps (check 1): every card's money adds (never multiplies), with +50% total from cards and sets. Walk speed from cards and sets is at most +2 studs/s, and carry speed is never raised. Net reach is at most +5%. Nothing adds a staff slot, because the Extra Slot pass sells that.

**Flame (money)**
- C Warm Tips: +4% tips.
- C Toasty Tables: customers wait 10% longer before leaving.
- R Ember Tips: +8% tips.
- R Night Glow: +12% night income.
- R Hot Seats: one extra customer seat in your cafe.
- E Smoke Signal: rich visitors come 15% more often.
- E Dragon Coin: every 10th customer pays double.
- E Furnace: tip piles grow 20% faster.
- L Golden Breath: every 10 minutes Cinder breathes gold over your cafe, paying 1 minute of income.
- L Treasure Tax: +15% money from cats in staff slots.

**Claw (catching)**
- C Sharp Eye: +3% net reach (+5% total cap with the Claw set).
- C Quick Paws: catch circles move 5% slower.
- R Steady Claw: the first miss in each catch is forgiven.
- R Ember Net: nets swing 8% faster.
- R Bait Whisperer: bait lasts 15% longer.
- E Lucky Scale: +5% bowl luck, within the luck cap.
- E Double Catch: 4% chance a caught Common or Rare brings a friend (a second copy).
- E Glint Spotter: gold coats show a spark from further away.
- L Dragon Gaze: every 30 minutes, the next catch is guaranteed to land.
- L Gold Fever: +0.10 gold luck, within the gold cap.

**Wing (moving and fun)**
- C Light Step: +0.5 stud/s walk speed.
- C Soft Landing: no wait after a cannon landing.
- R Glide: hold jump to glide down slowly.
- R Fire Trail: your footsteps leave a warm ember trail (look only).
- R Quick Cannon: cannon travel is 30% faster.
- E Double Jump: jump once more in the air.
- E Sky Mail: claim your Tip Jar from anywhere.
- L Dragon Ride: once every 10 minutes, ride Cinder to any open area.
- L Wingbeat: +1.5 stud/s and a small gust that pushes nearby loose cats toward your net.

**Hoard (golden fish and loot)**
- C Shiny Pocket: +2 golden fish from each daily quest set.
- C Coin Sniffer: 5% chance a tip pile drops 1 golden fish.
- R Treasure Nose: Mystery gifts show on the map.
- R Hoarder: crates give 10% more coins.
- R Fish Scale: repeat Epic or better catches give +1 golden fish.
- E Gem Hoard: +15 golden fish at the first catch of each day.
- E Ticket Dragon: +25% Ticket Booth tickets.
- E Lucky Crate: 5% chance a crate opens twice.
- L Dragon's Hoard: every 4 hours Cinder leaves a hoard chest in the Keep (50 to 150 golden fish).
- L Rummage King: the Rummage Bin's best prize odds go up by a quarter (the odds shown at the bin update to match).

**Heart (cats and XP)**
- C Cosy Nap: resting cats gain 10% more XP.
- C Pat Pat: petting lasts 15 minutes longer.
- R Fast Learner: +10% cat XP.
- R Spa Day: Oasis Spa soaks take 45 minutes, not 60.
- R Happy Crew: staff cats start the day at full mood.
- E Kindred: cats in the Keep add +0.1% money each, up to +10%.
- E Trait Spark: the first Mystic Pool roll each day is free.
- E Big Heart: the first cat in each role earns +10% (no extra slot).
- L Dragon Bond: your best cat wears a little dragon wing look and earns +25%.
- L Elder Lore: Fusion Observatory fusions take 25% less time.

**Crown (Mythic only)**
- M Crown of Embers: +20% money, and the crown shows over your cafe sign.
- M Skyfire: every 60 minutes a meteor of golden fish (20 to 40) lands in your area. Only you can pick it up.
- M Royal Decree: once a day, choose one cat rarity to give double Warmth and tickets for an hour.
- M Dragon Heart: +1 Rekindle hand every 24 hours at stage 5.
- M Mythic Roar: once an hour, roar to stun every loose cat near you for 3 seconds (an easy catch).

That's 54: Flame 10, Claw 10, Wing 9, Hoard 10, Heart 10, Crown 5.
By rarity: Common 11, Rare 16, Epic 13, Legendary 9, Mythic 5.

### 2.9 Keep UI
- The left side shows Cinder's portrait at his current stage, the Warmth bar to the next stage ("1,240 / 1,500") and a "Give cats" button.
- The right side shows his slots as 5 card frames, with empty ones locked and showing the stage that opens them. Under them sits the set bonus line.
- Rekindle hands waiting: a gold "!" chip "2 hands ready".
- A Binder tab beside the slots: the card grid from section 2.7a, 4 per row on PC and 3 on a phone. Tap a binder card, then a slot, to swap them.
- Phone: the portrait above and the slots in one row of small cards. Tap a card for its full text.

### 2.10 Station and look (Model-Agent)
- `CatCafe_Camp_Castle_DragonKeep`: a round stone keep yard about 14 studs across, with a gate arch, a gold pile in the middle and torches.
- Five dragon models, one per stage, drawn on the owner's client. Other players see a generic sleeping Hatchling.
  - All five share the same Motor6D names (Root, Neck, Head, Jaw, WingL, WingR, Tail1 to 3, four legs), so one animation set plays on every stage. Hatchling and Whelp leave out the joints they don't use.
  - Each stays under about 4k tris and 120 parts.
  - Scale colours are a Color swap on the _Scale parts.
  - The Crowned flight is one looping path tween on the owner's client (Model-Agent, 23:31 UTC).
- The cats that moved in nap around the pile. The owner sees up to 12, picked from their rarest.
- "!" shows while a hand waits, or while the player has a "repeat" spare that can be given.
- Picker line: "Dragon Keep: Drake · 1 hand ready !".

### 2.11 Saves and contracts (GE)
- `dragon` = { warmth, stage, cards = { [slot]: cardId }, binder = { [cardId]: true }, hands = n, colour, dealt = { cardIds }? }. The binder holds every card taken; slotted cards are in it too.
- Remotes:
  - `GiveToKeep({ catUids })`: the server checks each cat with the rules in section 2.3.
  - `PickDragonCard(index, slot?)`: with no slot, the card goes to the binder.
  - `SlotDragonCard(cardId, slot)`: a binder card into a slot, and the card that was there back to the binder. Rate limited.
  - `KeepCards()`.
- The server makes every deal, saves it before showing it, and keeps the same hand on rejoin, so leaving can't reroll it.
- Config: `DragonWarmth`, `DragonCoatMult`, `DragonStages`, `DragonRekindle` 1,500, `DragonHandCap` 3, `DragonCardOdds`, `DragonCards`.
- Behind LiveFlags `dragonKeep`.

---

## 3. Golden fish link (#4055)
- Both stations hand out more golden fish late, as Derek asked:
  - the Ticket Booth's 25 fish prize (up to 100 a day);
  - the Hoard cards;
  - Skyfire;
  - 25 fish for keeping your cards on a Rekindle.
- The #4055 plan sets the full fish prices and other rewards.

## 4. Open questions for Derek (with my picks)
1. Dragon name Cinder? (pick: yes)
2. Booth Plush Cat at 8,000 tickets, about 40 hours of catching? (pick: yes)
3. Should other players see your dragon's real stage? (pick: no for now. One shared model keeps phones fast. Revisit later.)

## 5. Build notes from the other threads (2026-11-14)
- **Model-Agent, Ticket Booth models (PR #4082):**
  - Kiosk `CatCafe_Camp_WaterPark_TicketBooth`, with the child Model `_Sign_Spin` and the attachments PromptAnchor and BangAnchor.
  - Wearables: `CatCafe_Accessory_SnorkelMask` and `_StarfishShades` (Glasses spot), `_SwimCap` and `_SunVisor` (Hat spot).
  - Decor: `CatCafe_Decor_FlamingoFloat`, `_SplashFountain`, `_TicketArch`, `_WavePoolTiles`, `_LifeguardChair`, `_SnackHut`.
  - The toys are cards only; no models.
  - Shelf art: `Model-Agent/areas/next-three-2026-11-13/ticket-booth/ticket-booth-shelf-items.png`.
- **Model-Agent, Dragon Keep models:** PR #4081.
- **Motion-FX, card flips (PR #4083, Effects/CardFlip):**
  - Each card is a GuiObject with two filling children: `Back` (shown first) and `Front` (hidden first).
  - Call `CardFlip.deal(cards, rarities, onFlip, onDone)` with rarities from "common" to "mythic". It flips one card every 0.42 s and returns a stop function.
  - It adds the UIStroke `RarityEdge` on Front, so don't put a UIStroke of your own on Front.
  - It adds the UIScale `FlipScale`. Keep each card's Size fixed.
  - Legendary and Mythic cards get rays behind them, so the deal's ScreenGui needs DisplayOrder 1 or higher.
  - Enable a card's tap in `onFlip(i)`.
