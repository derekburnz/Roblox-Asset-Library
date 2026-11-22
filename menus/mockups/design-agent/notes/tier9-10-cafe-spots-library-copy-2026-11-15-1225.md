# Cafe work spots for Tier 9 (Water Park) and Tier 10 (Medieval Castle)

Status: Design pick, 2026-11-14, under Derek's global OK (he can change it). Asked by Model-Agent for #4066 and #4067.

Yes, both tiers add cafe work spots, the same way Tier 8 did (tier8-snowy-mountain.md section 1): two more slots a tier, so a new tier always has room for the new cats it brings.

| Tier | New spots | Roles after |
|---|---|---|
| 9 | `greeter_5`, `entertainer_5` | barista 5, greeter 5, waiter 7, entertainer 5 |
| 10 | `barista_6`, `entertainer_6` | barista 6, greeter 5, waiter 7, entertainer 6 |

The picks even out the roles, since waiter already has 7.

How it works:
- The pass pair stays the newest two spots, as at Tier 8. Saved cats never move.
- Snowy used the last free places in the room, so the four new spots need more floor. Model-Agent proposes an extension or an upstairs with a picture. The room stays uncluttered. The coordinator sends the picture to Derek.
- Gameplay-Engineer wires the slot counts per tier in Catalog and Config. The Espresso machine and Lucky Cat caps go up one level a tier, at about 2 to 3% of that tier's cost, as at Tier 8.
- The Pace check: Tier 9 and 10 times aren't set yet. When they are, the extra slots are counted in the income curve, so no tier comes early.
