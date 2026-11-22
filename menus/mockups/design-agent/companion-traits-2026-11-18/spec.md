# Companion traits (Design-Agent spec, Nov 18 2026)

Derek, 17:17 UTC: "make new traits (if I havnt said this) that effect companion bonuses".
These are new Mystic Pool traits that raise a cat's **Cat Companion** boosts, Money and Luck (#5296: every companion gives both). They sit behind the switch `companionTraits` (off by default). A trait is saved as `{ id }`, so new ids need no save step. An older server would still drop unknown ids, so the switch goes on after a restart publish, as `traits` did.

## Two new effect kinds (Traits.KINDS)
- `companionMoney`: percentage points added to the cat's companion Money share. It works only while that cat is your companion.
- `companionLuck`: added to the cat's companion Luck. It also works only while that cat is your companion, and is still capped by LuckMax 3.
These are additive, not multiplied, so a Common cat with a good trait is a real choice (Common 3% + 5% = 8%). Coat multiplies the base boost only, not the trait part, so the numbers stay easy to read.

## The new traits
Rarity odds do not change (Common 30, Uncommon 25, Rare 18, Epic 12, Legendary 10, Mythic 4.9, Secret 0.1). Each new trait joins its rarity's even pick, and the Odds list shows the new per-trait share.

| Trait | Rarity | Effects |
|---|---|---|
| Loyal Heart | Common / Uncommon / Rare / Epic | companion Money +1% / +2% / +3% / +5% |
| Lucky Shadow | Common / Uncommon / Rare / Epic | companion Luck +0.03 / +0.05 / +0.08 / +0.12 |
| Best Friend | Legendary | companion Money +8%, companion Luck +0.15 |
| Trail Buddy | Legendary | companion Money +6%, income +0.25 (its own cafe pay) |
| Guardian Spirit | Mythic | companion Money +12%, companion Luck +0.25, income +0.50 |
| Eclipse (Secret, existing) | Secret | gains companion Money +12% and companion Luck +0.25, the highest of any trait, as #3908's rule says |

**Biggest companion possible:** a rainbow Secret cat with Eclipse gives 30% + 12% = 42% Money and 0.60 + 0.25 = 0.85 Luck. That is well under LuckMax 3 and under the event money cap rules, because companion Money is a tip multiplier source that is still clamped where it is today.

## Where it shows
- **Companion picker (#5296):** each card's Money and Luck already include the trait. A small trait chip under the numbers, in the trait's rarity colour, reads for example "Loyal Heart +3%".
- **Mystic Pool roll card:** the effect line reads "+3% Companion Money (while following you)".
- **The cat card's trait line** uses the same words.

## Monetization
Trait Tokens are sold, so a roll is a paid random item. The odds text (oddsText, summing to 100) must list the new traits before the prompt, and policy-restricted players still never see bundles. Review-QA checks this against `monetization-policy`.

## Checks
- Specs:
  - the odds still sum to 100 with per-rarity shares updated
  - the companion effects count only for the current companion
  - Eclipse has every kind at the max
  - Luck is capped
- UI gate: the picker card with a trait chip fits on phone.
