# First 90 seconds and contextual tips (#5285 part E: E1 to E3), Design-Agent spec, Nov 18 2026

The video's point: D1 went from about 7% to 16% after one fix, removing the progression wall at minute 5 to 10. Teach only the core loop up front. Everything else is taught the first time the player needs it. Players still tap every step themselves (Derek's Nov 18 rule).

## E1. Only the core loop in the first 90 s (switch `needTips`, off by default)
**The first 90 s stay as they are now:** bowl cat, then cannon, then the first net catch, then check-in, then Rank Up to Tier 2 (about 75 s on phone). That already is the core loop: catch, earn, rank up.

**Moved out of the first 90 s:**
- **Cat Companion scene (#5290):** it waits for the first Park check-in, or 3 minutes into the session, whichever comes first. It is never right after the Tier 2 Rank Up, where it would sit between the player and the Park.
- **nextGoalBeat card:** stays after the first Park catch, which already fits.
- **Store, Notify Me and like asks:** stay past 6 min (promptsAfter5, likeAskEarly at the first Park or Rare catch).

**New contextual tips.** Each one shows once per account, through the Tips ledger (Tips.cleared keeps them). Each is a soft pulse ring with a one-line caption on the HUD button, with no dim and no window opened. It goes away when tapped or after 6 s, and never shows over a catch, cutscene, flight, carry or window.

| Trigger (first time it is true) | Pulse on | Caption |
|---|---|---|
| Coins reach the cheapest Upgrades row that raises income or catching (Net, tables, a station) | Upgrades | "You can afford an upgrade!" |
| Every cafe seat is full for 10 s | Upgrades, then the Tables row ringed inside if they open it | "Cafe full! More tables, more coins" |
| A bowl is empty, the player has food, and they are within 40 studs of the bowl | Bait bowl ring in the world | "Fill your bowl for a free cat" |
| A new rarity's first cat is caught (first Rare, Epic and so on) | Cats | "New best cat! See it in Cats" |
| The second Rank Up need is met (cats or rarity) but coins are short | Goal card coins line glows | "Catch more to earn the rest" (points to earning, as the Rank Up Go does) |
| Trading unlocks (Tier 3) | Trade tile pop only, as today (#5217) | (no caption) |

**Rules:**
- At most one tip a minute, and none in the first 90 s.
- With the switch off, nothing changes.
- The existing dim plus arrow steps before Tier 2 (tameCannonPoint, firstRankLock and rankSpotPlain) stay. They are the core loop.
- Read: the E5 milestone funnel (first upgrade bought, first table, second bowl cat, Tier 3), with the switch's on minute marked.

## E2. A wow first catch (switch `firstCatchWow`, client only, off by default; Motion-FX)
This plays only on the account's first net catch, at the moment the catch lands. It adds under 1.5 s, so it does not bring back dead time.
| Time | Beat |
|---|---|
| 0.0 s | 0.25 s slow-motion, and the camera pushes in 15% toward the cat |
| 0.25 s | A big pop: a ring burst twice the normal size, about 30 coins flying to the coin counter (3x normal), confetti in the Cozy Cream colours |
| 0.3 to 1.3 s | Banner "FIRST CATCH!" in the catch strip spot (not a card), plus a short bright sting (sound-designer: one cue, no louder than the Rank Up chime) |
| 1.3 s | The camera eases back and play goes on (carry to the safe zone) |
On low or phone graphics, the confetti count halves. The look is checked in the uigate scene "FirstCatchWow".

## E3. Nothing to pick or equip in the first session (switch `autoEquipFirst`, off by default)
On the account's first UTC day, anything earned or bought that is better than what is in use goes on by itself, with a small "Equipped!" toast:
- a new Net
- a better cat for a role (Equip best runs for them)
- the Cat Companion (auto-picked already in #5284)

Outfits and decor are cosmetic, so they stay the player's choice. After day 1 it goes back to normal.

## Not in this spec
- E4: Sync's timed fresh-account run. E5: the milestone funnel (Growth, GE). E6: the coin pack check (Growth). Design will cut the cost of the first step under 60% once E4 and E5 report.
