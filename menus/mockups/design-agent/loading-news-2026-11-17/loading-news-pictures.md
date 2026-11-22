# Loading screen WHAT'S NEW pictures (#5114, Design-Agent, 2026-11-17 15:40 UTC)

Derek, 15:24 UTC: "for loading screen make it better images/models of how recent updates are shown". Low priority: it comes after the Harvest fold (Wed Nov 18) and the switch work.

## The frame (Screens/Intro, main)
- The picture box is 288 x 124 design px (card 320 x 286, rounded 14). The card only shows when the screen is 860 design px or wider, so most phones in portrait never see it. Keep the picture count small.
- Render at **576 x 248 PNG** (2x), under about 150 KB each. The box is short and wide (about 2.3 : 1), so put one hero in the middle third and keep the left and right edges as background only.
- No text in the picture. The card already carries the title, line and when.

## Cards (LoadingNews.ENTRIES now, plus the next two)
| key | Picture (real models, store art look) |
|---|---|
| worlds | Three slices side by side: a Snowy Mountain slope, Water Park rides, Castle walls, with one area cat in each |
| rift | The Rift Run portal glowing, with a cat in front holding a Mythic trait glow |
| outfits | Three cats in a row in the Winter, Chef and Space outfit packs |
| secret | Dark cat shapes only, with a #E2D6FF rim on #16161D (dark-shape rule for in game) |
| devices (new, Better on Every Device) | A cafe cat with a generic phone, tablet and gamepad (from Model-Agent's devices poster, no brand shapes) |
| harvest (new, Wed Nov 25) | The Harvest arch with pumpkins and two harvest cats (crop of the #5090 launch art) |

Never use the wooden crate with the gold cat coin. Use Classic Crate if a crate shows at all.

## UI side (Motion-FX or GE, whoever is free)
- LoadingNews.Entry gets an optional `image: string?` (rbxassetid). When it is set, Intro shows it as an ImageLabel (ScaleType Crop) in place of the tiles.
- Until the image is loaded (ContentProvider, or IsLoaded on the label), show the old tiles. The loading screen never waits for a picture.
- Preload only the first card's picture. The others load while the first one shows.
- Spec: an entry with `image` still needs `tiles` as the fallback (or `secret`). Add a uigate scene for the card with an image, on tablet and desktop.

## Order
Model-Agent renders and uploads (asset ids in a list in the issue). Then the UI field, then the entries get their ids. Add `devices` and `harvest` entries to LoadingNews with their `at` and `flags` when the pictures come in.
