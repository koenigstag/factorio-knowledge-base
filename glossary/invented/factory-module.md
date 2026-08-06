# factory module

A self-contained production cell for one function (mining, smelting,
gear/cog crafting, science-pack assembly, research labs, ...). Its
size (machine count) is set by throughput-matching against whatever
belt(s) feed its import `port` — not a fixed ratio. Depending on belt
tier and the module's own consumption rate, several modules can share
one import belt, or one module can need more than one belt;
`relations/smelting_ratios.json`'s `furnaces_per_belt` gives the
per-tier saturation point for the single-module case specifically, not
a universal 1:1 module-to-belt rule.

Scaling rule: when a module's throughput need exceeds what its current
port(s) provide, add capacity — another belt at the port, or an
entirely new module with its own port — rather than overloading what's
already there. Like adding a RAM stick to an empty slot instead of
overclocking the one you have: the `port` (see
`glossary/invented/port.md`) is the slot, the module is what plugs
into it. A `city-block` can hold several factory modules side by side,
same function or different ones.

Implements one `contract` (see `glossary/invented/contract.md`): the
function stays fixed (e.g. "produces steel-plate from iron-plate"),
but which tier fulfills it (stone/steel/electric-furnace) changes the
concrete module's machine count for a given belt, since
`furnaces_per_belt` differs by tier.

Renamed from the earlier "module" — collided with `data.raw`'s
`module` prototype type (`quality-module`, `productivity-module`,
...), and on closer reading was used inconsistently across this
project's own files (the old `module.md` meant the whole cross-tier
family; `port.md` meant one concrete sized instance). This definition
settles on the second, concrete-instance meaning.

Coined during initial architecture discussion; refined 2026-08-07.
