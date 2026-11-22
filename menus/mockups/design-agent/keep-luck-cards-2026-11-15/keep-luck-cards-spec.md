# Dragon Keep: crate, trait and spin luck cards (spec)

Design-Agent, 2026-11-15 20:40 UTC, for Gameplay-Engineer (follow-up to #4569). Card ids stay as they are; only names, words and the bonus change.

## 1. Cards (remapped, no new ids, binder stays 54)

| Card id | New name | Family, rarity | New words | Was |
|---|---|---|---|---|
| luckyCrate | Lucky Crate | Hoard, Epic | +15% crate luck. | +5% bowl luck (Lucky Charm) |
| traitSpark | Trait Spark | Heart, Epic | +15% trait luck at the Mystic Pool. | +15% cat XP |
| quickCannon | Lucky Spin | Wing, Rare | +10% spin luck. | +4% bowl luck (Lucky Wings) |

Each replaces a bowl luck or cat XP card, and other cards in the binder already give those two.

Sets: no change. Each set's bonus is its own line.

## 2. What each kind shifts, and the cap

The same rule applies to all three kinds.

- The bonus multiplies the Epic-and-rarer chances, and Common and Rare give up the difference. This is the same math as `Luck.applyMap`, so the odds always add up to 100.
- A kind counts only the cards in the slots, like every other card.
- Each kind's total from cards is capped at +30%.

| Kind | Applies to | Does not apply to |
|---|---|---|
| Crate luck | Plain crate opens. It folds into `playerLuck` in `Crates.oddsFor` and multiplies it, staying inside the existing luck cap. | Golden crates and the lucky twentieth, which keep their own odds as now. |
| Trait luck | Mystic Pool rolls (free and token). The Epic, Legendary and Mythic odds go up, and Common and Uncommon go down. Add `Traits.rarities(secret, luck)` and `Traits.oddsText(secret, luck)`, and make `Traits.roll` take the same luck. | Secret, which stays fixed at 0.1% so it stays special. |
| Spin luck | Spin Wheel slices of Epic-and-rarer prizes, through the same multiply-and-renormalise. | Nothing else. |

## 3. Where the player sees their own odds (monetization-policy)

Every odds list is built from the same function, with the same luck, that the server rolls with. Under each list a small line shows the bonus, for example "Your Dragon Keep cards: +15% trait luck".

- **Crates:** the Fish Market crate odds, and the crate odds on Today's Deal crate cards, which come from Robux products. FishMarket already calls `Crates.oddsFor` with `playerLuck`, so pass the combined luck.
- **Traits:**
  - The Mystic Pool Odds list.
  - Its token roll card.
  - The Trait Tokens product offer card before the Roblox prompt, which shows `oddsText` with the player's luck.
- **Spin Wheel:** the odds list on the wheel.

The server reads the bonus fresh at each roll. A player who swaps cards sees the new odds the next time a card opens.

## 4. Spin Wheel: free only?

What I read is one free spin a UTC day, plus banked spins from Cafe Pass rewards, with no Robux product for spins.

If the Cafe Pass premium track is bought with Robux, banked spins are paid-adjacent. That is why section 3 shows the spin odds anyway, so it is policy-safe either way.

## 5. Tests

- **Shared specs:**
  - Odds with each bonus add up to 100.
  - Each cap holds at +30%.
  - Secret trait stays at 0.1.
  - Golden crates and the lucky twentieth are unchanged.
- **UI gate:** the three odds lists show the boosted numbers and the bonus line when a card is slotted.
