# Wagon loading throughput

Total items/sec when a cargo wagon is loaded by the maximum number of
inserters of one tier, combining a `constraints/` count with a
`constraints/`-cited rate via `formulas/inserter_throughput.py`.

Formula: `count × inserter_throughput(cycles_per_sec)`.

## items_per_sec_at_max_inserters_per_wagon

| tier | count | rate (items/sec, base) | total |
|---|---|---|---|
| burner-inserter | 12 | 0.79 | 9.48 |
| inserter | 12 | 0.86 | 10.32 |
| fast-inserter | 12 | 2.5 | 30.0 |
| bulk-inserter | 12 | 5.0 | 60.0 |
| long-handed-inserter | 24 | 1.25 | 30.0 |
| stack-inserter | 12 | 15.0 | 180.0 |

Inputs:
- count: `constraints/trains.json` — `max_inserters_per_wagon=12` for
  the shared-geometry tiers (burner/regular/fast/bulk/stack all share
  identical `pickup_position`/`insert_position`),
  `max_inserters_per_wagon_long_handed_double_row=24` specifically for
  `long-handed-inserter`.
- rate: `constraints/inserters-throughput.md`'s cited chest-to-chest
  cycles/sec × items-per-cycle (1 for burner/regular/long-handed/fast;
  2 for bulk-inserter, 6 for stack-inserter — both now resolved via
  the wiki's stated *base*, unresearched grab sizes, see that file).

All 6 tiers are now covered at the **unresearched baseline** — none
of these account for `inserter-capacity-bonus` research, which would
increase `bulk-inserter`/`stack-inserter` further but isn't
computable yet (see `constraints/inserters-throughput.md`'s "Still
open" note: the wiki itself doesn't document how the two research
effect types combine with the base grab size).

## Why this number matters

`inserter`/`transport-belt` = 10.32 items/sec is a direct match for
this project's own founding architecture discussion (from the
not-yet-imported `ARCHITECTURE.md`/decision 0004 draft): "red science
pack production throughput on a saturated yellow belt (15/sec)
exceeds the physically achievable wagon-loading throughput even with
12 regular inserters (10.32/sec)". That comparison motivated the
original "inserter is a property of the port, not the module" design
principle (already reflected in `glossary/invented/port.md`) — this is
the first time 10.32 has actually been computed in this repo rather
than carried over as a remembered number from that earlier discussion.

Verified: 2026-08-06
