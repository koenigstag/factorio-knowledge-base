# Smelting → belt ratios

How many furnaces (of a given tier) running a given smelting recipe
are needed to saturate one belt (of a given tier), keyed as
`[recipe][furnace][belt]`.

Formula: `formulas/production_rate.py:machines_to_saturate`

## iron_plate

Inputs:
- `energy_required` = 3.2 — `datapacks/dump/vanilla/recipe/iron-plate.json`
- `crafting_speed` = 1 (stone-furnace) / 2 (steel-furnace, electric-furnace) — `datapacks/dump/vanilla/furnace/*.json`
- `consumer_rate` (belt throughput, items/sec) — `datapacks/dump/vanilla/transport-belt/*.json` `speed`, converted per `datapacks/dump/vanilla/UNITS.md`: transport-belt=15, fast-transport-belt=30, express-transport-belt=45, turbo-transport-belt=60

| furnace | transport-belt (15/s) | fast-transport-belt (30/s) | express-transport-belt (45/s) | turbo-transport-belt (60/s) |
|---|---|---|---|---|
| stone-furnace (speed 1) | 48 | 96 | 144 | 192 |
| steel-furnace (speed 2) | 24 | 48 | 72 | 96 |
| electric-furnace (speed 2) | 24 | 48 | 72 | 96 |

`electric-furnace` matches `steel-furnace` exactly, row for row —
not a coincidence to double-check, it's because both have
`crafting_speed=2` in the datapack, so `machines_to_saturate()`
produces the same output for the same recipe/belt. (`recycler`, the
fourth `furnace`-type entity, isn't included here — its
`crafting_categories` is `["recycling", ...]`, not `smelting`, so it
can't run the iron-plate recipe at all.)

All 12 values verified by actually running `machines_to_saturate()`
against the real datapack values (not hand arithmetic) — see project
history: `steel-furnace`/`transport-belt` = 24 and `stone-furnace`/
`transport-belt` = 48 are this project's founding cautionary example
(once misremembered as "12" — see CLAUDE.md rule 1); the rest are the
same formula applied to the other belt tiers and the third smelting
furnace, following directly once the pattern held for the first pair.

Verified: 2026-08-06
