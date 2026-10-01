# REDUX CONSOLE SESSION — run order + package list

Do these in order. Each card gates the next; stop at first red and report.

## Package checklist (prepare on PC first)

- [ ] USB1-DJH2: `X360/` tree + `DJ_Release.xex` (includes DJH9001 + forged
  Beginner+, Quickplay line, Beginner pads config)
- [ ] USB2-DJH3STOCK: `GODSRC/` contents (Default.xex + X360/ container)
- [ ] USB2 overlay set: `mods/DJH3/0080` → `X360/Xml/Quickplay.xml`,
  `0079` → `X360/Xml/EmpireMode.xml`, `0156` → `X360/Xml/Credits.xml`,
  `Attributes_Global_twindeck.xml` → `X360/Attributes_Global.xml`
  (twin deck test only — back up stock behavior first)

## Run order

1. **DJH2 stock boot** (no DJH9001 yet — verify baseline first if unsure).
2. **TESTCARD001** (wiring + forged chart by ear).
3. **DJH3 stock boot** (baseline: 2-track Universal, 6 clubs).
4. **TESTCARD003** (overlay: 91-track megalist, vocals setlist, dance 10,
   Encore 569, Studio club, Vegas battles, Party opener, Redux credits).
5. **TESTCARD002** (vocals setlist + mic).
6. **TESTCARD004** (twin deck flags).
7. **QA variant** (unlock-all) only to fast-verify content, then relock.

## Report format per card

PASS/FAIL per checkbox + one photo of anything unexpected. FAILs go
back into the repo as findings with the exact symptom.
