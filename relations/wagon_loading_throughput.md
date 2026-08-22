# Wagon loading throughput

Total items/sec when a cargo wagon is loaded by the maximum number of
inserters of one tier, combining a `mechanics/` count with a
`mechanics/`-cited rate via `formulas/inserter_throughput.py`.

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
- count: `mechanics/trains.json` — `max_inserters_per_wagon=12` for
  the shared-geometry tiers (burner/regular/fast/bulk/stack all share
  identical `pickup_position`/`insert_position`),
  `max_inserters_per_wagon_long_handed_double_row=24` specifically for
  `long-handed-inserter`.
- rate: `mechanics/inserters-throughput.md`'s cited chest-to-chest
  cycles/sec × items-per-cycle (1 for burner/regular/long-handed/fast;
  2 for bulk-inserter, 6 for stack-inserter — both now resolved via
  the wiki's stated *base*, unresearched grab sizes, see that file).

All 6 tiers are now covered at the **unresearched baseline**. The
researched (`inserter-capacity-bonus-1..7` maxed) case is now also
resolved — see `mechanics/inserters-throughput.md`'s "Researched grab
size" section and `formulas/inserter_capacity_bonus.py`:

## items_per_sec_at_max_inserters_per_wagon (max research)

| tier | count | rate (items/sec, maxed research) | total |
|---|---|---|---|
| burner-inserter | 12 | 2.37 | 28.44 |
| inserter | 12 | 2.58 | 30.96 |
| fast-inserter | 12 | 7.5 | 90.0 |
| bulk-inserter | 12 | 30.0 | 360.0 |
| long-handed-inserter | 24 | 3.75 | 90.0 |
| stack-inserter | 12 | 40.0 | 480.0 |

`bulk-inserter` at 12 inserters × 30 items/sec (360/sec) already
exceeds a turbo-belt's 60 items/sec rated throughput 6× over — at full
inserter research, wagon-loading throughput stops being the
bottleneck for any belt tier; the belt itself becomes the limit well
before inserter count/rate does.

## Unresolved discrepancy: wagon-specific cycle rate

`factoriocheatsheet.com`'s source gives noticeably lower chest-to-*wagon*
cycles/sec than this file's chest-to-*chest* figures (from
`mechanics/inserters-throughput.md`, cited from the generic Inserters
wiki page): burner 0.6 vs 0.79, `inserter` 0.83 vs 0.86, long-handed
1.2 vs 1.25, fast/bulk/stack 2.31 vs 2.5 — a consistent ~8-24% lower
rate across every tier, suggesting a real wagon-geometry effect (the
cargo-wagon's larger footprint could plausibly slow an inserter's
swing versus a 1×1 chest) rather than random noise. Checked
`wiki.factorio.com/Cargo_wagon` directly for a wagon-specific figure —
it states only the 12-inserters-per-wagon count, no throughput numbers
at all, so there's no third source to arbitrate. **Not resolved**:
this project doesn't know which figure is more accurate, and isn't
switching `wagon_loading_throughput`'s numbers on a single
uncorroborated source per this project's confidence bar. Flagged here
rather than silently picking one.

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
