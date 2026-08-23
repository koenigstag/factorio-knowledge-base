# Military Science Module

Third-party blueprint, one entry from the same blueprint book as
`automation-science-module`/`logistic-science-module` in
`curated/earlygame/`: "Tileable Science Production 1.0-2.0 - Early to
Mid Game (Vanilla)" by Christoffer Ramqvist,
https://factorioprints.com/view/-KnQ865j-qQ21WoUPbd3 (created
2017-06-24, 4007 favorites as of 2026-08-23). This entry is its
`Military Science 0.75/s` blueprint specifically. Filed under
`curated/midgame/` (not `earlygame/`, unlike its two siblings) at the
project owner's own placement instruction.

Blueprint's own label: `"Military Science 0.75/s"`. 172 entities:
`assembling-machine-2` (13), `fast-transport-belt` (69),
`fast-underground-belt` (36), `inserter` (9), `long-handed-inserter`
(17), `fast-inserter` (14), `medium-electric-pole` (8),
`constant-combinator` (6, unwired — pure lane labels, see
`blueprints/README.md`'s "Constant-combinator signals as informal
lane labels"). Uses `fast-*` belt tiers throughout, unlike the two
earlygame siblings' plain `transport-belt`/`underground-belt`.

## Layout

`military-science-pack`'s recipe (0.5 piercing-rounds-magazine + 0.5
grenade + 1.0 stone-wall) pulls in more distinct raw/semi-raw
ingredients than any other curated science module so far, spread
across two sub-crafting chains: a `x=-7` column (1x `stone-wall` +
4x `grenade`) and a middle pair (1x `firearm-magazine` feeding 2x
`piercing-rounds-magazine`). Both feed a `x=8` column of 5
`assembling-machine-2` running `military-science-pack` directly.

Ports (tunnel identity confirmed via the unwired constant-combinator
sitting directly below each): [military-science-module.ports.json](military-science-module.ports.json).

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
40 inserters and 18 underground-tunnel pairs.

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
  to curate this blueprint (and `chemical-science-module`, its
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
