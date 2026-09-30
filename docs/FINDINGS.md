# DJH3 Prototype Findings Log

Source: November milestone dev build (`Default.xex` 2010-11-20, Title ID
`4156089F`, 3.9GB image). Self-identifies as
`DJ HERO 3 PROTOTYPE / NOVEMBER MILESTONE BUILD`.

## Library

- 199 referenced track IDs: ~105 DJH1-era + ~94 DJH2-era. Sequel was a
  merged-library game.
- 4 exclusive tracks: DJH2292 (91 BPM, dance-marked), DJH2304 (127),
  DJH2311 (121), DJH2315 (97). Full registry entries, no display names
  in XML.
- TrackList registry (inside ATTRIBUTES XML): 119 entries, 115 ondisc,
  68 with vocal markup. Per-track: ingame/ondisc flags, per-mode
  leaderboard IDs (battle/quickplay/difficulty/vocals), BPM, audio
  folder, sample-stream map.

## Modes by completeness

1. **Vocals** — full engine (5 difficulties, 3 accuracy tiers,
   rap-note handling, per-platform mic DSP, calibration), 68 marked
   tracks, setlist type + ADD/REMOVE strings. No shipped setlist.
2. **Party Play** — DJH2 lineage, strings present.
3. **Twin Deck** — unlockable cheat (`DUALPLATTER` + warnings).
4. **Dance** — 10 tracks charted, battle/routine strings, cast unmodeled.
5. **Ghost Challenges** — strings + 3-track setlist, no code.
6. **Guitar/Drums** — art entries + score column only.
- Also named: Power Decks, live-setlist blending, freestyle sampling,
  AI spectate battles, vocals/drums/guitar setlist backgrounds.

## Roster

- DJH2 cast carried over (166 entries), nothing new modeled.
- Ghost DJs (localized names, no other data): DJ DDZASTER, DJ AMANDA.

## Achievements

- None authored. Scaffolding: 109 medals + criteria, trophy tracker UI
  (`trophy_tracker` scenes/icons), `?G` score templates, cheat warnings.
- Recovery recipe in `DJH3_Achievements.md`.

## Formats cracked

- XDVDFS (360 image FS): 16-bit unit-scaled BST offsets. See `tools/`.
- FSG-FILE-SYSTEM container: BE, 16B records, string table @0x40000.
- FAR v2: 32B header, 0x120B entries (path + numeric tail), zlib blobs.
- Audio: FMOD banks (v4 + one v5). FSB4 sample tables self-identify by
  track (`djh2125_sample2.wav` pattern) — exclusives mapped: 2292→0274
  (11.6MB), 2304→0275 (16.1MB), 2311→0276 (12.4MB), 2315→0277
  (2MB — small, verify completeness on hardware). Video: Bink.
  Text DBs: binary.

## Cheats (33 strings)

Assists (AUTOCROSSFADER/AUTODSP/AUTOEUPHORIA/AUTOGEMHIT/AUTOSCRATCH),
unlocks (UNLOCKALL*), jokes (BEDROOMDJ/RAINBOW/INVISIBLEDJ/MIDAS/
HAMSTERSWITCH...). Entry UI missing — `g_bUnlockAll*` flags are the
levers (QA only).

## AI / Tutorial

- Two AI tiers (3.5/4.5-star) + authored scratch patterns.
- Full lesson scripting (HUD toggles, voice slots, sync points).

## Career

- Empire: 6 clubs, 40 stock setlists (megamix openers, star/win/battle
  challenges, bonuses). Legacy 2007 GAMEDATA tour is dead weight.
- Rebuilt: 102-track Universal megalist, first vocals setlist (68),
  Ibiza02 Encore finale (exclusives, lb 569, 250-star gate).
- Note: DJH3's Empire is a direct copy of the DJH2 proto career
  (same 39 setlists) + 1 commented-out test block. Corrections logged;
  early claims otherwise were file-listing errors.
- Quickplay restructured between games: DJH2's dev-facing lists (Mix
  Testing + ungrouped) became DJH3's mode-facing setlists (Universal,
  Live, FSPP, GHOST, AI DEMO, DANCE). New IDs on 3: exclusives,
  TST2237/3015/3017/3027/3040/3041/3048/3049, plus 2181/2214/2236.
- Retail DJH2 (carved from RTM ISO): Quickplay stripped to Credits +
  39 ungrouped (dev lists removed for ship); Empire identical 6 clubs
  / 39 setlists. Retail container mirrors proto layout 1:1 (412 FAR,
  233 FSB, 253 BIK, 99 XML) — same tools, same formats.
- TST live-blend test tracks are registered citizens (8 in TrackList);
  TST3001-3004 (commented Ibiza1 Branching block) reference
  UNREGISTERED tracks — dead pointers, do not revive as-is.
- The registry carries the devs' own todo list: 25 `WorkInProgress`
  tracks (newest DJH2264/2265, TST2237/3015/3017/3027/3048/3049, all 17
  TUT2000-2016). TST3040/3041 are finished. Tutorials never got voice.
- Tutorial content is audio-complete (all 17 TUT audio dirs exist) but
  was missing visual packs for TUT2000/2001 — forged by cloning (all
  TUT packs share byte-identical visuals, MD5-verified). Tutorial now
  17/17 complete on the tree.
- Pack audit (114 referenced IDs vs DJH2 tree): 15 packs missing
  (exclusives, all TST, plus DJH2221 which HAS audio but no visuals —
  inverse of the tutorial case). Architectural consequence: the merged
  library can ONLY boot from the DJH3 side (container + loose
  override). The DJH2 tree cannot host Redux content. TESTCARD003 is
  the whole project now.
