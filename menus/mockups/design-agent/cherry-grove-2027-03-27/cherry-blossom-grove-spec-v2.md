# Cherry Blossom Grove, the spring event (Design-Agent spec v2, Nov 18 2026)

Replaces ../cherry-grove-2026-11-15/cherry-blossom-grove-spec.md (Dec 5 dates, its own code). Dates from Derek, Nov 17 14:29 UTC. This version sits on the same EventArea row as Snowglobe Village, so GE writes no new event code: it is the third row after Harvest Hollow (vaulted) and Snowglobe Village.

## 1. Dates and switch
- Opens **Sat Mar 27 2027 20:00 UTC (4 PM ET, daylight time)**. Closes **Sat Apr 3 2027 20:00 UTC**. Both live in the row, and the server's date check has the last word.
- Kill switch `cherryGrove` (LiveFlags, off by default). While it is off, nothing shows: no cannon card, no portal, no HUD Grove button, no What's New row or banner, and the set stays in ServerStorage.
- It goes on after Sync's look, about Mar 24. The dates then open it on time with no restart.
- Portal at **Tier 2**, like the other two events. Below Tier 2 the arch reads "Opens at Tier 2".
- No group post with @everyone for this one (Derek, Nov 15). A normal update post is fine.

## 2. The area
A portal arch of blossom branches on Town Square's open side. Through it is a valley of pink trees with a pagoda, a tea house, a koi pond and two waterfalls (Model's blockout #4423, 27k triangles, kept on its branch). Petals fall slowly (Motion-FX #4446, inside the phone FX budget).

The **Petal patch** works like the pumpkin and snowflake patches: 12 shared spots of glowing petal piles, picked by walking over them, on Harvest's regrow timings. The currency is **Petals**. Catches give Petals on Harvest's numbers. The day's first visit gives 40.

## 3. The 8 Grove cats (the event shape: 2 Common, 3 Rare, 1 Epic, 1 Legendary, 1 Mythical)
Kept forever. They earn like the other event cats (two rarities lower in the owner's newest area, never below Common), count toward no Index page, total, track or reward, and take gold and rainbow coats.

| id | Name | Rarity | Role | Pattern | Base colour | Look notes for Model | Line |
|---|---|---|---|---|---|---|---|
| sakura | Sakura | Common | greeter | spots | 245,190,205 | soft pink with white petal spots | Naps under the blossoms and wakes up covered in petals. |
| koi | Koi | Common | waiter | patches | 250,245,240 | white with orange and black patches like a koi fish | Sits by the pond all day and never gets wet. |
| matcha | Matcha | Rare | barista | solid | 170,200,140 | pale green, a tiny tea cup on its back | Makes the calmest cup of tea in town. |
| origami | Origami | Rare | entertainer | solid | 245,245,240 | paper white, folded paper ears, a paper crane on its back | Folds a paper crane for every new friend. |
| paper_lantern | Paper Lantern | Rare | greeter | gradient | 215,70,55 | warm red to gold, a tiny paper lantern on the tail tip that glows at night | Lights the path home after dark. |
| bonsai | Bonsai | Epic | waiter | patches | 95,130,80 | moss green with a small bonsai tree on its back | Grows a little taller every spring. |
| blossom_fox | Blossom Fox | Legendary | entertainer | gradient | 250,250,250 | white with pink tail tips and a flower crown | Its flower crown never wilts. |
| petal_dragon | Petal Dragon | Mythical | greeter | gradient | 245,170,200 | long pink and white body, blossoms fall behind it as it walks | Blossoms fall wherever it walks. |

Model names (Model #5339): every cat is CatCafe_Cat_<PascalCase id>, so paper_lantern is CatCafe_Cat_PaperLantern (the Sewer already has a Lantern cat, so the id and name are Paper Lantern). The stall tree is CatCafe_Decor_GroveBlossomTree (Decor_BlossomTree already exists).

Cut from v1 and saved for a later spring: Bamboo, Waterfall and the Secret Moon Petal. Teasers show dark shapes only (the secret cats rule).

## 4. The Blossom Stall (6 items, fixed prices in Petals, nothing random, nothing for Robux)
| id | Kind | Name | Price |
|---|---|---|---|
| flower_crown | outfit (Outfit_Hat) | Flower Crown | 100 |
| paper_lantern_hat | outfit (Outfit_Hat) | Lantern Hat | 150 |
| koi_pond | decor | Little Koi Pond | 150 |
| grove_blossom_tree | decor | Grove Blossom Tree | 200 |
| tea_set | decor | Tea Set | 150 |
| paper_lanterns | decor | Lantern String | 200 |
TOTAL 950. The window is 7 days, so a casual player who visits on about 5 days gets everything (Harvest: 1,440 over 12 days; Snowglobe: 1,800 over 34 days).

## 5. The Wishing Tree (the row's daily gift)
A big blossom tree with ribbons. Once a day the player ties a ribbon and picks one of three gifts shown face up: 1 h of earnings (5k floor, as Daily Treat v2), 5 spins or 3 Trait Tokens. Nothing random, nothing for Robux. After picking, the tree shows "Come back tomorrow" with the time left. Walk-up ring opens it, and the player taps the gift themselves.

## 6. Schedule (everything published and switched on before Mar 27)
| By | What | Who |
|---|---|---|
| Wed Nov 18 2026 | This spec | Design |
| Before Nov 25 2026 | The old Cherry entry leaves Config.UpdateEvents (#5098) | GE |
| Mon Mar 1 2027 | Merge main into #4423 and #4446, re-append the manifest and gates rows | Model, Motion-FX |
| Fri Mar 12 | 8 cat models merged | Model |
| Mon Mar 15 | Set, portal arch, stall, Wishing Tree and 6 item models merged | Model |
| Wed Mar 17 | Grove row, patch, stall, Wishing Tree and save field behind cherryGrove | GE |
| Wed Mar 17 | Petals, waterfalls, lantern glow at night, cat idles, stall sparkle | Motion-FX |
| Fri Mar 19 | Review-QA pass, publish with the switch off | Review-QA |
| Sat Mar 20 | Dark-shape teaser picture for the Mon Mar 22 post | Model, Growth |
| Mar 20 to Mar 23 | Sync's phone and PC look with a test date override, fixes | Sync, all |
| Wed Mar 24 | Switch cherryGrove on (the dates hold it closed until Mar 27 20:00 UTC) | GE |
| Sat Mar 27 19:55 / 20:00 UTC | Shout, update post, code BLOSSOM, admin events | Growth |
Spare days are Mar 25 and Mar 26, for slips only.

## 7. Checks
- Fresh Tier 2 account: the portal shows, entering lands in the Grove, the patch, stall and Wishing Tree work and a Grove cat can be caught and kept.
- Tier 1: the arch says "Opens at Tier 2".
- Before Mar 27 20:00 UTC: closed with a countdown. After Apr 3 20:00 UTC: closed, cats and items kept, the arch says "Back next spring".
- Phone: stall and Wishing Tree windows fit; petals and waterfalls stay inside the phone FX budget.
- Harvest and Snowglobe save data untouched.
