# Train loading

## max_inserters_per_wagon = 12

Maximum number of inserters that can access a single cargo wagon,
both sides combined, using regular (or any single-row) inserters — one
row per side.

Source: https://wiki.factorio.com/Cargo_wagon
Verified: 2026-08-06

## max_inserters_per_wagon_long_handed_double_row = 24

Using long-handed inserters specifically (longer reach), two staggered
rows fit on each side instead of one, doubling the total to 24 (12 per
side × 2 sides). Mechanism, per multiple independent community
sources: the wagon is 2 tiles wide, so a long-handed inserter's
extended pickup/drop reach lands inside the wagon from either of the
two staggered rows without the rows colliding — something a single
regular-inserter row can't exploit.

Unlike the base 12 figure, this isn't stated on the official wiki page
itself — it's a community technique, sourced here from consistent
descriptions across Factorio Forums and Steam Community discussion
threads, not an authoritative dev-written number. Treat it as solid
(multiple independent sources agree on both the value and the
mechanism) but a lower source tier than `max_inserters_per_wagon`.

Sources (community, not official wiki):
- https://forums.factorio.com/viewtopic.php?t=24367
- https://steamcommunity.com/app/427520/discussions/0/143388380482475488/
Verified: 2026-08-06

## Related: wagon dimensions

The wiki's cargo wagon infobox states `Dimensions: 2×6` (tiles) — note
this is the wiki's curated rail-grid footprint, *not* the same as
`cargo-wagon.collision_box` in `datapacks/dump/vanilla/cargo-wagon/`
(1.2×4.8 tiles, which would round to 2×5 by the `ceil()` rule used for
buildings — rail vehicles genuinely don't follow that building rule).
`cargo-wagon.json`'s `tile_box: [2, 6]` uses this wiki value rather
than the usual dump-derived computation — see the exception note in
`datapacks/dump/vanilla/UNITS.md`.

6 tiles of length × 2 sides = 12, matching the base inserter cap
exactly — a suggestive coincidence, but the wiki doesn't state this as
the actual cause of the 12-inserter limit, so it isn't treated as a
confirmed derivation here.

Source: https://wiki.factorio.com/Cargo_wagon
Verified: 2026-08-06
