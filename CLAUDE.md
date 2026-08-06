# CLAUDE.md

Operating rules for working in this repository.

## Language

All content and documentation in this repository is in English.

## About the project

Factorio Knowledge Base: stores values, formulas and patterns for the
game Factorio, and teaches LLMs how to work with them to plan bigger
factories.

## Hard rules

1. **Never add a numeric fact without a source.** Every entry in
   `datapacks/` or `constraints/` must include `source_url` and
   `verified_date`. A bare remembered number is rejected — this
   project already caught an error this way once: an early pass cited
   rail turn radius as 10 tiles from an unreliable search snippet; the
   actual sourced value (Friday Facts #377) is 11 tiles pre-2.0 / 13
   tiles in 2.0.

2. **Distinguish `constraints/` from `datapacks/`.** A constraint is a
   hard engine limit that cannot be recalculated differently (e.g.
   rail turn radius, chunk size, max inserters per wagon). A datapack
   is raw input data that feeds a formula (recipe times, crafting
   speeds, belt throughput). If a fact changes under different formula
   inputs, it's not a constraint.

3. **Never state a derived number without its derivation.** A number
   obtained by combining two or more sourced facts (e.g. "26 tiles
   between rail centers" from radius × 2) belongs in `relations/` with
   a reference to the `formulas/` function that produces it — not as a
   flat value in `datapacks/`, `constraints/`, or prose.

4. **New term while describing something → `glossary/invented/`.** One
   file per term, plain English definition, a note on where/why it was
   coined.

## Current structure

```
datapacks/    raw game data (recipes, machine/belt throughput) — sourced, cited
constraints/  hard engine limits — sourced, cited
glossary/     canonical/ (established terms) vs invented/ (ours)
```

Not created yet (planned, not to be scaffolded speculatively):
`formulas/`, `relations/`, `patterns/`, `contracts/`, `modules/`,
`blueprints/`, `layouts/`, `generators/`, `benchmarks/`, `decisions/`,
`changelog/`. `contracts/`/`modules/` specifically should only be
created once a second interchangeable implementation of the same slot
exists — not upfront.

## Versioning

Content currently targets Factorio **2.0**. When a second game version
is actually needed, use one git branch per major version (not per
patch/minor release, not a folder inside the tree) — the repository is
meant to be checked out wholesale for one version at a time.
