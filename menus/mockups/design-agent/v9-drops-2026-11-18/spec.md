# onboarding_v9: the two drops before Tier 2 (Design-Agent, Nov 18 23:55 UTC)

Source: Growth's read at Growth-Agent/funnel-v9-2026-11-18/v9-drops-to-tier2.md. Derek, 23:35 UTC: look into the bad drops before Tier 2. Each fix goes behind its own off switch and goes on as soon as it merges (Derek's rule since 23:04 UTC).

## 1. strayMeets: the waiting stray comes to the player (stray_marked to near_stray keeps 85 to 89%)
GE's proposal, with these details:
- On alley_arrived, while the second-cat stray is marked and the player has not caught by hand yet, the stray trots from its spot to a point 8 studs in front of the landing pad's exit side. It walks at its normal walk speed, not a teleport, so it reads as "this cat is coming to you". The trip is capped at 3 s; if the path is blocked, it snaps to the point after 3 s.
- It stops, faces the player, does its happy idle and keeps its marker. The catch prompt shows as soon as the player is in range, as today. The player still taps the catch themselves (tutorial rule).
- While it waits there, its leash is 12 studs around that point, not 30 around its old spot, so it never wanders back out of reach.
- If the player walks off without catching, after 20 s it stays where it is (no chasing). The trail still points at it.
- Only the first hand catch of the account. Later strays act as today.
- Success: near_stray at 95% or more in the first hour after the switch goes on.

## 2. bowl_hint_seen (first_move to bowl_hint_seen keeps 85 to 92%)
What can sit between first_move and the food line, from UIController's tutorial path (refreshTutorial, then nightLine.body):
- a carry line (rare this early),
- the pal next-door line (palJoinLine returns before the bowl part, but only for friend joins),
- the rarity guide (Tier 2 and up, so not here),
- the strip only reports `bowl:food` when it actually draws. A screen open at the time (the Smooth phone ask until phoneSmooth went on at 23:37, the loading screen fade, a What's New card) leaves the strip hidden, and nothing fires until the next refresh.
Many of the lost players may simply be leaving in the first minute (first-play bounce under 60 s was 20.3% at the #5285 baseline), so part of this drop is the bounce itself, not a hidden line.

Ask for GE, before building:
- Read the time from first_move to bowl_hint_seen. StepGaps only has loaded_to_first_move now, so add a first_move_to_bowl_hint gap behind the same switch if needed. If the median gap is under 2 s, it is mostly bounce; the fix is in #5285's first-60-seconds work. If the gap is long or has a tail over 5 s, something is holding the line.
- If it is held: behind `bowlLineNow`, show the food line within 0.5 s of intro_done whatever else is open, on top of any non-modal screen. The line is "Put food in your bowl to get your first cat!" with the ring and arrow on the bowl. Fire bowl_hint when the line is first drawn, not on a later refresh.
- Either way, wait for Growth's 00:00 to 01:00 hour, since phoneSmooth may already fix most of it.

## Not touched yet
rank_up_cue_seen to rank_up_ready_shown (79% in the 21:00 hour only): GE waits for Growth's 00:00 to 01:00 read, as planned.
