# DJH Customs Pipeline (TrackPacks + FAR)

Derived from DJH2 proto tree (`X360/`) + DJH3 carves. All multi-byte ints
below are big-endian unless noted.

## 1. TrackPack layout (on-disc unit of a mix)

`X360/TrackPacks/<ID>/` — e.g. `DJH2002/`:

- Exactly one `*.FAR` per pack in the proto tree (`Male.FAR` etc.). The FAR
  name seems to be the pack's content bank; more banks per pack likely in
  retail (DLC packs).
- The game resolves a mix ID (`DJH2188`, `TST3015`...) to its pack through
  the track database (Quickplay/Empire XML reference by ID; engine maps
  ID -> pack). **Rule #1 for customs: new IDs must be added to
  Quickplay + Empire XML or the game never lists them.**

## 2. FAR v2 archive format (verified by carving)

```
offset  size  field
0x00    4     magic "FSAR"
0x04    4     version (2)
0x08    4     table bytes? (0x260 in Male.FAR)
0x0C    4     entry count (N)
0x10    16    archive-name field ('x' filler in protos)
0x20    ...   N entries, 0x120 bytes each
```

Entry (0x120 bytes, verified: header 0x20 + 2*0x120 = data @0x260):

```
0x00    ~     NUL-terminated path, e.g.
              animations.txt / animation\assgrp\djanimsmalefrontend.far.grp
              (also seen: art\hud\..., xml\fe....wld, entities\...)
...     ?     zero padding
tail    ~16   numeric tail, e.g. entry1 of Male.FAR @0x244:
              00 00 00 00 | 38 a4 60 00 | 00 19 a1 5a | 00..01 00..02 ..
              - data blobs start right after the table (0x260 here)
              - compressed size field carries 0x19A15A (matches blob len)
              - flag 0x02 == zlib stream (starts 78 da)
```

Blob area: entries' payloads back to back. Payloads observed:

- zlib streams (`78 da ...`) decompressing to path lists / text
  (`Animation\crowd\core\130bpm_m_dance_std_01.gr2` ...)
- raw high-entropy data (audio banks, textures) following the text
- 6-byte file trailer (`cc c4 2d...` in Male.FAR — checksum? TBD)

`.grp` files are NOT archives-in-archives; `animations.txt.grp` is a text
manifest (animation paths) + raw data in one blob.

## 3. Audio

`X360/AUDIO/**`: FMOD banks (`*.fsb`, v4 + one v5 in DJH3) + `*.sdef`
sample-definition text. Stems for a mix live in FSBs; charts reference
them by name. Customs need: new FSB (FMOD Designer rev matching v4)
or — much easier — **chart-swap customs**: re-chart existing stems.

## 4. Making a custom mix (easiest -> hardest)

1. **Chart-swap (easy):** copy an existing TrackPack dir, keep audio,
   rewrite the note-chart entries. New ID + Quickplay/Empire XML lines.
2. **Stem-swap (medium):** same BPM/structure audio over existing charts.
   FSB tooling required.
3. **Full custom (hard):** new audio + charts + DJ/venue/env refs. Needs
   FSB authoring + FAR repack (template-copy method: clone a 1-entry FAR,
   swap blob, patch size fields).

## 5. Wiring a new mix ID into the game

1. `DJH3/0080` Quickplay → add `<Track>DJHxxxx</Track>` to Universal
   Setlist (proven: 102-track megalist already in place).
2. `DJH3/0079` Empire → add setlist block to a club (proven: Ibiza02
   Encore pattern — IDTag, LeaderboardID (unused 571+), Cover, Name
   STR_, InitiallyLocked gate, Tracks, Challenge/Criteria/Unlocks).
3. `TrackPacks/DJHxxxx/` dir with the FAR bank(s).
4. DJ/venue/env must already exist (DJList/EnvironmentList) or be added.

## 6. THE TrackList registry (DJH3 `0000` file — authoritative!)

