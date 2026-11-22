# Tier 8: the Snowy Mountain (design draft 2)

Status: draft 2 by Design-Agent, 2026-11-13, for #3934. It now follows Model-Agent's plan that Derek approved at 18:54 UTC ("those look good only 10 per area for now"): [plan.md](../../Model-Agent/areas/next-three-2026-11-13/plan.md) and [cats-draft-2.png](../../Model-Agent/areas/next-three-2026-11-13/cats-draft-2.png). Where the two docs overlap (name, place, size, zones, traps, cats, Cocoa Stand), plan.md and what is built in #3999 and #4003 win. This doc only adds the tier numbers, stations, crate, Index prizes and the build checklist. Draft 1 (Frost Peak Cafe, Snowball, Yeti, Aurora and so on) is withdrawn.

## 1. The new tier (draft numbers; the Pace run sets the final ones)

| | Tier 7 (today) | Tier 8 (draft) |
|---|---|---|
| Cafe name | Wonder Cafe | **Summit Cafe** (plan.md) |
| Area | Ruins | Snowy Mountain (`snow`) |
| Cost | 54B | about 520B (the same step as Tier 6 to 7) |
| Different cats | 47 | 56 |
| Rarity need | 3 Mythical or better | 4 Mythical or better |
| Slots | 14 | 16 |
| Tier multiplier | 2.50 | 2.75 |
| Area income (`AREA_INCOME`) | 729 | 2187 (plan.md) |

- **Pace target:** Tier 8 comes about 12 to 15 h after Tier 7, in one sitting. The Tier 1 to 7 times stay as they are.
- **Slots and stations:** Tier 7's 14 slots plus the pass's 2 use all 16 role stations today. Tier 8 needs 2 more: `barista_5` and `greeter_4` open at Tier 8, and `waiter_7` and `entertainer_4` become the new pass-only pair. Saved cats never move. Model-Agent fits the four spots in `Layout.plot.spots` and keeps the room uncluttered.
- **Caps:** the Espresso machine and the Lucky Cat get one more level each (8), at about 2 to 3% of the Tier 8 cost.

## 2. Place and cannon (as built)

North-west of town, the one free direction, with the camp cannon guide aim at **-45°** (#4003). That keeps 45° to the Neighbourhood and the Woods, above the 38° minimum. The Theme Park and Water Park launches from the Desert camp and the Medieval Castle from the Ruins camp (plan.md §0); Gameplay-Engineer makes the final call. Cannon checks for Review-QA: the barrel is within 1° of the line to the pad, the flight lands on the Cocoa Lodge pad, the picker shows "(opens at Tier 8)" until then, and the camp cannon lists Town Square first.

## 3. The area (as built in #3999 and #4003)

150 wide by 560 deep, camp at the town end. Zones in order: **Cocoa Lodge camp**, **Pine Slopes**, **Frozen Lake**, **Ice Cave**, **Summit Peak** (flag, observatory dome, northern lights; the Mythical zone). Rescue traps: `snowdrift` (two), `snowman`, `sled` and `snow_log`. No grass anywhere, backdrop peaks at every edge, blockers at least 9 studs high. The lake's slide is a look only: walking stays the same. Snowfall particles stop under Reduce Motion and Low performance. Nothing cold or painful shows on the cats (no shivering), for the young audience.

## 4. The 10 cats (Derek approved, plan.md §1e)

| Rarity | Name | Role | Look |
|---|---|---|---|
| Common | Flurry | barista | Snow-white with pale grey ticking |
| Common | Mitten | waiter | Grey with four white mitten paws |
| Common | Hot Chocolate Cat | greeter | Cocoa brown, two marshmallow tufts, mug-shaped tail tip |
| Common | Spruce | entertainer | Brown tabby of the pine woods |
| Rare | Snow Boots Cat | greeter | Red bobble hat, four fur-topped snow boots |
| Rare | Ski Cat | waiter | Goggles up, striped scarf round its tail |
| Epic | Snow Leopard Cat | entertainer | Rosettes and a very thick tail |
| Epic | Ice Cat | barista | Clear ice-crystal spikes, frosted paws, soft frost shine |
| Legendary | White Tiger Cat | waiter | About 1.2x, snow-white with bold black stripes, ice-blue eyes |
| Mythical | Blizzard Cat | greeter | About 1.25x, a swirl of wind and snowflakes, glowing ice eyes, frost trail |

Draft ids (none clash with today's catalog): `flurry`, `mitten`, `hot_chocolate`, `spruce`, `snow_boots`, `ski`, `snow_leopard`, `ice`, `white_tiger`, `blizzard`. The scarf on Ski Cat sits round its tail, so the no-neck-props rule holds. The Blizzard swirl and the Ice Cat shine hold still under Reduce Motion. The optional Secret (Snow Spirit Cat) waits for Derek and follows the dark-shape rule. Model-Agent runs the model check on this roster as for the Desert and Ruins.

## 5. Its station: the Cocoa Stand (plan.md §1d)

At the camp, free every 2 hours. It gives **Warm Paws**: +10% money for 10 minutes. It does not stack with a money potion; while both run, only the bigger one counts. The stand says exactly what it gives and sells nothing. Menu: the batch 5 camp-extra layout, a picture of the stand on the left and "Warm Paws: +10% money for 10 min", "Next one in 1 h 42 m" and a green COLLECT on the right. It can reuse the Yard Sale's timer code.

## 6. Crate and Index (Design-Agent additions)

**Crate:** `snow` ("Snowy Crate") and `snow_golden_crate`, at `Config.CratePrice` (40), opening at Tier 8. Twelve cafe decor pieces (these are room decor, separate from Model-Agent's area props): 5 Common, 4 Rare, and one each of Epic, Legendary and Mythical. The odds show on the crate as every crate does.

| id | Name | Kind | Rarity |
|---|---|---|---|
| `snow_log_cabin` | Log Cabin | wallpaper | Common |
| `snow_knit_pattern` | Knit Pattern | wallpaper | Rare |
| `snow_pine_planks` | Pine Planks | floor | Common |
| `snow_aurora_ice` | Aurora Ice | floor | Mythical |
| `snow_frost_white` | Frost White | paint | Common |
| `snow_cocoa_brown` | Cocoa Brown | paint | Rare |
| `snow_fireside_rug` | Fireside Rug | furniture | Common |
| `snow_stone_fireplace` | Stone Fireplace | furniture | Legendary |
| `snow_sled_shelf` | Sled Shelf | decoration | Rare |
| `snow_snow_globe` | Giant Snow Globe | decoration | Epic |
| `snow_chalet_door` | Chalet Door | door | Common |
| `snow_igloo_flap` | Igloo Flap | catflap | Rare |

**Index prizes:** the Ruins' rows with coins at about 3 times (cats3: 810,000 coins and 25 fish, and so on). No `goldLuck`, since it is capped. `decor_snow` is like every decor page.

## 7. Everything else a new area touches

The checklist from tier6-7 §7: Catalog, Config.World, the Layout sets, WorldBuilder, Theme, Format, Demo, DecorPictures, Effects presets, PityAreaWeights (Snowy Mountain 45), the live event weights, the Rally steps, the rank-up screen, the leaderboards, and a stress run with 128 live strays across eight areas.
