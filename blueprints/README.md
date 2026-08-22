# blueprints/

Tooling for working with real Factorio blueprint strings, plus a local
store of curated blueprints — both third-party reference designs this
project's own claims depend on, and the project owner's own personal
collection. Distinct from [tools.md](../tools.md), which just links to
external sites — this folder holds the actual parsing code and the
actual data.

Was on CLAUDE.md's "not created yet, don't scaffold speculatively"
list until there was real content to justify it — see CLAUDE.md's
"Current structure" section for when/why it was created.

## codec.py

Pure functions, no game-specific hardcoding: `decode_blueprint_string`
(Factorio's own export format — version byte + base64 + zlib-deflated
JSON — into a plain dict), `encode_blueprint_dict` (the inverse,
round-trip verified), `walk_blueprints` (flattens a blueprint or
nested blueprint-book into its individual blueprints), and
`entity_bounding_box` (min/max x/y among a blueprint's entities,
optionally filtered by prototype name — e.g. rail-only).

Not a `formulas/` file: `formulas/` per CLAUDE.md is specifically
"parameters in, number out" derivations over `datapacks/` primitives;
this is general-purpose parsing/analysis of third-party blueprint
data, a different kind of thing.

## validate.py

Stronger validation than `codec.py`'s bare decode — checks a blueprint
string actually parses into well-formed entities (known prototype
names, valid placement) using
[factorio-draftsman](https://pypi.org/project/factorio-draftsman/), a
third-party library (`pip install -r requirements.txt` from repo
root). `codec.py` deliberately stays stdlib-only (decode/measure
doesn't need real entity validation, and zero install friction matters
for something used mid-research); `validate.py` is the one place in
this project that takes on a real dependency, specifically because
draftsman's validation (entity/item schema, mod compatibility, 2.0
support, actively maintained) is a different tier of correctness-
checking than this project's own ~50-line codec ever aimed to provide.

```bash
pip install -r requirements.txt
python blueprints/validate.py blueprints/curated/*.txt blueprints/curated/*/*.txt
```

