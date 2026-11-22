# Perfect catch replaces Charm (#5300), Design-Agent spec, Nov 18 2026

Derek, 17:16 UTC: "remove charm from game and just have it if you perfect catch a cat make it give +50% money and show in a bubble like gold/rainbow bonuses".
Switch `perfectCatch` (off by default). With it off, Charm plays as today. The save keeps each cat's `charm` field untouched.

## The rule
- **A Perfect cat** is one caught by net where **every ring of the catch was graded Perfect**. That is today's "Purrfect" test (the one that doubles the charm bonus), so the server already knows it at the catch. Paw rings and both halves of a double each count as rings, and one Good or Miss means no mark.
- Rescues, bowl and bait cats, crates, spins, the Collector, trades in and gifts have no rings, so they are never Perfect at the source. A Perfect cat traded to someone else keeps its mark.
- **The tutorial's guided first catch counts.** Its held rings stop on the ring, so most new players get a Perfect first cat. That is a nice early win, and it pairs with E2's wow moment.
- **Scripted presses:** while the AutoPress flag is set (reviewer S23), a catch never marks Perfect, as it never got the charm bonus.
- **Saved:** a `perfect = true` field on the cat instance. An older server ignores it.

## The bonus
- A Perfect cat's own pay is **x1.5**, stacking by multiplying with its coat: a gold Perfect cat is x2.25 and a rainbow Perfect cat is x3. It applies wherever the coat multiplier applies (online and offline cafe pay). The Collector's price stays coat only, so the mark isn't a selling machine.
- Charm's spread (CharmSpread, 0.8 to 1.2) stops counting while the switch is on, and every cat's charm factor is 1.

## Existing cats (so nobody loses much when Charm goes)
When the switch goes on, every owned cat with **charm 80 or more** gets `perfect = true`, once, when the save loads. Those cats earned up to +12 to 20% from charm and now get +50%. Cats under 50 earned less than base and now earn base. Only cats with charm 50 to 79 lose, at most 11.6% of that one cat's pay (charm 79 is x1.116 today). Charm was Derek's call to remove, so that is acceptable. GE logs how many cats fall in that band.

## The bubble (pill)
- **On the cat card's tag row**, after Rarity, Gold and Rainbow: a pill reading **"Perfect +50%"** in pale sky blue (Theme sky, or #8FD3FF) with ink text and a small white star. It shows next to Gold or Rainbow when both apply, and has the same height and corner as the Gold pill.
- **On the Cats list thumbnail:** a small white star in the top right corner, the same place as the gold glint, so Perfect cats are easy to spot when picking.
- **At the catch:** the existing catch result line gains "PERFECT! +50% money" in the same sky blue, one line with no new card. E2's first catch wow plays its own banner, so on that catch the line says only "+50% money".
- **The Charm UI goes:** the charm bar, the charm number on the cat card and in the Cats list sort, and the charm tip. The "Sort by charm" option becomes "Sort by Perfect".

## Words
Tip, shown once, the first time a catch fails to be Perfect after the player has seen one: "Hit every ring Perfect to catch a Perfect cat: +50% money!"

## Checks
- Spec: all Perfect rings give the mark, one Good gives none, a rescue gives none, AutoPress gives none, and the multiply with gold and rainbow is right.
- The charm 80 migration runs once, and switching off and on does not stack it.
- UI gate: the cat card with Gold plus Perfect pills fits on phone.
