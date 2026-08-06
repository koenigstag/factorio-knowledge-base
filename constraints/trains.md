# Train loading

## max_inserters_per_wagon = 12

Maximum number of inserters that can access a single cargo wagon,
both sides combined — applies to the whole shared-geometry class of
inserters, not just "regular": `inserter`, `fast-inserter`,
`burner-inserter`, `bulk-inserter`, and `stack-inserter` all have the
identical `pickup_position=[0,-1]`/`insert_position=[0,1.2]` in
`datapacks/dump/vanilla/inserter/`, so this count is the same 12 for
any of them. What differs *within* that shared count is throughput per
inserter (`extension_speed`/`rotation_speed`, plus items-per-cycle via
`bulk`/`stack_size_bonus` for the last two) — that's a rate, not a
count, and needs the geometry-aware cycle-time formula noted in
`datapacks/dump/vanilla/UNITS.md` (not built yet). Total wagon loading
throughput = this count × that per-inserter rate — a `relations/`
question combining this constraint with a `formulas/` result, not a
constraint by itself.

Source: https://wiki.factorio.com/Cargo_wagon
Verified: 2026-08-06

## max_inserters_per_wagon_long_handed_double_row = 24

Only `long-handed-inserter` reaches this — it's the one tier with
different geometry (`pickup_position=[0,-2]`, `insert_position=[0,2.2]`,
`starting_distance=1.7`, `hand_size=1.5`, all distinct from the
shared-geometry class above). Two staggered rows fit on each side
instead of one, doubling the total to 24 (12 per side × 2 sides).
Mechanism, per multiple independent community sources: the wagon is 2
tiles wide, so a long-handed inserter's extended pickup/drop reach
lands inside the wagon from either of the two staggered rows without
the rows colliding — something the shared-geometry class's shorter
reach can't exploit.

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
exactly. This has a physical explanation, not just numeric
coincidence: a wagon's two long sides (6 tiles each) are the only
sides an inserter can reach along, because the two short (2-tile)
ends are where the wagon couples to whatever's next in the train —
another wagon or a locomotive — so there's no free side there to
place an inserter against regardless of reach. That's a reasoned
account of *why* 12 specifically (not some other number) rather than
proof of a documented engine rule — no source found in this session
states it as the official cause, so it's still not promoted to a
confirmed derivation, just a considerably less arbitrary-looking
coincidence than before.

Source: https://wiki.factorio.com/Cargo_wagon
Verified: 2026-08-06
