# Mining drill → furnace ratios

How many mining drills are needed to keep one furnace fed with ore,
for the ore/recipe pairs that actually connect: `iron-ore`→`iron-plate`,
`copper-ore`→`copper-plate`, `stone`→`stone-brick` all have
`mining_time=1` on the ore side and `energy_required=3.2` on the
recipe side (same grouping as `relations/smelting_ratios.md` and
`relations/mining_belt_ratios.md` — this is the intersection of both).
**They do *not* all share the same ratio, though** — see the
correction below.

`coal` and `calcite` also have `mining_time=1` but aren't smelted by a
`furnace`-type entity via a `smelting` recipe, so they're excluded
here (they're still in `mining_belt_ratios.md`, which doesn't require
a furnace connection). `uranium-ore`/`tungsten-ore` are processed by
`centrifuge`/`foundry` respectively, not `furnace` — out of scope for
this file.

Formula: furnace ore-consumption rate ÷ drill ore-production rate.
Furnace consumption rate is `production_rate(crafting_speed, 3.2,
ingredient_amount)` — passing the recipe's *ingredient* amount as
`production_rate`'s third argument gives the consumption rate per
machine, the same function `relations/smelting_ratios.md` uses for
*output* rate, just fed the other side of the recipe. Drill production
rate is `production_rate(mining_speed, 1, 1)`.

## Correction (2026-08-08): stone-brick doesn't share iron/copper-plate's ratio

An earlier version of this file grouped `copper-plate`, `iron-plate`,
and `stone-brick` under one shared table, with the formula note
"1 ore in per craft" applied uniformly to all three. That's true for
`iron-plate`/`copper-plate` (1 ore → 1 plate) but **wrong for
`stone-brick`**, whose recipe is 2 `stone` → 1 `stone-brick`
(`datapacks/dump/vanilla/recipe/stone-brick.json`) — double the
ingredient amount. A furnace making stone-brick consumes stone twice
as fast as one making plates from ore, so it needs (up to) twice as
many drills feeding it. This was caught by re-deriving the ratio with
the correct `ingredient_amount=2` and finding it didn't match the
shared table.

## copper-plate / iron-plate (ingredient_amount=1)

| furnace | electric-mining-drill | burner-mining-drill | big-mining-drill |
|---|---|---|---|
| stone-furnace | 0.625 (5:8) | 1.25 (5:4) | 0.125 (1:8) |
| steel-furnace | 1.25 (5:4) | 2.5 (5:2) | 0.25 (1:4) |
| electric-furnace | 1.25 (5:4) | 2.5 (5:2) | 0.25 (1:4) |

## stone-brick (ingredient_amount=2) — exactly double the table above

| furnace | electric-mining-drill | burner-mining-drill | big-mining-drill |
|---|---|---|---|
| stone-furnace | 1.25 (5:4) | 2.5 (5:2) | 0.25 (1:4) |
| steel-furnace | 2.5 (5:2) | 5.0 (5:1) | 0.5 (1:2) |
| electric-furnace | 2.5 (5:2) | 5.0 (5:1) | 0.5 (1:2) |

`steel-furnace` and `electric-furnace` match row for row within each
table — same reason as in `smelting_ratios.md`: both have
`crafting_speed=2`.

**Reading a fractional drill count**: e.g. 1.25 `electric-mining-drill`
per `steel-furnace` (ratio 5:4) means 4 drills feed exactly 5 furnaces,
not that a single furnace needs a fraction of a drill running — this
is also why the integer-ratio form is often more directly actionable
for laying out a blueprint than the per-unit decimal.

**Community cross-check**: `steel-furnace`/`electric-mining-drill` =
5:4 (iron/copper-plate table) matches an independent community-
published ratio exactly (see `examples/full_iron_plate_chain.md`'s
cross-check section for the source and caveats — ore patch depletion
and research/module levels drift this from the unmodified baseline in
a real base). That community figure is specifically about
iron-plate/steel-furnace, not stone-brick, so it isn't affected by the
correction above.

**Looser community rule of thumb (r/factorio, lower confidence —
explicitly given as an approximation, not a derived figure)**:
*"roughly 2 stone or 1 steel/electric [furnace] per [electric] miner"*
— read as furnace *tier* (stone vs. steel/electric), not product,
matching the iron/copper-plate table above (the thread's context is a
player running low on iron/steel, not stone-brick specifically):
inverting to furnaces-per-drill, `stone-furnace`/`electric-mining-drill`
= 1÷0.625 = **1.6** and `steel-furnace`/`electric-mining-drill` =
1÷1.25 = **0.8**, both roughly 25% below the reddit rule of thumb's 2
and 1 — same direction and right order of magnitude, more
furnace-frugal than the casual estimate, expected since the commenter
explicitly left the exact calculation to the reader.

All values verified by actually running the formula against the real
datapack values, both tables; the ratio strings via Python's
`fractions.Fraction`, not by hand.

Verified: 2026-08-08
