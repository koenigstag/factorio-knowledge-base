# Fluid system throughput

Factorio 2.0 reworked fluid mechanics ("Fluids 2.0", Friday Facts
#416): contiguous pipe runs merge into a single "segment" holding one
fluid, and — unlike pre-2.0 — throughput no longer degrades with
pipeline length/segment count. The limit that remains is **per unique
input/output connection** (e.g. where a machine or pump connects to a
segment), not per pipe or per distance.

## max_flow_per_connection_tick = 100

Theoretical maximum flow through a single connection, in fluid
units/tick (the game's internal fluid-unit scale — see
`datapacks/dump/vanilla/UNITS.md`'s `fluid_box.volume` entry, not
liters or any real-world unit).

## max_flow_per_connection_sec_theoretical = 6000

Same figure as above, ×60 (consistent with this project's established
tick→second convention). Direct wiki quote: *"Each unique input and
output connection has a theoretical maximum throughput limit of 6000
fluid per second (100 fluid per tick)."*

## max_flow_per_connection_sec_practical = 4200

**Softer figure than the two above** — the wiki states this as "usually
around" 4200, not a hard guarantee: actual flow rate depends on the
segment's current fill level (an emptier segment fills faster than a
fuller one), so 4200/s is a commonly-observed steady-state figure, not
a fixed cap. Treat 6000 as the hard ceiling and 4200 as a practical
planning estimate, not interchangeably.

**Doubling note**: if a machine has two separate output connections of
the same fluid, the limit applies to each independently — effectively
~8400/s combined, not a shared 4200/s pool. Same "per connection, not
per machine" logic likely means a pipe segment feeding N separate
consumer connections could theoretically deliver up to N × the limit,
though this hasn't been checked against a worked example yet.

Source: https://wiki.factorio.com/Fluid_system
Verified: 2026-08-06
