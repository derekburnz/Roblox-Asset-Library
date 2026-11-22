# One Secret cat per area, and a Secret tab in the Index

Derek, 2026-11-14 15:02 UTC: "secrets are not locked to area btw but maybe they should be changed so that there is a separate secret tab of the index and make one secret per area so 10 total (7 more because i believe there is 3)".

Picture: Design-Agent/secret-per-area-2026-11-14/secret-index-tab-mockup.png (phone landscape, the Secret tab with 3 of 10 found; found cards use a stand-in shape, not the cats' real looks).

## 1. What is in the game now (checked in code on main)

- 3 Secret cats exist: Nebula, Glitch and Cafe Ghost (`Catalog.secretCats`). Derek's count is right.
- None belongs to an area. Any rolled Mythical (wild stray, bait bowl or rescue trap) turns Secret 1 time in 100 while the `secretCats` switch is on, and the Secret is picked evenly from all 3 (`Catching.secret`).
- The Index has no Secret tab. A small Secret page appears at the end of the Cats, Gold and Rainbow tabs once a player has found one, listing only the ones found, with no total.

## 2. The change

**One Secret per area, 10 in all.** Each area's Secret only comes from that area. The odds stay exactly as now: a rolled Mythical turns Secret 1 time in 100, so no shown odds change and no bait card needs a new line.

| Area | Tier | Secret (Model-Agent's draft names, can change) |
|---|---|---|
| Alleyway | 1 | Cafe Ghost (exists) |
| Park | 2 | Lucky Clover (new) |
| Neighbourhood | 3 | Glitch (exists) |
| Woods | 4 | Moonstag (new) |
| Sewer | 5 | Ooze (new) |
| Desert | 6 | Djinn (new) |
| Ruins | 7 | Phoenix (new) |
| Snowy Mountain | 8 | Nebula (exists) |
| Water Park | 9 | Abyss (new) |
| Medieval Castle | 10 | Excalipurr (new) |

**Where each one comes from.**
- Wild stray: a Mythical rolled in an area turns into that area's Secret.
- Rescue trap: the trap's area's Secret.
- Bait bowl: the bowl already picks evenly among every area the player's tier opens, so its Secret is picked evenly among those areas' Secrets. A Tier 1 player can only get Cafe Ghost; a Tier 10 player can get any of the 10.
- Admin Secret Hunt (#4197): each hidden cat is the Secret of the area it hides in.
- A new Secret only rolls once its model is in the game. Until then its area keeps rolling a Mythical as before, so the 7 new ones can switch on one at a time.

**Players who already own one.** Nothing is taken away. An owned Nebula stays Nebula and now counts as the Snowy Mountain Secret, even if the player has not reached Tier 8.

## 3. The Secret tab

- A fourth tab, "Secret", after Cats, Gold and Rainbow, in the starlight colours (#16161D with the pale starlight #E2D6FF), shown to everyone while the `secretCats` switch is on.
- The old Secret page at the end of the other three tabs goes away.
- One card per area in tier order, 5 across on PC and phone landscape (2 rows), scrolling on a narrow phone.
  - **Found:** the cat's real look and name on a dark starry card, with a small gold or rainbow dot if the player has it in that coat.
  - **Not found, area open:** a black filled shape and "???" (the Index's normal "not found" look).
  - **Area not open yet:** the dimmed card with "Tier 9", like a locked area on the Cats tab.
- The header says "One Secret cat hides in every area. Not counted in the Index." and "3 / 10 found".
- Showing the total is new (until now the book never said how many exist). With one per area the number is no secret, and an empty slot per area gives players a goal. Recommended.
- The tab counts toward no Index total, track or reward, as now. The Collector and the Relic Museum still never ask for a Secret.
- Until a new Secret's model lands, its area's card shows "Coming soon" instead of "???". All 10 areas always show and the total stays 10.

## 4. Dark-shape rule (unchanged)

Outside the game (ads, thumbnails, event cards, group posts, store art) Secret cats only ever appear as dark shapes, the new 7 included. Model-Agent's sheet of the 10 is for Derek only. In the game the Secret tab shows the real look only for a cat the player has found.

## 5. Who does what

- **Model-Agent:** the 7 new cat models with gold and rainbow coats, two props and lit parts each like Nebula and Glitch, concept sheet first for Derek (already started on this roster).
- **Gameplay-Engineer (server):** a `secretArea` on each Secret cat in Catalog; `Catching.secret` takes the area (wild, rescue) or the bait's open areas; a Secret only rolls when its model exists; save is unchanged (owned Secrets keep their ids).
- **Design-Agent (UI):** the Secret tab in the Index (IndexBook and the Index screen), the starlight tab style and a gate scene on phone and PC.
- **Secret Hunt:** Design-Agent switches the hunt's cats to the area's own Secret once the server change lands.

## 6. Timing

Derek 15:12 UTC Nov 14: its own update event, scheduled after the 3 new areas (Growth-Agent sends the date). Not in Sunday's build. Everything sits behind its own LiveFlag switch `secretAreas`, off by default; off means Secrets work exactly as now. Order: server change and the Secret tab first (they work with the 3 that exist, Cafe Ghost in Alleyway, Glitch in Neighbourhood, Nebula in Snowy Mountain), then each new cat switches on as its model lands.

## 7. Open choice for Derek

1. Show "3 / 10 found" and an empty slot per area (recommended), or keep the old rule of never showing how many exist.
