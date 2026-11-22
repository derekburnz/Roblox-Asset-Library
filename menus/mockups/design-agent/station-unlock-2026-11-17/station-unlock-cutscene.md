# Station unlock cutscene on rank up (Design-Agent, 2026-11-17 15:30 UTC)

Derek, 15:17 UTC: when a rank up unlocks an important station, cut to where it stands, play an appear animation with VFX and "Unlocked", then cut back. Only for the tiers that unlock important things. Priority: after the Rank Up tutorial work.

## What each tier unlocks today (code, main)
| Tier | Area | Station (perk) | Other |
|---|---|---|---|
| 2 | Park | Picnic Basket (Fresh Bait) | Harvest portal during the event |
| 3 | Neighbourhood | Yard Sale (Haggler) | Trading (the Trade tile already has its lock-falling animation, #4280) |
| 4 | Woods | Fish Pond (Lucky Line) | |
| 5 | Sewer | Lost and Found (Homing Bell) | quicker Common and Rare rings |
| 6 | Desert | Oasis Spa (Warm Paws) | |
| 7 | Ruins | Relic Museum (Curator) | |
| 8 | Snowy Mountain | Cocoa Stand (Cocoa Break) | **Fusion Observatory** (rainbow cats) |
| 9 | Water Park | **Ticket Booth** (Ticket Stubs) | |
| 10 | Medieval Castle | **Dragon Keep** (Dragon Warmth) | |

There are no tier-locked stations in the Town Square. The Mystic Pool (traits) stands there and is open from Tier 1, so Derek's "Tier 4 trait" example has no unlock to show. Each station stands at its own area's camp. Today a gold beam and sparkle burst play the first time you walk into that camp (Effects/StationReveal), followed by the Unlocked card.

## Which tiers get the cutscene
Tiers 8, 9 and 10 (Fusion Observatory, Ticket Booth, Dragon Keep). They are whole new things to do, not a small perk.
- Not Tier 2. The first rank up already moves the player into the Park, and the path to Rank Up and the Park is the top priority. A 4 s cut there costs funnel time.
- Not Tiers 3 to 7. Their perk stations keep the first-visit burst and card. Tier 3's Trade unlock keeps its own lock animation.
- The tier list is one table (`StationCut.TIERS`), so we can add a tier later without code.

## The moment
1. **Trigger:** right after RANK UP is pressed for tier 8, 9 or 10, once per account. Save the tipsSeen id `station_cut_<tier>`. It plays before any card that follows the rank up (perk card, Cafe grew line), and those wait for it.
2. **Stream first:** the client asks for the station's spot (RequestStreamAroundAsync on the server, as the cannon does). Wait up to 2 s. If it is not in by then, skip the cut and show only the Unlocked card.
3. **Cut, about 4.5 s, skippable with one tap, click or gamepad button:**
   - 0.0 s: quick fade to the station, with the camera on a slow push in from 3/4 front.
   - 0.4 s: the station appears. It scales up from 0.85 with a gold beam rising, sparkles and two rings at its foot (reuse StationReveal's burst, made bigger).
   - 1.2 s: a big "UNLOCKED!" label with the station's name and one line under it, for example "Fusion Observatory: fuse 5 gold Mythicals into a rainbow cat".
   - 4.0 s: quick fade back to the player. Control returns at once.
4. **Rules:** no black bars on phones (Derek #4366). It is never mid catch, carry or flight. Reduce Motion gives a cut with no push in and no scale, only the sparkles. Low performance halves the particles. Sound: Sound's station fanfare on the reveal.
5. Because the cut already showed the station, the first walk into that camp shows only the burst, not the card a second time.

## Owners
- **Gameplay-Engineer:** the trigger after the rank up, the stream request, the once-per-account save id, holding the following cards, and the switch `stationCut` (OFF_BY_DEFAULT).
- **Motion-FX:** the camera path, the appear animation and VFX, the label, skip and Reduce Motion.
- **Review-QA:** a Tier 7 to 8, 8 to 9 and 9 to 10 dev save on phone and PC: plays once, the skip works, a missing stream falls back to the card, and nothing stacks.
- **Telemetry:** `station_cut` with the tier and an outcome of watched, skipped or fallback.

## Correction and addition, 15:40 UTC (Derek's Town Square ask)
The Town Square does have tier-locked stations. Since #4539 (closed Nov 15, switch `stationTiers` on), StationTiers hides each of these until its tier: the Mystery Market until Tier 2, the Cat Arcade until Tier 3 and the Mystic Pool until Tier 4. Since #4680 they show no sign or "!" while locked. Derek's Tier 4 trait example is right.
- Add Tier 3 (Cat Arcade) and Tier 4 (Mystic Pool) to `StationCut.TIERS`. They are in the Town Square, so the cut has to pan across and needs no area stream.
- Tier 2 (Mystery Market) gets no cut, so the first rank up into the Park stays fast. It gets the gold burst and the Unlocked card the first time the player is back in the Town Square.
- Codes: codes already need Tier 2 (Codes.MIN_TIER, Derek Nov 15), but the Codes Cat stand still shows at Tier 1. Add `CodesCat = 2` to StationTiers.BY_TAG so the stand is hidden until Tier 2 like the others. It gets no cut, only the Tier 2 burst with the Market.
