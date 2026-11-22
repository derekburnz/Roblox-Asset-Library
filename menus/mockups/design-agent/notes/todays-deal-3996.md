# Today's Deal (#3996)

Status: spec by Design-Agent, 2026-11-14 03:55 UTC, from Growth-Agent's proposal (Growth-Agent/spend-days-daily-deal-2026-11-14.md). Picks are under Derek's overnight OK ("go with your recommendations"); he can change any of them.

Builders:
- Gameplay-Engineer: the products, ProcessReceipt, the once-a-day record, the switch and telemetry.
- Design-Agent: the card on the Store's Featured tab.

Why: Home counts spend days, not amounts. Nothing in the Store changes from day to day, so a payer has no new reason to come back to it. A small fixed deal that changes each UTC day gives one.

## 1. Policy (monetization-policy skill)
- **Fixed contents, fixed price.** Nothing random is sold by the card itself, so it needs no odds of its own.
- **Trait Tokens are rolls**, which are paid random items. The token deal follows the Trait Token bundles' rule (#3864): it is never offered where `ArePaidRandomItemsRestricted` holds, and the Mystic Pool's odds list stays one tap away from where tokens are spent. Those players get deal 1 on that day instead.
- **No pressure.** No ticking countdown, no "only today", no "last chance", no flashing, no pop-up that opens the card, no reminder after a decline. The card never shows outside the Store.
- **Honest value line.** The card says what is in it and its price in Robux before the prompt. It may say "More than Potion Pack S" only where that is true by count (section 2).
- **Young audience.** Nothing about streaks or buying on several days. No word that suggests the player loses something by not buying.

## 2. The four deals
All R$25 (the price of Potion Pack S and the Steady Paw Pack). Rotation by UTC day number: `os.time() // 86400 % 4`.

| # | Contents | Count | Next normal pack | Value |
|---|---|---|---|---|
| 1 | 5 Big Money + 2 Swift Potions | 7 | Potion Pack S: 5 potions, R$25 | 1.4x |
| 2 | 7 Trait Tokens (traitBundles on, not restricted, room in the token bank) | 7 | 20 tokens for R$99 (5 per R$25) | 1.4x |
| 3 | 10 Steady Paw + 2 Big Money Potions | 12 | Steady Paw Pack: 10, R$25 | 1.2x, and two Big Money on top |
| 4 | 4 Big Money + 1 Swift + 2 Steady Paw Potions | 7 | Potion Pack S | 1.4x |

Deal 4 is one Swift less than Growth's draft, so every potion deal sits at about the same 1.4x and none undercuts Potion Pack M (10 for R$49) per potion.

Deal 2 falls back to deal 1 for a player who can't get tokens (switch off, restricted, or the bank too full for 7). The server decides which one a player sees, and the receipt pays only that one.

## 3. Who sees it
- Tier 2 and up, so the first minutes stay quiet (#3887).
- Not while the `dailyDeal` switch is off (ships off).
- Once per player per UTC day. After the buy the card stays and reads "Bought today. A new deal comes tomorrow." with the Buy button gone.

## 4. The card (Store, Featured tab)
- Revised 04:25 UTC while building (#4146): an unbought deal is Featured's hero card, and the usual hero leads the picks. A pick on a 667x375 phone has room for one line, and the token deal's odds must be on the card itself. Once bought, the deal drops to the first pick ("Bought today").
- **Title:** "Today's Deal".
- **Contents:** the potion or token icons with counts, as the pack cards show them ("5 Big Money · 2 Swift").
- **Value line:** "7 potions for R$25, more than Potion Pack S" (deal 3: "12 potions, 2 more than the Steady Paw Pack"; deal 2: "7 Trait Tokens, more than the 20 pack gives for R$25").
- **Change line:** "A new deal each day at 7:00 PM" in the player's local time (UTC midnight), as plain text that never ticks.
- **Tomorrow line:** "Tomorrow: Steady Paw deal". Saying what comes next takes away the fear of missing today's and lets a player wait for the one they want.
- **Buy button:** "R$25", the normal one-tap Roblox prompt. No second confirm, as the other packs.
- On a phone (667x375) the card keeps every line: the value line may drop to the card's info i before anything is cut.

## 5. Build (Gameplay-Engineer)
- Four developer products `deal_1` to `deal_4`, R$25 each, regional pricing off, made with dev-products.yml and named in Config.ProductIds and products.json like the Trait Token bundles.
- `PlayerState.dailyDeal = { deal = n, bought = boolean, tomorrow = m }` or false; the client sends it as `s.dailyDeal or false`.
- The prompt opens only for today's deal and only when `bought` is false (the server checks before `PromptProductPurchase` and refuses with a toast otherwise).
- ProcessReceipt: grants the deal that was today's when the receipt was made (receipt day from `PurchaseId` time or the server clock at receipt), records `profile.dealDay = day`, and pays once per PurchaseId as every product does. A receipt for a deal that was not that day's is still paid (Roblox took the Robux) and logged.
- Telemetry: the store funnel's sku `product_deal_n`, and a `deal_bought` event with the deal number and the tier. Counts only.

## 6. QA checks
1. Tier 1: no card. Tier 2 with the switch on: the card shows today's deal and tomorrow's name.
2. Buy: the contents land, the card turns to "Bought today", a second prompt cannot open that day.
3. At UTC midnight the next deal shows without a rejoin, with no countdown on screen at any time.
4. A restricted-policy player, or one with traitBundles off or a full token bank, gets deal 1 on token day, and its receipt pays deal 1.
5. Phone 667x375 and PC: every line fits, nothing overlaps the Featured cards under it.

## 7. How we judge it (Growth-Agent)
Spend days per payer and payer conversion over 7 days, against the 7 before the switch went on. Also the share of deal buyers who buy again within 3 days, and whether Potion Pack S and Steady Paw Pack sales drop.
