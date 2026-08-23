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
python blueprints/validate.py blueprints/curated/*/*.txt blueprints/curated/*/*/*.txt
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

## build_vectors.py + `.vectors.json`

Reduces a blueprint's entities to a flat list of directed vectors —
`belt_runs`, `inserters`, `underground` tunnels, `splitters` — instead
of a tile-by-tile adjacency chain (`belt1->belt2->beltN`). Written
after repeated manual-tracing mistakes in this project's own analysis
(see CLAUDE.md hard rule 6's inserter-directionality history); a flat
vector list is meant to be read directly instead of re-derived by eye
each time.

```bash
python blueprints/build_vectors.py blueprints/curated/earlygame/24x2-stone-furnaces-module/24x2-stone-furnaces-module.txt \
  blueprints/curated/earlygame/24x2-stone-furnaces-module/24x2-stone-furnaces-module.vectors.json
```

Key rules (see the module docstring and inline comments for the
geometry sources):

- **Homogeneous runs only** — consecutive belt tiles merge into one
  `belt_runs` entry only when both `name` (tier) and `direction` match;
  a tier change or a turn ends the run even on an otherwise-straight
  line.
- **Underground entrance/exit pairing** follows
  [underground-belt-pairing.md](../mechanics/underground-belt-pairing.md) —
  same-tier only, nearest-match with no skip-over; an unpaired entrance
  is recorded as a dead-end sink, not a parse error. The buried middle
  itself (`interactable: false`) is a separate vector from the
  surface belts on either side.
- **Splitters carry position/direction plus their actual
  `input_priority`/`output_priority`/`filter` config** (each `null` if
  unset — the blueprint format omits these fields entirely rather than
  writing a "none" default, so their absence is itself meaningful, not
  missing data) **and a `configured` flag**. An unconfigured splitter
  (`configured: false`, the common case — none of this project's own
  curated blueprints happen to set any of the three) is a
  **balancer**: per
  [splitter-priority.md](../mechanics/splitter-priority.md), no
  priority set means items split evenly between both outputs, a fully
  resolved, deterministic behavior, not an unresolved junction. Only a
  splitter that actually sets one of the three stays genuinely
  unresolved as input→output flow (routing then also depends on
  runtime backpressure, per the same doc) — but even then its actual
  settings are in the vector, not just a "check the JSON yourself"
  note.

`<slug>.vectors.json` is an optional sibling file for a `curated/`
entry (see "curated/" below) — regenerate it whenever the source
`.txt` changes, don't hand-edit it.

**Mirrored client-side in `pages/index.html`'s inline JS** (same
geometry, same merge rules) so the visualizer (see below) can
vectorize a blueprint string pasted into its `?source=` query
parameter without a server round-trip. Keep the two in sync if the
rules here change — there's no shared module between them (Python for
the batch/repo path, JS for the in-browser path).

## Visualizer (`pages/index.html`, GitHub Pages)

An interactive SVG viewer for `build_vectors.py`'s output — pan/zoom,
per-layer toggles (base entities, belts, inserters, underground,
splitters), and a hover tooltip with each vector's `entity_number`(s)
and `from`/`to`. Built to check the vector geometry visually against
the real blueprint layout while `build_vectors.py`'s rules were being
worked out, rather than trusting the JSON by eye.

Served via GitHub Pages, deployed by `.github/workflows/pages.yml` on
every push to `main` that touches `pages/` (`actions/upload-pages-artifact`
+ `actions/deploy-pages`, not a branch/folder Pages source, which is why
this could be renamed from the original `docs/` without touching the
platform-side config at all — Actions-based Pages was never tied to that
folder name). One manual step is still required once, outside git:
Settings → Pages → Source: **GitHub Actions**. After that it's live at
the repo's Pages URL and stays in sync automatically. Two ways to load
a blueprint:

- **Default (no query string)** — shows a pre-baked demo dataset
  embedded in the page (`24x2-stone-furnaces-module`).
- **`?source=<blueprint string>`** — decodes and vectorizes the given
  Factorio blueprint string entirely client-side (`DecompressionStream`
  for the zlib payload, no bundled inflate library), so any blueprint
  string can be inspected without adding it to `curated/` first.
  `encodeURIComponent` the string when building the link — a literal
  `+` in an un-encoded value is read back as a space by query-string
  parsing, though the page also repairs that specific case defensively
  since blueprint strings are base64 and never contain real spaces. If
  the value starts with `https://`, it's fetched as a URL first and the
  response body used as the blueprint string instead (subject to the
  target host allowing CORS for this page's origin).
- **Import blueprint… button** — a modal for pasting a string (or a
  `https://` link to one) without hand-building the URL. Stages the text
  in `sessionStorage` and reloads onto a fixed `?source=local` marker
  rather than `?source=<the string itself>`, then reuses the exact same
  decode/vectorize path as a hand-built link. Putting the string directly
  in the URL (the original approach) broke on exactly the designs this
  modal is most useful for: an entity-dense blueprint (solar field, city
  block) easily produces a base64 string tens of KB long, well past what
  browsers/servers/proxies reliably accept in a URL, where a short
  blueprint pasted as a `?source=` link works fine.
- **Download vectors.json button** — saves the currently-loaded `VEC`
  object as a `.json` file, named from the blueprint's own label.

### Tier/type colors

Belt runs, underground tunnels, splitters, and inserters are colored
by their exact prototype name (`entity` field in the vector JSON), not
one flat color per vector category — added after an early version
colored every belt tier, every splitter tier, and every underground
tier identically, and folded `bulk-inserter`/`stack-inserter` into
`fast-inserter`'s color, making tier impossible to tell apart on
sight.

**None of this is extractable from `data.raw`** — `item`/entity
prototypes for belts, splitters, underground-belts, and inserters
carry no tint/color field in this repo's dump (or in the real
prototype at all; sprite coloring is baked into the art assets, not
data). So unlike everything else this project sources from the dump,
these are visual picks, sourced by looking at the actual
wiki.factorio.com icon images rather than assumed from memory — see
below for where each came from and one place this went wrong before
being corrected.

Belts, underground tunnels (by matching tier: `fast-underground-belt`
gets the same color as `fast-transport-belt`), and splitters (same
matching-tier rule) all share one palette:

| Tier | Color |
|---|---|
| `transport-belt` / `underground-belt` / `splitter` | yellow |
| `fast-*` | red |
| `express-*` | blue |
| `turbo-*` | teal |

Inserters get their own six-way palette (not tied to the belt
palette — inserters aren't belt-tiered):

| Prototype | Color |
|---|---|
| `burner-inserter` | dark gray |
| `inserter` (basic) | yellow |
| `long-handed-inserter` | red |
| `fast-inserter` | blue |
| `bulk-inserter` | green |
| `stack-inserter` | white/silver |

`bulk-inserter` and `stack-inserter` were guessed wrong on the first
pass (assigned violet and green respectively, arbitrarily, without
checking) and corrected by fetching and directly viewing the actual
`Bulk_inserter.png`/`Stack_inserter.png` icons from
wiki.factorio.com — bulk's arm is green, stack's is white/silver.
**The lesson driving this note**: for anything sourced from a sprite's
actual appearance rather than `data.raw`, verify against the real
icon (fetch and view the image) before assigning a color — don't
guess from memory or assume a plausible-sounding scheme, the same
"don't state it from recollection" discipline CLAUDE.md's hard rule 6
already applies to engine behavior.

Only six inserter prototypes exist to color — no `filter-inserter` or
`stack-filter-inserter`. Those were separate colored entities pre-2.0;
[filter-inserter was removed from the game entirely in
2.0.7](https://wiki.factorio.com/Archive:Filter_inserter) once every
inserter gained built-in filtering, which is also where
`stack-inserter`'s white color came from — freed up by that removal
and reused for the new (2.0-renamed) stack tier rather than invented
fresh.

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

## Constant-combinator (or `display-panel`) signals as informal lane labels

A separate, complementary heuristic from the edge-port one above:
authors commonly drop a `constant-combinator` set to a single item
signal (or, since 2.0.7, the purpose-built `display-panel` entity —
"a small monitor that can display icons and text above the entity",
wiki.factorio.com/Display_panel) right next to or above a belt/
underground lane purely to label what that lane carries for a human
reading the blueprint later — not to feed a circuit condition
anywhere. Observed directly while analyzing a blueprint pasted into
this project: three `constant-combinator`s sat in a row, each filtered
to one item (`automation-science-pack`, `copper-plate`,
`iron-gear-wheel`), each positioned directly above one of three
parallel lanes — and matching each label's x-coordinate to the lane
beneath it resolved which lane carried which ingredient, including
correcting a wrong guess (the vertical spine had looked like the
gear-input bus from its belt/underground geometry alone; the label
above it said `automation-science-pack`, i.e. it was the packed
*output* collector instead).

**Confirm it's actually just a label before trusting it**: check the
entity for a `connections` field (or the blueprint's top-level `wires`
array in the 2.0 wire format) — a combinator/display-panel *can* be
wired to a real circuit condition (train limits, a logistic request)
elsewhere in the same design, in which case its signal reflects actual
circuit logic, not necessarily "this is the lane directly below me."
No wire connections at all is what confirms pure-label intent (as in
the observed case above); don't assume it from position alone the way
`classify_edge_ports`'s candidates shouldn't be trusted from position
alone either — same "candidate, not ground truth" caution as that
section.

## curated/

**"ideal-blueprint" = a blueprint worth keeping a verified local copy
of, with full provenance** — either a best-in-class third-party
published design this project's own claims cite as evidence, or an
entry from the project owner's own personal collection. Both get the
same treatment; the `.md` file is what distinguishes which kind an
entry is and, for third-party ones, what claim elsewhere in this
project it backs.

One entry = one `<slug>/` folder, holding three files sharing that
basename (same `<topic>.json` + `<topic>.md` pairing convention used
elsewhere in this project, extended with a third sibling here), plus
two optional ones. Moved from flat sibling files at the stage level to
one folder per entry once a single entry routinely grew to 4-5 files —
`ls`ing a stage folder was starting to show a wall of same-prefixed
filenames rather than a list of blueprints.

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
- `<slug>.vectors.json` — **optional**, generated by `build_vectors.py`
  (see above) — a flat directed-vector reduction of the entry's belts/
  inserters/underground/splitters, for entries where that
  representation was worth generating rather than tracing tile
  adjacency by hand.

### Layout: entry folder directly under `curated/` for third-party, under a game-stage folder for personal

`nilaus_100x100_city_block/` sits directly in `curated/`'s root — the
third-party example, backing `layouts/city_block_grid.md`'s block-size
and rail-spacing findings.

The project owner's own personal collection lives one level deeper, in
`curated/earlygame/`, `curated/init-game/`, and `curated/midgame/` —
each entry's own `<slug>/` folder underneath that. This isn't
cosmetic: the same conceptual design recurs at different tiers as a
game progresses — e.g. `city-block-100x100/` exists in *both*
`earlygame/` and `midgame/`, same slug, genuinely different content
(`earlygame/`'s uses many `small-electric-pole`, `midgame/`'s uses
fewer, longer-reach `big-electric-pole`; belts, furnaces, and
inserters follow the same pattern elsewhere in the collection — stone
furnaces → electric furnaces, tier-1 → tier-2 belts). Grouping by
stage is how this project tells those variants apart without
inventing a distinct name for what's conceptually the same block at a
different point in the tech tree; the two `city-block-100x100/`
folders sit at `earlygame/city-block-100x100/` and
`midgame/city-block-100x100/` — same slug, no collision, since the
stage folder disambiguates them.

Exception: `automation-science-module` and `logistic-science-module`
in `earlygame/`, and `military-science-module` and
`chemical-science-module` in `midgame/`, are third-party — all four
are individual blueprints extracted from Christoffer Ramqvist's
"Tileable Science Production 1.0-2.0" book,
https://factorioprints.com/view/-KnQ865j-qQ21WoUPbd3 — not personal,
but sit under a game-stage folder rather than `curated/`'s root at the
project owner's explicit instruction — their own `.md` files say so,
so this isn't silently inconsistent with the rule above. The book's
own 6 base-game science-pack blueprints were deliberately split across
both stage folders (not all filed together) at the project owner's
instruction — `military-science-module`/`chemical-science-module` use
`fast-*` belt tiers and are noticeably larger/more entity-dense than
their earlygame siblings, consistent with a midgame-tier build even
though they share the same book and the same pre-2.0 `version`.

A related but distinct case: `midgame/lab-setup-module` (factorio.school,
"Science Lab Setup" by Roel) is third-party per the rule above, filed
correctly at midgame since its own site listing requires `fast-*`
tiers. `earlygame/lab-setup-module` is **not** an independent
third-party fetch — it's the project owner's own tier-1 downgrade of
that same entry, done in-repo (belts/inserters/poles re-tiered, 2
poles added because tier-1's shorter `supply_area_distance` left 4
inserters uncovered, and — after a first pass mistakenly kept one
underground-belt pair at `fast-` tier — one `long-handed-inserter`
removed to shorten that pair's span to exactly tier-1's `max_distance`
instead, at the cost of one lab losing that inserter's feed; see that
entry's own `.md` for the full derivation and verification). Treated
as a personal entry for folder-placement purposes since the
modification work is the project owner's, even though the base design
isn't.

`earlygame/electronic-circuit-module` is also third-party — one entry
("Basic Green Circuits") from Robbie Theron's "Nauvis Start - Factorio
2.1" book, https://factorioprints.com/view/-P-hYRfTCEjpttIq9oSr. It
replaced an earlier from-scratch draft the project owner built at this
same slug: the project owner pasted this design in for comparison,
judged it better, and asked for the replacement — see that entry's own
`.md` for how the two compared.

Current personal entries: `earlygame/` (`24x2-stone-furnaces-module`,
`4-boilers-w-burner-inserters`, `4x2-stone-furnaces-w-upgrade-spacing`,
`coal-burner-miners-w-burner-inserters`, `city-block-100x100`,
`furnaces-import-block`, `high-density-miners`, `iron-gear-tileable`,
`starter-electrical-miners`, `lab-setup-module` [derived, see above]),
plus the three third-party exceptions noted above
(`automation-science-module`, `logistic-science-module`,
`electronic-circuit-module`),
`init-game/` (`4-burner-miners-w-chests`,
`4-burner-miners-w-furnaces-and-chests`, `4-burner-drills-into-one-chest`,
`4-burner-drills-chained`), `midgame/`
(`4x2-electrical-furnaces-w-tier2-belts`, `city-block-100x100`,
`iron-gear-tileable`), plus the three third-party exceptions noted
above (`military-science-module`, `chemical-science-module`,
`lab-setup-module`).
