# Roblox Asset Library

Reusable assets, code and lessons packed up from **Catch a Cat Cafe** (Nov 22 2026) for the next Roblox game. The game repo is `derekburnz/Cat-Cafe`; the agent setup and workflows starter is `derekburnz/Roblox-Game-Template`, so this library holds what that template does not.

Tags used below: **Generic** works in any game as is, **Reskin** needs new names or colours, **Cat Cafe** is kept as reference.

## Folders

| Folder | What is in it | Tag |
|---|---|---|
| `models/cats/` | 462 cat models (walk, `_Sit` and `_Work` poses, every joint its own pivoted part), 40 accessories, 5 dragons | rig Generic, cats Cat Cafe |
| `models/areas/<area>/` | Whole maps: sets, backdrops, gates, night fences, nooks and camp bases for alley, park, woods, sewer, neighbourhood, town, town square, desert, snowy mountain, castle, ruins, water park, harvest hollow, snowglobe village, cherry blossom grove, rift run, plus the sky | Reskin |
| `models/filler/` | Area filler split into `signs-and-boards`, `lights-and-posts`, `plants-and-trees`, `fences-and-paths`, `street-props` and `decorations` | Generic |
| `models/cafe/` | Shop buildings and plots in four sizes, furniture, doors and cat flaps | Reskin |
| `models/stations/` | Stalls, booths, carts, spin wheel, arcade cabinet, leaderboard row, and `cannons/` for travel | Reskin |
| `models/items/` | Nets, bowls, food and drinks, crates (with golden twins), gifts, treats, props | Reskin |
| `models/npcs/` | Customers (standing and seated), townsfolk, dealer, collector, mystery visitor | Reskin |
| `models/materials-wall-floor-styles/` | 72 wall and floor style models, palette and textures | Generic |
| `models/blender-generators/` | The Python that builds every model above (`common.py` Builder, `palette.py`, `rbx_export.py`, `build_all.py`, QA and contact sheets). Change a palette or bevel and rebuild everything | Generic |
| `menus/luau-ui-kit/` | The whole client UI: `Theme`, `Scale` (phone sizing), `Components/` (MenuFamily, Modal, Panel, Button, gamepad nav, dim plus arrow, toasts) and 105 `Screens/` including AskCard and TipCard | Generic kit, Reskin screens |
| `menus/icons/` | Every UI icon set, store cards, currency icons, area pictures | Reskin |
| `menus/posters-and-loading/` | Update posters, loading screen news, event launch art | Cat Cafe |
| `menus/mockups/` | Design mockups and before and after pictures for every menu (`design-agent/`) | reference |
| `menus/UI-best-practices.md` | The written UI guide | Generic |
| `thumbnails-and-icons/` | Game icon history, Home thumbnail sets, all dated store art, the build scripts, the Home results reads, and `RESULTS.md` with what worked | lessons Generic |
| `effects/` | `luau-effects/` (tween and particle presets, guide arrow, cutscene shell, rarity glow, sky, card flips, cat motion), headless animation preview, trailer camera rig | Generic |
| `code/` | Saving (ProfileStore, DataService, schema), typed remotes with rate limiter and guard, telemetry funnels, products and passes, codes, leaderboards, daily and playtime gifts, bug reports, perf watch, live flags, test kit, cloud checks (UI gate), Open Cloud scripts and every GitHub workflow | Generic after renames |
| `audio/` | 82 original sounds and music made from code (`synth/`), the upload script, audio gate and the client audio module | Generic, all original |
| `guides/` | Style guide (104 swatch palette), bugs never to repeat, module map, save safety, comps, monetization, onboarding funnel, store page, analytics plan | reference |

## How to use a model
- `.model.json` files are part built Roblox models. Drop one into a Rojo project (for example under `ReplicatedStorage.Assets`) or open it with Rojo. No uploads needed, so they work in any game.
- `.fbx` files are the mesh version. Import in Studio with the 3D Importer, Scale Unit Studs, and save as `.rbxm`.
- To restyle, edit the generator in `models/blender-generators/` and rerun `build_all.py` (needs Blender or the `bpy` pip module).
- GLB copies were left out; `build_all.py` rebuilds them.

## Ids and secrets
No secrets are in this repo. The universe, place and group ids were taken out: workflows read `vars.ROBLOX_UNIVERSE_ID`, `vars.ROBLOX_PLACE_ID` and `vars.ROBLOX_GROUP_ID`, shell scripts stop unless the id is set, and docs say `<UNIVERSE_ID>`, `<PLACE_ID>` or `<GROUP_ID>`. Uploaded Roblox asset ids (icons, sounds) belong to the old group and will not load in a new game until re uploaded.

## To start a new game from this
1. Set up the game repo from `Roblox-Game-Template`.
2. Copy `code/` modules you need into `src/`, rename `CatCafe` prefixes, and move workflows from `code/workflows/` to `.github/workflows/`.
3. Copy `menus/luau-ui-kit/Theme.luau`, `Scale.luau` and `Components/` first; build screens on `MenuFamily`.
4. Pull models by folder and rebuild with new colours from `palette.py`.
5. Read `menus/UI-best-practices.md` and `thumbnails-and-icons/RESULTS.md` before the first menu and the first icon.
