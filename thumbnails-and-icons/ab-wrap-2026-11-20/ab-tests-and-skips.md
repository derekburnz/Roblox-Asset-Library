# Ending the A/B tests, and what players skip

Growth, Nov 20 2026, 13:20 UTC. For Derek's ask at 13:04 UTC. Numbers are from Creator Hub. Nov 20 is still filling in, so today's counts are low.

## The A/B tests that are live

| Test | Since | What it splits | Players so far | Call |
|---|---|---|---|---|
| Order test (switch orderSplit) | Nov 20 03:10 UTC | New players get catch first or bowl first, half each | 52 catch first, 38 bowl first joined; 31 and 29 are in the funnel data so far | End it |
| Held back group (switch holdout) | Nov 20 01:06 UTC | 1 new player in 10 does not get daily gifts, the away row or the welcome back card for 7 days | 15 held back, 118 not | End it |
| Intro test (introSplit and the Creator Hub introMode setting) | Nov 12 | Not a real split any more: every new player gets the label "intro_short", and the intro is off since 11:48 UTC today | 166 labelled today | Retire the label |

I found no other split in the code. Other switches are on or off for everyone.

### Order test: no proven winner, catch first leans ahead late

| Reached | Catch first (31) | Bowl first (29) |
|---|---|---|
| First catch | 26 (84%) | 25 (86%) |
| Tier 2 | 21 (68%) | 21 (72%) |
| Park catch | 17 (55%) | 13 (45%) |
| Tier 3 | 12 (39%) | 6 (21%) |
| Tier 4 | 8 (26%) | 5 (17%) |

About 30 players each is too few to call. The two are level up to Tier 2. Catch first is ahead at Tier 3, but a gap that size shows up by chance about one time in six with groups this small.

The two halves also log different funnels (catch first writes onboarding_v7, bowl first writes onboarding_v9). That is the tracking mess.

**Call:** switch orderSplit off now. New players then all get bowl first, which is today's default and the funnel we have read all week (v9), until the new start replaces both orders tonight. The new start is catch first, and this lean is one more small reason to think that is right.

### Held back group: end it

It needs day 1 and day 7 returns to say anything, and it has 15 players. The features it holds back are the ones Derek asked for. Switch holdout off so every player gets daily gifts, the away row and the welcome back card.

## What players skip (Nov 18 to 20 UTC)

| Piece | Got it | Skipped | Skip rate | Live now? |
|---|---|---|---|---|
| Intro scene | 1,440 | 533 | 37% (phone 42%) | Off since 11:48 UTC today |
| First bait cutscene | 1,633 | 1,283 | 79% | Yes |
| Companion unlock scene | 378 | 297 | 79% | Yes |
| Cat station scene, 3 cats | 350 | 233 | 67% | Yes |
| Cat station scene, 4 cats | 204 | 134 | 66% | Yes |
| Cat station scenes, 8 to 10 cats | about 60 | 37 | about 60% | Yes |
| Bowl tip scene | 51 | 27 | 53% | Yes |
| Spin wheel scene | 18 | 9 | 50% | Yes |
| Golden fish, dealer | 56 | 7 | 13% | Yes |
| Area reveal tips (Park and later) and other tips | about 3,500 | 0 | cannot be skipped, or never are | Yes |

The walk-through steps themselves (bowl, cannon, catches, Rank Up) have no skip button, so they have no skip rate. Their losses are in the funnel.

**Read:** every scene that takes the camera away is skipped by half to four fifths of players. The worst are the first bait cutscene and the companion unlock scene, both 79%. Those two and the cat station scenes are the ones to cut or shrink to a short pop-up. The area reveals are not skipped because they cannot be.

## The two new funnels (after the new start is live)

1. **Overall:** onboarding_v10, 10 steps, already built by the engineer (#5546): joined, loaded, first catch, first time home, 3 catches, Rank Up ready, Tier 2, Park arrived, Park catch, Tier 3.
2. **First 5 minutes in detail:** needs new logging. Every prompt shown, every first tap, each window opened, each trip, each catch try and miss, first coins, first Rank Up tap, plus still here at 30 s, 1, 2, 3 and 5 minutes. I send the step list to Design and the engineer once the new start's steps are final, so the funnel matches what is built.

With the tests ended, both funnels carry one group ("free"), so every player is in one funnel.
