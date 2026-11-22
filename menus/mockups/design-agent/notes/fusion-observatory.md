# Cat Fusion Observatory (Snowy Mountain, Tier 8)

Status: spec by Design-Agent, 2026-11-14, for #4027. Derek picked the station on 2026-11-13 at 22:39 UTC ("1 is good for snowy"). The rules come from his idea: "5 mythic normals make 1 gold of that mythic, 5 gold mythics makes 1 rainbow of that mythic but for all tiers". The numbers below are Design picks under his global OK, and he can change any of them.

Builders:
- Gameplay-Engineer: the server side, save, remotes and the Pace check.
- Design-Agent: the window (`Screens/FusionObservatory.luau` and `Components/FusionLogic.luau`).
- Model-Agent: the dome.
- Motion-FX: the fusion swirl.
- Sound-Agent: two cues.

It follows the camp-extra rules (late-stations.md section 1 and section 2):
- Nothing is sold, sped up or refilled for Robux or golden fish.
- Nothing is random.
- It never changes catch, luck, gold or rainbow odds.

## 1. What it does

Five copies of one cat in one coat become one copy of the next coat:
- 5 normal give 1 gold.
- 5 gold give 1 rainbow.
- Rainbow is the top coat.

It works for every cat with a gold and a rainbow look, at every rarity, Secret cats included. Event-only cats work too once owned, but shop-only cats are left out if they have no coat looks. The cat is never lost: 5 go in and 1 of the same cat comes out, so a player can't fuse away their only cat of a kind.

**The cats that may go in.** Each must be:
- owned;
- not locked (the favourite lock, the same F62 rule as selling and trading);
- not working;
- not at the Oasis Spa;
- not waiting on a Mystic Pool choice;
- not in an open trade.

They all read the one `CatStats.busy` helper plus `locked` and `spotId`. Working cats show "Working" and are skipped; the player takes them off their job first.

**The cat that comes out:**
- **Level:** it keeps the best level of the five and that copy's XP toward the next level.
- **Trait:** if any of the five has a trait, the confirm card lists each one and the player picks which stays. The default is the rarest. With no traits, it has none.
- **Name:** it keeps the name of the copy whose level it kept.
- **Not locked:** it comes out unlocked and resting. Equip Best does not run on it.
- **Index:** its coat counts as found (`goldCollection` / `rainbowCollection`) the moment it is collected. That is the real late-game pull, because the Gold and Rainbow tracks of the Index pay out on those.

**The default pick.** It takes the best-level copy plus the four lowest-level others (lowest level, then lowest charm, then uid). That way the result keeps the level the player worked for and spends the weakest copies. The player can tap any copy in or out, and exactly five must be picked.

**Time.** A fusion runs in the dome for a while and counts offline time too, like every camp extra:
- **Gold:** `FusionGoldSeconds` 600 (10 minutes).
- **Rainbow:** `FusionRainbowSeconds` 3600 (1 hour).
- The Dragon Keep card Elder Lore (L, Wing) takes 25% off.
- **One dome, one fusion at a time.** When it's done the cat waits in the dome until collected, so it never lands in the middle of a trade or a job change.

**No undo after start.** The five cats leave the save when the fusion starts, and the server holds the result. So the confirm is two taps:
- the first tap reads "Fuse 5 → 1 Gold";
- the second tap reads "Tap again: 5 Mochi become 1 Gold Mochi".

## 2. The window

The panel is cocoa MenuFamily with an ice blue accent (`7FC8F0`), titled "Fusion Observatory" with the subtitle "5 of a cat make 1 in the next coat". It has two tabs.

**Fuse tab.**
- **Dome card on top:**
  - empty: "The dome is free";
  - running: a live timer, "Gold Mochi · 6:42";
  - finished: "Rainbow Mochi is ready" with a Collect button.
- **The ready list under it.** Every cat and coat the player has five or more free copies of, best result first: rainbow before gold, then rarity, then name. Each row shows:
  - the cat's portrait in its coat;
  - "Mochi ×7";
  - the arrow and the next coat's portrait;
  - "Fuse" (grey with "Dome busy" while a fusion runs).
- **"Almost" rows.** Up to three dimmed rows for cats at 3 or 4 copies ("Mochi ×4 · 1 more"), so the player knows what to catch next.
- **The empty state:** "Catch 5 of one cat in one coat to fuse them".

**Confirm card** (over the window, after Fuse):
- **Top:** the five picked copies, each with level and trait tags. Tapping one swaps it with another copy from a strip of the rest.
- **The arrow down to the result:** portrait in the new coat, "Lv 34 · keeps Mochi's name", and the trait pick when there is one ("Keep: Lucky Paws (Epic)" as chips).
- **Time line:** "Ready in 10 min".
- **Buttons:** the two-tap Fuse button and Back.

