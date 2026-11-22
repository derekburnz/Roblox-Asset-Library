# Friend joiners stay with their friend (#3995)

Status: spec by Design-Agent, 2026-11-14 04:20 UTC, from Growth-Agent's issue. Picks are under Derek's overnight OK; he can change any of them. Derek's rule from 2026-11-13 19:25 UTC holds: no on-screen friend bonus, so nothing here mentions the +10%.

Builders: Gameplay-Engineer (server, switch, telemetry); Design-Agent (the two notes and the tutorial strip line).

## What happens today
A player who joins through an invite or by following a friend (Roblox's Join button sets FollowUserId) already lands at the friend's front door and both characters wave (F92, `CannonService.palArrival`). Then, for a new player:
- the intro scene may play itself (the intro test arms), and its camera and its last shots go to the player's own cafe;
- the player's cafe is the first free plot on the street, often far from the friend's;
- the tutorial strip sends them to that cafe and on to the Alleyway.

So within the first minute the joiner is taken away from the friend they came to play with. Friends-source playtime is about 2 minutes against 38.7 average.

## The change (behind the `palJoin` switch, ships off)
Applies to a player for whom `PalService.joinedVia(player)` returns a friend on this server when their character first spawns.

1. **Cafe next door.** `PlotService.assign` gives this player the free plot whose door is nearest the friend's door. If none is free nearby it falls back to the first free plot, as today.
2. **Land at the friend's door** (already built), with the wave.
3. **No intro scene by itself this session.** A new joiner skips the auto-play intro on this join. The ? Tutorial tile still glows and plays it on a tap. The save stays out of the intro test (no intro group), so the test's arms stay clean.
4. **Joiner's note** (a small top card, 6 s, one tap to dismiss, never during a menu): "You joined Sam!" and, for a new player whose cafe is next door, a second line "Your cafe is next door." No bonus, no chip.
5. **Friend's note** (same card): "Mia joined you! They're at your front door." 6 s.
6. **First tutorial line for a new joiner:** the strip's first step reads "Your cafe is next to Sam's: step inside 🐾" until they enter it, then the tutorial goes on as normal. No tutorial step is skipped: the steps teach the basics, and the Tier 2 fall is handled in #4098.
7. **Where the friend is:** the existing marker "Sam is in the Park" and the tagged area card stay as they are. A friend in an area the joiner can't open yet gets today's toast.

Names are the Roblox display name, cut as the cafe sign cuts it (`CafeName.shown`).

## Edge cases
- The friend leaves before the joiner loads: a normal join.
- Two joiners for one friend: each gets the nearest free plot left.
- A returning joiner (intro seen): steps 1, 2, 4 and 5 apply; their own cafe moves next door for this session (plots are per session).
- Private server: everyone is a pal there, but only an invite or a follow counts as joining through a friend.

## Telemetry (Gameplay-Engineer)
`pal_join` once per join that this applies to: how they were linked ("invite" or "follow"), new or returning, cafe next door yes or no. Counts only. Growth-Agent reads Friends-source playtime and `pal_time` before and after.

## QA checks
1. Two test accounts, switch on: B joins A by following. B lands at A's door, both wave, B's cafe is the next plot, no intro plays, both notes show and go after 6 s.
2. B new: the strip's first line names A's cafe and moves on once B enters their own cafe.
3. Switch off: today's behaviour exactly.
4. Phone 667x375 and PC: the notes fit and cover nothing important (goal card, strip, clock).
