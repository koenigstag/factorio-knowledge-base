# Smelting → belt ratios

How many furnaces (of a given tier) running iron-plate smelting are
needed to saturate one yellow (basic) transport belt.

## steel_furnace_iron_plate_per_yellow_belt = 24

## stone_furnace_iron_plate_per_yellow_belt = 48

Formula: `formulas/production_rate.py:machines_to_saturate`

Inputs:
- `consumer_rate` = 15 items/sec — `datapacks/dump/vanilla/transport-belt/transport-belt.json` (`speed=0.03125` tiles/tick, see `datapacks/dump/vanilla/UNITS.md` for the ×60 + density conversion to 15 items/sec)
- `crafting_speed` = 2 (steel) / 1 (stone) — `datapacks/dump/vanilla/furnace/steel-furnace.json` / `stone-furnace.json`
- `energy_required` = 3.2 — `datapacks/dump/vanilla/recipe/iron-plate.json`

Computation:
- steel: `machines_to_saturate(15, 2, 3.2)` = (2/3.2=0.625 items/s/furnace) → 15/0.625 = **24**
- stone: `machines_to_saturate(15, 1, 3.2)` = (1/3.2=0.3125 items/s/furnace) → 15/0.3125 = **48**

Verified by actually running the formula against these datapack values
(not just arithmetic by hand) — see project history: this project's
CLAUDE.md rule 1 exists specifically because an early pass in this
project's history misremembered this exact ratio as "12" instead of
the correct 24/48. This is the first time these numbers have been
computed from sourced datapacks rather than recalled from memory.
