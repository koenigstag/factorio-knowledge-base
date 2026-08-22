# train configuration notation

Two related but distinct shorthand systems for describing a train's
makeup, both community convention, not official Wube terms.

## Count notation (N-N-N)

`[locomotives in front]-[wagons]-[locomotives behind]`. E.g. `2-4-2` =
2 locomotives pulling, 4 cargo wagons, 2 locomotives pushing from the
back (common for ore trains, per the source below); `1-2-1` for oil
(fluid wagons); `1-1-1` for sulfuric acid feeding uranium mines.

Locomotives on only one end (`N-N-0` style, though not usually written
with the trailing zero) means the train must reverse or use a turning
loop to leave a station the way it came; locomotives on both ends
(`N-N-N`) let it enter and leave a station in opposite directions
without reversing — the source distinguishes these as "Pass Through
Station" vs "Terminal Station" behavior.

Source: `github.com/deniszholob/factorio-cheat-sheet`
(`src/app/cheat-sheets/game-base/trains/`)
Verified: 2026-08-08

## Letter notation (L/C/F, explicit or grouped)

More precise than count notation — it encodes the actual *order* of
cars, not just front/back locomotive counts, so it can represent
configurations count notation can't distinguish (e.g. a fluid wagon
in the middle of a cargo train). One letter per car type: `L` =
locomotive, `C` = cargo wagon, `F` = fluid wagon (and others, per the
same scheme).

Two forms, per the defining source:
- **Explicit notation**: "One carriage symbol for each carriage" —
  e.g. `LCCCC` (1 locomotive, 4 cargo wagons) or `LLCCCCF` (2
  locomotives, 4 cargo wagons, 1 fluid wagon, in that exact order).
- **Group notation**: "Consecutive (one or more) carriages of the same
  type are grouped together... represented by the number of carriages,
  followed by the carriage symbol" — e.g. `4C` for four consecutive
  cargo wagons, so `LLCCCCF` compresses to `2L4CF`.

Source: `mods.factorio.com/mod/SchallRailwayController/faq` (the
Schall Railway Controller mod's documentation, which defines this
notation explicitly)
Verified: 2026-08-08

Both notations describe the same underlying thing from different
angles: count notation is faster to say for the common symmetric case
(locomotives only at the front/back, all wagons the same type),
letter notation is unambiguous for anything more irregular.
