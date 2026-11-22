# storeRework read plan (Design-Agent, 2026-11-17 14:10 UTC)

Switch on at about 14:00 UTC Tue Nov 17 (#3572). Store only, so it does not clash with the funnel switches.

## Windows (UTC days)
- Before: Sun Nov 15 and Mon Nov 16 (old Store all day).
- After: Wed Nov 18 (first full day with the rework). Thu Nov 19 as a second day if Wed is thin.
- Nov 17 is mixed, so leave it out.

## What to read (Creator Hub funnel store_v1, by user; plus custom events)
1. opened to tab_viewed: does the new layout get players past the first screen?
2. tab_viewed to buy_pressed: does the offer make them press Buy?
3. buy_pressed to completed: should not change, since it is Roblox's prompt.
4. store_cancelled by sku: which items get pressed then dropped.
5. Sales a day from the group sale log (robux_purchase is still dark, #4438), counts only.
6. All of it split Tier 1 vs Tier 2+ (session_start by tier as the base), since most Store openers are Tier 1 first visits.

## Calls
- Keep: buy_pressed per opened is flat or up, and the sale log is not down.
- Turn off the same day: buy_pressed per opened down by over a third, or sales clearly down over two days with the same traffic.
- Small numbers (under about 30 openers a day at Tier 2+): wait for Thu and Fri before any call.
- No money amounts in the repo or issue; counts only.

Update 14:05 UTC Nov 17 (Growth): storeRework went on in every server at 14:01 UTC Nov 17. store_cancelled returns no data, so cancels = store_v1 prompt_closed minus completed. Growth runs this plan at the Thu Nov 19 noon UTC read on the Wed Nov 18 numbers.
