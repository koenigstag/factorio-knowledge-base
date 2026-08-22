# Thruster fuel/oxidizer supply ratio (space platforms)

`thruster` is a space-platform-only entity (`surface_conditions:
[{"property":"pressure","min":0,"max":0}]` — zero pressure, i.e. open
space/vacuum) that converts `thruster-fuel` + `thruster-oxidizer` into
thrust. Both feed fluids are themselves zero-gravity-locked recipes
(`surface_conditions: [{"property":"gravity","min":0,"max":0}]`),
consistent with being craftable only aboard a platform, not on a
planet's surface.

Formula: `formulas/production_rate.py:production_rate`.

Inputs: `datapacks/dump/vanilla/thruster/thruster.json`
(`max_performance`/`min_performance`), `recipe/thruster-fuel.json`,
`recipe/thruster-oxidizer.json` — `chemical-plant` `crafting_speed=1`
assumption, same as elsewhere in `relations/`.

## Fuel/oxidizer production rate: 37.5/sec per chemical plant

Both recipes are identical in shape: `energy_required=2`, 75 fluid out
per craft. `production_rate(1, 2, 75)` = 37.5/sec, for each fluid.

## Thruster consumption: throttle-dependent, 6–120/sec per fluid

The thruster has no single fixed consumption rate — `fluid_usage`
scales with how full its fluid buffer is, between `min_performance`
(`fluid_usage=0.1/tick`, `effectivity=1`) and `max_performance`
(`fluid_usage=2/tick`, `effectivity=0.51`). At 60 ticks/sec: `0.1 × 60`
= 6/sec (min) to `2 × 60` = 120/sec (max), for **each** of fuel and
oxidizer (both fluid boxes share the same performance curve).

**Matches `wiki.factorio.com/Thruster`** (fetched directly, not
cited secondhand): *"at 0-10% filled reserves, thrusters operate at
100% efficiency but consume only 6... units/s"* and *"at 80-100% full
reserves, efficiency drops to 51% while consumption peaks at 120...
units/s"* — both endpoints confirmed independently against the `min_
performance`/`max_performance` fields above. The wiki explicitly does
**not** give a derivation for thrust vs. fuel (*"thrust has diminishing
returns in either thrusters or fuel, unless both of them are added"*,
no closed-form formula stated), so only these two throttle endpoints
are derived here — not a general thrust curve.

## fuel_plants_per_thruster = oxidizer_plants_per_thruster = 3.2 (at max throttle)

At full/max-throttle operation (the sustained-thrust design point, not
the fuel-efficient low-throttle one): `120 / 37.5` = 3.2 chemical
plants needed per thruster, for fuel and for oxidizer identically (both
recipes and both consumption rates are symmetric).

**Cross-check against `factoriocheatsheet.com`'s space-platform
`thrusterRatio`** (source cited there as `wiki.factorio.com/Thruster`,
though the wiki fetch above found no explicit ratio on that page):
normalizing its stated "0.625 thruster : 2 storage-tank : 2
chemical-plant(oxidizer) : 2 chemical-plant(fuel) : 1
chemical-plant(water) : 0.15/0.3/0.3 crusher" to 1 thruster gives
`2/0.625 = 3.2` chemical plants for both fuel and oxidizer — an exact
match to the value derived here from `data.raw` alone.

## Not independently derived (flagged, not fabricated)

The cited ratio's storage-tank (3.2/thruster, buffer sizing — not a
rate this project has a formula for), water-supply chemical-plant
(1.6/thruster — ambiguous what recipe this represents; possibly a
mislabeled reference to the 5 water/sec each fuel/oxidizer recipe
consumes, `10 water ÷ 2 energy_required`, rather than a literal
water-producing chemical plant, but not confirmed), and the three
asteroid-crushing `crusher` counts (need `crusher`/asteroid-crushing
recipe data this project doesn't hold yet) are left uncited rather than
guessed. Only the fuel/oxidizer chemical-plant count above is derived
and verified; the rest of the cited ratio is noted here as an
unverified community figure, not imported as fact.

Verified: 2026-08-08
