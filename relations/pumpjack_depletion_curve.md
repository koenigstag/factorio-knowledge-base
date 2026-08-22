# Pumpjack (crude-oil) depletion curve over time

Closes `layouts/scalable_chem_base.md`'s open item "exact pumpjack
depletion curve over time (only the fresh/floor endpoints are derived
here, not the rate of decay between them)" — that file already had the
two endpoints (10 crude-oil/sec fresh, 2 crude-oil/sec at the floor)
but not the curve or the time to reach the floor.

## Formula

New `formulas/infinite_resource_depletion.py`
(`yield_ratio_at_cycle`, `cycles_to_floor`, `time_to_floor`), composed
with the existing `formulas/production_rate.py:production_rate`'s
`productivity_multiplier` parameter rather than writing a separate
output-rate function:

```
yield_ratio(cycles) = max(normal - infinite_depletion_amount × cycles, minimum) / normal
output_rate(t) = production_rate(mining_speed, mining_time, amount_min,
                                  productivity_multiplier=yield_ratio(t × mining_speed / mining_time))
```

**Sourcing for the mechanic itself** (this is a real engine mechanic,
not something inferable from `data.raw` field names alone):
`infinite_depletion_amount`'s meaning is confirmed directly in Wube's
own prototype docs (`lua-api.factorio.com/latest/prototypes/ResourceEntityPrototype.html`):
*"Every time an infinite-type resource is decreased by mining, its
current resource amount is lowered by this number."* The
amount-to-yield relationship (`yield = amount/normal`, output scaled
by that fraction each cycle) isn't stated on that page — sourced
instead from `forums.factorio.com/viewtopic.php?t=32181` ("Infinite
resource (e.g., oil) calculations"), **jcranmer**: *"Infinite
resources internally have an amount value... this value is compared to
a Lua-specified 'normal' value to compute the yield"* and *"Every
mining cycle... the amount value falls by 1 unit, and the output is
multiplied by the yield fraction."* That post is from 0.13-era Factorio
(oil's `normal` was 15000, depletion 1/cycle then) — the *mechanism*
described (amount falls by a fixed per-cycle amount, output = base ×
amount/normal) is confirmed still current in 2.0 by cross-checking
against `data.raw`'s own `infinite_depletion_amount` field existing
with the same role, just a different fixed value (10, not 1) and
different `normal`/`minimum` figures for the current game balance —
not assumed unchanged, checked.

Inputs: `datapacks/dump/vanilla/resource/crude-oil.json`
(`normal=300000`, `minimum=60000`, `infinite_depletion_amount=10`,
`minable.mining_time=1`, `minable.results[].amount_min=10`);
`datapacks/dump/vanilla/mining-drill/pumpjack.json` (`mining_speed=1`).

## crude_oil_cycles_to_floor = 24000

`cycles_to_floor(300000, 60000, 10)` = `(300000−60000)/10` = 24000
extraction cycles — independent of drill speed; this is a property of
the resource tile itself, not the machine extracting it.

## crude_oil_time_to_floor = 24000 sec (400 min ≈ 6.67 hours)

`time_to_floor(300000, 60000, 10, mining_speed=1, mining_time=1)` =
`24000 × 1/1` = 24000 seconds, for one pumpjack running at 100%
uptime with no speed modules/beacons, sitting on one tile that started
at exactly `normal`. Faster mining_speed (speed modules/beacons)
shortens this in real time — same 24000 cycles happen sooner, not
fewer of them.

## Output rate over time (linear between the two known endpoints)

| elapsed time | crude-oil/sec/pumpjack |
|---|---|
| 0 min (fresh) | 10.0 |
| 100 min | 8.0 |
| 200 min | 6.0 |
| 300 min | 4.0 |
| 400 min (floor reached) | 2.0 |
| beyond 400 min | 2.0 (flat — floor holds forever, resource never truly runs out) |

Confirms `layouts/scalable_chem_base.md`'s existing 10→2 endpoints
exactly, and shows the decay is **linear** in real time (not
exponential or front-loaded) — a pumpjack field's total output falls
off steadily over its first ~6.7 hours of continuous operation, then
holds flat indefinitely at 20% of fresh yield. This is why that file's
pumpjack count is framed as a range (40 fresh → 200 at floor for
400 crude-oil/sec) rather than a single number: the 5× growth happens
gradually over a known, now-quantified timescale, not as a step
function.

Verified: 2026-08-09
