# UI best practices (learned on Catch a Cat Cafe)

Most players are kids on phones. Every rule here came from a real fix or a real drop in the funnel.

## Sizing and devices
- Check every screen on a phone (about 844 x 390), a small phone (about 667 x 375), a tablet, a desktop and a 1080p console view. `code/tools/cloudcheck/uigate.mjs` does this without Studio.
- Build sizes from `Scale.luau`, never fixed pixels. Buttons are never squished and pictures never clipped at phone size.
- Draw items big enough to read on a phone. Cats were made bigger twice before players could tell them apart.
- Keep words inside a safe area gui. A gui with `ScreenInsets = None` puts text under the notch; only edge art goes there.
- Every menu scrolls on touch with no spring back. Sideways scrollers get arrows.
- Console: every screen works with a gamepad (`GamepadNav`, `GamepadTabs`, `GamepadHints`).

## Menus
- No menu ever opens by itself. A window the player did not ask for reads as an ad and gets closed unread. The one exception Derek allowed: walking into the cannon after a Rank Up opens the area picker with the new area pointed at.
- Build every menu on `MenuFamily` tokens (`MenuFamily.pal`, `MenuFamily.card`), never hard coded colours, so a theme change is one edit. The live theme is cocoa brown; purple read as cluttered and near black was swapped back.
- One clear job per menu. Store words say exactly what you get: numbers, durations, contents. Was prices and worth tags must be real.
- Anything claimable or ready shows a "!" or a highlight. Anything you cannot afford or use is grey, not active.
- Menus react at once: no dwell, no slow polls, pictures preloaded rather than loaded on open.
- Renames reach every label. Stale names were a repeated bug.

## Tutorials
- Dim plus arrow, and the player taps. Dim the screen, point one arrow at the one thing to press and wait. Never press it for them and never open the menu the step is about.
- Every tutorial or first session change ships behind an off switch (`LiveFlags`) so it can be rolled back in a minute.
- Scenes are short with no skip, or they are cut. The bait scene is 1.3 s; the arcade and companion scenes were removed.
- Tips sit small at the top, not over the middle of the screen.
- Read the funnel (`code/server/Services/Telemetry.luau`, `code/shared/StartFunnel.luau`) after every change to the first five minutes.

## Pop ups
- Use the two clean templates: `Screens/AskCard.luau` (a question with clear buttons and an X) and `Screens/TipCard.luau` (a short tip). Toasts follow `Components/ToastRules.luau` and queue through `TipQueue` and `AskPacing`.
- No pop ups while the store or another full screen menu is open, except warnings and purchase confirmations.
- Every new pop up type is gated (busy, calm) and rate limited or switchable.

## Luau UI traps
- A `UIGradient` on a TextLabel or TextButton tints its text too. Put the letter on a child label.
- A Luau function can hold only 200 locals. A big UI `init.luau` hits that; hang new state on a table instead.
- `Tween.popIn` reuses a frame's first `UIScale` and cancels tweens on it. Looping scale tweens must restart themselves.

## Young audience
- Odds are always shown on anything random. No dark patterns: no fake timers, no fake was prices, no guilt wording.
- Filter all player text.

## Review checklist for every UI change
1. Phone size: scrolls, arrows, nothing squished or clipped.
2. Responsiveness: no visible wait.
3. Pop up noise: nothing over full screen menus, new types gated.
4. Next step cues: "!" on ready, grey on not affordable.
5. Clear wording: exact rewards, true numbers, no stale names.