Run this before adding a new `curated/` entry — confirms the string
isn't corrupt/truncated, and surfaces anything draftsman flags at the
entity level, before it's worth spending time writing the provenance
`.md`. In practice, several of this project's own personal blueprints
(see below) fail draftsman's parse outright (`list index out of
range`) or come back with `direction`-key warnings on symmetric
entities (`Lamp`/`ElectricPole`/`Roboport`/`Container`) — `draftsman
update` didn't fix it, and `codec.py`'s own decode succeeds cleanly on
every one of them, so this is treated as a schema-version gap between
draftsman's bundled prototype data (pinned to Factorio `2.0.0`) and
whatever exact 2.0.x patch these blueprints were exported from, not
evidence the blueprints themselves are corrupt. Recorded per-entry in
each blueprint's own `.md` rather than silently ignored.

## Import/export port heuristic (and its limits)

`classify_edge_ports` (in `codec.py`) flags belt/underground-belt/
splitter entities sitting exactly on a blueprint's bounding-box edge
as import or export *candidates*, based purely on direction relative
to that edge (facing in = import candidate, facing out = export
candidate, facing parallel to the edge = not a port at all, since it
never crosses the boundary).

**This is a candidate-generator, not ground truth — confirmed by a
real false positive**, not just a theoretical caveat:
`curated/earlygame/24x2-stone-furnaces-module.md` had a
`transport-belt` at the edge coordinate, facing into the schema,
exactly matching the "import candidate" pattern — and it turned out to
not be a port at all, just an entity that happened to share the edge
coordinate. Direction and position alone can't distinguish "this
crosses into/out of the module" from "this happens to sit at the same
coordinate as the boundary but isn't functionally a port."

**Rule for this project: don't state a port claim from
`classify_edge_ports` output alone — confirm it with the author (or,
for a third-party design, trace actual belt connectivity) before
writing it into a curated entry.** Where confirmation adds real detail
(e.g. an import lane turning out to be coal specifically, traced into
an `underground-belt` a tile in; two ore lanes confirmed to feed a
shared `splitter`), record that too — the goal is a verified port map,
not just "which edge."

**Confirmed ports go in `<slug>.ports.json`, not prose in the `.md`.**
Same reasoning as everywhere else in this project (`mechanics/`,
`relations/`): a confirmed port is a fact, and facts belong in
structured `.json`, not a hand-written markdown table — machine-
readable, greppable, and consistent in shape across every curated
entry rather than reinvented per file. Schema:

```json
{
  "bbox": {"x_min": ..., "x_max": ..., "y_min": ..., "y_max": ...},
  "ports": [
    {"tile": [x, y], "edge": "x_min|x_max|y_min|y_max", "direction": N,
     "role": "import|export", "resource": "...", "notes": "..."}
  ]
}
```

Only include entries in `ports` that are actually confirmed — a
`classify_edge_ports` candidate that turned out to be a false positive
(see `24x2-stone-furnaces-module.ports.json`'s missing `(33.5,-3.5)`)
doesn't get a row; the `.md` prose is where that kind of negative
result and its reasoning belongs, not the JSON. Optional fields as
needed per entry (`tileable`/`tiling_notes`, `layout_pattern`, `role`
for a non-smelter block) — the four required keys per port are `tile`,
`edge`, `role`, `resource`.

## curated/

**"ideal-blueprint" = a blueprint worth keeping a verified local copy
of, with full provenance** — either a best-in-class third-party
published design this project's own claims cite as evidence, or an
entry from the project owner's own personal collection. Both get the
same treatment; the `.md` file is what distinguishes which kind an
entry is and, for third-party ones, what claim elsewhere in this
project it backs.

One entry, three files sharing a basename (same `<topic>.json` +
`<topic>.md` pairing convention used elsewhere in this project,
extended with a third sibling here), plus an optional fourth:

- `<slug>.txt` — the raw blueprint string, exactly as fetched/saved,
  directly pasteable back into the game.
- `<slug>.json` — decoded via `codec.py`'s `decode_blueprint_string`.
  Can be large (multi-MB for entity-dense designs like solar fields) —
  accepted as the cost of storing the full design rather than a
  trimmed summary, per this project's chosen convention.
- `<slug>.md` — provenance (author — third-party site + original
  designer, or "project owner (self-authored)" for personal ones — and
  how/when it was added) and, for third-party entries specifically,
  **why it's curated here** — what claim elsewhere in this project it
  backs, not just "this looked like a good blueprint." Personal entries
  don't need that last part; they're the project owner's own working
  collection, not evidence for a documented claim.
- `<slug>.ports.json` — **optional**, only for entries where import/
  export ports have actually been analyzed and confirmed. See "Import/
  export port heuristic" below for the schema and why this is a
  separate JSON file rather than a table in the `.md`.

### Layout: flat for third-party, game-stage folders for personal

`nilaus_100x100_city_block.*` sits directly in `curated/`'s root — the
third-party example, backing `layouts/city_block_grid.md`'s block-size
and rail-spacing findings.

The project owner's own personal collection lives one level deeper, in
`curated/earlygame/`, `curated/init-game/`, and `curated/midgame/`.
This isn't cosmetic: the same conceptual design recurs at different
tiers as a game progresses — e.g. `city-block-100x100.*` exists in
*both* `earlygame/` and `midgame/`, same name, genuinely different
content (`earlygame/`'s uses many `small-electric-pole`,
`midgame/`'s uses fewer, longer-reach `big-electric-pole`; belts,
furnaces, and inserters follow the same pattern elsewhere in the
collection — stone furnaces → electric furnaces, tier-1 → tier-2
belts). Grouping by stage is how this project tells those variants
apart without inventing a distinct name for what's conceptually the
same block at a different point in the tech tree; a flat directory
would force either name collisions or awkward suffixing for something
that's genuinely just "this design, but upgraded."

Current personal entries: `earlygame/` (`24x2-stone-furnaces-module`,
`4-boilers-w-burner-inserters`, `4x2-stone-furnaces-w-upgrade-spacing`,
`coal-burner-miners-w-burner-inserters`, `city-block-100x100`,
`furnaces-import-block`, `high-density-miners`, `iron-gear-tileable`,
`starter-electrical-miners`), `init-game/` (`4-burner-miners-w-chests`,
`4-burner-miners-w-furnaces-and-chests`), `midgame/`
(`4x2-electrical-furnaces-w-tier2-belts`, `city-block-100x100`,
`iron-gear-tileable`).
