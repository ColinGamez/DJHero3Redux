# DJ Hero 3 Redeux

Finishing the unreleased DJ Hero 3 — merged 1+2+3 library, new career,
first-ever vocals setlist, and a authored-from-scaffolding achievement
list — built on the November 2010 milestone prototype.

> This repo contains **only our work**: docs, tools, mod XMLs, test
> cards. No game content, no proto dumps, no binaries. You need your own
> dump of the prototype disc to use any of this (see `tools/`).

## Layout

- `docs/` — research + design
  - `DJH3_Achievements.md` — 50-for-1000G list drafted off the proto's
    medal scaffolding
  - `DJH_Customs_Pipeline.md` — FAR format, TrackPack layout, wiring
    checklist, open unknowns
- `mods/DJH3/` — drop-in mod XMLs (back up your files first)
  - `0080_Quickplay_megalist_vocals.xml` — 102-track Universal megalist
    + first vocals setlist (68 tracks)
  - `0079_Empire_encore.xml` — Ibiza02 Encore finale (4 exclusive
    tracks, lb 569, 250-star gate)
- `tools/` — `xdvdfs.py` (360 image lister/extractor), `fsg_extract.py`
  (FreeStyle container parser), `carve.py` + `magicscan.py` (magic
  carver). Temp-grade scripts, improve freely.
- `testcards/` — hardware test scripts with pass/fail reads.

## Status

See `docs/FINDINGS.md` for the full discovery log.

## Ground rules

- Unlock-through-play beats cheats. `UnlockAll*` flags are QA equipment
  only: verify fast, relock, play for real.
- Back up everything (`*.stock.*` convention, never committed).
- No copyrighted material in git. Ever.
