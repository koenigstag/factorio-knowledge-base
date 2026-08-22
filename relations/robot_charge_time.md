# Robot charge time

How long a robot takes to recharge at a roboport, in seconds.

Formula: `formulas/robot_charge_time.py:charge_time_seconds`
(`energy_to_add / charging_power`) — kJ ÷ kW = seconds directly, no
conversion factor needed.

Inputs: `robot.max_energy`, `min_to_charge`, `max_to_charge` (see
`relations/robot_flight_range.md` for sourcing) and
`roboport.charging_energy=500kW` from
`datapacks/dump/vanilla/roboport/roboport.json` — confirmed via
`lua-api.factorio.com/latest/prototypes/RoboportPrototype.html` to be
the power delivered to *each individual* charging station, not a
500kW pool split across every robot docked at that roboport. This
matters: a roboport charging several robots at once isn't
throughput-limited by this field the way it would be if it were
shared — see `roboport.material_slots_count`/`robot_slots_count` for
the actual concurrency cap (how many can dock/charge at once), still
unconfirmed in this project (open question).

## Charge time by scenario

| robot | full charge, 0→100% (s) | usable-band charge, 20%→95% (s) |
|---|---|---|
| construction-robot | 6.0 | 4.5 |
| logistic-robot | 3.0 | 2.25 |

The usable-band figure is the more realistic one for layout planning:
per `mechanics/robot-types.md`/`UNITS.md`'s hysteresis note, a robot
only returns to charge once below `min_to_charge` (20%) and only
leaves once above `max_to_charge` (95%) — so 4.5s / 2.25s is the
typical top-up time a returning robot actually needs, not the
worst-case 0%-start figure.

Combined with `relations/robot_flight_range.md`: a construction robot
flies for up to ~385.7 tiles (usable band) then spends ~4.5s
recharging before its next trip — the charge time is small relative
to a full flight leg unless the network is very densely packed with
short hops.

Verified: 2026-08-08
