# black-start coal supply

A `self-fueling burner drill` pair (see `glossary/canonical/`), kept
running specifically as a coal source for a coal-fired power plant
(`boiler` + `steam-engine`), *in addition to* whatever `electric-mining-drill`s
normally supply the base's coal.

The problem it solves: if a coal-fired power base's *only* coal supply
comes from electric mining drills, there's a circular dependency —
electric drills need power to mine coal, and the plant needs coal to
make power. A total blackout (power drain, sudden load spike, attack)
stops the electric drills, which stops the coal supply, which means
the plant can never recover once it goes fully dark — nothing in the
system can restart it. A small burner-drill coal supply doesn't have
this dependency (it needs no electricity at all), so it keeps feeding
the boiler through a blackout and lets the plant — and from there the
rest of the base — restart on its own.

Named after "black start" in real-world power engineering: a power
station's ability to restart from a total shutdown without drawing on
an external grid.

Coined in this project during discussion of the `self-fueling burner
drill` mechanic — not yet backed by a `decisions/` entry or a sizing
formula (how much burner-drill coal throughput is "enough" of a
black-start reserve isn't derived anywhere in this repo yet).
