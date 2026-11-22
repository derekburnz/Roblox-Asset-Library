# Cafe work spots for Tiers 8, 9 and 10

Status: Design pick, 2026-11-14 03:45 UTC, under Derek's global OK (he can change it). Revised to match Gameplay-Engineer's Tier 8 build. Derek picked wall perches for the new spots (02:28 UTC); Model-Agent's perch models are PR #4117.

One rule every tier: the old pass-only pair opens for everyone, and two new spots become the pass-only pair. A pass holder's cats never move, and every tier gives free players two more slots.

| Tier | Opens for everyone | New pass-only pair |
|---|---|---|
| 8 | `entertainer_3`, `waiter_6` | `barista_5`, `greeter_4` |
| 9 | `barista_5`, `greeter_4` | `waiter_7`, `entertainer_4` |
| 10 | `waiter_7`, `entertainer_4` | `greeter_5` (perch over the front door), `entertainer_5` (west wall perch) |

So Tier 10 uses two of the four perches. `barista_6` (back wall) and `entertainer_6` (east wall) stay built but unused, for Tier 11 and up.

- Gameplay-Engineer wires the slot counts per tier in Catalog and Config. The Espresso machine and Lucky Cat caps go up one level a tier, at about 2 to 3% of that tier's cost, as at Tier 8.
- Pace: count the extra slots in each tier's income curve so no tier comes early.
