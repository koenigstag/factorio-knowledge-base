# Smelting → belt ratios

How many furnaces (of a given tier) are needed to saturate one belt
(of a given tier), for every recipe in the `smelting` category.

Formula: `formulas/production_rate.py:machines_to_saturate`

## Why keyed by `energy_required`, not by recipe name

There are only 5 recipes with `category: "smelting"` in the current
dump (checked directly against `datapacks/dump/vanilla/recipe/` plus
the full `data.raw["recipe"]` for the ones not yet extracted as
individual datapack files: `copper-plate`, `iron-plate`, `stone-brick`
all have `energy_required=3.2`; `lithium-plate`=6.4; `steel-plate`=16).
`machines_to_saturate()` only depends on `energy_required`,
`crafting_speed`, and belt throughput — not on which recipe it is — so
keying by recipe name would mean `copper-plate`, `iron-plate`, and
`stone-brick` carry three byte-identical furnace×belt tables. Keying
by `energy_required` instead stores each table once, with a
`recipes` list of everything that shares it.

`lithium-plate` and `steel-plate` are `enabled: false` in the recipe
data (not available at game start, need research) — included anyway
since the ratio itself doesn't depend on whether the recipe is
currently unlocked.

Inputs:
- `crafting_speed` = 1 (stone-furnace) / 2 (steel-furnace, electric-furnace) — `datapacks/dump/vanilla/furnace/*.json`. `recycler` (the fourth `furnace`-type entity) is excluded: its `crafting_categories` is `["recycling", ...]`, not `smelting`.
- belt throughput (items/sec) — `datapacks/dump/vanilla/transport-belt/*.json` `speed`, converted per `datapacks/dump/vanilla/UNITS.md`: transport-belt=15, fast-transport-belt=30, express-transport-belt=45, turbo-transport-belt=60

## energy_required = 3.2 (copper-plate, iron-plate, stone-brick)

| furnace | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| stone-furnace | 48 | 96 | 144 | 192 |
| steel-furnace | 24 | 48 | 72 | 96 |
| electric-furnace | 24 | 48 | 72 | 96 |

This is the project's founding cautionary example (`steel-furnace`/
`transport-belt`=24, `stone-furnace`/`transport-belt`=48 — once
misremembered as "12", see CLAUDE.md rule 1) — now for `iron-plate`
specifically, but the table applies equally to `copper-plate` and
`stone-brick`.

## energy_required = 6.4 (lithium-plate)

| furnace | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| stone-furnace | 96 | 192 | 288 | 384 |
| steel-furnace | 48 | 96 | 144 | 192 |
| electric-furnace | 48 | 96 | 144 | 192 |

## energy_required = 16 (steel-plate)

| furnace | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| stone-furnace | 240 | 480 | 720 | 960 |
| steel-furnace | 120 | 240 | 360 | 480 |
| electric-furnace | 120 | 240 | 360 | 480 |

All 36 values verified by actually running `machines_to_saturate()`
against the real datapack values (not hand arithmetic).

Verified: 2026-08-06
