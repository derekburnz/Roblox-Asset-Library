# Christmas Advent Calendar (Design-Agent spec v1, Nov 19 2026, #5502)

Derek, Nov 19 21:59 UTC: "Setup a christmas advent calendar with limited christmas cats that are as good as secrets along it and some really good rewards so people come back (make sure it doesn't accidentally start until proper date)".

Goal: D1 and D7 through December. One door a day gives every player, new or old, a reason to open the game tomorrow.

## 1. Dates and the two locks
- Door 1 opens **Tue Dec 1 2026 20:00 UTC**, with Snowglobe Village. Doors 2 to 24 open at 00:00 UTC on Dec 2 to Dec 24.
- Doors can be opened until **Sun Jan 3 2027 23:59 UTC**. After that the board goes and everything earned is kept.
- **Lock 1, the dates.** The server decides which doors are open from its own UTC clock against dates in the calendar's config row. The client's clock is never used. Before Dec 1 20:00 UTC the server answers every open with "not yet" and pays nothing.
- **Lock 2, the switch.** `adventCalendar` (LiveFlags, off by default). It also needs `christmasEvent` on. Either one off hides the board and refuses every open.
- **No test override on live.** A date override exists only in Studio and through the owner test service, never from a flag or a remote.
- **Spec tests that must exist:** for every time before Dec 1 20:00 UTC, zero doors are open with both switches on; with either switch off, zero doors are open at any time; door N is never open before its date; nothing opens after Jan 3 23:59 UTC.

## 2. Where it is
- A big calendar board in **Town Square beside the giant snow globe**, with 24 numbered doors. Any tier can use it, Tier 1 included, so brand new players get it on day one. It is not inside the village.
- The Christmas event chip on the HUD opens the same calendar card from anywhere. The chip shows a small dot when a door is ready.
- Not shown in a new player's first 4 minutes (the quiet start). No pop-up ever: the dot and the board are the only signs.

## 3. Rules
- One door per UTC day opens "on time". Opening is one tap on the door, then the prize shows with the normal prize toast.
- **Missed doors are not lost.** A player can open every door that is on time today, plus **one earlier missed door a day**. A player who starts on Dec 20 still finishes all 24 by Jan 3.
- The four cats sit behind doors 6, 12, 18 and 24, so they need that many doors opened in order. Doors open in number order only.
- Every door shows its prize before it opens (dark shape only for the cats, the secret cats rule). Nothing is random. Nothing is sold, sped up or skipped for Robux.
- No streak and no countdown clock. A door that is not open yet shows its date ("Dec 9").

## 4. The four calendar cats (limited, as good as Secrets)
Only from the calendar, only this Christmas. Kept forever.
- **Rarity shown:** Secret, with the Secret night tile and starlight edge.
- **Earning:** each earns like a Secret from the owner's newest open area, the same "newest area" rule the Royal Cat uses, so it stays strong as the player climbs.
- They count toward no Index page, total, track or reward. They can't be traded or fused and can't move into the Dragon Keep (add all four ids to `DragonKeep.eventCat` before Dec 1). Gold and rainbow coats do not roll on them.
- A cafe that is full gets the cat in the cat room, never lost.

| Door | id | Name | Role | Look notes for Model | Line |
|---:|---|---|---|---|---|
| 6 | peppermint_swirl | Peppermint Swirl | waiter | white with a red spiral from nose to tail tip, a round peppermint on the collar, faint mint sparkle | Spins three times before every nap. |
| 12 | nutcracker | Nutcracker | greeter | red soldier jacket with gold buttons, tall black hat with a gold band, white whisker moustache | Stands guard by the door, very seriously. |
| 18 | northern_lights | Northern Lights | entertainer | deep night blue coat with slow green and pink aurora bands that glow at night | The sky followed it home one winter. |
| 24 | silent_night | Silent Night | barista | midnight blue to silver gradient, tiny stars along the back, a soft halo of falling snow around it | Arrives with the first quiet snow on Christmas Eve. |

## 5. The 24 doors
Prizes use the fields Payout already pays, plus Snowflakes (the event currency, a new prize field for GE). Bigger gifts land on Sundays and before each cat so the next day always looks worth it.

