# catchCurve: one smooth catch difficulty curve (Nov 19)

Owner: Design-Agent spec, Gameplay-Engineer build. Switch: `catchCurve` (LiveFlags, off by default; on as soon as it publishes, no restart needed beyond Derek's).

## Why
Derek: "lower tier area mythics are harder then much higher tier mythics." Today the only area factor on windows is the Alleyway's catchWindowScale 1.2, and QuickRing only speeds Common and Rare from tier 5. Mythical rings are the same speed everywhere, so what changes is the net: a Net 0 player in a low area gets a Mythical good band of 0.11 x 0.68 = 0.075 s, while a Net 3 player late on gets 0.122 s plus Dragon Keep slow rings and potions. The net gap swamps the area gap.

## Rule (switch on)
Rarity keeps its own shrinkSeconds, catchWindow and trustNeed. Coat (CoatDifficulty), early, touch, tutorial, ParkFirstEasy, slowRings and potions all stay on top unchanged.

### 1. Band widths
half-width = base x N(net) x W(areaTier) x rarity catchWindow x coat x (early/touch/tutorial scales as today)

- base: perfect 0.06, good 0.14 (replaces Config.NetWindows while on)
- N(net) = 1 + 0.15 x netLevel (Net 0 1.00, Net 3 1.45, Net 5 1.75)
- W(areaTier), replaces catchWindowScale while on:

| Tier | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| W | 1.25 | 1.20 | 1.12 | 1.05 | 1.00 | 0.97 | 0.94 | 0.91 | 0.88 | 0.85 |

Checks: tier 1 Net 0 perfect/good 0.075/0.175 (today 0.054/0.132). Tier 10 Net 3 0.074/0.172 (today 0.08/0.18). Tier 1 Net 5 good x early 1.3 = 0.40 s, under CircleGapMin 0.55; clamp any band to 0.5 just in case.

### 2. Ring speed
shrink = shrinkSeconds x S(areaTier) x (1 + slow); replaces QuickRing while on (all rarities, not only Common and Rare).

| Tier | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| S | 1.15 | 1.10 | 1.05 | 1.00 | 0.975 | 0.95 | 0.925 | 0.90 | 0.875 | 0.85 |

Both W and S only fall with tier, so the same rarity is never easier in a higher area. Tiers 1 to 4 sit above today's feel so new players don't rage quit.

### 3. Mutations
Speed on top of today's window CoatDifficulty (gold 0.90, rainbow 0.80): shrink x 0.95 for gold, x 0.88 for rainbow. Add as Config.CoatSpeed.

### 4. Heart bar (Derek: "upgraded net should also make the heart bar go up more on perfect especially for lower tier areas")
Perfect gain = round(TrustPerfect x (1 + 0.10 x netLevel x A(areaTier))), A = 2 at tiers 1 to 2, 1.5 at tiers 3 to 4, 1 from tier 5.
Examples: Net 0 anywhere 3. Net 3 tier 1 round(4.8) = 5. Net 5 tier 1 6. Net 5 tier 7 round(4.5) = 5 (Luau math.floor(x + 0.5)).
Good and Miss unchanged. Keep "at least two hits": cap the Perfect gain at need - start - 1 so one Perfect never catches. netTiers' start head start stays as it is.
Both server (Circles.trustDelta via the attempt) and the client bar preview must use the same number; put the function in Circles so both share it.

## Build notes
- New pure functions in Circles: curveWindows(net, rarity, areaId, variant), curveSpeed(rarity, areaId, variant), perfectGain(net, areaId). Config tables CatchCurve = {base, netStep 0.15, W, S, heartNet 0.10, heartArea}.
- Branch on LiveFlags.get("catchCurve") in CatService where windowsFor / schedule / trustDelta are called (around lines 2895 to 2960).
- Spec tests: W and S non-increasing over tiers 1 to 10; widest band x 1.3 < CircleGapMin; perfectGain never lets one Perfect catch; switch off gives today's numbers exactly.
- Funnel: no new events needed; catch fail rate by area tier is already readable from the catch events. Growth compares fail rate per tier before and after the flip.
