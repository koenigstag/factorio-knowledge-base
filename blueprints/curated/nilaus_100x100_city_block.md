# Nilaus — Updated 100×100 City Blocks, Snapped to Grid

A blueprint book of 8 sub-blueprints implementing a 100×100-tile,
train-connected city-block cell: base edge infrastructure (lamps,
big-electric-poles, roboports, radar), solar-power variants, and three
rail-infrastructure pieces (train station, T-junction, elbow) meant to
snap onto the same 100×100 grid. Curated here as this project's first
`blueprints/curated/` entry because it's already the primary evidence
behind two sourced claims elsewhere in this project:
[glossary/canonical/city-block.md](../../glossary/canonical/city-block.md)/
[layouts/city_block_grid.md](../../layouts/city_block_grid.md)'s 100×100
block-size figure, and `city_block_grid.md`'s "Rail spacing between
blocks" cross-check (rail infrastructure fits entirely inside the
block's own footprint here, 0 tiles of extra margin needed).

## Files

- `nilaus_100x100_city_block.txt` — the raw blueprint-book string,
  pasteable directly into Factorio's blueprint-string import.
- `nilaus_100x100_city_block.json` — decoded via
  [blueprints/codec.py](../codec.py)'s `decode_blueprint_string`
  (Factorio's own string format: version byte + base64 + zlib-deflated
  JSON — not a hosting-site-specific encoding). Large (~3.8 MB) because
  the solar-power sub-blueprints alone place over 1300 entities each;
  kept in full rather than trimmed, per this project's chosen storage
  convention (raw string + full decoded JSON, not a summary).

## Provenance

- Author: Nilaus (content creator; content credited by the blueprint's
  own title/description, not independently identity-verified beyond
  that — the hosting site's author record is only a Firebase user ID,
  `g6nTlQ9ykaWTUm5Rxq7jntr8wjC2`, not a display name).
- Hosted at: https://factorioprints.com/view/-MOy8SsNcu5BNqCZ2ZnL
  (title: *"Updated 100x100 City Blocks - Snapped to Grid"*, 55
  favorites at fetch time). See [tools.md](../../tools.md) for this
  project's own research on how factorioprints.com/factorio.school
  relate — the same record is not confirmed reachable via a
  factorio.school URL, so only the factorioprints.com link is given
  here.
- Site's own recorded dates: created 2020-12-20, last updated
  2020-12-20 (same day) — this is a 1.x/pre-2.0 design; not confirmed
  to still be mechanically valid post-2.0 rail changes (2.0 rail
  geometry is stated to be unchanged from 1.1 per
  [mechanics/rails.md](../../mechanics/rails.md), but this specific
  blueprint hasn't been re-verified against a live 2.0 game).
- Fetched and decoded directly from the site's public Firebase
  Realtime Database REST endpoint
  (`facorio-blueprints.firebaseio.com/blueprints/<id>.json` — see
  `tools.md` for how this endpoint was found), not copy-pasted by
  hand, so the stored string is byte-identical to what the site
  itself serves.

## Why curated (not just linked)

This project's own analysis (`layouts/city_block_grid.md`'s rail-
spacing section) depends on specific measurements taken from this
blueprint's decoded entity positions. Storing the source data locally,
not just citing a URL, means that analysis stays reproducible even if
the hosting site's content changes or the link breaks — the same
reasoning `datapacks/dump/vanilla/` already applies to game data,
extended here to third-party reference designs this project's own
claims depend on.

Verified: 2026-08-09
