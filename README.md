# Factorio Knowledge Base

Knowledge base for the game [Factorio](https://factorio.com/): stores values, formulas and patterns, and teaches LLMs how to work with them to plan bigger factories.

## Status

🚧 Early stage. Currently populated: sourced game facts (`datapacks/`, `constraints/`), derived relations (`relations/`), terminology (`glossary/`), base-layout patterns (`layouts/`), and curated importable blueprints (`blueprints/curated/`). Automated blueprint generation and `patterns/` are not built yet.

## Key principle

**Formula over constant.** No numeric rule (e.g. "24 steel furnaces saturate a yellow belt") is stored as a bare number. It's built from raw sourced data (`datapacks/`, `constraints/`) and, once available, a derivation function (`formulas/`) producing a checkable result. Every fact is sourced, but not the same way everywhere — `datapacks/dump/` provenance lives in a shared manifest, `constraints/` splits bare values from their sourcing into a paired file — see [CLAUDE.md](CLAUDE.md) for the exact convention per domain.

## Repository layout

- `datapacks/` — raw game data (recipes, machine/belt throughput): a formula input, not a result. `datapacks/dump/<mod-set>/` (e.g. `vanilla`) is extracted directly from the game via `factorio --dump-data` — one file per prototype, provenance in that mod-set's own `source.json` — rather than transcribed by hand.
- `constraints/` — hard engine limits that can't be recalculated differently (e.g. rail turn radius, chunk size, max inserters per wagon).
- `formulas/` — pure Python functions (e.g. machine ratio from crafting speed, recipe time, consumer throughput). No hardcoded values.
- `relations/` — derived numbers that come from applying a `formulas/` function to specific `datapacks/` values (e.g. "24 steel furnaces saturate a yellow belt") — never stored as a bare constant, always with the formula + inputs that produced it.
- `glossary/` — `canonical/` for established Factorio/community terms, `invented/` for terms coined in this project.

More domains (`patterns/`, `generators/`, ...) are planned but not created yet — see [CLAUDE.md](CLAUDE.md).

## Versioning

Targets Factorio **2.0** for now. The plan is one git branch per major game version when a second version is actually needed, rather than versioning every file — see [CLAUDE.md](CLAUDE.md).

## Useful links

- [FactorioLab](https://factoriolab.github.io/2x1?v=11) — web-based production planner: pick target items/rates and it computes the full recipe tree, machine counts, modules/beacons, and power draw. Handy for cross-checking `relations/` entries against an independent calculator.
- [Factory Blueprint Editor (FBE)](https://fbe.factorygamefan.com/) — decodes/encodes Factorio blueprint strings and renders them as an editable grid (entities, recipes, filters). Useful for inspecting or hand-tweaking blueprints, including the ones under `blueprints/curated/`.
- [Kirk McDonald's Factorio Calculator](https://kirkmcdonald.github.io/calc.html#data=2-0-55&items=advanced-circuit:f:1) — another web-based production ratio calculator: set a target item and rate, get the full ingredient tree with machine counts per tier. A second independent tool (alongside FactorioLab) for cross-checking `relations/` entries.

## License

Not defined yet.
