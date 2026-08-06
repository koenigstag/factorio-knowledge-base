# Mining drill → furnace ratios

How many mining drills are needed to keep one furnace fed with ore,
for the ore/recipe pairs that actually connect: `iron-ore`→`iron-plate`,
`copper-ore`→`copper-plate`, `stone`→`stone-brick` all have
`mining_time=1` on the ore side and `energy_required=3.2` on the
recipe side (same grouping as `relations/smelting_ratios.md` and
`relations/mining_belt_ratios.md` — this is the intersection of both).

`coal` and `calcite` also have `mining_time=1` but aren't smelted by a
`furnace`-type entity via a `smelting` recipe, so they're excluded
here (they're still in `mining_belt_ratios.md`, which doesn't require
a furnace connection). `uranium-ore`/`tungsten-ore` are processed by
`centrifuge`/`foundry` respectively, not `furnace` — out of scope for
this file.

Formula: furnace ore-consumption rate (`production_rate(crafting_speed,
3.2, 1)`, 1 ore in per craft) ÷ drill ore-production rate
(`production_rate(mining_speed, 1, 1)`).

## energy_required_3.2 (recipes: copper-plate, iron-plate, stone-brick; ore_mining_time: 1)

`drills_per_furnace` (decimal) and `drills_per_furnace_ratio`
(simplified integer `drills:furnaces`, via Python's
`fractions.Fraction` — not a new derivation, just a different
notation of the same value) both live in `mining_furnace_ratios.json`:

| furnace | electric-mining-drill | burner-mining-drill | big-mining-drill |
|---|---|---|---|
| stone-furnace | 0.625 (5:8) | 1.25 (5:4) | 0.125 (1:8) |
| steel-furnace | 1.25 (5:4) | 2.5 (5:2) | 0.25 (1:4) |
| electric-furnace | 1.25 (5:4) | 2.5 (5:2) | 0.25 (1:4) |

`steel-furnace` and `electric-furnace` match row for row — same
reason as in `smelting_ratios.md`: both have `crafting_speed=2`.

**Reading a fractional drill count**: e.g. 1.25 `electric-mining-drill`
per `steel-furnace` (ratio 5:4) means 4 drills feed exactly 5 furnaces,
not that a single furnace needs a fraction of a drill running — this
is also why the integer-ratio form is often more directly actionable
for laying out a blueprint than the per-unit decimal.

**Community cross-check**: `steel-furnace`/`electric-mining-drill` =
5:4 matches an independent community-published ratio exactly (see
`examples/full_iron_plate_chain.md`'s cross-check section for the
source and caveats — ore patch depletion and research/module levels
drift this from the unmodified baseline in a real base).

All 9 values verified by actually running the formula against the
real datapack values; the 9 ratio strings via `fractions.Fraction`,
not by hand.

Verified: 2026-08-06
