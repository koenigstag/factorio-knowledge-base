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

2. **Distinguish `constraints/` from `datapacks/`.** The test is
   simple and has no exceptions: **if it's in `data.raw`, it's
   `datapacks/`, never `constraints/`.** `constraints/` is only for
   game conventions that have no `data.raw` representation at all —
   things you can't extract with `factorio --dump-data` no matter how
   you look, because they live in engine code, not data (rail turn
   radius, chunk size, map coordinate bounds, max inserters per
   wagon). This project first got this wrong for `quality`/`roboport`/
   `electric-pole` (all `data.raw` prototypes, moved to `datapacks/`),
   then again for `utility-constants.max_fluid_flow` (looked like a
   bare engine constant, turned out to be a real `data.raw` entry too
   — also moved to `datapacks/`). Before adding anything to
   `constraints/`, check the dump first — don't assume something is
   engine-only just because it isn't obviously per-entity data.

3. **Never state a derived number without its derivation.** A number
   obtained by combining two or more sourced facts (e.g. "24 steel
   furnaces saturate a yellow belt", from `recipe.energy_required` ÷
   `furnace.crafting_speed` ÷ `belt.speed`) belongs in `relations/`
   with a reference to the `formulas/` function that produces it — not
   as a flat value in `datapacks/`, `constraints/`, or prose. The test
   isn't "has anyone else published this number" (they probably have)
   — it's "do we already have the primitives to derive it ourselves":
   if yes, derive it via `formulas/`, don't cite someone else's
   pre-computed answer. Same `<topic>.json` (bare values) +
   `<topic>.md` (formula reference, inputs, computation) split as
   `constraints/` — see `relations/smelting_ratios.*` for the pattern.
   Contrast with a `constraints/` fact like max inserters per wagon:
   even though it's also a number, it isn't the output of any known
   formula over primitives we hold — it was discovered by empirical
   in-game testing, not computed, so it stays a constraint.

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
formulas/                  .py functions, pure — parameters in, number out, nothing hardcoded
relations/                 derived numeric relations — <topic>.json (bare values) + <topic>.md (formula + inputs used)
glossary/                  canonical/ (established terms) vs invented/ (ours)
decisions/                 ADRs — 000N-title.md, context/alternatives/decision/consequences
examples/                  walkthroughs: question → which files to read → formula call → result
layouts/                   spatial arrangement patterns for base-building (drills/furnaces/main-bus/labs/...) — one <name>.md per pattern; numeric params cite formulas/relations or stay flagged open, never guessed
```

`examples/` vs `relations/`: `relations/` is the cached answer,
`examples/` is the method that produced it — a plain-English question,
the primitives it needs, the actual `formulas/` call, and (where one
exists) a cross-check against the matching `relations/` entry. Write
one when the *pattern* of using a formula is worth showing, not one
per `relations/` entry.

Not created yet (planned, not to be scaffolded speculatively):
`patterns/`, `contracts/`, `modules/`, `blueprints/`,
`generators/`, `benchmarks/`, `changelog/`. `contracts/`/`modules/`
specifically should only be created once a second interchangeable
implementation of the same slot exists — not upfront. (`layouts/` was
in this list too until there was a first concrete pattern —
`city_block_grid.md` — worth writing up: how `city-block`, `main-bus`,
`city-block gap`, `export-block` position relative to each other. Other
approaches — plain main-bus, drill-to-furnace arrays, lab layout —
still belong in `layouts/` once written, not scaffolded ahead of
content.)

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
