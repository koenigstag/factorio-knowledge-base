# Vulcanus power chain: acid-neutralisation → steam-condensation / steam-turbine

Vulcanus skips the boiler entirely: `acid-neutralisation` produces
steam directly at 500°C — exactly `steam-turbine.maximum_temperature`
(`datapacks/dump/vanilla/generator/steam-turbine.json`) — so turbines
run at full rated output with no heat-exchanger step either. This is
the same steam-turbine prototype and the same `generator_power_output`
formula already used for the nuclear chain
(`relations/nuclear_power_chain.md`), fed by a different source recipe.

Formulas: `formulas/production_rate.py:production_rate`,
`formulas/generator_power_output.py:generator_power_output`.

Inputs: `datapacks/dump/vanilla/recipe/acid-neutralisation.json`,
`recipe/steam-condensation.json`, `generator/steam-turbine.json`,
`fluid/steam.json` — all `crafting_speed=1` (`chemical-plant`, per the
same assumption `oil_cracking_ratio.md` and `bus_lane_ratios.md`
already use).

## Cleanly derived

- **acid-neutralisation → 2000 steam/sec at 500°C**:
  `production_rate(1, 5, 10000)` = 2000/s. `surface_conditions:
  [{"property":"pressure","min":4000,"max":4000}]` matches Vulcanus's
  own `pressure=4000` (`glossary/canonical/surface.md`) exactly,
  confirming the recipe is Vulcanus-exclusive.
- **steam-condensation consumes 1000 steam/sec, produces 90
  water/sec**: `production_rate(1, 1, 90)` = 90/s water;
  `1000/1` = 1000/s steam consumed.
- **1 acid-neutralisation : 2 steam-condensation balances exactly**:
  `2000 / 1000` = 2 — self-consistent sub-ratio, confirmed independent
  of the turbine count below.
- **steam-turbine at 500°C = 5.82 MW**: `generator_power_output(
  fluid_usage_per_tick=1, effectivity=1, heat_capacity_kj=0.2,
  temperature=500, ambient_temperature=15, ticks_per_sec=60)` = 5820 kW
  — the same 5.82 MW figure `nuclear_power_chain.md` derived for the
  same prototype at the same temperature (wiki-confirmed there), simply
  reached via a different steam source here. Steam consumed:
  `1 × 60` = 60/sec.
- **100 turbines ≈ 580 MW**: `100 × 5.82` = 582 MW, matching the cited
  580 MW target via energy conservation (rounding) — this part of the
  ratio checks out independent of the flow-rate flag below.

## Flagged: the cited "1 : 2 : 100" ratio does not mass-balance as a single flow chain

`factoriocheatsheet.com`'s Vulcanus data (`vulcanus.data.ts`,
`steamTurbinePowerRatio`) states 1 acid-neutralisation : 2
steam-condensation : 100 steam-turbine for 580 MW, with no stated
derivation or source URL (empty `source` field in the upstream file).

Taken as a literal single production line, it doesn't balance:
100 turbines at full flow need `100 × 60` = 6000 steam/sec, but 1
acid-neutralisation only supplies 2000 steam/sec — a 3x shortfall. To
actually feed 100 turbines at full output requires **3** acid-
neutralisation units (`6000 / 2000`), and by the confirmed 1:2
sub-ratio, **6** steam-condensation units, not 1 and 2.

The 1:2 sub-ratio and the 100-turbine power target are each internally
consistent on their own (see above) — what doesn't reconcile is
treating all three counts as one connected flow. Two readings are
possible: either the source's "1:2" is a per-repeatable-module ratio
(build N of these 1:2 pairs, scaled independently of the stated 100
turbines) and the numbers were never meant to combine into a single
literal count, or it's simply an uncorroborated/imprecise community
figure — this project has already caught one stale cheat-sheet citation
this session (`science_pack_ratios.md`'s space-science-pack). Left
unresolved rather than forced, per this project's standing policy for
unreconciled discrepancies (see `wagon_loading_throughput.md`'s
wagon-inserter-cycle-rate flag for the same pattern).

Verified: 2026-08-08