**Index tab.** Every cat with a coat track, in Index order:
- three small dots (normal, gold, rainbow), each lit when found;
- the copies owned of each coat;
- a cat that can fuse now gets a small "!".

It's the same picture set as the Index, so there's nothing new to draw.

**The "!"** shows on the dome and in the cannon picker while a fusion is ready to collect, or while the dome is free and some cat has five free copies.

**Picker line:**
- "Observatory: Gold Mochi 6 min"
- "Observatory: Rainbow Mochi ready !"
- "Observatory: 3 can fuse !"
- "Observatory: free"

## 3. The station

The station is `CatCafe_Camp_Snowy_FusionObservatory` on Summit Peak, next to the flag (tier8-snowy-mountain.md section 3):
- A round stone base about 10 studs wide, with a white dome split by a brass slit.
- A short telescope points at the northern lights, and a "Fusion Observatory" sign sits on a post.
- It's solid, climbable and finished on every side, with a `PromptAnchor` at the door and a `BangAnchor` over the sign.

**While a fusion runs:**
- the dome slit glows in the coat's colour (gold or the rainbow ramp);
- a slow ring of five small paw lights circles it;
- the effect is owner-only, and everyone else sees the glow.

**Motion-FX:**
- **On start:** five portraits fly into the centre and swirl.
- **On collect:** a burst in the coat's colour.
- The flash limit is one a second at most, with Reduce Motion respected.

**Sound:**
- a rising chime on start;
- a bright "ta-da" on collect, with the rainbow one longer.

## 4. Contracts (Gameplay-Engineer)

**Config:**
- `FusionCopies` 5
- `FusionGoldSeconds` 600
- `FusionRainbowSeconds` 3600
- `FusionTier` 8

**Save** (optional field; claim `DataService.luau` and `ProfileSchema.luau` and share the next save version bump):
```
fusion = {
  running = { catId: string, coat: "gold" | "rainbow", startedAt: number, doneAt: number,
              level: number, xp: number, name: string?, trait: TraitInstance? }?,
  made = { gold: number, rainbow: number },   -- counts, for the picker line and analytics
}
```
The sanitizer checks three things:
- `catId` is known;
- `coat` is one of the two;
- `doneAt` is a number no later than startedAt + the longest time.

**Remotes** (one call a second each, tier and range checked, everything checked again inside the save update):
- `StartFusion(uids: { string }, keepTraitUid: string?)`:
  - exactly `FusionCopies` distinct uids;
  - all owned, same catId and same coat (nil for normal, then "gold");
  - none locked, working, at the spa, pending a trait or in a trade;
  - the dome is free;
  - `keepTraitUid` is one of the uids and has a trait, or nil.
  - The five leave the save and `running` is set from the best-level copy.
- `CollectFusion()`: once `doneAt` has passed, it adds the new instance (a new uid), sets the coat's collection entry if new, counts `made` and clears `running`.

**PlayerState.fusion** (the window's view; nil below the tier or while the switch is off; the client sends `s.fusion or false`):
```
{
  running = { catId, coat, doneAt, level, name?, trait? }?,   -- trait = { id, rarity } for the card
  ready = boolean,                                            -- running and doneAt passed
  goldSeconds = number, rainbowSeconds = number,              -- after Elder Lore
  made = { gold = number, rainbow = number },
}
```
The window works out the ready and almost lists from `PlayerState.cats` with the same busy rules, so the server sends no list.

**Switch:** `LiveFlag_fusion`. It ships with the Snowy Mountain update and its restart.

**Analytics** (counts only, never who):
- `fusion_start`, with coat and rarity;
- `fusion_collect`, with coat and rarity.

## 5. QA checks
1. Five normal copies give one gold copy of the same cat after 10 minutes, offline time included. Five gold copies give one rainbow after an hour.
2. The result has the best level of the five and its XP. With traits, the picked trait stays and the others go.
3. Refused: 4 or 6 uids, a uid twice, mixed cats or coats, a rainbow input, and a locked, working, spa, pending or trading copy. Also refused: a second start while the dome is busy, and another player's or a made-up uid.
4. Collect before `doneAt` is refused. Collecting twice gives one cat.
5. A first rainbow from fusion lights the Index's rainbow entry and its track step once.
6. Pace.spec: tier times are unchanged (the station opens at Tier 8). Check the Index rainbow track's late milestones don't all land in the first hour of Tier 8. If they do, raise `FusionRainbowSeconds` or the copies.
