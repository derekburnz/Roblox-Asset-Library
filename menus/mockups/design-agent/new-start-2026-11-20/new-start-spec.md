# The new start: first three minutes, coin-only tiers and one tap Rank Up

Design-Agent, Nov 20 2026. Derek, 11:38 to 11:41 UTC: look into each funnel leak, "rework the entire start", "make it fun and interactive game for first 3 minutes and especially first minute", "lets not gatekeep behind cats lets make it just coin amount", "a quick easy rankup system", "no build it now we need a huge change", "drop the freeze".

Rules that still stand: players tap every step themselves, no menu or window opens by itself, every piece sits behind its own off switch, no new systems (reuse what is built), young audience, no dark patterns.

## 1. Why each step leaks today

Evidence is marked: (code) read in the source today, (data) from Growth's funnel reads, (guess) not proven.

| Leak Derek named | Cause | Fix in this spec |
|---|---|---|
| Bowl hint "not being seen" | Two things. (code) Since orderSplit went on at 03:10 UTC Nov 20, half of new players are in the catch first arm and never get the bowl line before their first catch (UIController only reports `tut_bowl_food` while bowl first runs). In onboarding_v9 a later step proves the earlier ones, so every catch first player who quits before swinging the net is counted as lost at bowl_hint_seen. The step now mixes two different starts and reads worse than it is. (data) Before the split it still lost 8 to 15%: the line only reports when the strip really draws, and the first minute bounce lands here. | A. No bowl line at the start at all. New funnel onboarding_v10 with one order. |
| 9% from bowl hint to bowl cat tamed | (code) The cut is already 2.7 to 3.0 s, so the animation is not the cost. The cost is the count of things to do: reach the bowl, open the Bait window, find Kibble, press Use, watch, press Tame, press the card's button. Six actions and a window before the player has done anything fun. (data) bowl_opened alone lost 7% before bowlOptionsButton. | C. The bowl cat is one tap: Tame. No window. |
| 12% at the cannon | (code) After the tame card the player must press the Cannon button, wait for the picker, find the ringed Launch and press it. Sync's stopwatch put that at 8 to 16 s. It is a menu step sitting between the player and their first catch. firstFlightDirect (straight flight, no picker) exists but was switched off Nov 18 because walking into the cannon ring flew the player without a tap. | B and E. The cannon is not in the first minute any more. The first flight is the Rank Up reward, started by one tap. |
| 8% from Alleyway landing to starting a catch | (data) Touch players lose 10% walking to the stray against 6% on PC; strayMeets helps but the player still lands, turns and walks. (guess) Some of it is the flight itself ending in a place with no instruction on screen for a second or two. | B. The first cat stands in front of the player at spawn. No walk. |
| 6% from Rank Up ready to clicked | (code) Ready, then the cue on the goal card, then the window, then RANK UP: two taps and a window. (data) 12.1% lost cue to shown after auto open went off, 2.3% with it on. rankSpotStay's read is not in yet. | D. Derek's idea as written: the goal card becomes the Rank Up button. One tap, no window. |
| 10% at Park arrive | (code) After the Rank Up: companion scene, then Cannon button, picker, Park Launch. Same menu chain as the first cannon, right after the best moment of the session. | E. The Rank Up celebration has one button, "Fly to the Park!". |
| Huge loss before Tier 3, many Park steps | (data) Phones lose 36% finishing the first Park catch against 12% on PC, and tier_3_ready lost 68% after park_catch while Tier 3 asked for kinds and 2 Rares. (code) A player can hold the coins and still be blocked by a cat need they cannot see how to meet. | F and G. The Park's first cat meets the player. Tiers ask coins only. |
| Intro cutscene | (data) Nov 11 read: loaded to first move took 27 s and lost 9% of players who loaded when the intro played by itself. v9 shows 1 to 4% lost at intro_done now that Skip is big. The bigger cost is time: up to 30 s of watching before any play. | A. `noIntro` on. Growth's skip numbers decide if it stays. |

## 2. The new first three minutes

Target times are from "loaded" on a phone. Every beat is a thing the player does.

