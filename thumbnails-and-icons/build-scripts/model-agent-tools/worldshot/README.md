# worldshot: render and overlap-test the world as the game builds it (Model-Agent, 2026-11-11)

Made for #3349 (clipping). Works in a cloud session, no Studio.

1. Build the world's parts list with colours. In `games/cat-cafe/tools/cloudcheck` (after `npm ci`), add two local
   edits that are never committed:
   - `world-shim.luau`, in `dumpParts` after `table.insert(fields, assetName)`: append the part's colour,
     `local col = p.Color; table.insert(fields, if col then string.format("%.3f,%.3f,%.3f", col.R, col.G, col.B) else "")`.
   - `worldscan.mjs`, after it writes `world-parts.tsv`: `if (process.env.PARTS_ONLY) process.exit(0);` (the full scan
     runs out of memory with seven areas).
   Then `PARTS_ONLY=1 node worldscan.mjs --out <dir>` (about 6 minutes) and `git checkout` both files.
2. Render a region: `python worldshot.py -- <dir>/world-parts.tsv OUT "x0,x1,z0,z1" cams.json` (bpy venv). Cameras are
   in Roblox world studs (`cams_ruins.json` is an example). Colours are the real part colours; Neon glows.
3. Overlap tests: `obb.py` has `load`, `sat` (true box against box, any turn) and `hits(A, B, shift, shrink)`.
   `boards2.py` tests every Index Board against everything near it at several moves; `crate.py` does one Alley crate.
   A negative `shrink` asks for clearance (-0.25 means at least 0.5 studs apart).
4. Whole-world audit: `python audit.py <dir>/world-parts.tsv 0.15` prints a table of every pair of placed models
   whose visible parts sink into each other (deepest first, about 2 seconds). Ignore the CampBasket rows (the scan's
   stand-in Roblox builds a second basket) and ground-level footings in floor slabs. `detail.py` lists the parts of
   one pair; `trap.py` searches for clear spots for one model by sliding it.
