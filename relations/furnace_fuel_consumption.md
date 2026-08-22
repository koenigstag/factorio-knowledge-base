# Burner furnace fuel (coal) consumption

How much coal a burner furnace consumes per second at 100% uptime
(continuously crafting, never idle), and how many furnaces one full
coal belt can sustain — the fuel-side counterpart to
`relations/smelting_ratios.md`, which only covers the ingredient/
product side.

Formula: `formulas/fuel_consumption_rate.py:fuel_consumption_rate`
(`(energy_usage / effectivity) / fuel_value`).

Inputs:
- `energy_usage` = 90kW for both `stone-furnace` and `steel-furnace`
  (`datapacks/dump/vanilla/furnace/{stone,steel}-furnace.json`) —
  identical between the two tiers in the current dump; this is a fact
  about this specific game version's data, not a rule that furnace
  tiers always share power draw, so don't assume it holds for other
  furnace types without checking.
- `effectivity` = 1 for both (`energy_source.effectivity`).
- `fuel_value` = 4MJ for coal (`datapacks/dump/vanilla/item/coal.json`).
- belt throughput (items/sec) — same conversion as
  `smelting_ratios.md`: transport-belt=15, fast-transport-belt=30,
  express-transport-belt=45, turbo-transport-belt=60.

`electric-furnace` is excluded: its `energy_source.type` is
`"electric"`, not `"burner"` — it draws power directly, consumes no
fuel item at all, so this relation doesn't apply to it.

## Coal consumption per furnace

Both `stone-furnace` and `steel-furnace`: **0.0225 coal/sec**
(90,000W / 4,000,000J), since they share the same `energy_usage` and
`effectivity` in this dump.

## Furnaces sustained per full coal belt

| furnace | transport-belt | fast-transport-belt | express-transport-belt | turbo-transport-belt |
|---|---|---|---|---|
| stone-furnace | 666.67 | 1333.33 | 2000 | 2666.67 |
| steel-furnace | 666.67 | 1333.33 | 2000 | 2666.67 |

## Practical consequence

This dwarfs the furnace counts in this project's actual smelting
modules by 1-2 orders of magnitude — e.g.
[layouts/steel_smelting_module.md](../layouts/steel_smelting_module.md)'s
120-steel-furnace (or 240-stone-furnace) module needs only 2.7 coal/sec
(or 5.4 coal/sec), **under half of one `transport-belt`** either way.
Coal supply is never the bottleneck for a furnace module sized to
saturate a plate belt — a single shared coal lane (often not even
running at full throughput) covers the whole module; there's no need
to size or split coal per furnace row the way ore/plate lanes need to
be.

Verified: 2026-08-22 (derivation re-run directly against
`formulas/fuel_consumption_rate.py`, not hand arithmetic).
