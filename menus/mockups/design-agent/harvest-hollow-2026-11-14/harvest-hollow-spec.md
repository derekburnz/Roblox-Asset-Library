# Harvest Hollow: spec (Derek OK'd 2026-11-14 17:55 UTC with changes)

Design-Agent, 2026-11-14 16:25 UTC, updated 18:05 UTC. Builds on Growth-Agent/copy-2026-11-14/harvest-hollow-area-plan.md (dates, 8 cats, featuring).

Dates OK by Derek 2026-11-14 18:04 UTC: Wed Nov 25 20:00 UTC (3 PM ET) to Sun Dec 6 23:59 UTC.

Derek's changes (17:55 UTC): opens at **Tier 2**; the pumpkin patch is **per server**; make it **obvious when something is only for points** and you don't get the cat; harvest cats **can be kept**, scaled to the player: each harvest rarity earns like the cat **two rarities lower in your newest area**, never below your newest area's Common (section 3b).

Kid-safe rules that hold throughout: everything is earned by play, no random roll for Robux, odds shown on every card that has them, a calm countdown only on the portal sign, nothing owned is taken away when the area closes.

## 1. Portal and sign (Town Square)

- A wooden arch of hay bales and pumpkins on the Town Square's open side, away from the middle and the Mystic Pool (Derek's "keep it uncluttered" rule for Town Square), with a short path of leaves leading to it.
- Sign over the arch: **HARVEST HOLLOW**, and under it a small line that changes:
  - before it opens: "Opens Wed 3 PM ET" (the player's local time where the sign can fill it),
  - while open: "Open until Sun Dec 6",
  - after: "Back next autumn" (the arch stays as decor, no walk-in).
- Walking through teleports into the area (no cannon). **Opens at Tier 2** (Derek): below it the arch is closed with a soft barrier and the sign's small line reads "Opens at Tier 2" (about 15 minutes of play for a new player).
- A HUD travel button "Harvest" (pumpkin icon) sits beside Home and Cannon while the area is open and the player is Tier 2 or higher, so phone players do not need to find the arch.

## 2. The area layout (notes for Model-Agent)

About the size of the Park. Golden hour light all day (the area keeps its own sky and the day and night cycle only dims it a little).

| Spot | What | Notes |
|---|---|---|
| Arrival | the bridge over the creek, a "Welcome to Harvest Hollow" board | spawn point faces the patch |
| Pumpkin Patch | 12 pumpkin spots in rows | the pickups (section 3) |
| Harvest Stall | a red-and-cream market stall | the shop (section 4) |
| Thankful Board | a big chalkboard with the Feast Pie | the shared goal (section 5) |
| Feast table | a long table under string lights | Great Cat Feast admin hour, Fri Nov 27 |
| Hay bale maze | small, about 8 x 8 bales | a hidden nook spawn point that only rolls Rare or better |
| Orchard and red barn | apple trees, barn with open doors | stray spawn points in both |

Strays: about 14 spawn points across the patch, orchard, barn and maze, spread so no two clump. Moving scenery (leaves falling, windmill turning, creek glints) follows the area-scenery naming rules.

## 3. Pumpkins (the area's own currency)

- **Patch (per server, Derek):** the 12 spots are shared by everyone in the server; touch one to pick it (+1 to you), and it regrows 90 seconds later. With 6 or more players in the area every spot regrows in 45 seconds, so a busy server is not a race. No pushing or stealing: a picked spot just shows a sprout and its regrow ring.
- **Catching:** every harvest cat caught gives pumpkins: Common +1, Rare +2, Epic +3, Legendary +5, Mythical +10.
- **First visit each day:** +10 at the arch.
- Target: an active player earns about 60 pumpkins an hour; everything on the Stall (section 4) costs about 480, so about 8 hours over the 12 days buys all of it. A player who drops in for 20 minutes a day still leaves with two outfits.
- Pumpkins stay in the save after the area closes (they come back next autumn with it), shown in the Bag, not on the HUD.

## 3b. Harvest cats: kept, scaled to you (Derek)

The 8 harvest cats (odds shown like every area): Common Hay Bale and Acorn Cap (key AcornCap: the Woods already has an Acorn); Rare Apple Pie, Cornstalk and Pumpkin Spice; Epic Cranberry; Legendary Maple Leaf; Mythical Harvest Moon. (Growth's draft had Uncommon, which the game does not have; those two move to Rare.)

Every harvest cat you catch is **yours to keep**. It earns like the cat **two rarities lower in your newest area**, and never less than your newest area's Common. It follows you: when you open a new area it earns like that area's cats.

| Harvest rarity | Earns like (in your newest area) |
|---|---|
| Mythical | Epic |
| Legendary | Rare |
| Epic | Common |
| Rare | Common |
| Common | Common |

Example: newest area the Woods, a Harvest Moon (Mythical) earns like a Woods Epic.

Where the player sees it: the catch card and the cat card say "Yours to keep · earns like a Woods Epic"; the Index's Harvest section shows the same line under each cat. Harvest cats count toward no Index total, track or reward (like the Secrets).

**Points only must be obvious (Derek):** anything that gives points and not the cat says so before you start. Nothing in Harvest Hollow is points only by default. If a mode ever is (for example a Great Cat Feast catch race), its strays wear an orange "Points only" tag instead of the rarity tag, its catch card reads "+3 pumpkins · cat not kept" in the same orange, and the mode's start toast says "Catch for points: these cats are not kept".

## 4. Harvest Stall (fixed prices, no random)

| Item | Kind | Pumpkins |
|---|---|---|
| Acorn Hat | outfit | 40 |
| Sunflower Hat (CatCafe_Accessory_SunflowerHat) | outfit, hat | 50 |
| Wheat Wreath (CatCafe_Accessory_WheatWreath) | outfit, hat | 60 |
| Pumpkin Hat | outfit | 70 |
| Feather Cap | outfit | 80 |
| Hay Bale Sofa (CatCafe_Decor_HayBaleSofa) | decor | 25 |
| Paw Pumpkin (CatCafe_Decor_PawPumpkin, glowing paw print) | decor | 30 |
| Apple Bushel (CatCafe_Decor_AppleBushel) | decor | 30 |
| Corn Sheaf | decor | 25 |
| Pie Counter | decor | 40 |
| Harvest Wreath | decor | 30 |

Total 480. One window, MenuFamily cocoa style, two tabs (Outfits, Decor), each card with the item's picture, name and a pumpkin price button; owned shows "Owned". No golden fish or Robux prices here. The optional Robux Harvest Outfit Pack stays a direct buy in the Store only (different outfits, never a pop-up).

Model-Agent changes (2026-11-15 01:58 UTC, PR #4375): Sunflower Hat replaces Autumn Scarf (wearables never sit on the neck) and Wheat Wreath replaces Leaf Crown (Season 1 already has an Autumn Leaf Crown); all five outfits are hats on the Outfit_Hat spot. Decor (PR #4378, renamed because Season 1 already has a Hay Bale Seat, a Pumpkin Lantern and an Apple Crate Shelf): CatCafe_Decor_HayBaleSofa, PawPumpkin, AppleBushel, CornSheaf, PieCounter, HarvestWreath, and the Feast Pie CatCafe_Decor_FeastPie.

## 5. Feast Pie (shared goal, all servers)

- The Thankful Board shows a giant pie that fills in eight slices. Each harvest cat caught in any server adds one.
- **Goal size:** **25,000** harvest cats (Growth-Agent 16:17 UTC: about 9,000 to 10,000 a day, so it fills by Sat Nov 28 evening, the reward hour). A server-read value (LiveFlags number or Config read live), not baked into the build, so it can be lowered on Thu Nov 26 after Growth's first-day read at 12:00 UTC.
- Slice marks at each eighth: a server-wide toast "The Feast Pie is 3/8 baked!" (no prize, just progress).
- When full: everyone who caught at least one harvest cat gets the **Feast Pie** decor and one Spin Wheel spin (pick 3 settled at the recommended "everyone who helped"), delivered at once (or at their next join), plus a Town Square firework moment. If it fills before Sat Nov 28 20:00 UTC the Saturday hour still runs as the party with the Admin Wheel.
- Real progress only: the number is never faked or pushed down.

## 6. Thankful Board

- Players pick one of six fixed thank-you notes ("Thank you, cats!", "Thanks for the pie!", ...) and pin it with their avatar; no typed text, so nothing needs filtering. The board shows the last 12 pinned in that server.

## 7. When it closes (Sun Dec 6 23:59 UTC)

- The arch shows "Back next autumn", the HUD button goes, the area's spawns stop. Cats, outfits, decor and pumpkins stay owned. The 8 harvest cats keep their own Index section marked "Back next autumn" and count toward no total, track or reward while away.

## 8. Who

- Design-Agent: this spec, the Stall and portal mockups on phone and PC, the HUD button, the Stall window, the pie board UI.
- Gameplay-Engineer: the date switch (LiveFlag plus start and end times), the Tier 2 gate, pumpkins in the save, per-server patch spots, the harvest cats' scaled earning (earns-like rarity from the owner's newest area), the shared goal across servers (MemoryStore), the Stall purchases.
- Model-Agent: area, arch, stall, board, 8 cats with gold and rainbow coats, 5 outfits, 6 decor pieces and the Feast Pie.
- Growth-Agent: event page with featuring by Mon Nov 16, the goal size from the first day, copy.

## 9. Picks

1. Patch: per server (Derek 17:55 UTC), with faster regrow in a busy area so it is not a race.
2. Pumpkin target about 8 hours for everything (recommended pick, settled under the global OK).
3. Feast Pie reward to everyone who helped (recommended pick, settled).
