# Nuclear power chain: reactor → heat exchanger → steam turbine → heat pipe

Formulas: `formulas/nuclear_power_chain.py` (`heat_exchangers_per_reactor`,
`heat_exchanger_steam_output_per_sec`, `turbines_per_heat_exchanger`,
`heat_pipe_paths_needed`), `formulas/generator_power_output.py`
(`generator_power_output`).

## heat_exchangers_per_reactor = 4

`nuclear-reactor.consumption=40MW` ÷ `boiler/heat-exchanger.json`'s
`energy_consumption=10MW` (both `datapacks/dump/vanilla/`).

## steam_turbine_power_output_mw = 5.82

`generator_power_output(fluid_usage_per_tick=1, effectivity=1,
heat_capacity_kj=0.2, temperature=500, ambient_temperature=15,
ticks_per_sec=60)` = `1×60×1×0.2×(500-15)` = 5820 kW.

Inputs: `generator/steam-turbine.json`'s `fluid_usage_per_tick=1`,
`effectivity=1`, `maximum_temperature=500`; `fluid/steam.json`'s
`heat_capacity=0.2kJ` (see `UNITS.md`'s `heat_capacity` section: "Joule
needed to heat 1 Unit by 1°C", official `FluidPrototype` docs) and
`default_temperature=15` — the ambient baseline the engine measures
energy from (see `UNITS.md`'s Temperature section).

**Matches wiki.factorio.com/Steam_turbine exactly**, which gives the
identical calculation: *"(500°C - 15°C) × 0.2 kJ × 60 units/s = 5820
kJ/s, or 5.82 MW"* — independent confirmation that both the formula
and the `data.raw` inputs are right, not just a copied figure.

## heat_exchanger_steam_output_per_sec = 103.09

`heat_exchanger_steam_output_per_sec(energy_consumption_kw=10000,
heat_capacity_kj=0.2, target_temperature=500, ambient_temperature=15)`
= `10000 / (0.2 × 485)` = 103.09 — the heat exchanger spends its whole
10MW turning water into 500°C steam, using the same per-degree cost as
the turbine's formula, just solved for flow rate instead of power.

## turbines_per_heat_exchanger = 1.7182, turbines_per_reactor = 6.87

One heat exchanger's 103.09 steam/s ÷ one turbine's consumption
(`fluid_usage_per_tick=1` × 60 = 60/s) = 1.7182 turbines to fully
drain one exchanger. × 4 exchangers/reactor = 6.87 turbines/reactor.
Cross-check via energy conservation instead of fluid flow: 1 reactor's
40,000 kW ÷ 1 turbine's 5820 kW = 6.87 — same number both ways.

Not rounded up here (this file holds exact derived values, same
convention as `mining_furnace_ratios.json`'s fractional
`drills_per_furnace`) — a real build rounds up to whole machines, e.g.
7 turbines per reactor if you want the exchangers never bottlenecked,
or fewer if some turbine idle time is acceptable.

## min_heat_pipe_paths_by_reactor_grid

Whether one `heat-pipe` line out of a reactor block is enough, or the
pipe itself becomes the bottleneck: `heat_pipe_paths_needed(total_heat_kw,
max_transfer_kw)`, ceiling'd to a whole number of parallel routes.
Inputs: `heat-pipe.json`'s `heat_buffer.max_transfer=1GW` (1,000,000 kW)
per path; grid outputs from `relations/reactor_neighbor_output.json`'s
`total_mw_by_grid` (not repeated here, see that file).

| grid | total MW | ÷ 1000 MW/path | paths needed |
|---|---|---|---|
| 1 reactor | 40 | 0.04 | 1 |
| 2×2 | 480 | 0.48 | 1 |
| 2×4 | 1120 | 1.12 | 2 |
| 2×6 | 1760 | 1.76 | 2 |

**Why this matters**: a maxed 2×6 reactor grid (1760MW, see
`reactor_neighbor_output.md`) physically cannot dump its heat through
a single-tile-wide `heat-pipe` line — that path caps out at 1000MW,
44% short. This is a real, commonly-hit constraint (confirmed by
multiple independent Factorio forum threads on large reactor arrays
choking at "~1GW/pipe width"), not a theoretical edge case — any 2×4
or larger grid needs at least 2 separate heat-pipe routes leaving the
block, not just a wider manifold on one route.

Not covered: heat loss / maximum straight-line pipe distance before
temperature drops below the exchanger's 500°C `min_working_temperature`
— community formulas exist for this, but they weren't independently
verified against `data.raw` fields the way everything else in this
file was, so left out rather than cited secondhand (per this project's
sourcing rule).

Verified: 2026-08-07
