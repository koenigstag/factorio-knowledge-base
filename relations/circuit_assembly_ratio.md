# Copper cable → electronic circuit assembler ratio

How many `copper-cable` assemblers are needed to perfectly feed a given
number of `electronic-circuit` assemblers, assuming both run the same
assembling-machine tier.

Formula: `formulas/production_rate.py:production_rate` /
`machines_to_saturate`.

## Primitives

Both recipes are `category: "crafting"`, so any single
assembling-machine tier (1/2/3) can craft both — see CLAUDE.md rule 2's
`data.raw`-only test for why these are `datapacks/`, not
`constraints/`. Neither recipe is yet in `datapacks/dump/vanilla/recipe/`
(only 6 recipes are extracted there so far); recorded instead in
`datapacks/wiki/recipe/` per rule 5 (no live game install available
this session to fill the dump gap directly).

| Recipe | `energy_required` | ingredients | `results` amount | Source |
|---|---|---|---|---|
| `copper-cable` | 0.5 | copper-plate × 1 | 2 | `datapacks/wiki/recipe/copper-cable.json` |
| `electronic-circuit` | 0.5 | copper-cable × 3, iron-plate × 1 | 1 | `datapacks/wiki/recipe/electronic-circuit.json` |

## Derivation

For any assembling-machine `crafting_speed = cs` used for both recipes:

- `copper-cable` production rate = `production_rate(cs, 0.5, 2)` = 4·cs cable/s per machine
- `electronic-circuit` production rate = `production_rate(cs, 0.5, 1)` = 2·cs circuits/s per machine, each consuming 3 copper-cable → cable demand = 6·cs cable/s per circuit machine

`cable_machines / circuit_machines` = (6·cs) / (4·cs) = **3/2** — `cs`
cancels, so this ratio holds at every assembling-machine tier (unlike
`relations/smelting_ratios.json`, where furnace tier changes the
absolute count). Reduced to whole numbers: **3 copper-cable machines :
2 electronic-circuit machines**.

## Cross-check

Independently confirmed by two sources:
- wiki.factorio.com/Electronic_circuit states this exact ratio directly: *"the ratio of assembling machines of the same tier to craft this item is 3 copper cable assembling machines to 2 electronic circuit assembling machines"*.
- The Xterminator short cross-checked in `relations/steam_power_ratio.md` also states "three copper cable machines can perfectly supply two green circuit machines" — matches.

Verified: 2026-08-22
