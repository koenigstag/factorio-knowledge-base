# Chemical Science Module

Third-party blueprint, one entry from the same blueprint book as
`automation-science-module`/`logistic-science-module` in
`curated/earlygame/`: "Tileable Science Production 1.0-2.0 - Early to
Mid Game (Vanilla)" by Christoffer Ramqvist,
https://factorioprints.com/view/-KnQ865j-qQ21WoUPbd3 (created
2017-06-24, 4007 favorites as of 2026-08-23). This entry is its
`Chemical Science 0.75/s` blueprint specifically. Filed under
`curated/midgame/` (not `earlygame/`, unlike its two siblings) at the
project owner's own placement instruction.

Blueprint's own label: `"Chemical Science 0.75/s"`. 197 entities:
`assembling-machine-2` (24), `fast-transport-belt` (51),
`fast-underground-belt` (36), `inserter` (22), `long-handed-inserter`
(44), `fast-inserter` (4), `medium-electric-pole` (12),
`constant-combinator` (4, unwired — pure lane labels, see
`blueprints/README.md`'s "Constant-combinator signals as informal
lane labels"). Uses `fast-*` belt tiers throughout, unlike the two
earlygame siblings' plain `transport-belt`/`underground-belt` — the
largest and most entity-dense of the four science modules curated so
far.

## Layout

`chemical-science-pack`'s recipe (1.0 engine-unit + 1.5
advanced-circuit + 0.5 sulfur) needs `engine-unit` crafted on-site: a
10-assembler column (`x=-8` and `x=0`, 5 each) makes `engine-unit`,
backed by single support assemblers for `pipe` and `iron-gear-wheel`
(engine-unit's own direct ingredients). That combines with imported
`advanced-circuit` and `sulfur` to feed 12 `assembling-machine-2`
running `chemical-science-pack` directly, in two columns of 6 (`x=3`,
`x=11`).

Ports (tunnel identity confirmed via the unwired constant-combinator
sitting directly below each): [chemical-science-module.ports.json](chemical-science-module.ports.json).
One import tunnel's combinator carries two item filters at once
(`advanced-circuit` + `sulfur`) rather than one — most likely labeling
both of a transport-belt's two independent lanes on a single shared
tunnel, consistent with this project's other observed uses of this
labeling convention, though which physical lane is which item wasn't
traced further.

## Pre-2.0 export

This blueprint's `version` field decodes to `0.17.79.0` — a pre-2.0
export, same as the two earlygame siblings from this book. Its
`direction` values are on the 8-value pre-2.0 scale (cardinals 2
apart), not the 16-value 2.0+ scale (cardinals 4 apart); see
[mechanics/inserters-directionality.md](../../../../mechanics/inserters-directionality.md)'s
"Pre-2.0 blueprints use a different `direction` scale" section.
`build_vectors.py`'s `normalize_pre_2_0_directions()` rescales this
automatically before computing geometry — the `.vectors.json` sibling
here is already in modern-scale cardinals, zero ambiguity across all
70 inserters and 18 underground-tunnel pairs.

## Provenance

- Author: Christoffer Ramqvist (factorioprints.com user, display name
  resolved via the site's public Firebase Realtime Database at
  `/users/<userId>/displayName`).
- Source: https://factorioprints.com/view/-KnQ865j-qQ21WoUPbd3 — the
  book's own `blueprintString` was fetched from factorioprints' public
  CDN cache (`factorio-blueprint-firebase-cdn.pages.dev`, the same
  backing store the site's own front end reads from), decoded with
  this project's `codec.py`, and re-encoded as a standalone single
  blueprint via `encode_blueprint_dict` — round-trip verified
  (re-decoding the standalone `.txt` reproduces the stored `.json`
  exactly).
- Added to the repository: 2026-08-23, at the project owner's request
  to curate this blueprint (and `military-science-module`, its
  sibling in this same folder) — extends `automation-science-module`/
  `logistic-science-module` toward the full 6-pack set needed to match
  wiki.factorio.com's science-pack production ratio (5:6:5:12:7:7,
  see that page's "Creating science packs" section).

## Validation

`blueprints/validate.py` (factorio-draftsman): **failed to parse** —
`No converter exists for version (0, 17, 79, 0)`. Same cause as the
two earlygame siblings: draftsman's bundled converters don't cover
pre-2.0 blueprint versions at all, independently confirming this is a
genuine pre-2.0 export. `codec.py`'s own decode succeeds cleanly.

Verified: 2026-08-23
