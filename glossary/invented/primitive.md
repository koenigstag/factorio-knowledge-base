# primitive

A raw, verified (with `source_url` + `verified_date`) quantitative fact
about a game entity — a recipe, crafting speed, belt/inserter
throughput. Stored in `datapacks/`. Difference from a `constraint`: a
primitive is what gets plugged into a formula as a parameter; a
constraint is a hard limit a formula cannot exceed (e.g. the physical
cap on inserters per wagon).

Defined during initial architecture discussion.
