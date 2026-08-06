# layouts/

`glossary/invented/` defines `city-block`, `main-bus`, `gap-chunk`,
`export-block` as separate terms, each in isolation. `layouts/`
composes them into one concrete, repeatable base pattern — how they
connect spatially, not just what each one means on its own.

Difference from `decisions/`: a decision records *why* a choice was
made (context/alternatives/consequences); a layout records the
resulting arrangement itself, and can reference whichever decision
produced a given parameter. Numeric parameters here either cite a
`formulas/`/`relations/`/`constraints/` value or stay explicitly
flagged open — never guessed, same rule as everywhere else in this
repo (see CLAUDE.md rule 1).