| Door | Date | Prize |
|---:|---|---|
| 1 | Tue Dec 1 | 100 Snowflakes, spins 3 |
| 2 | Wed Dec 2 | fish 150 |
| 3 | Thu Dec 3 | potions: lucky_potion 2 |
| 4 | Fri Dec 4 | coinSeconds 3600 (an hour of income) |
| 5 | Sat Dec 5 | crates: highest_golden 2 |
| 6 | Sun Dec 6 | **Peppermint Swirl** |
| 7 | Mon Dec 7 | 150 Snowflakes |
| 8 | Tue Dec 8 | fish 250 |
| 9 | Wed Dec 9 | traitTokens 5 |
| 10 | Thu Dec 10 | spins 10 |
| 11 | Fri Dec 11 | crates: highest_golden 3 |
| 12 | Sat Dec 12 | **Nutcracker** |
| 13 | Sun Dec 13 | fish 400, 150 Snowflakes |
| 14 | Mon Dec 14 | coinSeconds 7200 |
| 15 | Tue Dec 15 | potions: lucky_potion 2, swift_potion 2 |
| 16 | Wed Dec 16 | traitTokens 10 |
| 17 | Thu Dec 17 | crates: highest_golden 4 |
| 18 | Fri Dec 18 | **Northern Lights** |
| 19 | Sat Dec 19 | fish 500 |
| 20 | Sun Dec 20 | spins 15, 200 Snowflakes |
| 21 | Mon Dec 21 | coinSeconds 14400 |
| 22 | Tue Dec 22 | traitTokens 15 |
| 23 | Wed Dec 23 | crates: highest_golden 5, fish 500 |
| 24 | Thu Dec 24 | **Silent Night**, fish 1000 |

Totals besides the cats: 2,800 golden fish, 28 spins, 14 top golden crates, 30 trait tokens, 600 Snowflakes (a third of the Gift Stall) and 7 hours of income. That is about three and a half weeks of the big Daily Treat, on top of it.

## 6. Save and server (GE)
- `profile.advent = { year = 2026, opened = number, extraDay = number }`: the count of doors opened (they open in order, so a count is enough) and the UTC day the last catch-up door was used. Version bump, so it must be published and on servers before Dec 1 with the Christmas restart.
- One remote, OpenAdventDoor, no arguments. The server works out the next door, checks both locks, the date, the order and the one catch-up a day, pays through Payout and saves. Rate limit one call a second. The client's board is display only.
- A year field so next year's calendar starts clean and this year's cats stay unique.

## 7. Telemetry
- `advent_door`: value the door number; fields on time or catch-up, device, account age bucket (first day, first week, older).
- `advent_board`: once a session when the card opens.

## 8. Models and FX
- Model: the calendar board prop (24 doors that swing open, readable numbers at walk-up distance, fits beside the snow globe), four cat models, four dark-shape teaser pictures, four cat icons.
- Motion-FX: a door swing and a small burst on open, a soft glow on the door that is ready, the aurora glow and the snow halo on the two late cats. Phone FX budget applies.

## 9. Schedule (fits the Snowglobe plan)
| By | What | Who |
|---|---|---|
| Thu Nov 19 | This spec | Design |
| Tue Nov 24 | Board prop and four cats merged | Model |
| Wed Nov 25 | Calendar code, save field, both locks and the spec tests | GE |
| Thu Nov 26 | Review-QA pass, publish with both switches off | Review-QA |
| Fri Nov 27 to Sat Nov 28 | Sync's look in Studio with the date override, phone and PC | Sync |
| Sun Nov 29 | `adventCalendar` on with `christmasEvent`. The dates hold it shut until Dec 1 20:00 UTC | GE |

## 10. Checks
- Nov 30 on live with both switches on: no board doors open, the chip shows no dot, OpenAdventDoor pays nothing.
- Dec 1 19:59 UTC: still shut. 20:00 UTC: door 1 opens.
- Skip three days: on return today's doors plus one missed door open, the rest the days after.
- Fresh Tier 1 account: board usable after 4 minutes of play.
- A full cafe at door 6: the cat goes to the cat room.
- The four cats refuse trade, fusion and the Dragon Keep.
- Jan 4: board gone, cats and prizes kept.

## 11. Read
D1 and D7 for the Dec 1 to 7 cohorts against Nov 22 to 30, the share of daily players who open a door, and how many reach doors 6, 12, 18 and 24.
