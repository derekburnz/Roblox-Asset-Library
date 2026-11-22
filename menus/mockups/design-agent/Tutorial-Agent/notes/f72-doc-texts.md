# F72 texts for the design docs (for Design-Agent to paste)

Derek approved the intro on 2026-10-27 at 20:45 ("1 yes, 2 yes, 3 keep them but keep it brief"). The full spec is `intro-cutscene-spec.md` in this folder; it can go into the repo as `docs/design/cat-cafe/intro-cutscene.md`, which the row below links to.

## features.md row (a new section after 2g, or wherever fits)

| F72 | Intro cutscene and Tutorial button ([intro-cutscene.md](intro-cutscene.md), Derek 2026-10-27 20:11, approved 20:45): a 23.7 s client camera fly-through of nine shots with one caption each, shown once to every player whose `introSeen` is false (existing saves too); HUD, prompts and controls off while it runs; Skip bottom right after 2.0 s, at once on a replay; a player who has not seen it spawns just inside their own back door; `IntroDone(shot, replay)` saves `introSeen` and logs `intro_cutscene`; a Tutorial tile in the HUD's top right row replays it and its × hides it (`settings.tutorialButton`), with a switch and a Replay tutorial row in Settings; demo cats, the wheel spin and the night lighting are client-only | P1 | M | engineer, ui | F66 (night shot), F65 (Codes Cat; fallback caption without it) | A fresh account sees the intro once, Skip appears at 2 s and ends it at once, and the character stands inside its back door with the first hint showing; a rejoin does not replay it; the Tutorial tile replays it with Skip at once, × hides it across a rejoin and Settings brings it back; nothing staged is left after it ends |

## gdd.md, "The first ten minutes", beat 1

1. Watch the intro, about 24 seconds with Skip after 2 (F72), then start inside your cafe by the back door. Tabby is already behind the counter in an apron. A toast shows the rate.

## data-model.md additions

- Profile (section 14): `introSeen` | boolean | false | F72: set by the first non-replay `IntroDone`; every save starts false, existing ones included, so the friends testing see the intro once.
- Profile `settings`: a ninth key `tutorialButton` (boolean, default true) for the HUD's Tutorial tile.
- Remotes (section 15): `IntroDone` | event | shot, replay | F72: `shot` an integer 0 to 9 (0 = played to the end), `replay` a boolean; 1 per second | the first non-replay call sets `introSeen`; every call logs `intro_cutscene` (finished or skipped, shot, replay).
- Spawn: a player whose `introSeen` is false spawns just inside their own cafe's back door, facing it (plot-local about x -8, z 11).
- Analytics: custom event `intro_cutscene` for the growth thread's plan.

## decisions.md entry

### Decided by Derek, designed by the Tutorial-Agent thread (2026-10-27, the intro cutscene)
- 2026-10-27 20:45: New players watch a short intro before they can move (F72, docs/design/cat-cafe/intro-cutscene.md). Derek (20:11): a quick camera fly-through of the map, the most important things first because people skip tutorials at once, quick scene changes, a small Skip button bottom right after a couple of seconds and a button at the top to replay it that can be dismissed. Approved at 20:45 with his answers: new players land inside their own back door, the friends already testing see it once, and the four area cuts stay but brief. Nine shots in 23.7 s: catch a stray behind your cafe, the catch circle, cats working for tips, rank up and the Park gate, four 0.45 s area cuts, the Index Board, the plaza, night closing and sunrise, then back to you. Skip appears at 2.0 s (at once on a replay); a Tutorial tile in the HUD's top right row replays it, its × hides it and Settings brings it back. Why: shot 1 alone teaches the core loop to someone who skips at 2 s, and gates, the Index, the plaza stations and night closing get their first teaching; the existing step hints stay as they are.
