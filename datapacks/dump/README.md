# datapacks/dump/

`data.raw` extracts, one folder per mod-set (`vanilla/` = base + official
DLCs, no data-affecting third-party mods). Provenance lives once per
mod-set in that folder's own `source.json` — game version, extraction
method, and an `exceptions` array for any individual file (or field)
that came from somewhere other than this project's own
`factorio --dump-data` run. See CLAUDE.md hard rule 5 for the full
convention.

Each mod-set's own dump is a **curated field subset per file, not a
full `data.raw` capture** — whichever fields mattered for whatever this
project was sourcing at extraction time. A prototype can be missing a
field that genuinely exists in the real game (e.g. `iron-chest.json`
has no size field at all; mining-drill's `vector_to_place_result` was
missing until 2026-08-22 — see `vanilla/source.json`'s exceptions
entry). Before assuming a field is engine-only or doesn't exist, check
whether it's simply absent from *this project's own curated capture*,
not the game's actual data.

## Authoritative sources for filling a gap

When a needed field is missing from the dump and re-running
`factorio --dump-data` isn't available in the current environment, the
sources below are ranked by how directly they reflect the real game
data, most authoritative first — prefer the highest-ranked one that
actually has the field:

1. **[wube/factorio-data](https://github.com/wube/factorio-data)** —
   Wube's own officially published mirror of the base game's and
   DLCs' Lua prototype source. First-party, not a re-serialization —
   the closest thing to reading `data.raw` directly without a running
   game instance. Prototype `.lua` files are organized by mod
   (`base/prototypes/entity/`, `space-age/prototypes/entity/`, ...),
   matching this dump's own mod-set folders.
2. **[lua-api.factorio.com](https://lua-api.factorio.com/)** — the
   modding API docs. Authoritative for a field's *semantics* (what it
   means, whether it's relative to the entity's direction, valid
   ranges) but not for vanilla's specific per-prototype *values* —
   cross-check against source 1 or 3 for an actual number.
3. **wiki.factorio.com/Data.raw**-linked community serializations
   (e.g. the Bilka2 gist already used throughout `vanilla/source.json`'s
   `exceptions`) — third-party, but a full `data.raw` dump rather than
   hand-picked fields, useful when source 1 doesn't have a field
   either (some fields are runtime-computed or come from a different
   prototype stage than the raw Lua source shows).

A gap filled this way gets recorded as an `exceptions` entry in the
relevant mod-set's `source.json`, same as every other non-native file
or field in this dump — not silently folded into the main provenance,
and not treated as equivalent-confidence to this project's own
`factorio --dump-data` runs (source 1 is first-party and high
confidence, but still a different extraction method than running the
dump command against the actual game).
