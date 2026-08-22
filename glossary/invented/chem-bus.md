# chem bus

The internal transport spine of a chem-base — a
[main-bus](../canonical/main-bus.md)-shaped pattern adapted for a
site whose inputs mostly arrive by rail rather than by local mining,
and whose intermediates are mostly fluids rather than solid items.
Two things distinguish it from a plain main bus:

- **Its solid lanes start from a rail station, not an ore patch.**
  Everything a chem-base can't make from its own local resource (coal,
  a little iron/copper-plate, electronic-circuit, engine-unit) arrives
  by train and is unloaded straight onto the bus, the same way
  `layouts/scalable_main_base.md`'s ore-train-station feeds
  its furnace block — just carrying finished/semi-finished items
  instead of raw ore.
- **It runs pipes alongside belts**, not belts alone. Most chem-base
  modules connect to their neighbors by fluid (petroleum-gas, water,
  sulfur... — sulfur is solid, but sulfuric-acid, lubricant, heavy-oil
  are fluids), not by belt, so the bus itself has to carry pipe lanes
  for the fluids that *do* travel between modules on-site, alongside
  belt lanes for the few solids that do. Pipe-side throughput/distance
  limits, the analog of `relations/underground_belt_crossing_gap.md`
  for belts, are now sourced: max flow per connection
  (`mechanics/fluids.md`, 4200/sec practical, 6000/sec theoretical) and
  underground crossing gap (`relations/pipe_underground_crossing_gap.md`,
  9 tiles) — not an open gap anymore, just wasn't cross-linked from
  here when this term was first coined.

Coined in `layouts/scalable_chem_base.md` while designing chem-base
internal transport; not yet backed by a `decisions/` ADR.
