# CLAUDE.md

Operating rules for working in this repository.

## Language

All content and documentation in this repository is in English.

## About the project

Factorio Knowledge Base: stores values, rules, formulas and patterns
for the game Factorio, and teaches LLMs how to work with them to plan
bigger factories.

## Hard rules

1. **Never add a fact or rule without a source — numeric or textual.**
   In `mechanics/`, a bare numeric value lives in `<topic>.json` (no
   source fields — keep it lean so an LLM can query the fact without
   loading prose), and its sourcing/history/caveats live in a paired
   `<topic>.md` of the same basename (`Source:`/`Verified:` per value,
   plus whatever narrative context applies — e.g. `rails.json`'s
   `curve_radius_tiles` is explained in `rails.md`). The pairing is by
   filename convention, not an explicit cross-reference field. A
   purely qualitative/behavioral rule with no number to extract (e.g.
   "an inserter can only pick up from and drop to the tile directly
   behind/in front of it, never a perpendicular tile") skips the
   `.json` and lives as `<topic>.md` alone — still with `Source:`/
   `Verified:`, the official wiki (wiki.factorio.com) counts as a
   valid source alongside Friday Facts. Entries under
   `datapacks/dump/<mod-set>/` get their provenance from the shared
   `datapacks/dump/<mod-set>/source.json` manifest instead — see rule
   5. A bare remembered fact is rejected — this project already
   caught an error this way once: an early pass cited rail turn radius
   as 10 tiles from an unreliable search snippet; the actual sourced
   value (Friday Facts #377) is 11 tiles pre-2.0 / 13 tiles in 2.0.

2. **Distinguish `mechanics/` from `datapacks/`.** The test is
   simple and has no exceptions: **if it's in `data.raw`, it's
   `datapacks/`, never `mechanics/`.** `mechanics/` is only for game
   rules and conventions that have no `data.raw` representation at
   all — things you can't extract with `factorio --dump-data` no
   matter how you look, because they live in engine code/behavior,
   not data. This covers both hard numeric limits (rail turn radius,
   chunk size, map coordinate bounds, max inserters per wagon) and
   qualitative behavioral rules useful for layout/design reasoning
   (an inserter's pickup/drop axis, a belt's side-loading behavior).
   This project first got this wrong for `quality`/`roboport`/
   `electric-pole` (all `data.raw` prototypes, moved to `datapacks/`),
   then again for `utility-constants.max_fluid_flow` (looked like a
   bare engine constant, turned out to be a real `data.raw` entry too
   — also moved to `datapacks/`). Before adding anything to
   `mechanics/`, check the dump first — don't assume something is
   engine-only just because it isn't obviously per-entity data.
   Overlaps in subject matter with `glossary/canonical/` (e.g.
   `belt-side-loading.md` explains a mechanic as part of defining that
   named term) — the split is by shape, not exclusivity: `glossary/`
   defines a *named* concept, `mechanics/` documents an engine rule or
   limit that isn't anchored to a term of its own (an inserter's
   pickup/drop axis has no special name — it's just how inserters
   work).

3. **Never state a derived number without its derivation.** A number
   obtained by combining two or more sourced facts (e.g. "24 steel
   furnaces saturate a yellow belt", from `recipe.energy_required` ÷
   `furnace.crafting_speed` ÷ `belt.speed`) belongs in `relations/`
   with a reference to the `formulas/` function that produces it — not
   as a flat value in `datapacks/`, `mechanics/`, or prose. The test
   isn't "has anyone else published this number" (they probably have)
   — it's "do we already have the primitives to derive it ourselves":
   if yes, derive it via `formulas/`, don't cite someone else's
   pre-computed answer. Same `<topic>.json` (bare values) +
   `<topic>.md` (formula reference, inputs, computation) split as
   `mechanics/` — see `relations/smelting_ratios.*` for the pattern.
   Contrast with a `mechanics/` fact like max inserters per wagon:
   even though it's also a number, it isn't the output of any known
   formula over primitives we hold — it was discovered by empirical
   in-game testing, not computed, so it stays in `mechanics/` rather
   than being re-derived.

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

6. **Read the relevant `mechanics/` files before reasoning about engine
   behavior — don't answer from memory.** If a question turns on how an
   entity actually behaves (which side an inserter picks up/drops from,
   which belt lane an inserter places onto, etc.), check whether
   `mechanics/` already has a sourced file for it *before* asserting an
   answer. This project already produced a confidently wrong analysis
   this way: an inserter-direction/resource-flow hypothesis for
   `blueprints/curated/earlygame/iron-gear-tileable/iron-gear-tileable.md` was built from
   an assumed mirrored pattern instead of checking inserter direction
   against the actual recipe first, and had to be corrected by the
   project owner. If `mechanics/` doesn't cover it yet, source it (rule
   1) before using it — don't state it from recollection either way.
   Reading the file isn't enough if the file itself is wrong, either:
   [mechanics/inserters-directionality.md](mechanics/inserters-directionality.md)
   stated the pickup/drop-side rule backwards from 2026-08-08 until
   2026-08-22 — sourced, "verified," cited, and still wrong, because
   its source was a wiki paraphrase nobody had cross-checked against
   `datapacks/dump/vanilla/inserter/*.json`'s own `pickup_position`/
   `insert_position` fields. It produced the *same* wrong answer twice
   on two independent real blueprints before the mistake was caught by
   re-deriving from the dump directly instead of trusting the file's
   prose. When a `mechanics/` claim is about to drive a consequential
   judgment (like which belt is import vs export), and a primitive
   dump value can check it directly, check the primitive — don't just
   cite the file.

