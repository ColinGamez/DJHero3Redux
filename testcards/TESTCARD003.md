# TEST CARD 003 — Loose-file override (THE critical test)

Date staged: 2026-09-30
Goal: determine whether the DJH3 devkit build prefers loose files over
container data. EVERYTHING (megalist, encore, vocals, customs) depends
on a YES.

## Background

All Redux mods are loose XMLs. The DJH3 build reads from the
FSG-FILE-SYSTEM container (`DISC0.IMG.part0+1`). Sibling DJH2 proto
tree proves the engine family CAN run loose — unproven for this XEX.

## Package (PC side)

On HDD, next to a stock DJH3 extract (`Default.xex` + `X360/`):

```
X360/Xml/Quickplay.xml      <- mods/DJH3/0080_Quickplay_megalist_vocals.xml
X360/Xml/EmpireMode.xml     <- mods/DJH3/0079_Empire_encore.xml
X360/Xml/Credits.xml        <- mods/DJH3/0156_Credits_redeux.xml
```

(If the build ignores `X360/Xml/`, retry with the files beside
`Default.xex` directly, then report both results.)

## Hardware steps (RGH)

1. Boot stock first (no overlay): confirm baseline (Quickplay =
   2-track Universal, 6 clubs, stock credits).
2. Add the overlay, reboot.
3. Check, in order:
   - [ ] Quickplay Universal lists 92 tracks?
   - [ ] Vocals Setlist present (68 tracks)?
   - [ ] DANCE SETLIST has 10 tracks?
   - [ ] Empire shows Ibiza02 Encore (lb 569)?
   - [ ] Studio vocals club exists (7th club)?
   - [ ] Credits roll shows the Redux block?

## Reads

- All yes → loose override CONFIRMED. Redux ships as an overlay pack.
  Customs pipeline fully unblocked.
- Partial (some files read, others not) → per-system paths differ.
  Report exactly which. Next: path hunt per system.
- None → engine is container-only. Next: FSG hash function becomes
  THE project (repack container with mods baked in).
- Crash → overlay format rejected. Next: compare byte-level (BOM?
  NUL tails? line endings?) stock-vs-mod.
