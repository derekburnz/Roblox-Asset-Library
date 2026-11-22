# Roblox official guidance and published data: first session onboarding, early retention, Home recommendation signals (2025 to 2026)

Research date: 2026-11-20. Method note for the report writer: pages were read through a fetch tool that summarises, so quoted strings below are as that tool returned them. They are close to verbatim but should be spot-checked against the live page before being printed as exact quotations. Several DevForum threads returned a maintenance redirect on 2026-11-20 and could not be read; they are listed under Gaps.

## 1. What signals does Roblox say drive Home recommendations, and what definitions and thresholds are published?

### Takeaway
As of the June 2026 change, "Recommended for You" (RFY) ranks on eight per-user signals measured over a 28-day view (Day 1, Day 2 to 7, Day 8 to 28). The four "most important" are play through rate, first play bounce rate (a negative signal with published bands at under 60 seconds and 61 to 180 seconds), play days per user, and playtime per user (capped at 60 minutes per user per game per day). The older single "qualified play through rate" (QPTR) signal has been split up, and Roblox has never published a numeric threshold for a "qualified play".

### Cited Findings

Current signal list (Creator Hub "Discovery" page, page metadata last updated 2026-11-20)
- Two stages: retrieval, then ranking. In retrieval, games with "even a small number of people playing can signal to the system that the game is worth considering". — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)
- "Most important" signals, with definitions as published:
  - Play through rate: "The rate at which users play your game after seeing it in the Recommended for You sort."
  - First play bounce rate (negative): "The rate at which users leave your game after a short play session." Published bands: "< 60 seconds average rate" and "61-180 seconds average rate".
  - Play days per user: "The average number of unique days users engage with your game." Reported for Day 1, Day 2-7 and Day 8-28.
  - Playtime per user: "The average amount of time users spend in your game." Cap: "There is a maximum of 60 minutes per user, per game, per day."
  — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)
- "Important" (second tier) signals:
  - Intentional co-play days per user: "The average number of unique days that users come back to play your game with friends."
  - Qualified play sessions per user: "A 'qualified play' refers to a user's meaningful play session with your game."
  - Spend days per user: "The average number of unique days users spend Robux in your game."
  - Robux spent per user: "The average amount of Robux users spend in your game."
  — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)
- Scope: "Each signal is based on users who organically joined from the Recommended for You sort on Home." In ranking, "Roblox doesn't count the engagement, monetization, or retention of users first acquired from ads". Ads, search, curation and friends can get a game considered sooner but are not what it is ranked on. — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)
- Signals are per-user averages, not totals: "These recommendation signals are calculated as averages per user, not total values." So a small game is not penalised for size. — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- Eligibility: "A custom thumbnail is required for your game to receive impressions from homepage recommendations." "If your game only has a default thumbnail, it is not eligible." — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)
- "Benchmarks and benchmark games do not impact the Recommended for You algorithm in any way." — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)

Discovery FAQ (Creator Hub, read 2026-11-20)
- "There is no single signal that determines ranking." Signals are "considered both separately and combined together to decide impression volume." Advice: "Focus individually first, especially playthrough rate, bounce rate, playtime, and play days". — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- "PTR and first play bounce only measure users acquired organically from Home recommendations in their first session." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- New games: "No. New games do not have to wait 28 days before Home can recommend them." "Early signals kick in immediately." Order in which signals arrive: "Playthrough rate and bounce rate capture the first session", "Then Day 1 signals (playtime, play days, Robux spend, co-play)". — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- Retrieval "requires only a very low minimum number of plays from any source." No number is given. — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- Priority order: "If retention is low, focus on core gameplay first." "Once retention is strong, improving monetization can help you increase your Home impressions." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- "Genre and gameplay type are not explicit ranking factors." "Story-driven and finite games are not penalized simply because their genre tends to have lower long-term retention." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)
- Day 2-7 play days is defined as: "Out of the 6 days in the 2–7 window, how many days on average did those users play". — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq.md)