| Time | Beat | What the player does | Reuses |
|---|---|---|---|
| 0 s | Spawn at the cafe's back door, net in hand, facing a Common stray 10 studs away that sits and looks at them. No intro, no strip of text longer than three words: "Catch the cat!" | nothing yet | noIntro, catch first order's stray, pointNet |
| 3 to 10 s | First catch: the catch button pulses with the arrow, one slow ring. A miss never loses the cat. FIRST CATCH! slow motion and coin burst. | 2 taps | quickFirstRings, missKeepsCommon, firstCatchWow |
| 10 to 20 s | Carry it through the door (a short trail, 10 studs). It takes a job by itself, a customer is at the table within 5 s and coins fly to the counter. "+400 First cat!" | walks 10 studs | EquipBest, check-in, coin fly |
| 20 to 35 s | A cat is already eating at the bowl outside the door (the server fills a new save's bowl once). A big Tame button floats over it. "+400 New friend!" | 1 tap | first bait cat, Tame card's pay |
| 35 to 60 s | Two cats work, coins tick up, the goal card shows a bar filling to 1,000. When it fills the card turns into a gold RANK UP button. | 1 tap | goal card, rankSpotStay's dim and arrow |
| 60 to 75 s | Rank Up celebration with one button: "Fly to the Park!" The cannon shot is the reward. | 1 tap | Rank Up cutscene, cannon flight, cannonAnywhere |
| 75 to 120 s | Land in the Park. A Park stray walks up to the landing. Catch it with the Alleyway's wide bands. "Catch 3 Park cats" 0/3 on the strip, each catch worth clearly more coins than the first. | catches | strayMeets, parkFirstEasy, missKeepsCommon |
| 2 to 3 min | Third Park catch: the "What next?" card, then the goal card fills to Tier 3 on coins alone. Companion scene plays here, not before the Park. | catches, 1 tap | nextGoalBeat, companionScene |

Taps before the first cat is caught: 2 (today about 8, with two windows). Windows opened in the first three minutes: 0.

## 3. The pieces, each behind its own off switch

**A. `noIntro` (exists, off).** Switch on. The intro stays on the ? tile. No build.

**B. `doorCatch` (new).** For a new save in its first session with no step done: everyone gets the catch first order, whatever orderSplit says (a save already in an arm keeps it; orderSplit goes off for new saves when this goes on). The waiting stray spawns as a Common at a point 10 studs from the spawn, on the player's side of the back door, and stays within 6 studs of it until caught. The player spawns facing it with the net out. Strip: "Catch the cat!". The Town Square cannon hint, tameCannonPoint and the Alleyway picker ring do not show at Tier 1. First check-in pays a one time 400 coins.

**C. `bowlGift` (new).** On a new save's first check-in the server puts one Kibble in the player's own bowl and its cat arrives in 3 s (the existing first bait path, no cut scene). A world button "Tame" sits over the cat, at least 48 px tall on touch. One tap tames it and pays a one time 400 coins. The Bait window is not opened and is not pointed at in the first session. The bowl is taught later by the existing empty bowl tip.

**D. `rankOneTap` (new), all tiers.** When the next tier is affordable the goal card becomes a gold RANK UP button in the same spot, with the cost on it. One tap ranks up; no Rank Up window opens. The first time, the dim and arrow from rankSpotStay sit on it. When it is not affordable the card shows one bar, coins of cost. The Rank Up window still exists from the menu for players who want the list of what a tier unlocks. A tap within 0.4 s of the card changing is ignored so nobody ranks up by accident.

**E. `rankFly` (new), all tiers that open an area.** The Rank Up celebration ends on one big button, "Fly to the <area>!", and a small "Stay here". The tap launches from wherever the player stands (cannonAnywhere), no picker. With this on, parkLead's dimmed picker and hoodTrail's ring are not shown for a player who pressed Fly. The companion scene waits for the first Park check-in.

**F. `parkMeets` (new, small).** strayMeets for the first Park catch: the nearest Common or Uncommon Park stray walks to 8 studs from the Park landing. Strip "Catch 3 Park cats" with a count.

**G. `coinsOnly` (new).** Every tier asks coins only: `distinctCats` 0, no `needsRarity`, laid on top of the rows in use through Catalog.setTierNeeds like CheapTiers. Costs: Tier 2 1,000 (1,500 now), Tiers 3 to 7 as tiersEasy has them (10,000, 60,000, 400,000, 3,000,000, 30,000,000), Tier 8 and up keep their coin costs. Cats still matter because better and more cats earn the coins faster; that is the only gate. The goal card, Rank Up card, return goals, Tier3Path and SecondCatHelp drop their cat lines when this is on. GE runs Pace before it goes on: Rank Up 1 ready at 45 to 75 s for the focused player, Tier 3 inside 6 minutes.

**H. Funnel `onboarding_v10` (new).** One order: joined, loaded, first_move, catch_prompt_shown, catch_started, first_catch, first_checkin, bowl_cat_tamed, rank_up_ready, rank_up_pressed, tier_2, fly_pressed, park_arrived, park_catch_started, park_catch, park_catch_3, tier_3_ready, tier_3, then the area steps as v9. Plus seconds from loaded to first_catch and to tier_2. Saves on the old start keep reporting v9.

## 4. Order of work

1. Today: `coinsOnly` and `rankOneTap` (they help every player, old start or new), and `noIntro` on.
2. Next: `doorCatch` with `bowlGift` and the v10 funnel, then `rankFly` and `parkMeets`.
3. Each piece: Review-QA, then Sync walks it on a 667x375 phone, then on in the same hour it publishes.
4. Read after 24 h on all new players: share reaching first_catch, median seconds to first_catch (target under 15), share reaching tier_2 (v9 window A was 47%), share reaching park_catch, playtime and D1.

## 5. Open points

- Tier costs with no cat needs are a first guess above Tier 7. Growth reads how fast players move once it is on.
- If the first minute is too fast to feel earned, raise Tier 2's cost before adding steps back.
- The old Alleyway camp stays as it is and is reached by cannon like any area; it is just no longer part of the walk-through.
