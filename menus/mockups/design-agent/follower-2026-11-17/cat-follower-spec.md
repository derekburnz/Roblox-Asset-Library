# Cat follower (Design-Agent, 2026-11-17)

Derek 23:56 UTC: pick one of your cats and it follows you around for a bit more money or luck. Player idea credit is kept privately (project memory, idea-credits-players), never in the public repo.

## How it works
- Opens at Tier 2 (after the first Rank Up, so the first minute stays clean). One follower at a time.
- Pick it in the Cats menu: a "Follower" slot sits at the top; every cat card gets a small "Follow" button. Tap Follow, the cat hops out of the cafe and runs to you. Tap "Send home" on the slot to stop.
- The cat keeps earning its normal cafe income while it follows (its seat shows a little paw note "Out with you"). No loss for picking.
- A cat in a trade offer cannot follow; trading it away sends it home first.
- The player picks the boost on the slot: **Money** or **Luck** (one toggle, free to switch, 10 second cooldown).

## Boost by rarity
| Rarity | Money | or Luck |
|---|---|---|
| Common | +3% | +0.05 |
| Rare | +5% | +0.10 |
| Epic | +8% | +0.15 |
| Legendary | +12% | +0.20 |
| Mythical | +16% | +0.30 |
| Secret | +20% | +0.40 |

## Mutation bonus (Derek 2026-11-18 01:07 UTC: "better mutation have better improvements also")
The coat multiplies the rarity boost: base x1, **gold x1.25**, **rainbow x1.5** (same order as their income, 1.5 and 2, but softer so a follower never beats the cat's own earnings). The top is a rainbow Secret: +30% money or +0.60 Luck. A Mythical rainbow gives +24% or +0.45. The slot and the card show the total, with a small "Gold x1.25" or "Rainbow x1.5" chip under it, so a player sees why their gold cat gives more.

Money multiplies cafe income like the Money Potion and stacks with it. Luck adds to the Luck number (bait and crate Epic and up chances) and stays under LuckMax. Run the Pace test with Legendary on before it goes live; if a tier gets more than about 10% faster, raise that tier's cost (raise costs, never cut rewards).

## How it moves
- Walks 4 studs behind and to the side, matches walk speed, hops when you jump, sits and grooms after 3 seconds idle.
- More than 40 studs away (teleports, falls) it pops to you with a small puff.
- During a net catch it sits and watches, never stands in the circle.
- Others see your follower. On phone, other players' followers show only within 80 studs, at most 8 at once. The model is the cat's normal model, no extra parts.

## Not sold
No Robux for follower slots or boosts in v1. A second slot later (Tier 6) would be earned, never bought.

## Switch and owners
Behind `catFollower`, OFF_BY_DEFAULT. Server: the chosen cat id and the boost (validate the player owns the cat, rate-limit the remote). Client: the walk. Gameplay-Engineer builds; Motion-FX the walk, sit and puff; Model-Agent previews; Review-QA the Studio pass.

Mockups: follower-picker-phone.png and follower-picker-pc.png here.
