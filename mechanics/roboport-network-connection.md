# Roboport network connection: border-touching, two independent networks

See `mechanics/robot-types.md` for why roboports exist at all (the
resting/charging anchor for construction and logistic robots),
`mechanics/logistic-chest-priority.md` for how logistic robots use the
network this file describes to actually move items between chests,
and `mechanics/construction-robot-job-assignment.md` for why a larger
merged network (easy to end up with given the border-touching rule
below) makes construction bots more likely to fly past near jobs for
far ones.

## "Connected" means coverage-area borders touch, not overlap

Two roboports join the same network if their square coverage areas'
borders merely **touch** — this is a `≤` condition on center-to-center
distance, not a strict overlap requirement. The wiki states it
directly: *"two or more roboports can connect to form a logistic
network, if the borders of the orange logistic areas touch."* Same
rule for the green construction area. Practical consequence: the
`2 × radius` center-to-center spacing (see
`relations/roboport_network_range.md`) is the actual maximum usable
spacing, not merely a close approximation of it.

## Logistic and construction connectivity are two independent networks

A roboport has two separate coverage areas — logistic (orange,
smaller) and construction (green, larger) — and whether two roboports
cooperate on *each* is judged independently, using that area's own
touching rule. This is a deliberate design choice, not a side effect:
the wiki states roboports were specifically built so they *"can build
each other without interconnecting their logistic areas."*

Practical consequence for layout design: a new roboport placed just
inside construction range (up to 110 tiles from vanilla's
`construction_radius=55`, per `relations/roboport_network_range.md`)
but outside logistic range (>50 tiles) gets built/repaired by the
existing network's construction bots — useful for walking an outpost
outward one hop at a time — but its *own* logistic network (shared bot
inventory, item requests) stays isolated until a roboport bridges the
50-tile logistic gap too. Assuming 110-tile spacing keeps one shared
logistic network is a common design mistake this rule explains.

Neither rule is a `data.raw` field — the coverage-area *radii* are
(`roboport.logistics_radius`/`construction_radius`, see
`datapacks/dump/vanilla/roboport/roboport.json`), but "what counts as
connected" and "why two independent rules" are network-simulation
behavior, not stored values.

Source: https://wiki.factorio.com/Roboport
Verified: 2026-08-08
