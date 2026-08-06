# layouts/

Documents concrete spatial-arrangement patterns for base building —
how specific building types (mining drills, furnaces, assembling
machines, labs, main bus, ...) are positioned relative to each other —
side by side as different named approaches, not one "correct" answer.

`glossary/invented/`+`glossary/canonical/` define individual terms
(`city-block`, `main-bus`, `gap-chunk`, `export-block`, ...) in
isolation; a file here composes specific terms/building types into one
concrete, named pattern. One file per pattern — `city_block_grid.md`
is the city-block approach specifically. Other approaches (a plain
main-bus layout without city-blocks, a drill-to-furnace smelting
array, a lab layout) get their own files as they're written up, not
merged into one.

Difference from `decisions/`: a decision records *why* a choice was
made (context/alternatives/consequences); a layout records the
resulting arrangement itself, and can reference whichever decision
produced a given parameter. Numeric parameters here either cite a
`formulas/`/`relations/`/`constraints/` value or stay explicitly
flagged open — never guessed, same rule as everywhere else in this
repo (see CLAUDE.md rule 1).
