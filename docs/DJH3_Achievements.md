# DJ HERO 3 — Achievements FINAL (50 / 1000G)

> Aligned to the DJH2 retail list (50/1000G, TrueAchievements
> reference). `←DJH2` = carried/evolved. `NEW` = DJH3-only.
> Scaffolding: 109 medals + criteria, trophy tracker UI, hint
> strings, engine attributes, TrackList registry.
>
> Hard rule learned from retail: 8 DJH2 achievements DIED as
> discontinued (all online-dependent). Nothing here requires servers.

## Empire (9 — 220G)

| Name | How | G |
|------|-----|---|
| Opening Act | Play your opening night in Empire | 10 |  <!-- ←DJH2 -->
| Ibiza Nights | Clear the Ibiza club | 20 |
| Headliner | Clear every Empire club | 85 |
| Five Star General | 5-star any Empire set | 15 |
| Perfectionist | 5-star 10 Empire sets | 30 |
| Bonus | Unlock all the Empire bonus mixes | 20 |  <!-- ←DJH2 -->
| Rise To The Challenge | Complete 3 Empire Setlist Challenges | 15 |  <!-- ←DJH2 -->
| Dance Commander | Win a Dance Battle | 10 |  <!-- NEW -->
| Dancer vs DJ | Win as dancer AND as DJ | 15 |  <!-- NEW -->

## Performance (9 — 120G)

| On a Roll | 50-note streak | 5 |
| Centurion | 100-note streak | 10 |
| Double Up | 200-note streak | 15 |
| Triple Threat | 300-note streak | 20 |
| Precision Cuts | 300 perfect-timing notes | 10 |
| Metronome | 1000 perfect-timing notes | 20 |
| Euphoria! | Trigger Euphoria 10 times | 10 |
| Euphoric | Trigger Euphoria 100 times | 25 |
| Spinback King | Nail a spinback inside the window | 5 |  <!-- s_fSpinBackAchievementTimeLimit -->

## Technique (5 — 90G)

| Scratching The Itch | 25,000 scratches | 20 |  <!-- ←DJH2 -->
| Fades Of Fury | 20,000 crossfades | 20 |  <!-- ←DJH2 -->
| Tappity Tap Tap Tappy | 50,000 taps | 20 |  <!-- ←DJH2 -->
| Fader Master | Complete a mix hitting every crossfade | 15 |
| To The Left | Only crossfade left in all Freestyle sections, any mix | 15 |  <!-- ←DJH2 -->

## Battles (9 — 230G)

| Challenger | Play 5 battles | 5 |
| You Want Some? | Complete 30 battles | 15 |  <!-- ←DJH2, offline-countable -->
| Battle Royale | Play 200 battles | 30 |
| Winner | Win your first battle | 10 |
| Battle Star Spectacular | 50 battle wins | 55 |  <!-- ←DJH2 -->
| Streaker | 5 consecutive wins | 15 |
| Mix Master | 100 mix wins | 25 |
| Encore | Clear Ibiza02 Encore | 45 |  <!-- NEW, our setlist -->
| Studio Session | Clear the Studio vocals club | 30 |  <!-- NEW, our club -->

## Modes (7 — 110G)

| The Emperor | Win all DJ Battle setlists in Empire | 20 |  <!-- ←DJH2 -->
| Big Bad Boss | Beat all employee-DJ Checkpoint Battles in Empire | 15 |  <!-- ←DJH2 -->
| Professional Face Removal | Win 5 Star Battles | 15 |  <!-- ←DJH2 -->
| Mama Said... | Win a Checkpoint Battle by knockout | 10 |  <!-- ←DJH2 -->
| Accumulate! | Win 10 Accumulator mixes with a 50+ streak | 15 |  <!-- ←DJH2 -->
| Like Bacon? | Win 6 Streak mixes by a 20-streak margin | 15 |  <!-- ←DJH2 -->
| Twin Decks | Win a battle in Twin Deck mode | 20 |  <!-- NEW -->

## Collection (5 — 120G)

| Fashion Icon | Unlock 20 costumes | 20 |
| I Have The Power Decks! | Unlock all the Power Decks | 15 |  <!-- ←DJH2 -->
| Full Deck | Unlock every DJ | 20 |
| Archivist | Play every mix in the game | 50 |
| Ghostbuster | Win a Ghost Challenge | 15 |  <!-- NEW -->

## Vocals (4 — 75G)

| Perfect Pitch | 100% of vocal notes in a mix | 15 |  <!-- ←DJH2 -->
| Microphonical Magic! | 200 vocal streak in any vocal mix | 15 |  <!-- ←DJH2 -->
| Go Crazy Broadway Style! | Perform vocals in every supporting mix | 30 |  <!-- ←DJH2, now shippable -->
| The Magic Number | Play a mix with another DJ and a Vocalist | 15 |  <!-- ←DJH2 -->

## Secrets (2 — 35G)

| Secret Achievement | Find the secret (their literal string) | 25 |
| Credit Is Due | View the game credits | 10 |  <!-- ←DJH2 -->

## Total

220 + 120 + 90 + 230 + 110 + 120 + 75 + 35 = **1000G, 50 achievements.**
Carried from DJH2: 24. New: 26.

## QA + alternates

- Medal/tag debug flags exist in attributes (`s_bUnlockMedalsAndTags`,
  `s_bUnlockRandomMedalsAndTags`) — same QA class as `UnlockAll*`.
- Cut in favor of the final 50 but viable swaps: CombatVeteran (battle
  count), PFO battles, HigherGrade wins, Contender, Button Masher,
  Crate Digger, New Threads, En Sink. All sourced from the same
  scaffolding.
