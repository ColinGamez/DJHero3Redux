# TEST CARD 002 — First vocals setlist (DJH3)

Date staged: 2026-09-29
Goal: prove the vocals chain end-to-end: engine scoring + vocal-marked
tracks + Vocals setlist type + ADD/REMOVE VOCALS UI.

## What was staged (PC side, already done)

1. `DJH3/0080_qxml.xml` — new `Vocals Setlist` (8th setlist,
   `Name=STR_SetListVocals`, selectable) with all 68 vocal-marked
   tracks. Stock backed up to `0080_qxml.stock.xml` (which itself
   already carries the 91-track Universal megalist — re-apply megalist
   first if restoring!).
2. Nothing else touched. TrackList registry, engine, strings all stock.

## Hardware steps (RGH, DJH3 proto + loose files)

1. Boot the DJH3 build, open Quickplay.
2. Look for the vocals setlist entry (name resolves via
   `STR_SetListVocals` — expect correct text, it shipped on-disc).
3. Start any track with a mic connected. Try ADD VOCALS if offered.
4. Sing. Report scoring behavior (pitch judgments? multiplier?).

## Report back

- [ ] Vocals setlist appears?
- [ ] Tracks boot to gameplay?
- [ ] Mic input registers (pitch UI, judgments)?
- [ ] Score/multiplier reacts to singing?

## Reads

- All yes → DJH3 HAS a working vocals mode and we shipped its first
  setlist. Next: vocals Empire club + vocal customs.
- Setlist missing → setlist-type needs more than Name (binary registry
 ?). Next: XEX setlist-type mapping RE.
- Boots but mic dead → mic path needs `s_iVocalController`/calibration
  setup. Next: attributes tuning session.
- Crash → one of the 68 tracks has bad vocal data. Next: bisect by
  halves (34/34) until the bad one drops out.
