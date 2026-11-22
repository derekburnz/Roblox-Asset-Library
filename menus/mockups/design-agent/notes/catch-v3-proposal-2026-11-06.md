# Catch v3: making the core catch fun (proposal, 2026-11-06)

By Design-Agent for Derek2, who asked to "re-work the cat catching mechanic/minigame to be more fun but still clean, it's one of the core gameplay loops". The issue is #1884. Builds on catch-rework.md (F93), which stays the base: net swing, circles by rarity, bands by net.

## 1. What we have now and what's wrong
- **Loop:** walk up, swing the net, then shrinking circles (3 for a Common up to 7 for a Mythical), then carry the cat home. One Miss ends the try and the cat sprints off.
- **What's good:** one button, works on a phone, server-judged, quick.
- **What's flat:**
  1. Every catch plays the same. Rarity only changes the count and speed.
  2. One Miss on circle 6 of 7 wipes the whole try, so hard cats feel unfair, not exciting.
  3. The cat doesn't react while you catch it. The circles float over a statue.
  4. There's no build-up or payoff moment at the end, and nothing for playing well beyond "caught".
  5. The approach is empty: you just walk up.

## 2. What good catch loops do (research)
- **Pokémon GO's throw:** one shrinking ring with a clear grade (Nice, Great, Excellent). The tension comes from the ball wobbling up to three times before it clicks. Skill gives a bonus (more XP for Excellent and curveballs), never a gate.
- **Stardew Valley fishing:** it's loved because the fish fights back and a progress bar lets you recover from mistakes. Its creator admits it "starts too hard" ([PC Gamer](https://www.pcgamer.com/games/life-sim/a-lot-of-people-hate-it-but-i-think-its-fun-eric-barone-backs-stardew-valleys-fishing-minigame-but-does-admit-that-it-starts-too-hard), [GamesRadar](https://www.gamesradar.com/games/simulation/concernedape-regrets-making-stardew-valleys-fishing-minigame-too-hard-when-you-start-out-but-still-thinks-its-good-overall-i-know-its-controversial)). The lesson: use a meter instead of instant fail, and keep the first hours easy.
- **Rhythm games and "game feel" work:** every hit needs feedback (a short hit-stop, sound with rising pitch, the target reacting), and a combo should feel like it builds ([juice overview](https://www.pulse.bot/gaming/news/the-juice-factor-designing-game-feel-910cc98a-a568-4687-82d0-1d741ff22207/), [Wayline game feel course](https://www.wayline.io/learn/game-feel)).
- **Animal Crossing bug and fish catching:** the approach matters, because sneaking up slowly is half the fun, and it costs no extra buttons.

## 3. The proposal

### 3a. The approach: cat moods (no new buttons)
Each stray shows a small mood icon when you come within 15 studs:
- **Sleepy (zZ):** stays put. Common and Rare cats are often sleepy.
- **Curious (?):** walks toward you for 2 s, and a swing while it comes gives +1 trust to start (see 3b).
- **Skittish (!):** if you *sprint* within 10 studs it hops away. Walking is fine. Epic and above can be skittish.

The mood is rolled when the stray spawns, from per-rarity weights, and shown above its head. Players learn "walk up to the jumpy ones". The tutorial stray is always Sleepy.

### 3b. The calm: a trust bar instead of instant fail
- The circles stay (the same one-button timing), but each one appears **on the cat in the world**, around its head, with the cat reacting: ears perk, a little lean in.
- A **Trust bar** sits above the cat. It starts at 1. A Perfect adds +2, a Good +1, and a Miss takes 1 (the cat wriggles and hisses softly).
- **The cat is caught when the bar fills.** It needs 3 for a Common, 5 Rare, 7 Epic, 9 Legendary and 11 Mythical.
- **It bolts** (today's sprint-off) if the bar hits 0. One slip no longer ends a good run, but a bad run still fails.
- The circles come on a steady beat. A soft purr rises in pitch as trust grows, so a streak sounds like it builds.
- Gameplay-Engineer re-fits the numbers by simulation so the catch chance per try stays close to today's table (catch-rework.md §2). A Mythical on a Basic Net stays a real challenge.

### 3c. Rarity twists (variety, introduced slowly)
- **Epic and above: the double ring.** Two rings shrink together and need two quick taps. It's marked by a doubled outline.
- **Legendary and above: the paw ring.** A red ring with a paw print, shown about 1 in 6 times. *Don't* tap it: the cat swats, and tapping costs 1 trust. Leaving it gives +1.
- **Commons and Rares** keep plain rings, so new players only meet twists once they're ready.

### 3d. The finish: a wobble, then the payoff
- When the bar fills, the net wraps the cat and wobbles once or twice (0.6 s), then pops with confetti and a grade banner:
  - **PURRFECT!** if every ring was Perfect.
  - **GREAT!** if at most one wasn't Perfect.
  - **NICE!** otherwise.
- **Purrfect bonus:** the cat joins with 1 level of XP already earned. It's small, it's earned and it costs no coins. A "Purrfect streak x3" counter shows on the HUD across catches and resets on a non-Purrfect.
- After that, the carry home stays as it is.

### 3e. Feel (per lane)
- **Animation-Engineer:** the cat's ear perk and lean per hit, the Miss wriggle, the paw swat, the net wrap and wobble, and the mood idles (sleepy curl, curious walk-up, skittish crouch).
- **VFX-Agent:** a ring pop per grade, a 60 ms hit-stop on Perfect (client only), the trust bar glow, confetti on the finish and a gold burst on Purrfect. Lighter versions with Reduce Motion and Low performance.
- **Sound-Agent:** the purr layer that rises with trust, grade ticks (Perfect, Good, Miss), the hiss on a Miss, the swat, the net wobble and pop, and the Purrfect jingle.
- **UI-Engineer:** the trust bar, the mood icons, the grade banner and the streak counter.

### 3f. Stays clean
- One button, phone friendly. The server still judges every press, and nets stay coin upgrades.
- Nothing about catching is sold for Robux. The current Steady Paw potion only widens bands.
- No new remotes beyond what CatchSchedule and CatchResult carry today: grades per press, plus trust and the finish grade in CatchResult.

## 4. Picks for Derek2 (recommended first)
1. **Trust bar** instead of one-miss-fails? (recommend yes)
2. **Rarity twists:** both the double ring and the paw ring (recommended), only the double ring, or none.
3. **Purrfect reward:** +1 cat level (recommended), 1 golden fish, or the banner only.
4. **Cat moods** on the approach: now (recommended) or later.

## 5. Build order once picked
1. Gameplay: trust maths and re-fit (Circles, Catching, a CatchResult grade), plus a Pace.spec re-check.
2. UI: the bar, the banner and the streak.
3. Animation, VFX and Sound: the feel passes.
4. Moods and twists in a second PR.
5. QA live playtest on phone and desktop.

QA targets: a new player's first 3 catches all succeed. A Common takes about 4 s from swing to caught. A Mythical on a Basic Net is caught about 1 try in 4.
