# DJ HERO 3 — Achievement Design (built off prototype scaffolding)

> Source: November milestone proto (`4156089F`). No XAchievements were ever
> authored — this list is derived from what FreeStyle left behind:
> `OnlineMedalList` (109 medals + criteria), the trophy/medal tracker UI
> (`0087` FAR), hint strings (`0084`: `Secret Achievement`, `?G` template,
> cheat warnings), engine attributes (`s_fSpinBackAchievementTimeLimit`,
> `g_bUnlockAll*` debug flags), and DJH3-only features (Dance Battle).
>
> Shape: 50 achievements / 1000G, mirroring DJH2's structure.
> `Scaffold:` cites the exact proto source for each.

## Empire / Tour (190G)

| # | Name | How | G | Scaffold |
|---|------|-----|---|----------|
| 1 | First Night Out | Complete your first Empire set | 10 | Empire XML clubs |
| 2 | Club Hopper | Complete sets in 3 different clubs | 15 | Empire clubs |
| 3 | Ibiza Nights | Clear the Ibiza club | 20 | `Venue Ibiza01` |
| 4 | Headliner | Clear every Empire club | 50 | Empire completion |
| 5 | Five Star General | 5-star any Empire set | 15 | star ratings |
| 6 | Perfectionist | 5-star 10 Empire sets | 30 | star ratings |
| 7 | Dance Commander | Win a Dance Battle | 20 | `DANCE BATTLE` hint |
| 8 | Dancer vs DJ | Win as dancer AND as DJ | 30 | `DANCER VS DJ` hint |

## Performance (160G)

| # | Name | How | G | Scaffold |
|---|------|-----|---|----------|
| 9 | On a Roll | 50-note streak | 5 | `online_50streaks` |
| 10 | Centurion | 100-note streak | 10 | `online_100streaks` |
| 11 | Double Up | 200-note streak | 15 | `online_200streaks` |
| 12 | Triple Threat | 300-note streak | 20 | `online_300streaks` |
| 13 | Halfway to Heaven | 500-note streak | 30 | `online_500streaks` |
| 14 | Precision Cuts | 300 perfect-timing notes | 10 | `online_perfect_timing` |
| 15 | Metronome | 1000 perfect-timing notes | 20 | `online_perfect_timing` |
| 16 | Euphoria! | Trigger Euphoria 10 times | 10 | `online_euphorias 10` |
| 17 | Euphoric | Trigger Euphoria 100 times | 25 | `online_euphorias 100` |
| 18 | Spinback King | Nail a spinback inside the window | 15 | `s_fSpinBackAchievementTimeLimit` |

## Technique (130G)

| # | Name | How | G | Scaffold |
|---|------|-----|---|----------|
| 19 | Wax Rookie | 1000 scratches | 5 | `online_scratches` |
| 20 | Wax Veteran | 8000 scratches | 15 | `online_scratches` |
| 21 | Wax Legend | 25000 scratches | 40 | `online_scratches 25000` |
| 22 | Crossfader | 2000 crossfades | 10 | `online_crossfades` |
| 23 | Fader Master | 20000 crossfades | 25 | `online_crossfades 20000` |
| 24 | Tap Happy | 3000 taps | 10 | `online_taps` |
| 25 | Button Masher | 10000 taps | 20 | `online_taps 10000` |
| 26 | Spike Driver | 25 crossfade spikes | 5 | `online_crossfade_spikes 25` |

## Battles (220G)

| # | Name | How | G | Scaffold |
|---|------|-----|---|----------|
| 27 | Challenger | Play 5 battles | 5 | `online_battles 5` |
| 28 | Contender | Play 50 battles | 15 | online_battles ladder |
| 29 | Battle Royale | Play 200 battles | 40 | `online_battles 100` (top medal tier) |
| 30 | Winner | Win your first battle | 10 | `online_wins 1` |
| 31 | Dominator | 25 wins | 20 | `online_wins 25` |
| 32 | Untouchable | 100 wins | 50 | `online_wins 100` |
| 33 | Streaker | 5 consecutive wins | 15 | `online_consecutive_wins` |
| 34 | Unstoppable | 25 consecutive wins | 30 | `online_consecutive_wins` |
| 35 | Mix Master | 100 mix wins | 25 | `online_mixwins 100` |
| 36 | Grade Grinder | Reach Grade 25 | 10 | `online_grade` |

## Collection (135G)

| # | Name | How | G | Scaffold |
|---|------|-----|---|----------|
| 37 | New Threads | Unlock 10 costumes | 10 | `online_costumes 10` |
| 38 | Fashion Icon | Unlock 20 costumes | 20 | `online_costumes 20` |
| 39 | Roster Call | Unlock 5 DJs | 10 | DJList roster |
| 40 | Full Deck | Unlock every DJ | 40 | DJList roster |
| 41 | Brand Deal | Unlock 5 brands | 10 | BrandList |
| 42 | Crate Digger | Play 25 different mixes | 15 | Quickplay setlists |
| 43 | Archivist | Play every mix in the game | 30 | merged 1+2+3 library |

## Secrets & Misc (165G)

| # | Name | How | G | Scaffold |
|---|------|-----|---|----------|
| 44 | Secret Achievement | Find the secret (their literal string!) | 25 | `Secret Achievement` hint |
| 45 | Cheat On, Scores Off | Enable any cheat | 5 | "cheat will turn off achievements" hint |
| 46 | Party Animal | Play a Party Play session | 10 | Party Play mode |
| 47 | Soundcheck | Complete calibration | 5 | Calibration mode |
| 48 | Tutorial Graduate | Finish the tutorial | 5 | Tutorial setlists |
| 49 | November Milestone | Boot the prototype | 5 | `NOVEMBER MILESTONE BUILD` |
| 50 | New To DJ Hero 3 | Trigger every NEW hint | 110 | `NEW TO DJ HERO 3` hint |

## Total: 190+160+130+220+135+165 = 1000G, 50 achievements

## Notes / deviations from scaffolding

- Medal thresholds are online-grind tuned (e.g. battles medal tops at
  threshold 100 while named "200 Battles") — Gamerscore tiers use the
  medal *names* as the design intent, thresholds re-tuned for sanity.
- `#28 Contender`: medal file only goes to threshold 100 ("200 Battles"
  name); achievement keeps the name, threshold 200 as written.
- `#50` at 110G breaks the 5-50G convention deliberately — it's the
  "see everything new" meta-achievement. Split into smaller ones if
  cert-style compliance matters (it doesn't — this is a mod).
- Icons: `medal_*.img` + trophy textures already in the `0087` FAR.
- Debug: `g_bUnlockAllContent=TRUE` in XEX attributes unlocks all for
  testing the full list fast.