## Current structure

```
datapacks/dump/vanilla/   data.raw extract, base+DLC, one file per prototype — provenance in source.json
mechanics/                 engine rules & hard limits, numeric or behavioral — <topic>.json (bare values, when numeric) + <topic>.md (sourcing/history)
formulas/                  .py functions, pure — parameters in, number out, nothing hardcoded
relations/                 derived numeric relations — <topic>.json (bare values) + <topic>.md (formula + inputs used)
glossary/                  canonical/ (established terms) vs invented/ (ours)
decisions/                 ADRs — 000N-title.md, context/alternatives/decision/consequences
examples/                  walkthroughs: question → which files to read → formula call → result
layouts/                   spatial arrangement patterns for base-building (drills/furnaces/main-bus/labs/...) — one <name>.md per pattern; numeric params cite formulas/relations or stay flagged open, never guessed
blueprints/                 blueprint-string parsing tooling (codec.py) + curated/ reference designs, one <slug>/ folder per entry (<slug>.txt raw string + <slug>.json decoded + <slug>.md provenance) — third-party entry folders directly at curated/, personal collection grouped by game stage in curated/{earlygame,init-game,midgame}/<slug>/ — see blueprints/README.md
```

`examples/` vs `relations/`: `relations/` is the cached answer,
`examples/` is the method that produced it — a plain-English question,
the primitives it needs, the actual `formulas/` call, and (where one
exists) a cross-check against the matching `relations/` entry. Write
one when the *pattern* of using a formula is worth showing, not one
per `relations/` entry.

`patterns/`, `contracts/`, `factory-modules/`,
`generators/`, `benchmarks/`, `changelog/`. `contracts/`/`factory-modules/`
specifically should only be created once a second interchangeable
implementation of the same slot exists — not upfront. (`layouts/` was
in this list too until there was a first concrete pattern —
`city_block_grid.md` — worth writing up: how `city-block` and
`main-bus` position relative to each other. `main_bus.md` (the bus as
a standalone pattern, without a city-block grid around it) followed
the same way. `city_block_grid.md` was later split (2026-08-09) once
it became clear its own dominant community usage is rail-connected,
not bus-connected — the belt-through-gaps composition moved to its own
`main_bus_consumer_layout.md`, leaving `city_block_grid.md` for the
(more common) rail-connected variant. `decisions/0003` then stated this
project's own position (main-bus as bootstrap, city-block + train-bus
as the long-game target), which `main_bus_to_city_block_transition.md`
followed up on: how a base built on the bootstrap pattern actually
migrates into the target grid, block by block, without rebuilding
production. Other approaches — drill-to-furnace arrays, lab layout, a
railway-system layout, a mini-base (`micro-factory`/`monolith`/
`train-base`) layout — still belong in `layouts/` once written, not
scaffolded ahead of content. `blueprints/` followed the same
reactive-creation path (2026-08-09): it existed only as a planned,
uncreated folder until this project's own rail-spacing research
(`city_block_grid.md`) started depending on measurements taken from a
real third-party blueprint — at that point there was real content
(the parsing code already written ad-hoc for that research, plus a
blueprint this project's own claims cite) to justify creating it,
rather than scaffolding an empty blueprint library speculatively.)

## Versioning

`main` always holds the latest supported game version directly (**2.0**
right now) — not an empty scaffold branch pointing at something else.
A version branch is cut **retroactively**, only at the moment a newer
version's data would actually diverge from what's recorded here: branch
off the last commit still valid for the old version (e.g. `2.0`),
freezing it, then keep evolving `main` forward as the new latest.
Branches are per major version (not per patch/minor release, not a
folder inside the tree), created reactively like `contracts/`/
`factory-modules/` — never pre-provisioned for a version that doesn't
need to diverge yet.
