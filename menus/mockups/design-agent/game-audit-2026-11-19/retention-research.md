# Research: bounce, playtime and D1 (Design-Agent, Nov 19 2026)

Derek asked for research on lowering bounce, raising playtime and raising D1, with money left for later. Sources were read through a fetch helper. One page (the DevForum thread on daily rewards) was down, so nothing here rests on it.

## What the outside numbers say
- **GameAnalytics 2025 Roblox report** (Jan 2023 to Jul 2025, large titles). Median D1 by average session length: under 3 min 4.3%, 4 to 6 min 6.2%, 7 to 12 min 7.9%, 13 to 18 min 10.2%, 19 to 24 min 11.5%. Casual players leave in under 2 minutes. The shortest quarter of sessions fell from 4.1 to 2.4 minutes between 2023 and 2025. These are links between numbers, not proof that one causes the other.
- **Roblox staff, "Improving Onboarding through Funnel Events"**: fix the biggest and earliest funnel drop before adding content. Their example lost 70% at step 2 and a marker over the thing to click fixed it.
- **Roblox engagement docs**: fun inside the first five minutes, contextual tips in place of a long tutorial, starter items. Advice, no numbers.
- **One team's own report (DevForum, Feb 2025)**: removing waits and adding a mode did nothing for session time or D1. A new thumbnail lifted players a lot.
- Nothing I found gives a measured lift for one onboarding trick. Most advice online is opinion.

## Where we sit
- Playtime 9.2 min and D1 2.8 to 4.0%. The median for our session length is 7.9%, so we are at about half.
- 47% of our players are gone by minute 2, which matches the report's "casual players leave in under 2 minutes". That group decides bounce.
- So the order is: win the first two minutes, then stretch the session past 12 minutes, then give tomorrow a number.

## What I am doing about each
| Goal | Action | Where |
|---|---|---|
| Bounce | Catch first against bowl first as an A/B, both arms checked end to end | #5498 |
| Bounce | Log why a started catch ends with no cat, before changing any catch rule | #5500 |
| Playtime | Tiers 4 to 7 much cheaper so more players reach the later areas | PR #5504 (tiersEasy) |
| Playtime | A visible gift every few minutes, fresh each day | #5506 |
| D1 | Away money and Daily Treat milestones as the reason to return | #5505 |
| All reads | 1 in 10 new players held on a frozen setup | #5499 |

Targets: 35% still playing at 5 minutes (25% now), playtime 12 minutes, D1 6% and then 7.9%.

Sources: https://www.gameanalytics.com/reports/2025-roblox-report , https://devforum.roblox.com/t/improving-onboarding-through-funnel-events/3064458 , https://create.roblox.com/docs/production/analytics/engagement.md , https://devforum.roblox.com/t/struggling-to-increase-games-key-metrics/3483721 , https://devforum.roblox.com/t/day-1-retention/3177419
