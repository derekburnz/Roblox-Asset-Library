# Day 1 hooks, top 3 (Design-Agent spec, Nov 18 2026)

Derek, Nov 18 16:58 UTC: "my d1 retention is really bad and we need to figure out how to help whether that is obvious that cats earn offline or what". D1 is 2.7% against a 12 to 15% bar (#5285).

What we have today is all words on cards: the welcome back card, the money card's "Cats earn while away" line, the minute 6 line, the tomorrow card (#3951) and the recap. Most new players are gone by minute 5, and a player who closes the app never sees a recap. So the three hooks below are **things in the world, seen while playing**, plus the one channel that reaches a player after they leave (notifications).

All three ship behind their own switch (off by default; they touch the first session). None has a timer that counts down to a loss, none says "you'll lose", and none is paid. Players tap every step themselves.
Mock: d1-hooks-mock.png in this folder.

## 1. Away Jar (switch `awayJar`)
**What it is:** "cats earn offline" shown as a number and an object.
- **HUD chip** under the coins from minute 3 of the first session (after QuietStart's hold): "💤 While you're away: +$X by tomorrow". X is `Economy.offlineGain` for the full cap at the current day rate (8 h at half pay, or 16 h at full pay with Long Nap). It updates each time income changes, so buying a cat makes it visibly jump. It does not count down. On phones it is one line, and shortened to "💤 Away: +$X".
- **Away Jar** on the cafe counter (Model: a glass tip jar, `CatCafe_Prop_AwayJar`). It fills from 0 to full as X climbs from the first-session figure to the cap of the current tier. That is only a look, so nothing is stored.
- **On return** (only when the welcome back card would show anyway): coins are piled beside the jar. The welcome back card gets one "Collect" button (gold), and the coin burst flies from the jar to the coin counter. The same amount is paid as today, with no change to the economy.
- **Data:** nothing new is saved. The client works it out from state it already has.
- **Read:** D1. Also check the share of first-session players who saw the chip.

## 2. Sleepover Bowl (switch `sleepoverBowl`, save field with a version bump)
**What it is:** a cat of their own, waiting for them tomorrow.
- **Who:** an account's first UTC day only, once. It is offered after the first bowl cat is tamed and when the player is calm (no window, card, catch or cutscene).
- **Card:** "Leave a Sleepover Bowl out? A Rare or better cat will be sleeping in it when you come back." The buttons are "Fill it, free" and X. The player taps. Nothing opens by itself.
- **Fill:** a second bowl appears beside the cafe with a dark-shape cat curled in it and the tag "Arrives tomorrow". Following the secret cats rule, the player sees a shape and the rarity colour only.
- **Server:** at fill, the server rolls a cat from the player's unlocked areas, Rare or better, using the bowl's odds with a Rare floor. It saves the id and `readyAt = fill time + 4 h`. The cat is claimable on the first join at or after readyAt. On that join, a short reveal plays (the bowl cut, "Your Sleepover cat woke up!"), and the player taps Tame. If they come back earlier, the tag still says "Arrives tomorrow", with no countdown.
- **Exploits:** one per account, ever. The server owns the roll and readyAt. Leaving and rejoining cannot reroll.
- **ReturnHook:** add "sleepover" at the top of the recap and early picks ("Your Sleepover cat arrives tomorrow"), and to the join pick ("Your Sleepover cat woke up!").
- **Read:** D1 for players who filled it against players who saw the card and closed it.

## 3. Tomorrow Board: the day 2 prize on the counter, plus Remind me (switch `tomorrowBoard`)
Derek, 17:00 UTC: "Maybe put a mythic cat or something flashy like 500 gold fish on day 2 and make the daily login rewards more obvious".
**What it is:** the Daily Treat as a thing in the cafe, with a day 2 prize worth coming back for. The notification opt-in is offered at the moment it makes sense.
- **The new day 2 prize:** **500 golden fish**, plus today's spin. It replaces day 2's 10 fish. That is enough for one gear piece in the Golden Fish Market (Long Net 320, Backpack 400, Speed Shoes 500), so the card can say "Tomorrow: 500 Golden Fish, enough for Speed Shoes!".
  - **Why fish, not a Mythical:** a Mythical at Tier 1 or 2 would earn far more than anything else the player owns. It would end the early climb (cheapTiers just made it short) and make the Mythical chase mean nothing. 500 fish is flashy and permanent, buys a power-up the player picks, and adds no income.
  - **Fair:** it is paid once per account, since stamps never reset. It is earned only, never random and never for Robux (golden fish are never sold). Day 7 stays the top day by crate, Star Treat and fish. The 500 is bigger than day 7's 30 fish, so Growth should watch whether day 3 to 7 returns drop. If they do, raise day 7 instead of cutting day 2.
  - The Sleepover Bowl (hook 2) already covers "a cat waiting".
- **Who sees the board:** everyone, from minute 4 of the first session. On a new account's first day it is the main "come back" thing.
- **The Daily Treat Board on the cafe wall** (Model: `CatCafe_Prop_TreatBoard`) has 7 paper tags, Day 1 to Day 7, with pictures.
  - Today's tag is stamped.
  - Day 2 glows gold with a fish pile and "Tomorrow".
  - The welcome back golden crate (ReturnGift) sits wrapped under the board with "Opens tomorrow".
- **Tap the board or the gift:** a card shows the 7 days in a row, day 2 big. It reads "Tomorrow: 500 Golden Fish and a golden crate."
  - If `CanPromptOptInAsync` is true, a gold **Remind me** button calls `PromptOptIn`. Otherwise there is just OK.
  - The card shows at most once a session, and never again after the player answers Remind me.
- **HUD:** the Daily Treat button gets a gold dot and a "1" whenever a stamp is due. On return, the board's day tag glows and a soft arrow points at the button. The player taps Claim, and nothing opens by itself.
- **The AwayNotify message on day 2:** "Your 500 Golden Fish are ready!", or, if there is a Sleepover cat, "Your Sleepover cat woke up and 500 Golden Fish are waiting!". It is one message, inside Roblox's once a day.
- **tomorrowCard:** the board replaces the tomorrow card for that player, so the same words don't show twice. ReturnHook's "treat" line names the fish.
- **Data:** the new day 2 prize is Catalog data behind the switch (follow pattern, as CheapTiers). There is no new save field.
- **Read:** D1, the opt-in rate, and the share of first-day players who tapped the board.

## Order and timing
- Build 3's prize change and HUD dot first (the cheapest and the most obvious, matching Derek's ask), then 2 (the biggest pull), then 1, then the board model. Model needs three props: the jar, the Treat Board and the wrapped gift. The Sleepover Bowl reuses the bowl model with a second colour.
- Switch them on a day apart, 2 h away from any other switch, so Growth can read each one (#5107). These are first-session changes, so each ships with its off switch, per Review-QA's rule.

## Considered, not top 3
- A 7 day streak calendar preview. Daily Treat already covers it. It could be a later upgrade to show day 2's prize on the counter too.
- Showing "come back tomorrow" text earlier. We already have three versions of this, and the words aren't landing.
- Pal Day and tomorrowCard are already built. They stay as they are.
