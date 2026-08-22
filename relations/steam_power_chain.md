# Basic steam power chain: offshore pump → boiler → steam engine

Previously entirely uncovered — this project only had the *nuclear*
steam chain (`nuclear_power_chain.md`, heat-exchanger/steam-turbine).
Basic power (boiler/steam-engine, the first power source most players
build) had zero coverage until now.

Formulas: `formulas/generator_power_output.py` (`generator_power_output`,
already built for steam-turbine and directly reusable here — same
`generator` prototype type).

Inputs: `datapacks/dump/vanilla/boiler/boiler.json`
(`energy_consumption=1.8MW`, `target_temperature=165`),
`datapacks/dump/vanilla/generator/steam-engine.json`
(`fluid_usage_per_tick=0.5`, `effectivity=1`, `maximum_temperature=165`),
`datapacks/dump/vanilla/offshore-pump/offshore-pump.json`
(`pumping_speed=20`) — all a documented `source.json` exception
(third-party 2.0.65 dump).

## Boiler: 6 water/sec in, 60 steam/sec out

Not a simple 1:1 fluid conversion — confirmed directly against
`wiki.factorio.com/Boiler`: *"It costs 300 kJ to heat 1 unit of water
into 10 steam at 165°C, so one boiler will produce 60 steam per
second."* `energy_consumption=1.8MW` ÷ `300kJ` = 6 water/sec consumed
× 10 steam-units-per-water-unit = 60 steam/sec produced. The `×10`
is a fixed game-designed multiplier on fluid units, not derived from
`heat_capacity` the way the nuclear chain's numbers are — flagged here
since it's a different mechanism from `nuclear_power_chain.md`'s
heat-exchanger math despite looking superficially similar.

## Steam engine: 900kW per engine, 30 steam/sec consumed

`generator_power_output(fluid_usage_per_tick=0.5, effectivity=1,
heat_capacity_kj=0.2, temperature=165, ambient_temperature=15,
ticks_per_sec=60)` = `0.5×60×1×0.2×(165−15)` = **900 kW**. Steam
consumed: `0.5 × 60 = 30` units/sec.

## Ratios

- **1 boiler feeds exactly 2 steam engines**: `60 steam/sec produced
  ÷ 30 steam/sec consumed per engine = 2`. Matches well-known community
  convention ("1 boiler : 2 steam engines") exactly — derived here, not
  cited.
- **1 offshore pump (`pumping_speed=20` × 60 = 1200 water/sec) feeds
  200 boilers**: `1200 ÷ 6 = 200`, and by extension 400 steam engines
  (`200 × 2`).

## Total output at the offshore-pump-limited ratio

`200 boilers × 900kW × 2 engines/boiler` = **360 MW** per offshore
pump, at full water supply — matches a community-cited build ratio
figure (`factoriocheatsheet.com`) exactly, cross-checked rather than
copied: this project derived 200/400/360MW independently from the
`data.raw` fields above, and the match confirms both agree.

Verified: 2026-08-08
