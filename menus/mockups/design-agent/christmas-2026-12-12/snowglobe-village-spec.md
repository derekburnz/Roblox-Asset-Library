# Snowglobe Village, the Christmas Event (Design-Agent spec v1, Nov 18 2026)

Derek, Nov 18 16:47 to 16:48 UTC: Harvest Hollow goes in the vault, and the Christmas Event starts earlier, on **Dec 1**. It ends Sun Jan 3 as before. The pitch it grows from is christmas-pitch.md in this folder.

## 1. Dates and switch
- Opens **Tue Dec 1 2026 20:00 UTC (3 PM ET)**. Closes **Sun Jan 3 2027 23:59 UTC**. Both live in the event row, and the server's date check has the last word.
- Kill switch `christmasEvent` (LiveFlags, off by default). It goes on after Sync's look, before Dec 1. The dates then open it on time with no restart.
- Portal at **Tier 2**, same as Harvest Hollow.

## 2. Code shape (GE)
A generalised EventArea: one config row per event (id, dates, tier, portal tag, cats, stall, currency, daily gift). Harvest Hollow becomes a vaulted row. Snowglobe Village is the second row, and Cherry Blossom Grove (Mar 27) will be the third. The save gets a field with a version bump, and Harvest saves keep working.

## 3. The area
You walk into the giant snow globe in Town Square (the portal) and land in a tiny snowy village inside it. It has:
- a log lodge with the StoneFireplace inside and a FiresideRug
- a lit tree in the square
- the Gift Stall
- three or four backdrop cottages
- gentle snowfall
- a curved glass sky at the edge, so you can tell you are inside the globe

The **Snowflake patch** works like the pumpkin patch: 12 shared spots of glowing snowflakes on the ground, picked by walking over them. It regrows on Harvest's timings. The currency is **Snowflakes**. Catches give Snowflakes on Harvest's numbers. The day's first visit gives 40.

## 4. The 8 Christmas cats (same rarity shape as Harvest: 2 Common, 3 Rare, 1 Epic, 1 Legendary, 1 Mythical)
Kept forever. They earn like Harvest cats do (two rarities lower in the owner's newest area, never below Common). They count toward no Index page, total, track or reward. Gold and rainbow coats work as for Harvest.

| id | Name | Rarity | Role | Pattern | Base colour | Look notes for Model | Line |
|---|---|---|---|---|---|---|---|
| gingerbread | Gingerbread | Common | greeter | stripes | 190,120,70 | white icing stripes on the paws and a white icing smile line | Always has a little icing on its nose. |
| snowball | Snowball | Common | waiter | solid | 245,245,250 | extra fluffy, round body, light blue inner ears | Rolls in fresh snow and comes back twice as fluffy. |
| candy_cane | Candy Cane | Rare | entertainer | stripes | 225,55,60 | white stripes on red, a curled tail tip | Red and white all over, with a sweet tooth to match. |
| tinsel | Tinsel | Rare | barista | spots | 200,205,220 | silver with small sparkly spots | Shimmers silver whenever it moves. |
| jingle | Jingle | Rare | greeter | patches | 70,125,80 | green with cream patches and a small gold bell on a red collar | The bell on its collar rings hello. |
| mistletoe | Mistletoe | Epic | waiter | patches | 85,145,85 | deep green with white berry dots and a sprig behind one ear | Waits under every doorway for a nose boop. |
| sugar_plum | Sugar Plum | Legendary | entertainer | gradient | 140,70,150 | purple to pink gradient, sugar sparkle on the tail | Dances on its toes, light as sugar. |
| star_topper | Star Topper | Mythical | greeter | gradient | 250,210,90 | gold to deep blue night gradient, a small gold star that floats above its head and glows at night | Sits on top of the tree and glows all night long. |

Teasers show **dark shapes only** (the secret cats rule). The banner's Hot Chocolate, Elf, Snow Boots and Flurry stay Snowy Peak cats.

## 5. The Gift Stall (8 items, fixed prices in Snowflakes, nothing random, nothing for Robux)
| id | Kind | Name | Price |
|---|---|---|---|
| santa_hat | outfit (Outfit_Hat) | Santa Hat | 150 |
| reindeer_antlers | outfit (Outfit_Hat) | Reindeer Antlers | 200 |
| knit_beanie | outfit (Outfit_Hat) | Knit Beanie | 250 |
| present_pile | decor | Present Pile | 150 |
| snowman | decor | Snowman | 200 |
| gingerbread_house | decor | Gingerbread House | 250 |
| stocking_wall | decor | Stocking Wall | 250 |
| little_tree | decor | Little Lit Tree | 350 |
TOTAL 1,800. That is about 25% more than Harvest's 1,440, over a 34-day window instead of 12, so a casual player who visits on about 8 days gets everything. If Model is short on time, the cut order is: decor becomes recolours of existing props, then fewer cottages, then the portal reuses the GiantSnowGlobe with a glow.

## 6. Schedule (everything published and switched on well before Dec 1)
| By | What | Who |
|---|---|---|
| Wed Nov 18 | This spec | Design |
| Fri Nov 20 | 8 cat models merged | Model |
| Sat Nov 21 | Dark-shape teaser picture for the Mon Nov 23 post | Model, Growth |
| Mon Nov 23 | EventArea generalised (no player change, Harvest specs green) | GE |
| Tue Nov 24 | Village, portal and stall models merged | Model |
| Wed Nov 25 | Snowglobe row, patch, stall, save field behind christmasEvent | GE |
| Wed Nov 25 | Portal, snowfall, night glow, cat idles, stall sparkle | Motion-FX |
| Thu Nov 26 | Review-QA pass, publish with the switch off | Review-QA |
| Fri Nov 27 to Sat Nov 28 | Sync's phone and PC look with a test date override, fixes | Sync, all |
| Sun Nov 29 | Switch christmasEvent on (the dates still hold it closed until Dec 1 20:00 UTC) | GE |
| Tue Dec 1 19:55 / 20:00 UTC | Shout, launch post, code SNOWGLOBE, admin events | Growth |
Spare days are Sun Nov 29 and Mon Nov 30, for slips only.

## 7. Checks
- Fresh Tier 2 account: the portal shows, entering lands in the village, the patch and stall work and a Christmas cat can be caught and kept.
- Tier 1: the portal says "Opens at Tier 2".
- Before Dec 1 20:00 UTC: the portal is closed with a countdown. After Jan 3: it is closed, and cats and items are kept.
- Phone: stall window fits; the snowfall stays within the phone FX budget.
- Harvest Hollow save data untouched.