The engine's real track DB hides inside the ATTRIBUTES XML as a second
concatenated doc. Per-track record:

```xml
<Track ingame="true" ondisc="true">
  <IDTag>DJH2006</IDTag>
  <LeaderboardID battle="103" quickplay="101"
                 quickplay_difficulty="102" vocals="104" />
  <IsTutorialTrack>0</IsTutorialTrack>
  <HasVocalMarkup>1</HasVocalMarkup>
  <BPM>128</BPM>
  <FolderLocation>AUDIO\Audiotracks\DJH2006</FolderLocation>
  <FSSampleStreamAss Sample="0">2</FSSampleStreamAss>
  ...
</Track>
```

119 entries, 115 ondisc, 68 with vocal markup. **Customs MUST join this
registry** (ingame/ondisc flags, per-mode leaderboard IDs, BPM, folder,
sample-stream map) or the engine won't acknowledge the ID no matter
what Quickplay says. Proven pattern for vocals: setlist
`Name=STR_SetListVocals` + only `HasVocalMarkup=1` tracks
(`DJH3/0080` "Vocals Setlist", 68 tracks, already staged).

## 7. Open unknowns (do not block v1 customs)

- Exact FAR tail field map (off/size/flags positions vary slightly).
- Male.FAR entry0 (`animations.txt`, 237B?) data location.
- FSG container record hash function (for naming carved files properly).
- XEX-side track DB (does the engine ALSO need the ID somewhere binary?
  Quickplay XML refs suggest XML-driven — test will tell).
- Note charts FOUND + PARTIALLY DECODED:
  `AUDIO/Audiotracks/DJHxxxx/DJ_{Beginner,Easy,Medium,Hard,Expert}.xmk`
  (13-20KB) + `Visual_Markup.xmk` + `Vocals.xmk`. Layout: header
  `[ver=2][hash][count][183]`, then `count` 16-byte events with ASCII
  type tags (  DJH2228/Medium: B493 + C237 + A81 + @17 + 8 zero-type +
  1 M-type; B = probable tap notes). Float timestamps in bodies.
  Difficulty scales count (837 Med → 1267 Exp). B-event anatomy
  (3101 samples, 5 difficulties): byte0='B', bytes12-13 always zero;
  byte14 ~always 0 + 12 hits of a difficulty-scaled value (58 Beg /
  79 Exp, same count — section flag?); byte15 dominated by 0/100 with
  value 1 strongly Expert-associated (5 Beg → 78 Exp — harder gem
  type?). Cross-difficulty alignment (Beg vs Exp, 365 shared
  timestamps): 214 byte-identical; 93 upgrade lane with difficulty;
  high b15 values (109-195, one-offs) = probable special gems;
  Expert adds 173 notes (mostly lane 0). Authoring rule of thumb:
  B-events + timestamps + b15 in {0,100} (+1 for spice).
- C-events (1403 samples): same 16B skeleton (byte0='C', bytes12-13
  zero). b4-8 = small-int enum topped by 0/1/2 (gesture type —
  crossfade direction/hold?), b8-12 = float durations topped by
  0x3D000000/0x3E000000. Counts scale with difficulty (237 Med →
  335 Exp). b14 carries the same difficulty-scaled flag as B-events
  (79 on Expert), confirming it as a shared section flag, not lane
  data. Probable: crossfade/scratch gestures.
- Small fry, all solved: M-type = author signature + chart name
  (`Matt Flint\0Intro`, 1 per file); 0x00-type = section-name text
  events (`Chorus 4`, `Bridge`, `Break A/B`, `Build A`, `Outro`);
  @-type = section markers with percent values (67/99/100);
  A-type = difficulty-scaled (81→115) with bitmask byte11 —
  probable star-power/euphoria triggers.
- `.sdef` = binary sample-name→index map + default volumes (NOT text).
  Kiosk-disc `.sdef` confirms tutorial stingers + `_kiosk` variants.
