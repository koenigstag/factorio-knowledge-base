# Fluid system throughput (soft cap)

## max_flow_per_connection_sec_practical = 4200

The hard theoretical cap (6000 fluid/s per connection, 100/tick) *is*
a `data.raw` value — see `datapacks/dump/vanilla/utility-constants/default.json`'s
`max_fluid_flow`, documented in `datapacks/dump/vanilla/UNITS.md`.

This 4200 figure is different in kind, not just in size: the wiki
states it as "usually around" 4200, not a stored constant — it emerges
from the segment's fill-level-dependent flow dynamics (an emptier
segment fills faster than a fuller one), which isn't captured as a
single value anywhere in `data.raw`. It fails both tests that would
route it elsewhere: not in `data.raw` (→ not `datapacks/`), and not
something this project can currently derive via a general formula from
primitives it holds (→ not `relations/`) — a soft, hedged, but still
sourced game-behavior fact, which is exactly what `constraints/` is
for. Kept separate from the hard 6000/s figure so the two aren't
mistaken for the same evidentiary weight.

Source: https://wiki.factorio.com/Fluid_system
Verified: 2026-08-06
