# Cherry Blossom moved to spring, Christmas slot (Design-Agent, 2026-11-17)

Derek, 14:29 UTC Nov 17: "move the cherry blossom event to wayy later after christmas because I am thinking about drafting a christmas update between thanks giving and cherry blossom".

## New order
| Update | Dates (UTC) | State |
|---|---|---|
| Harvest Hollow (Thanksgiving) | Wed Nov 25 20:00 to Sun Dec 6 | unchanged, stack folds Wed Nov 18 |
| Christmas update (Derek drafts) | Sat Dec 12 20:00 to Sun Jan 3 20:00 (proposed) | new slot, nothing built |
| Cherry Blossom Grove | Sat Mar 27 2027 20:00 to Sat Apr 3 2027 20:00 (proposed) | moved from Dec 5 to Dec 12; still one week, Tier 2, no group post |

Why these dates: Christmas opens six days after Harvest closes, so the Town is never dressed for two seasons at once. It covers the whole school break, Christmas Day and New Year, which are the busiest weeks of the year on Roblox. Cherry Blossom lands at peak bloom season, and spring fits its "Back next spring" sign.

## Christmas update sketch (for Derek to draft from; all of it is a suggestion)
Same shape as Harvest Hollow, so most of its code, switches and date gates can be reused:
- **A limited area through a Tier 2 portal** (working name "Frosty Hollow" or Derek's pick). Snowy streets, a big tree, lights, a gift workshop. It can reuse the Snowy Mountain kit and Harvest's portal and date gate.
- **About 10 festive cats** that players keep, scaled two rarities lower like Harvest's, plus one Secret.
- **An event currency** (snowflakes or bells) from catches and a patch, and a stall of items to keep. Use Harvest's fixed economy pace from day one: about 1,440 for everything, with regrow 300 s.
- **A gift calendar from Dec 12 to Dec 25.** One free gift a day and a bigger one on Christmas Day. There is no streak: a missed day only skips that gift. This fits the young audience rules.
- **The Town dressed in lights and snow** while the event runs.
- **One admin event after the restart.** Snow Storm could be a reskin of Cat Storm.
- **Nothing paid that is random without odds.** Any bundle follows monetization-policy.
- Build from about Mon Nov 30, once the Harvest fold is live. Freeze Thu Dec 10.

## What must change because of the move
- **Gameplay-Engineer:** remove the Cherry Blossom Grove entry from `Config.UpdateEvents` (id 6693355219203523122, startsAt 1796500800). Change EventRsvp.spec so that the next update after Harvest is nil, until a Christmas Roblox Event exists. Without this, from Nov 25 20:10 UTC the Notify Me ask, the Town Square update poster and the Thanks board would all say "Next update Sat Dec 5: CHERRY BLOSSOM GROVE". It must merge before the Wed Nov 25 publish. When Growth makes the Christmas Event page, add it with its id and Sat Dec 12 20:00 UTC (1797105600).
- **Growth:** move or cancel the Cherry Blossom Grove Roblox Event page (Dec 5 to Dec 12). Make the Christmas Event page once Derek names it. Update the placeholder file and the Harvest launch pack if they tease Cherry.
- **Model-Agent / Motion-FX:** Cherry PRs #4423 and #4446 stay closed with their branches kept. Merge main into them about Mar 1 2027.
- **Docs:** decisions.md entry and the GDD limited areas line (Design-Agent).

Update 14:35 UTC: Growth moved the Cherry Roblox Event to Mar 27 to Apr 3 2027 (accepted). GE now keeps the Config.UpdateEvents entry and moves it: startsAt 1806177600, title "Sat Mar 27". It no longer removes it.
