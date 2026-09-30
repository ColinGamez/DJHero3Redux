# HOWTO: Author a DJH Chart From Scratch (v0.1)

Status: structural spec. Timing/encoding values below are confirmed by
measurement (DJH2228, 5 difficulties); lane semantics by alignment
(Beg vs Exp); hardware validation still pending (see TESTCARD001).

## File set (per mix, per difficulty)

`AUDIO/Audiotracks/DJHxxxx/`:

- `DJ.fsb` — main stems (~20MB). `FSS.fsb` — freestyle samples (~1MB).
- `DJ_{Beginner,Easy,Medium,Hard,Expert}.xmk` — note charts (13-20KB).
- `Visual_Markup.xmk` — venue cues (~60-120KB).
- `Vocals.xmk` — vocal chart + embedded lyrics (if sung).

## .xmk container

```
u32be ver (=2), u32be hash?, u32be count, u32be (=183)
count × 16-byte events
```

Header size varies (208B DJ charts, 2096B vocals with lyric setup?,
6400B Visual_Markup with venue setup). Compute as
`filesize - count*16`, never assume.

## Event anatomy (16B)

| Byte(s) | Meaning |
|---------|---------|
| 0 | ASCII type tag |
| 1-11 | Timestamp + params (floats inside; bytes 1-4 work as an align key) |
| 12-13 | Always zero |
| 14 | Section flag (difficulty-scaled: 58 Beg / 79 Exp, 12 hits/track) |
| 15 | Lane (B-events): 0/100 = standard streams, 1 = hard gems, 109+ = specials |

## Types

- `M` (1/file): author signature + chart name (`Matt Flint\0Intro`).
  Sign yours.
- `0x00`: section names (`Chorus 4`, `Bridge`, `Break A/B`...).
- `@`: section markers with percent values (67/99/100).
- `A`: difficulty-scaled triggers, bitmask byte11 (star-power family).
- `B`: tap notes. b15 lane per table above.
- `C`: gestures. b4-8 small-int enum (0/1/2 = core moves), b8-12
  float duration.
- Vocals: same family; lyrics as text-fragment events in file order,
  codes `@` `=` `?`, section tags (`Verse 1`, `Chorus`).

## Authoring ladder (easiest first)

1. **Lane-flip** (proven: forge1 pattern, in-place b15 patch).
2. **Density edit**: copy Expert B-events at new timestamps into
   Beginner (timestamps are absolute — no reflow needed). PROVEN:
   DJH2228 Beginner 928 + 198 Expert-only B-events = 1126-event
   Beginner+ , mergesorted by timestamp key, count field updated,
   parses clean.
3. **New chart**: M + sections + B/C/A events on the 16B grid, header
   count updated. Keep bytes 12-13 zero, b14 = 0 (or match neighbors).
4. **New vocals**: lyric fragments in file order with `@`/`=`/`?`
   codes + `Verse`/`Chorus` tags.
5. **New mix**: files + TrackList registry entry + Quickplay/Empire
   lines (see Customs Pipeline §5-6).

## Difficulty design (measured)

- Beginner→Expert NEVER rewrites: 214/365 notes byte-identical
  (DJH2228 Beg vs Exp). Ladder = add notes (Expert +173, mostly
  lane 0) + upgrade lanes (93 changes).
- Counts: 837 Med → 1267 Exp (DJH2228). Scale new charts similarly.
- b14 flag: exactly 12 hits/track regardless of difficulty; value
  scales (58→79). Copy the pattern, don't invent.
