# main bus

A base-organization pattern: route the most-used intermediate items
(iron/copper/steel plates, circuits, etc.) down a shared set of belts
("the bus") that assembly lines tap off of, instead of routing each
item point-to-point ("spaghetti"). Direction (horizontal/vertical) and
belt grouping are a matter of preference, not an engine rule.

Official Wube tutorial, not just a community term:
> "The concept of a Main Bus is to put the most used and useful
> ingredients in a central spot to use for assembling machines."

This project's `tap-module` (see `glossary/invented/`) describes
infrastructure that plugs into a main bus at a city-block boundary. See
[layouts/main_bus_consumer_layout.md](../../layouts/main_bus_consumer_layout.md)
for how they all compose into one grid, or
[layouts/main_bus.md](../../layouts/main_bus.md) for the bus as a
standalone pattern (grouping, spacing, tap-off convention) without the
city-block grid around it. Contrasting delivery mechanism:
[train-base](train-base.md) (discrete train runs instead of
continuous belt flow).

Source: https://wiki.factorio.com/tutorial:main_bus
Verified: 2026-08-06
