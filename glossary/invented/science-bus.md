# science bus

A second, dedicated belt bus running alongside (not merged into) the
main bus, carrying only science-pack items from the city-blocks that
produce them onward toward labs — either directly to an on-site labs
block, or (the variant this project actually uses, see
`layouts/scalable_main_base.md`) to a pack train station
that ships them by rail to a labs field on a separate, remote site.
Distinct from routing science packs through the main bus itself:
keeping them separate means a science-pack producer block's output
side never contends with the main bus's general item traffic.

A science-pack-producing block that feeds this bus instead of the main
bus spends one of its two bus-facing ports on that instead — its
output leaves the grid in a different direction rather than rejoining
the main bus.

Coined in `layouts/scalable_main_base.md` while positioning
red/green science modules relative to a main-bus city-block grid; not
yet backed by a `decisions/` ADR.