June 2026 algorithm change (official newsroom, John Ciancutti, Chief Growth Officer, 2026-06-15)
- Roblox is "expanding the Recommended For You algorithm from its previous 7-day view to a 28-day view". New windows: day 1, day 2 to 7, day 8 to 28. — [Roblox Newsroom, 2026-06-15](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)
- The former qualified play through rate signal is split into separate signals for play-through behaviour, session quality and spend. — [Roblox Newsroom, 2026-06-15](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)
- Stated motive: overvaluing short-term engagement could favour games that "win attention with exciting thumbnails". Roblox says tests of the new version did "a significantly better job surfacing games that retain players over time" and raised platform DAU and engagement. No percentages are given. — [Roblox Newsroom, 2026-06-15](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)

Older definition (historical, July 2024)
- QPTR was introduced to analytics on 2024-07-18 by staff account signal_zzz. It "tracks the percent of users who have a qualified play in your experience after viewing it in recommendations." A qualified play is "a user's intentional engagement with your experience", as opposed to accidental clicks or quick bounces. No numeric cutoff was given. — [DevForum: Recommendations QPTR and Similar Experiences Benchmarks, 2024-07-18](https://devforum.roblox.com/t/analytics-recommendations-qualified-play-through-rate-and-similar-experiences-benchmarks/3075185?page=2)

Third-party restatement (not official)
- An investor blog (Indigo, 2026) restates QPTR as "the percentage of impressions that convert into qualified plays" and gives no threshold and no Roblox source for the wording. It also reports thumbnail testing lifts of "8.5% average, up to 50%" in QPTR and its own portfolio lifts of 70% to 180%; those are the firm's claims. — [Indigo: What is QPTR on Roblox](https://www.indg.vc/blog/what-is-qptr-on-roblox-and-why-it-matters)

### Inferences
- The only published time thresholds in the system are the two bounce bands (under 60 seconds, and 61 to 180 seconds) and the 60-minute daily playtime cap. For a first-minute redesign this is the hard target: a new player from Home who leaves inside 60 seconds counts in the worst band, and one who leaves inside 3 minutes still counts as a bounce. Getting a Home-sourced player past 3 minutes in session one is the smallest measurable win.
- Because playtime is capped at 60 minutes per user per day, AFK or idle padding has a ceiling; play days (returning on more distinct days) has no such cap inside the window and is listed in the top tier.
- Bounce and play through rate are measured only on a player's first session from Home. That means the first session is the only chance to affect two of the four top-tier signals, and FTUE changes should be judged on Home-sourced cohorts, not on ad or link traffic.
- Monetization signals sit in the second tier and Roblox says to fix retention first. An early paywall or purchase prompt in the first minutes risks bounce (top tier) for a second-tier gain.
- Any developer guide written before June 2026 that names QPTR as "the" signal, or cites a 7-day window, is out of date.

### Gaps
- No numeric definition of a "qualified play" (minimum seconds or actions) has been published, in 2024 or now. Widely repeated figures in developer circles are folklore; I found no staff source for any of them.
- No published weights for the eight signals beyond the two tiers.
- The March 2025 staff announcement ("Boost Your Discovery with the Improved Recommended For You Algorithm", thread 3587441) and the June 2026 DevForum companion post ("Recommended For You Algorithm Improvements That Better Value Long-Term Retention", thread 4684575) could not be read on 2026-11-20 (DevForum maintenance redirect). The second is likely to carry more detail than the newsroom post. URLs: https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441 and https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575
- No RDC 2025 or 2026 talk transcript was located in this pass.

## 2. What does Creator Hub recommend for onboarding and first time user experience?

### Takeaway
Roblox's written advice is consistent: get the player through the core loop once and to a designed "moment of joy" in about five minutes or less, teach only controls and the core loop, prefer visuals and contextual or timed hints over text and fixed tutorial sequences, and instrument every step as a funnel.

### Cited Findings
- FTUE target length: the first time experience should deliver the core loop "ideally in 5 minutes or less after entering your game." — [Creator Hub: Retention](https://create.roblox.com/docs/production/analytics/retention)
- D1 advice on the same page: use a short tutorial or contextual hints such as tooltips, avoid long tutorials, give a satisfying moment after the first core loop completion, and track completion of each FTUE step to fix the biggest drop-off. — [Creator Hub: Retention](https://create.roblox.com/docs/production/analytics/retention)
- The FTUE is judged on two things: Day 1 retention and onboarding goals. D1 depends on "the amount of players who make it through the FTUE." — [Creator Hub: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- Teach essentials only: first controls ("players need to grasp controls for navigation and interaction"), then the core loop, which the page calls "critical". — [Creator Hub: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- "Get to the fun quickly": players decide whether they like a game "within minutes". Keep early level thresholds "low" so players level up fast; give enough starter items and currency to enjoy the game and test the amount with Experiments. — [Creator Hub: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- "Leave players wanting more": show short, mid and long-term goals in visible places (skill trees, passes, quests, collections) and end onboarding with a designed reward or celebration that leaves players "feeling accomplished and excited to return." — [Creator Hub: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- A/B test tutorial steps; the page's example is "a shorter dialogue sequence versus a guided arrow". — [Creator Hub: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- On clarity: "Players who don't understand what to do in the first few minutes are likely to quit". — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- On text: "The more text a player is asked to read, the more likely they are to misinterpret or forget the information." "Players generally don't like to read instructions and skip through text prompts to get to gameplay." — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- On visuals: "Highlighting something that players should look at is more effective than describing it in text." "Prominent visuals can be harder to overlook, ignore, or misinterpret than text alone." Directional trails "provide direction while allowing players the freedom to explore". "Anytime a player takes an action in a game, it's imperative to provide clear feedback." — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- On fixed sequences: traditional fixed tutorials "can lead to boredom or frustration due to restricting player choice." — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- Contextual tutorials are "triggered by normal play, such as entering a new map zone or picking up a new weapon." "Delaying non-essential information to future sessions reduces what they must learn". Non-core features should not be taught in onboarding because "players may forget the information before they can use it." — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- Timed hints are "tutorial elements that appear to struggling players after a predetermined period of time". They "avoid annoying experienced players while giving newer players the opportunity to figure things out". Timing rule: show the hint "only after the majority of players have completed the objective". Worked example: "most players find and press the button within 10 seconds", so the highlight appears "at 11 seconds". The suggested A/B test is a "5-second or 10-second delay". — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- Funnels: "Your onboarding flow is a great place to start tracking funnel events." One-time onboarding funnels use `LogOnboardingFunnelStepEvent`, must be sent from the server in a published game, repeated steps count once, and skipped steps auto-complete earlier ones. Up to ten funnels on the dashboard. — [Creator Hub: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)
- Roblox's worked funnel example shows a 70% drop between step 1 "In Farm" and step 2 "Plant Seed", and the suggested fixes are contextual indicators that guide new users to plant, and requiring a first plant before free exploration. — [Creator Hub: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)

### Inferences
- Roblox's own guidance is against the pattern the owner describes as "dull, hard to follow and pushy": numbered fixed steps with text. The documented alternative is a world-led first loop (arrow, trail, highlight), hints that appear only for players who stall (about one second after the typical completion time), and deferring everything non-core to later sessions.
- The 70% example drop occurs at the very first required action, which matches the idea that the largest loss is between "spawned" and "did the first thing". The first action should be reachable without reading and without walking far.
- "Keep early thresholds low" and "starter currency" map directly onto a fast, coin-based early rank-up: Roblox explicitly recommends quick early level-ups and tuning the starting currency by experiment.

### Gaps
- The docs give no numeric guidance on tutorial step count, words per prompt, or seconds to first reward beyond "5 minutes or less" for the whole FTUE.
- The staff DevForum post "Learn More About First-Time User Experience & Onboarding" (thread 2621940, 2023) could not be read (maintenance redirect): https://devforum.roblox.com/t/learn-more-about-first-time-user-experience-onboarding/2621940

## 3. What benchmarks exist for D1, D7, session time and first session drop-off?

### Takeaway
Roblox publishes no absolute retention targets; it shows each game a private comparison against "similar experiences" or its genre in the dashboard. The only public dataset found is GameAnalytics' 2025 Roblox report, whose medians are far lower than the round numbers quoted in developer blogs (median D1 roughly 4% to 11% depending on session length, against blog claims of 20% to 30%).

### Cited Findings

Official
- Definitions: D1 "is the percentage of new users who come back to your game after visiting it for the first time"; D7 and D30 likewise, counted on the 8th and 31st day. — [Creator Hub: Retention](https://create.roblox.com/docs/production/analytics/retention)
- The retention docs give no benchmark percentages. — [Creator Hub: Retention](https://create.roblox.com/docs/production/analytics/retention)
- Benchmarks in the dashboard compare a game with "Similar experiences" when at least 50 similar experiences exist, otherwise with its genre, otherwise with all experiences. — [DevForum, staff signal_zzz, 2024-07-18](https://devforum.roblox.com/t/analytics-recommendations-qualified-play-through-rate-and-similar-experiences-benchmarks/3075185?page=2)
- Since 2025-10-16 creators can view D1, D7 and D30 by acquisition source and toggle the benchmark set between "similar experience" and "genre". The post's example: users from "Other" sources (external links) have "much lower D1 retention" than users from Home Recommendations. Benchmarks do not affect Home distribution. — [DevForum, signal_zzz, 2025-10-16](https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157)

Third-party data (GameAnalytics 2025 Roblox report; games using the GameAnalytics SDK only, 2025 data, not the whole platform)
- Platform session length per user, 2025: P25 2.36 min, P50 6.62 min, P75 14.53 min, P90 26.38 min. Total daily playtime per user, 2025: P50 16.77 min, P75 34.60 min. Sessions per day P50 2.02. — [GameAnalytics 2025 Roblox report](https://www.gameanalytics.com/reports/2025-roblox-report)
- Game-level retention by average session length (2025), D1 / D7 / D30 in percent:
  - 0-3 min sessions: P50 4.31 / 0.41 / 0.13; P75 7.44 / 1.02 / 0.31; P90 9.25 / 1.78 / 0.62
  - 4-6 min: P50 6.20 / 0.88 / 0.28; P75 8.61 / 1.65 / 0.46; P90 11.65 / 2.36 / 0.76
  - 7-12 min: P50 7.91 / 0.90 / 0.24; P75 9.82 / 1.46 / 0.45; P90 11.55 / 2.04 / 0.75
  - 13-18 min: P50 10.24 / 1.20 / 0.34; P75 12.16 / 1.80 / 0.56; P90 14.96 / 2.70 / 1.02
  - 19-24 min: P50 11.46 / 1.61 / 0.46; P75 13.55 / 2.79 / 0.80; P90 18.20 / 5.15 / 1.44; P98 32.30 / 8.54 / 2.99
  - 25+ min: P50 10.76 / 1.82 / 0.50; P75 12.32 / 2.91 / 1.20; P90 18.86 / 5.86 / 1.45
  — [GameAnalytics 2025 Roblox report](https://www.gameanalytics.com/reports/2025-roblox-report)
- The report has no genre breakdown; it groups by session length. — [GameAnalytics 2025 Roblox report](https://www.gameanalytics.com/reports/2025-roblox-report)

Developer folklore (unsourced)
- A RoWatcher article (2026-07-15) states genre ranges: obby D1 25-35%, D7 10-15%; roleplay/social D1 15-22%; tycoon/incremental D1 20-28%, D7 12-18%; shooter D1 22-30%, D7 12-16%. It cites no dataset, sample or method. — [RoWatcher, 2026-07-15](https://rowatcher.com/news/retention-benchmarks-by-roblox-genre-what-good-actually-looks-like); contradicted in scale by [GameAnalytics 2025 Roblox report](https://www.gameanalytics.com/reports/2025-roblox-report)
- A small developer reported about 5% D1 with 5 to 20 concurrent players in April 2026. — [DevForum thread, 2026-04-04](https://devforum.roblox.com/t/stuck-on-low-retention-players-leave-before-playing-the-tutorial/4557364)

### Inferences
- The two public sets of numbers disagree by a factor of two to three. Likely reasons: GameAnalytics samples many small games and may define cohorts differently from Roblox's dashboard, while blog figures describe what successful games see. Neither should be used as a target. The right benchmark is the game's own "similar experiences" and genre percentile in Creator Analytics, filtered to the Home Recommendations source.
- In the GameAnalytics data, longer average sessions go with higher retention at every percentile up to about 19 to 24 minutes (median D1 rises from 4.3% at 0-3 minutes to 11.5% at 19-24 minutes). This is correlation, but it is consistent with Roblox ranking on playtime and bounce.
- A quarter of Roblox sessions in that sample end before 2.4 minutes, which is inside Roblox's 180-second bounce band. Early exit is the norm, so shaving the first three minutes is where most players are affected.

### Gaps
- No public Roblox-issued table of D1/D7 percentiles by genre exists that I could find; the genre benchmark is visible only inside each creator's dashboard.
- No published platform-wide figure for first play bounce rate (what share of Home plays end under 60 or 180 seconds).
- The GameAnalytics table shows an odd jump in ARPPU at P95 in the 19-24 minute bucket; the retention figures look internally consistent but were read through a summariser and should be checked against the report charts.

## 4. What case studies report retention changes from onboarding changes?

### Takeaway
I found no well-sourced before and after numbers from a named Roblox game in this pass. The official material offers illustrative examples rather than measured case studies, and the developer posts that could be read give diagnosis without a measured result.

### Cited Findings
- Roblox's funnel documentation uses an example funnel with a 70% drop at the first required action ("Plant Seed") and recommends contextual indicators and gating exploration behind one completed loop. It is a teaching example, not a reported result. — [Creator Hub: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)
- Roblox states as a general claim that "Timed hints can increase the number of new players retained by a game", with no figure. — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- DevForum, April 2026: a developer with about 5% D1 found that "almost half" of joiners never reached the first tutorial step. Replies (community members, not staff) blamed a loading screen that one tester timed at over a minute on a mid-range PC, and a forced avatar change. The developer cut the loading screen to a fixed 3 seconds; no after number was posted before the thread closed on 2026-04-18. — [DevForum thread, 2026-04-04](https://devforum.roblox.com/t/stuck-on-low-retention-players-leave-before-playing-the-tutorial/4557364)
- Same thread, community advice: preload assets in chunks in the background with ContentProvider instead of blocking, add arrows and animated input icons where players stall at an input step, and note that sponsored (ad) players depress the stats. — [DevForum thread, 2026-04-04](https://devforum.roblox.com/t/stuck-on-low-retention-players-leave-before-playing-the-tutorial/4557364)
- Indigo (investor blog, 2026) reports thumbnail and icon work lifting QPTR by 70% to 180% on two of its games. This concerns the store page rather than in-game onboarding and is self-reported. — [Indigo: What is QPTR on Roblox](https://www.indg.vc/blog/what-is-qptr-on-roblox-and-why-it-matters)

### Inferences
- The absence of public numbers means the team's own onboarding funnel plus an Experiments A/B test is the only reliable evidence available; Roblox's docs point to exactly that workflow.
- The one concrete developer case points at pre-tutorial loss (loading, forced changes to the player's avatar) rather than tutorial content. Measure "joined" to "first input" as a funnel step of its own before rewriting tutorial steps.

### Gaps
- The DevForum post "Improving Onboarding for our Zombie Shooter" (thread 3323657) returned empty content twice and "Improving Onboarding through Funnel Events" (thread 3064458) was not read; both may contain real before and after figures. URLs: https://devforum.roblox.com/t/improving-onboarding-for-our-zombie-shooter/3323657 and https://devforum.roblox.com/t/3064458
- RoWatcher articles with relevant titles ("Your First 90 Seconds Are Destroying Roblox Retention", "The Roblox Onboarding Paradox: Fewer Tutorials, Better Day 3", "A/B Testing in Roblox: What Actually Moves Retention in 2026") were not read. Given that the one RoWatcher article checked cited no data, treat any numbers in them as unsourced unless they name a game and dataset.
- An X article by EvanZir, "I Was Wrong About the Roblox Algorithm (Mostly)", could not be fetched (robots block).
- No numbers found for removing a cutscene, shortening a tutorial, speeding the first reward or lowering an early wall in a named Roblox game.

## 5. What does Roblox say about tutorials for young and mobile players?

### Takeaway
Roblox's explicit guidance is to teach without words where possible, because text is too small on phones, young players are still learning to read, and visuals need no translation.

### Cited Findings
- Mobile: visuals matter on "mobile devices, where text can be too small to read comfortably". — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- Young players: "For games that appeal to younger players, teaching without words can help those that are still learning to read". — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- Localization: "Visuals like arrows and particle effects communicate without words and don't require translation". — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- "Visual elements are more broadly accessible than text." — [Creator Hub: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
- Controls: show complex controls on screen or in a tutorial so players can navigate and interact. — [Creator Hub: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding.md)
- D1 guidance includes testing on different devices and platforms and watching crash rate, frame rate and errors after each update. — [Creator Hub: Retention](https://create.roblox.com/docs/production/analytics/retention)
- "Reducing memory usage can greatly expand your addressable audience, especially on mobile." — [Creator Hub: Performance optimization](https://create.roblox.com/docs/performance-optimization)

### Inferences
- For a young, phone-first audience the tutorial should be readable with the text hidden: a world arrow or trail, a highlight on the one thing to touch, and feedback on every action. Text is a caption, not the instruction.
- Median Roblox session length is under 7 minutes in the GameAnalytics sample, so the first complete loop and first rank-up should fit well inside that.

### Gaps
- No Roblox document found that gives a reading level, word count, or minimum touch target size specifically for tutorials.
- No official statement found on session length by age group or by device.

## 6. How do loading time and time to first interaction affect bounce?

### Takeaway
Roblox states plainly that long join times cost acquisition and retention and that players leave before entering, but it publishes no curve or target number. The bounce bands in the recommendation system (under 60 seconds, 61 to 180 seconds) appear to be measured on the play session, so time spent on a custom loading screen after join is likely to count against them.

### Cited Findings
- "Join time is the total time from when a player clicks the play button to when the world is rendered and they can move." — [Creator Hub: Performance optimization](https://create.roblox.com/docs/performance-optimization)
- "Long join times hurt user acquisition and retention." "players may leave before ever entering your experience." — [Creator Hub: Performance optimization](https://create.roblox.com/docs/performance-optimization)
- Excessive memory use blocks players on weaker hardware and causes client crashes; server memory exhaustion disconnects everyone. — [Creator Hub: Performance optimization](https://create.roblox.com/docs/performance-optimization)
- Default frame target is 60 FPS (16.67 ms per frame). No numeric target is given for join time, memory or crash rate. — [Creator Hub: Performance optimization](https://create.roblox.com/docs/performance-optimization)
- First play bounce rate is a top-tier negative recommendation signal with bands at under 60 seconds and 61 to 180 seconds. — [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md)
- Developer report: nearly half of joiners lost before the first tutorial step in a game with a blocking preload screen over a minute long. — [DevForum thread, 2026-04-04](https://devforum.roblox.com/t/stuck-on-low-retention-players-leave-before-playing-the-tutorial/4557364)

### Inferences
- If a session is 40 seconds of loading screen followed by 30 seconds of confusion, the player lands in the 61 to 180 second bounce band having played almost nothing. A blocking custom loading screen, intro cutscene or sign-in modal eats directly into the bounce budget.
- Practical order of work: (1) measure join to first input as a funnel step, (2) remove or shorten anything blocking between spawn and first input, loading in the background instead, (3) then rework tutorial content.

### Gaps
- Roblox does not state whether the bounce timer starts at clicking Play, at join, or at character spawn. This matters for how much loading time counts and is not documented in the pages read.
- No published Roblox figure relating seconds of join time to percent of players lost.
