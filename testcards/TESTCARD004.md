# TEST CARD 004 — Twin Deck door (flag flip)

Date staged: 2026-09-30
Goal: open Twin Deck without the missing cheat-entry UI, by flipping
its engine flags directly.

## What was staged (PC side, already done)

`mods/DJH3/Attributes_Global_twindeck.xml` — container ATTRIBUTES with
exactly 2 flips (`s_bEnableDualPlatters` + `s_bBothPlattersCanStreamPress`
FALSE→TRUE). Everything else byte-identical.

## Hardware steps (RGH)

1. Place as loose `X360/Attributes_Global.xml` alongside the build
   (same TESTCARD003 override bet).
2. Boot, enter any battle-capable mode.
3. Try second-platter input (pad mapping per PadsCanBeDecks lineage?).
4. Report:
   - [ ] Boots with modded attributes (no parse reject)?
   - [ ] Second platter registers input?
   - [ ] DUALPLATTER cheat shows as enabled/unlocked?
   - [ ] Gameplay actually uses both decks?

## Reads

- All yes → Twin Deck door built. First dual-platter mode in history.
- Boots but single-deck → flags need the cheat-menu handshake too.
  Next: find the handshake (XEX cheat-state RE).
- Parse reject/crash → attributes are checksummed or container-only.
  Next: checksum hunt.
