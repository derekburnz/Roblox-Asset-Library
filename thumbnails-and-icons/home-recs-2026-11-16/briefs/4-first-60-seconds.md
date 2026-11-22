# First 60 seconds in game (Growth-Agent, 2026-11-16)
Data: 35.56% of Home players leave at 61 to 180 s; phone loses most (phone new players 438 left vs computer 162 in the last read); phone waits longest before the first intro shot.
Already in flight (no new issues needed, listed so nothing is dropped):
- Loading screen for everyone with Skip (live v752), client_load and client_fps telemetry (v757).
- #4814/#4817 ignore early hits on the first cat; #4815/#4818 net never scares cats in the tutorial, wider net.
- #4808/#4816/#4820 phone walk to the first Alleyway cat and the pointer at the net; #4307 phone leave read; #4788 streaming for join time.
Added asks (comment on #4307): (1) first catch must land inside 30 s on phone (bait cat arrives, net pointer shows at once); (2) Home players should see a rare cat glow on the first screen (the thumbnail promise: the thumbnails sell a rare catch, so the first minute must deliver one, even a scripted Rare); (3) no card or popup before the first catch.
Read plan: Tue Nov 17 first_circle_hit, first_catch and bolt rate by device; 12:00 UTC load read.
