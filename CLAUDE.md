# CLAUDE.md

Operating rules for working in this repository.

## Language

All content and documentation in this repository is in English.

## About the project

Factorio Knowledge Base: stores values, formulas and patterns for the
game Factorio, and teaches LLMs how to work with them to plan bigger
factories.

## Hard rules

1. **Never add a numeric fact without a source.** In `constraints/`,
   the bare value lives in `<topic>.json` (no source fields — keep it
   lean so an LLM can query the fact without loading prose), and its
   sourcing/history/caveats live in a paired `<topic>.md` of the same
   basename (`Source:`/`Verified:` per value, plus whatever narrative
   context applies — e.g. `rails.json`'s `curve_radius_tiles` is
   explained in `rails.md`). The pairing is by filename convention,
   not an explicit cross-reference field. Entries under
   `datapacks/dump/<mod-set>/` get their provenance from the shared
   `datapacks/dump/<mod-set>/source.json` manifest instead — see rule
   5. A bare remembered number is rejected — this project already
   caught an error this way once: an early pass cited rail turn radius
   as 10 tiles from an unreliable search snippet; the actual sourced
   value (Friday Facts #377) is 11 tiles pre-2.0 / 13 tiles in 2.0.

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

5. **`datapacks/` has sub-sources, not one format.**
   `datapacks/dump/<mod-set>/<type>/<name>.json` mirrors
   `data.raw[type][name]` from a `factorio --dump-data` run made with
   a specific set of mods enabled (e.g. `vanilla` = base + official
   DLCs only, no data-affecting third-party mods). Provenance (game
   version, mod set, extraction date) lives once in
   `datapacks/dump/<mod-set>/source.json`, not repeated per file — a
   modded playthrough gets its own `<mod-set>` folder alongside
   `vanilla`, never mixed into it, since a mod can change recipes,
   crafting speeds, or add/remove prototypes entirely. Other datapack
   sources that aren't dump-derived at all (manually sourced,
   community-curated, etc.) get their own sibling folder directly
   under `datapacks/` with their own provenance convention (per-entry
   `source_url`/`verified_date`, per rule 1).

## Current structure

```
datapacks/dump/vanilla/   data.raw extract, base+DLC, one file per prototype — provenance in source.json
constraints/               hard engine limits — <topic>.json (bare values) + <topic>.md (sourcing/history)
glossary/                  canonical/ (established terms) vs invented/ (ours)
```

Not created yet (planned, not to be scaffolded speculatively):
`formulas/`, `relations/`, `patterns/`, `contracts/`, `modules/`,
`blueprints/`, `layouts/`, `generators/`, `benchmarks/`, `decisions/`,
`changelog/`. `contracts/`/`modules/` specifically should only be
created once a second interchangeable implementation of the same slot
exists — not upfront.

## Versioning

`main` always holds the latest supported game version directly (**2.0**
right now) — not an empty scaffold branch pointing at something else.
A version branch is cut **retroactively**, only at the moment a newer
version's data would actually diverge from what's recorded here: branch
off the last commit still valid for the old version (e.g. `2.0`),
freezing it, then keep evolving `main` forward as the new latest.
Branches are per major version (not per patch/minor release, not a
folder inside the tree), created reactively like `contracts/`/
`modules/` — never pre-provisioned for a version that doesn't need to
diverge yet.
