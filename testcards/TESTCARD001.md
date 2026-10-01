# TEST CARD 001 — First custom (DJH9001 wiring proof)

Date staged: 2026-09-29
Goal: prove a new track ID + pack dir + one XML line is enough for the
engine to list and play a custom mix.

## What was staged (PC side, already done)

1. `X360/TrackPacks/DJH9001/Male.FAR` — byte-identical clone of DJH2002.
2. `X360/AUDIO/Audiotracks/DJH9001/` — full clone (DJ.fsb + 5 charts +
   Visual_Markup + Vocals, 8 files), PLUS a forged Beginner chart:
   10 lane flips (b15 0→100) + 333 Expert-only notes injected from
   DJH2002's own Expert (485→818 events). Same mix, spicier chart.
3. `X360/Xml/Quickplay.xml` — `<Track>DJH9001</Track>` first in ungrouped
   Tracks. Stock backed up to `Quickplay.stock.xml`.

## Hardware steps (RGH)

1. Copy the whole `X360/` tree + `DJ_Release.xex` to HDD (same layout as a
   working boot — change NOTHING else).
2. Boot `DJ_Release.xex` (Frontend mode, Beginner pads per `config.xml`).
3. Go to Quickplay / track list. Look for a new/unnamed entry
   (name comes from the TRAC text DB — expect blank or garbage text;
   THAT IS FINE, it still proves listing works).
4. Play it on Beginner with ears open: the first 10 notes should play
   on the OTHER stream vs DJH2002, and extra Expert notes appear
   throughout. Same mix, custom chart = chart modding proven by ear.

## Report back

- [ ] Entry appears in list? (photo of how the name renders)
- [ ] Mix boots to gameplay?
- [ ] Plays through without crash?
- [ ] Audio present?

## Reads

- All yes → wiring checklist CONFIRMED. Next: real chart edit + TRAC
  name entry, then same method ports to DJH3's loose tree.
- Entry missing → engine has a second track DB (binary?). Next: hunt it
  via XEX strings around "DJH2002".
- Crash on boot → pack needs more than Male.FAR (compare a big pack
  like DJH2010: it has TwoPlayer.FAR too). Next: clone DJH2010 instead.
