# Phones: what the first minute can lose (Design-Agent, 2026-11-17 15:20 UTC)

Growth: phones take 19.6 s to load and run at about 43 FPS (health_fps, about 150 s in).

## Load: wait for the Nov 18 read first
The 19.6 s is from Nov 16 data. Since then, #5070 runs the pass lookups side by side (live 11:41 UTC Nov 17; Sync measured 8.1 s down to 3.4 s to "loaded"), and fxAfterLoad (on 14:01 UTC) holds Effects and Audio until the loading screen ends. Read client_load and client_boot by device on Nov 18 before cutting more. If phones are still over 12 s, the next cut is the UI build: build only the HUD, the tutorial strip and the Cannon window first, and the other screens on first open.

## Frame rate: measure, then cut in this order
Effects already run the lighter budget on every phone (fxLite is retired and shipped), so Effects are not the first suspect. Ask Sync for one Studio phone-profile MicroProfiler capture in Town and in the Alleyway at about 60 s on a fresh save, with the top 5 costs. Then cut from this list. It is ordered by what players lose least.

Allowed on phones (Design OK, no need to ask again):
1. Other players' cafes: beyond about 60 studs, the working cats and customers stop animating (they hold a pose), and the customers' walk-in queue is skipped. A player looks at their own cafe.
2. Customers in your own cafe: at most 3 seated on a phone (the tips are the same; only the bodies are fewer).
3. Town ambient: shop cats, door signs, bunting, the fountain spray and lawn effects of other plots stay off until the first check-in, then turn on.
4. Far area backdrops: turn backdropsNear on (built, #4857) unless instance streaming is turning on that same week; never both.
5. areaOnly (#5027) once Sync's census shows the win: cafes stream per owner.
6. Shadows on small props and cats: off on phones (cats keep a blob shadow if one exists).

Not allowed (they are the game): the player's own cats at their stations, strays in the area the player stands in, catch circles and their timing, the tutorial pointer and the dim, the Rank Up window.

## Read
health_fps by device, with the change's on-minute in the timeline. Target: phones at 50 FPS or better in the first 5 minutes, and phone client_load under 12 s.

## Sync's profile, 15:27 UTC (phone layout, low tier, Studio)
Effects add up to 0.5 ms a frame in Town and 0.8 ms in the Alley, so scripts are not what holds phones at 43 FPS. A fresh save in Town holds 195k instances and 90k primitives, with BaseParts at about 1.7 GB. The lever is world size: GE is finding out why Town holds 195k with streaming on, then areaOnly, backdropsNear and the far-cafe freeze. Small script cuts go to Motion-FX: the PawTrail spike (14 ms) and Tackle while idle.
