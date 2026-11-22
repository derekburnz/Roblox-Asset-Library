# Design Agent (updated 2026-11-21 00:45 UTC, wrap-up handoff)

## State 2026-11-21 00:45 UTC (project wrap-up handoff; read this first, it wins over every older section)
- Nothing of Design's is in flight. No open PR, no open claim, no scheduled tasks, no uncommitted work. Branch claude/project-thread-8xc8nf has no open PR (last was #5630, merged); a new thread starts its branch from origin/main.
- Shipped and live Nov 20 (all UTC), each behind a switch that is on; turning the switch off is the rollback:
  - rankTapLook (#5593, on 16:33:44): green one tap RANK UP button on the goal card. Breath and outline fix rode #5610.
  - askClean (#5610, on 17:25:35): clean look for AskCard (slide-in asks). Also covers TipCard (one-line context tips) since #5626 (published 19:15:33) and the X letter fix #5630 (published 20:20:43). Toasts (pills) are unchanged on purpose.
  - Theme.potionColors.picnic_time (#5615).
  - catNamesTop (issue #5633, Motion-FX PR #5636, published 21:45, on 21:46): wild cat names sit above the rarity diamond and NEW pill. Design wrote the spec; Motion-FX built it because Effects/ is theirs.
- Not verified in the live game by Design: the TipCard X fix (#5630) and catNamesTop. Sync's re-look of the X was queued and never came back. First job for the next Design thread if Derek reports a covered name or a blank X: check those two in Studio or on a phone.
- Rules learned this round (also in memory): no menu opens by itself and the player is never moved without their own tap (only exception: rankPicker at the cannon after Rank Up, Derek Nov 20 16:03); scenes are short with no skip, or gone; every first-session change ships behind an off switch that goes on the hour it publishes; no restarts unless Derek says so.
- Code traps: UI/init.luau is at Luau's 200 local limit (hang state on a UI.<name> table). Tween.popIn reuses a frame's first UIScale and cancels tweens on it, so looping scale tweens must restart themselves. A UIGradient on a TextLabel or TextButton tints the text too, so put the letter on a child label. CI's luau-lsp is stricter than the local analyze on string unions: cast literals (`"secondary" :: Button.Style`). The place is landscape only, so check narrow layouts at 640x360, not portrait.
- Design does not edit `src/client/Effects/` (Motion-FX) or Controllers and server code (GE). Write the spec in a GitHub issue and hand it to the owner thread.
- Files from this round: ask-card-2026-11-20/ (mock), rank-button-2026-11-20/, new-start-2026-11-20/ (new start specs and step list).

## State 2026-11-20 17:20 UTC (Sync-Agent library backup; read this first, it wins over older sections)
- Current memory word for word: library `memory/project-memory.md` (index) and `memory/files-2026-11-20/` (every topic file). Project instructions unchanged since Nov 19: `memory/project-instructions.md`.
- Thread ids in this project (the older ids further down are dead): GE cmsg_01WMctLtVBdq3PtmMq1eAcCu3UTFzLJoCyG2pmzxn79P5v, Design cmsg_01WMctLtVBdq3PtmMq1eAcCuWcdU8B6E3ptNe87fcGxZFv, Review-QA cmsg_01WMctLtVBdq3PtmMq1eAcCuFZxrE2ahY7XmeXAXyJvA31, Motion-FX cmsg_01WMctLtVBdq3PtmMq1eAcCuCCwrgdRZLdkf8A2osrkKNN, Model cmsg_01WMctLtVBdq3PtmMq1eAcCuGPoVzSA1bp5tAbeSdji6Wq, Growth cmsg_01WMctLtVBdq3PtmMq1eAcCu1oT2iYf7EUS8VfQ2CLQtvb, Sync cmsg_01WMctLtVBdq3PtmMq1eAcCuBH5rWNW3vnkYUJvYoNYa5P. In a new project use list_threads.
- Derek's Nov 20 direction: freeze dropped, new fun start (freeStart, streetCats, goalChip, coinsOnly, cannonGlow, stallGlow, baitCutQuick, cutsQuick all on), Rank Up is coins only and one tap (rankOneTap, rankTapLook, rankPicker), A/B tests ended, Home recommendations are the lifeline (new Moonstag icon live), Picnic Party (#5572) is the hook for the Park leak. Benchmark: once every open PR and issue is done (on-hold #5339 aside), Growth stamps the benchmark start in Growth-Agent/benchmark-2026-11-20/benchmark-sheet.md.
- Design now: new start specs in Design-Agent/new-start-2026-11-20/ (new-start-v2-spec.md, first-five-minutes-steps.md, research notes), rank button look in rank-button-2026-11-20/ (#5593, breath fix 816a2d557 rides PR #5610), ask card clean-up in ask-card-2026-11-20/ (askClean #5610). Camp chip call: RANK UP may skip "Take it to camp" when firstCatchCoins reaches the Tier 2 cost (fine, no change). Picnic chip and sign words are Design's.

**ALWAYS CONTINUE (Derek 2026-11-15 08:58 UTC, top rule):** every thread always keeps working on issues and PRs. When stuck on anything (Derek, Studio, the PC, a build, review), park it with the coordinator in one line and immediately take a different open unclaimed issue or PR in any lane. Never wait for Derek. Never end a turn while open work remains.

**Model:** Opus 5.5. **Always on.** Thread title stays exactly "Design-Agent".
**Role today:** the game's UI and client screens (`games/cat-cafe/src/client/UI/`, the ui-designer folder), plus design specs (`docs/design/cat-cafe/`), pricing and policy calls (monetization-policy), and the intro and tutorial flow (absorbed Tutorial-Agent). Gameplay-Engineer (GE) owns server code; Motion-FX owns `src/client/Effects/`; Model-Agent owns models, pictures and uploads; Review-QA reviews every PR; Growth owns store page, ads, analytics and group posts; Sync-Agent owns the library repo.

## Read first, in order
1. The game repo's `CLAUDE.md` (rule 15: claims and the second project).
2. Project memory `MEMORY.md`, then `checkin-to-rankup-2026-11-17.md` and `design-agent-2026-11-16-night.md` (newest lane files), `design-agent-lane.md`, `derek-preferences.md`.
3. This file. Older history: `HANDOFF.md`, `handovers/`, `notes/`, `Tutorial-Agent/` beside this file.
4. For any spec: `docs/design/cat-cafe/` on main and the newest part of `docs/decisions.md`.

## Derek's standing rules for this lane
- **SLEEP MODE** (Derek 2026-11-15 01:38 UTC, every time he says he is going to sleep): keep working through issues and PRs all night. Never stop on anything stuck: park it with the coordinator in one line and take another issue in any lane. His approval covers our recommendations; make assumptions when needed.
- **NEVER STOP** (2026-11-14): a thread that finishes a batch takes the next open issue at once. Waiting on Studio, the PC or Derek means park and move on.
- **Two Claude projects** (2026-11-15 01:46 UTC): another account works on this game too. Before taking an issue, check it has no `claim` label and no open PR from anyone else; add `claim` and a comment when you take it; leave anything they claimed alone. Their branches start with `friend/`.
- **Always arm:** once Review-QA passes a PR, turn on GitHub auto-merge (merge commit) without asking (Derek 2026-11-14 17:50 and 19:44 UTC). Library repo PRs always auto-merge.
- **Publishing:** AUTO_PUBLISH is on. Every passing merge to main publishes silently (new servers only, about 20 minutes after the main check). Never force a restart or shutdown. A restart happens only when Derek OKs it, and the build must be live first (verify publish green and the place version) with the admin events announced.
- Features ship behind LiveFlags (`LiveFlag_<key>` attributes) so they can be turned on without a publish. Pick the switch route when something must change fast, and say plainly when a fix needs a publish.
- Young audience: no dark patterns, no fake timers or discounts. Paid random items always show odds (monetization-policy). Secret cats stay dark shapes outside the game; new Secret names stay out of the public repo until they ship.
- Public repo: never write a player's name or id anywhere in it. Secrets stay in env vars. Money and sales numbers stay out of the repo.
- **ART RULE, BANNED PICTURE** (Derek 2026-11-16 16:51 UTC, banned twice): never use the wooden crate with the gold cat coin icon (`assets/cat-cafe/ui/icons-clean-2026-11-03/Icon_Clean_Crate.png`, old asset 81784091360384) in the game, previews, mockups or posters. Use the Classic Crate (`exports/icons/CatCafe_Icon_Crate_Classic*.png`, Crate_Classic 72888217681662) or the area crates. Game fix: Cat-Cafe #4887.
- Menus use the cocoa MenuFamily style (`menu-theme-black` memory) and must work on phone, small phone, A06, tablet, console and desktop.
- Every post that says "here is" a picture carries the file (under `/mnt/project-files`). Write to Derek as if he is impatient: answer first, plain words, no emojis, no em or en dashes, no Oxford commas.

## Update 2026-11-17 13:00 UTC (new project, Design-Agent thread)
- #3951 built: PR #5079, switch `tomorrowCard` (off), Review-QA PASS, auto-merge armed. Turn on only after Growth's D1 read of the Nov 16 and 17 cohorts, proposed Sun Nov 22 12:05 UTC. Read: D1 of `tomorrow_card` shown vs `return_hook_early_shown`.
- Harvest Index "back next autumn" note done on claude/harvest-owned (#4439), rides the Wed fold.
- #4438 part 2: Starter Bundle timing already done; `storeGuard` waits on Growth's money pass buys by tier and first day.
- Growth caveat: bowl-first players log in_cannon to first_checkin within 1 s of the tame. The real leak is bowl tame (~50 s) to Rank Up shown (~102 s). Do not spec on step 14 to 15.
- Arming works from this thread: `gh api -X PUT repos/derekburnz/Cat-Cafe/pulls/<n>/ccr/auto_merge -f merge_method=merge`.

## Open work (handover 2026-11-17 11:35 UTC, Derek is remaking the project on another account)

**Funnel switches.** GE flips each one at 12:05 UTC, a UTC day apart, and sends Growth and Design the exact minute. All four passed Sync's PC check.
- Tue Nov 17: `rankUpRightAway`, #5031, PR #5039 with Motion-FX cue #5032. Fixes the first check-in to Rank Up drop, 27 to 34%.
- Wed Nov 18: `cafeGrows`, #4543.
- Thu Nov 19: `parkRingEarly`, #5034, PR #5035. Model-Agent also arms Tables spread #4763 (#3867) about 06:00 UTC that day.
- Fri Nov 20: `tier3Path`, #5038, PR #5049. Fixes park_catch to tier_3, 36% lost.
- Sat Nov 21: `parkTrailBack` plus `parkGateTrail`.
- `fxOneAdded` went on at 09:30 UTC Nov 17 (Park landing hitch, perf only).

**Live today.**
- Pal Day (#4913, PR #5007): code live since 02:29 UTC Nov 17, `palDay` OFF. It goes ON right after the Wed Nov 18 20:00 UTC Harvest restart (line added to the restart plan on #4251). Growth takes the friend vs alone D1 and D7 baseline first.
- Tier ladder #5056, live 06:27 UTC Nov 17: Tier 4 needs 10 kinds, Tier 5 needs 13 kinds and 12M, Tier 6 needs 150M, Tier 7 stays 3.125B. #4192 is closed. The one item left is the Tier 6 to 7 read: Tier 6 to 7 is now a 20x coin step, and Growth's after window starts 07:27 UTC Nov 17. If that step loses over 40% short on coins, set Tier 7 to 2.5B and check Pace keeps Tier 8 in band (plan section 8).
- Better on Every Device update is TODAY, Tue Nov 17 20:00 UTC, not Wed. The content was already released quietly Nov 16 22:04. The restart banner text "then better controls and ADMIN EVENTS!" is already in RestartNotice. Notify Me rolls to Harvest Hollow (Nov 25) by itself.

**Waiting on a read.**
- #3951 come-back reason: build only if Nov 16 D1 is under about 6%, otherwise close. Roblox had not filled D1 by 10:50 UTC Nov 17. Growth's 12:00 and 12:30 UTC reads have it.
- After rankUpRightAway: step 14 to 15 churn by device. The target is under 10%.

**Harvest Hollow** (#4251): stack #4382 to #4439 folds right before the Wed Nov 18 20:00 UTC restart (see `harvest-hollow-merge-plan` memory). claude/harvest-owned holds Design's #5025 UI fixes plus GE's harvest exclusions. Harvest cats count toward no kinds, quests or badges (spec 3b), and a harvest catch checks in after 1 s. Left: Index "Back next autumn" note after Dec 6.

**Other open issues.**
- #5050 timed-run fixes, GE: stale strip, carry pointer, Bait Bowl 10m text, Alleyway title twice.
- #4224 console, needs Derek.
- #2718 What's New: a standing refresh every 20 to 50 changes. #5059 is open from Motion-FX.

**Specs and reads** (copied beside this file in `specs-2026-11-17/`): checkin-to-rankup.md, park-to-tier3.md, tier ladder plan-draft.md (sections 1 to 8), nov-17-read-plan.md.

**Analytics:** run 44002569974 (Nov 15 to 16), run 44049999925 (Nov 16). Dispatch: `gh api -X POST repos/derekburnz/Cat-Cafe/actions/workflows/analytics.yml/dispatches -f ref=main -f 'inputs[days]=N'`. Read the log with `gh run view <id> --log`. Useful sections: onboarding_v8 by Platform, quit_have ready and first need missing (t<N>_kinds/coins/rarity), new_player_left by device, step_stall last hint.

## Tools and how to run them (cloud container)
- Worktree per PR: `git worktree add -q -b claude/<topic> <scratch>/wt-x origin/main`. Each worktree is about 1.2 GB; the disk fills after about 15 (commands then fail with "No space left on device"), so remove pushed ones (`git worktree remove --force`); their commits stay in the main checkout's `.git`.
- Fast checks from `games/cat-cafe/tools/cloudcheck` (link node_modules from the main checkout, remove the link before commit): `node analyze.mjs`, `node analyze.mjs --tests`, `node run-tests.mjs --filter <Spec>` (full run takes about 14 minutes), `node uigate.mjs --profile <phone|smallphone|a06|tablet|desktop|console> --flag menuFamily --scene A,B --out <dir>`.
- CI's own luau-lsp (1.70.1) is stricter than analyze.mjs. Run it locally with the rojo and luau-lsp binaries in the scratchpad `tools/` folder: `rojo sourcemap default.project.json -o sourcemap.json`, then `luau-lsp analyze --sourcemap=sourcemap.json --definitions=<globalTypes.None.d.luau> --ignore "Packages/**" --ignore "ServerPackages/**" --ignore "src/server/Vendor/**" src`. Delete sourcemap.json after.
- StyLua 2.x: `stylua --check src` from `games/cat-cafe` (CI checks src only).
- Gate pictures: the gate draws ScreenGuis to SVG (emoji in place of uploaded images; SurfaceGuis are not drawn). Convert with a small Playwright script to PNG.

## Gotchas
- Funnel reads: a ready Rank Up window closed inside 5 s never logged step 15 (throttled screen report); #5039 reports it at once. onboarding_v8 event steps are filled in by any later non-event step.
- Pace tool: `node run-tests.mjs --filter Pace` (about 2 min) prints `[Pace ...]` tier times; Catalog.spec has the tier table to update with any ladder change.
- A worktree's branch cannot be checked out in the main checkout; work in a fresh `git worktree add --detach` and `git push origin HEAD:<branch>`.
- The spec shim cannot load Theme (no Roblox types): pure logic modules use `ShortNumber` plus "$" instead of Format. A modal close slides out, so wait `UIShim.advance(0.6)` before asserting it is hidden. A nil in a spec override table is skipped; clear the field after building.
- AskCard on a phone is compact and hides its line, so a card that needs its words on a phone is a centred Panel modal.
- luau-lsp 1.70.1 rejects `for _, x in maybeList or {} do`: write `(maybeList or {}) :: { T }`. Calling a value whose type is a union of two function types also fails: annotate the local.
- Selene fails the job on any warning: an unused `self` must be `_self`; `assert` needs a message.
- A "Unit tests" job that fails on a 429 while downloading `globalTypes.None.d.luau` is not the PR's fault; another run of the same head covers it.
- Gate scenes share state: a scene must not toggle UI an earlier scene left open; restore anything you change in `Scenes.close`.
- `uigate-scenes.luau` starts with `--!nocheck`; never insert above that line.
- CanvasPosition, AbsoluteCanvasSize and AbsoluteWindowSize are on-screen pixels: multiply design px by `Scale.get()`.
- CI is slow at night (10 to 30 minutes a gate job, runs get cancelled when main moves). Do not cancel other runs.
- Force pushes are blocked: merge main into a branch instead of rebasing.

## PR, commit and comment format
- PR body starts with `<!-- claude-projects-attribution: {"github_login":"derekburnz"} -->` and `_Requested by **Derek** · [project thread](https://claude.ai/code/project/chan_01MCxxGJfsqHYWej39x2j9jk?thread=cmsg_01MCxxGJfsqHYWej39x2j9jkPLZP7qMpebFMmjtM1UJtJw)_`, ends with the Claude Code line and the session URL. Commits end with the Co-Authored-By and session lines. GitHub comments end with the Generated by Claude Code footer. No model ids anywhere.
- Subscribe to every PR you open. Ask Review-QA to review the exact head, arm on PASS.

## Key ids
- The ids below are from the first project; the Nov 15 to 17 project was `chan_016pRP8hSbRwRYsCUkxnF8qh`, and the new project after Nov 17 has new ids (read them from list_threads). Old project `chan_01MCxxGJfsqHYWej39x2j9jk`. Thread ids share the prefix `cmsg_01MCxxGJfsqHYWej39x2j9jk`: Design-Agent `...PLZP7qMpebFMmjtM1UJtJw`, Gameplay-Engineer `...RceKfPpTMbdcBeJfbWjUPf`, Review-QA-Agent `...5SFFx6iyzrxqoPEvMMm1p5`, Model-Agent `...C3guhHVcovdE2EGHQNyHQL`, Motion-FX-Agent `...Nrad4YEGJyBhNwtniFXoh2`, Growth-Agent `...3utQiHH2TzPj7jiwhsYeNb`, Sync-Agent `...JocHG8Y6NCpk1FtmdLP47E`.
- Repos: `derekburnz/Cat-Cafe` (public game), `derekburnz/Cat-cafe-library` (private library).
- Schedule: 3 New Worlds Sun Nov 15 20:00 UTC; Golden Fish Store Sun 22:00 UTC; 10 Secret Cats Mon Nov 16 03:30 UTC; Better on Every Device Tue Nov 17 20:00 UTC (moved by Derek); Harvest fold restart Wed Nov 18 20:00 UTC; Harvest Hollow Nov 25 to Dec 6. The update list the game teases from is `Config.UpdateEvents`.

## Rules held from earlier (still true)
- Same rarity odds everywhere; odds always shown; nothing truly limited (free event rewards return no sooner than 4 weeks later).
- No Robux or coins for golden fish, crates or spins without Derek's OK. Never reward likes or favourites. Nothing pays per trade.
- Economy rule: if a tier is too fast, raise its cost, never cut rewards.
- `docs/decisions.md` is append-only; on a conflict merge main and keep both sides, main first.
