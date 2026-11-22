# Cherry Blossom Grove: one week event area, cats and station (draft spec)

**MOVED 2026-11-17 (Derek 14:29 UTC):** now proposed for Sat Mar 27 2027 20:00 UTC to Sat Apr 3 2027 20:00 UTC, after a Christmas update. The Dec 5 dates below are old. See ../schedule-2026-11-17/cherry-move-and-christmas-slot.md.

Design-Agent, 2026-11-15 16:45 UTC. For issue #4386. Release placeholder: Sat Dec 5, 2026 (Derek 16:17 UTC). Nothing may be playable or visible in the game before then.

## Decided (Derek 2026-11-15 16:19 UTC: "do all 1 week long dec 5 start", no group announcement)

A limited event area like Harvest Hollow: **Sat Dec 5 20:00 UTC to Sat Dec 12 20:00 UTC**. No new tier.

## 1. How it works (same rules as Harvest Hollow)

- **Opens at Tier 2.** A portal arch on the Town Square's open side; below Tier 2 the arch's sign reads "Opens at Tier 2". A HUD travel button "Grove" (blossom icon) shows while the area is open and the player is Tier 2 or higher.
- **Cats are kept, scaled to you:** each Grove cat earns like the cat two rarities lower in your newest area, and never less than that area's Common (Harvest Hollow section 3b, same table). So a Tier 2 player and a Tier 10 player both get a cat worth having.
- **Nothing is taken away** when it closes. The arch stays as decor with "Back next spring".
- The sign before it opens reads "Opens Sat 3 PM ET"; while open "Open until Sat Dec 12".

## 2. The 10 Grove cats, plus one Secret

Each area has 4 Common, 2 Rare, 2 Epic, 1 Legendary and 1 Mythical, plus one Secret behind the secretAreas switch. The odds are the Castle's, with Mythical at 1.3.

| Rarity | Name | Look |
|---|---|---|
| Common | Sakura Cat | soft pink with white petal spots |
| Common | Bamboo Cat | green and cream stripes, a little leaf on one ear |
| Common | Koi Cat | white with orange and black patches like a koi |
| Common | Lantern Cat | warm red and gold, a tiny paper lantern on its tail |
| Rare | Matcha Cat | pale green, carries a tiny tea cup |
| Rare | Origami Cat | paper white with folded paper ears and a crane on its back |
| Epic | Bonsai Cat | moss green with a little bonsai tree growing from its back |
| Epic | Waterfall Cat | blue and silver gradient, mist around its paws |
| Legendary | Blossom Fox Cat | white with pink tail tips and a flower crown |
| Mythical | Petal Dragon Cat | a long pink and white dragon body, with blossoms falling as it moves |
| Secret | Moon Petal | a dark shape until caught, then deep blue with glowing petals (follows the Secret cats dark shape rule) |

Names and looks are our own, with no real brands or characters.

## 3. Station: the Wishing Tree

- A big blossom tree in the Grove with ribbons tied on it (Model-Agent's wishing tree model).
- Once a day the player ties a ribbon. They see three gifts face up and pick one: a Money potion, 25 golden fish, or a Lure. Nothing is random and nothing is for Robux, so it is kid safe and needs no odds.
- The walk-up ring opens it like the other camp stations. After picking, the tree shows "Come back tomorrow" with the time left.

## 4. Keeping it hidden until Dec 5

- An off-by-default switch `cherryGrove` (LiveFlags OFF_BY_DEFAULT). While it is off:
  - there is no cannon card,
  - the area set is not placed (it stays in ServerStorage),
  - no portal arch walk-in and no HUD Grove button,
  - no What's New row or banner shows.
- Dec 5 20:00 UTC: the switch goes on (no restart). After Dec 12 20:00 UTC the date gate closes the portal by itself.
- Model-Agent's PRs #4423 and #4446 stay on hold until the build starts (about Nov 30).

## 5. Build order (from about Nov 30)

1. Design: the cats in Catalog behind the switch, with the Harvest scaling, and the dates in the event schedule.
2. Model-Agent: the real set (#4423), the 11 cat models, the Wishing Tree, the arch and the HUD icon.
3. Gameplay-Engineer: the portal, the Wishing Tree server side and the switch and date gates (reuse Harvest Hollow's).
4. Motion-FX: the falling petals and waterfalls (#4446).
5. Growth: the event page and the countdown icons from Dec 4. No @everyone post for this one (Derek).

Idea for later, not part of this: a Tier 11 for players who reach Tier 10.
