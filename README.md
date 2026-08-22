# Factorio Knowledge Base

Knowledge base for the game [Factorio](https://factorio.com/): stores values, formulas and patterns, and teaches LLMs how to work with them to plan bigger factories.

## Status

🚧 Early stage. Currently populated: sourced game facts (`datapacks/`, `mechanics/`), derived relations (`relations/`), terminology (`glossary/`), base-layout patterns (`layouts/`), and curated importable blueprints (`blueprints/curated/`, parsed via `blueprints/codec.py`). Blueprints can also be reduced to a flat vector list (`blueprints/build_vectors.py`) and inspected in an interactive viewer served via GitHub Pages (`pages/index.html`, see `blueprints/README.md`). Automated blueprint generation and `patterns/` are not built yet.

## Key principle

**Formula over constant.** No numeric rule (e.g. "24 steel furnaces saturate a yellow belt") is stored as a bare number. It's built from raw sourced data (`datapacks/`, `mechanics/`) and, once available, a derivation function (`formulas/`) producing a checkable result. Every fact is sourced, but not the same way everywhere — `datapacks/dump/` provenance lives in a shared manifest, `mechanics/` splits bare numeric values from their sourcing into a paired file, or is prose-only for a behavioral rule with no number to extract — see [CLAUDE.md](CLAUDE.md) for the exact convention per domain.

## Repository layout

- `datapacks/` — raw game data (recipes, machine/belt throughput): a formula input, not a result. `datapacks/dump/<mod-set>/` (e.g. `vanilla`) is extracted directly from the game via `factorio --dump-data` — one file per prototype, provenance in that mod-set's own `source.json` — rather than transcribed by hand.
- `mechanics/` — hard engine limits and behavioral rules that can't be recalculated differently and have no `data.raw` representation (e.g. rail turn radius, chunk size, max inserters per wagon, an inserter's fixed pickup/drop axis).
- `formulas/` — pure Python functions (e.g. machine ratio from crafting speed, recipe time, consumer throughput). No hardcoded values.
- `relations/` — derived numbers that come from applying a `formulas/` function to specific `datapacks/` values (e.g. "24 steel furnaces saturate a yellow belt") — never stored as a bare constant, always with the formula + inputs that produced it.
- `glossary/` — `canonical/` for established Factorio/community terms, `invented/` for terms coined in this project.

More domains (`patterns/`, `generators/`, ...) are planned but not created yet — see [CLAUDE.md](CLAUDE.md).

## Versioning

Targets Factorio **2.0** for now. The plan is one git branch per major game version when a second version is actually needed, rather than versioning every file — see [CLAUDE.md](CLAUDE.md).

## License

Not defined yet.
