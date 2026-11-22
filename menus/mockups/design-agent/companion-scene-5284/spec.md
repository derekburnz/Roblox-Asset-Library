# Cat Companion unlock scene (#5284), Design-Agent, Nov 18 2026

Behind `companionScene` (off by default). It plays once, after the Tier 2 Rank Up, when nothing else is showing (GE's wait list).

## Names
- Noun everywhere a player reads it: **Cat Companion** (card title, Cats screen header line, What's New row). Code names stay `follower`.
- Button stays **Follow** (and **Stop** to undo). Short and clear on phones.

## Which cat
Auto-pick it. Take the best cat the player owns that isn't away: highest rarity, then highest income, then the newest caught. The scene sets it as their companion right away, so the reward is real the moment the card shows. This is not a menu opening by itself, so it keeps Derek's rule that players tap tutorial steps themselves.
If there is no free cat, skip the walk-in. Show the card with "Pick one in Cats", then dim the screen and point an arrow at Cats and then Follow. The player taps both.

## Beats (7.5 s, then the card waits for Nice)
| Time | Beat |
|---|---|
| 0.0 to 1.0 s | Controls pause. The camera eases to a three-quarter front view of the player, about 10 studs out, at head height. |
| 1.0 to 3.5 s | The cat trots in from behind the player's left at walk speed, with a small sparkle puff where it stops. It sits beside the player and gives one little hop. |
| 3.5 to 4.0 s | One heart pops above the cat. The player's avatar does nothing scripted. |
| 4.0 s | Card in: **Cat Companion unlocked!** Under it is "<Cat name> walks with you everywhere." Then one line with the real perk from the follower code (money or Luck, the same words the Cats screen uses). The button is **Nice**. |
| On Nice | The camera eases back in 0.6 s and controls return. The cat now follows. A soft arrow pulses on the Cats button for 5 s, or until the player taps it, with the caption "Change your companion here". There is no dim, because nothing is required. |

A tap anywhere during 0 to 4 s skips to the card. If the player leaves or resets mid-scene, mark it seen and set the companion anyway.

## Do not
- Open the Cats screen by itself.
- Show it again, or show it to players already past Tier 2 when the switch goes on. For them, a one-time What's New row is enough.
- Play sound louder than the Rank Up chime. Use one soft purr or sparkle cue.

## Check (Sync or Review-QA)
- Fresh account: Tier 2 Rank Up, then the scene after the Rank Up window closes. It never shows during the tutorial dim, bowl card, flight or carry.
- Phone: the card fits, the arrow lands on Cats, and the cat is fully in frame on a 16:9 phone and a tall phone.
- Switch off: today's behaviour, no scene.
