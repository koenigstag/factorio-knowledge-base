# Why roboports exist, and the two robot types

## Roboport: the resting/charging anchor for both robot types

A roboport is the resting place for every construction and logistic
robot in its network — robots return to a roboport to recharge, and a
robot with no roboport in range can't operate at all. It also defines
the two coverage areas the rest of `mechanics/roboport-*` and
`relations/roboport_*` are built on: a 50×50 logistic area (where
logistic robots may interact with logistic-network entities like
chests) and a 110×110 construction area.

## Construction robots vs logistic robots: different jobs, same charging infrastructure

- **Logistic robots** move items between logistic-network entities —
  chests, the player's own logistic requests, and other logistic
  robots' pending deliveries. They don't build anything; they're pure
  transport.
- **Construction robots** do the opposite: they repair damaged/destroyed
  entities, and build, deconstruct, or upgrade entities on command
  (blueprint placement, deconstruction planner, upgrade planner), plus
  handle item requests/removal requests created in remote (map) view.

`datapacks/dump/vanilla/item/construction-robot.json` and
`logistic-robot.json` record the *item* side (stack_size=50,
`place_result`); the entity's own movement/energy stats are now in
`datapacks/dump/vanilla/construction-robot/` and `logistic-robot/`
(speed, payload, battery — see `datapacks/dump/vanilla/UNITS.md` for
field meanings, flagged there as a third-party-dump exception in
`source.json` since it wasn't pulled in this project's own extraction
run). The functional role split above is still behavioral, sourced
from the wiki, not read off any stored field.

Practical numbers built on these stats: `relations/robot_flight_range.md`
(how far a robot flies on a charge) and `relations/robot_charge_time.md`
(how long recharging takes) — both at the unresearched baseline.
`mechanics/worker-robot-research.md` covers how research modifies
speed and cargo capacity on top of these base stats.
`mechanics/construction-robot-job-assignment.md` covers *which* job a
construction robot picks next — not nearest-first, contrary to the
intuitive assumption.

Source: https://wiki.factorio.com/Roboport, https://wiki.factorio.com/Logistic_network
Verified: 2026-08-08
