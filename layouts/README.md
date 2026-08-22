# layouts/

Documents concrete spatial-arrangement patterns for base building —
how specific building types (mining drills, furnaces, assembling
machines, labs, main bus, ...) are positioned relative to each other —
side by side as different named approaches, not one "correct" answer.

`glossary/invented/`+`glossary/canonical/` define individual terms
(`city-block`, `main-bus`, ...) in isolation; a file here composes
specific terms/building types into one
concrete, named pattern. One file per pattern —
[city_block_grid.md](city_block_grid.md) is the (dominant,
rail-connected) city-block approach, and
[main_bus_consumer_layout.md](main_bus_consumer_layout.md) is the
belt-through-gaps alternative, split out separately since it isn't
that same dominant case. Other approaches (a plain
main-bus layout without city-blocks, a drill-to-furnace smelting
array, a lab layout) get their own files as they're written up, not
merged into one.

Difference from `decisions/`: a decision records *why* a choice was
made (context/alternatives/consequences); a layout records the
resulting arrangement itself, and can reference whichever decision
produced a given parameter. Numeric parameters here either cite a
`formulas/`/`relations/`/`mechanics/` value or stay explicitly
flagged open — never guessed, same rule as everywhere else in this
repo (see CLAUDE.md rule 1).
