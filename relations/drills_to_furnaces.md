# Drills to furnaces (community integer-ratio format)

Same underlying numbers as `relations/mining_furnace_ratios.json`'s
`drills_per_furnace`, presented as a simplified integer ratio
(`drills:furnaces`) alongside the decimal — the ratio isn't a new
derivation, it's `Fraction(drills_per_furnace).limit_denominator(100)`
applied to that file's own values, kept in sync with it by
construction, not independently sourced.

Why this file exists in addition to `mining_furnace_ratios.json`:
community guides and blueprint layouts conventionally state these as
small-integer ratios ("build 5 drills for every 4 furnaces") rather
than a per-unit decimal — more directly actionable when laying out a
module, at the cost of needing to scale up to the smallest shared
multiple rather than reading off one furnace's requirement directly.

## energy_required_3.2 (recipes: copper-plate, iron-plate, stone-brick; ore_mining_time: 1)

| furnace | electric-mining-drill | burner-mining-drill | big-mining-drill |
|---|---|---|---|
| stone-furnace | 5:8 (0.625) | 5:4 (1.25) | 1:8 (0.125) |
| steel-furnace | 5:4 (1.25) | 5:2 (2.5) | 1:4 (0.25) |
| electric-furnace | 5:4 (1.25) | 5:2 (2.5) | 1:4 (0.25) |

`steel-furnace` and `electric-furnace` match row for row — same
`crafting_speed=2` reason as everywhere else this pairing shows up
(`smelting_ratios.md`, `mining_furnace_ratios.md`).

## Community cross-check

`steel-furnace` / `electric-mining-drill` = 5:4 matches an independent
community-published ratio exactly (see
`examples/full_iron_plate_chain.md`'s cross-check section for the
source and caveats — ore patch depletion and research/module levels
drift this from the unmodified baseline in a real base).

All 9 ratios computed via Python's `fractions.Fraction`, not by hand.

Verified: 2026-08-06
