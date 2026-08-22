# Day/night cycle (default map setting)

## dawn_ticks=5000, day_ticks=12500, dusk_ticks=5000, night_ticks=2500

Length of each phase of Nauvis's day/night cycle, in ticks (60 ticks =
1 second — total cycle 25000 ticks ≈ 416.7 seconds). Solar power
output ramps linearly 0→full over `dawn_ticks`, stays full through
`day_ticks`, ramps linearly full→0 over `dusk_ticks`, and is 0 through
`night_ticks`.

**Not `data.raw`-backed** — checked `planet`/`surface` prototypes
directly, no day/night timing field exists there. This is a *default*
map-generation setting, adjustable by the player when creating a game
(the "day/night cycle" slider), not an unchangeable engine constant
like `chunk_size_tiles`. Treat this file as "the default, unless the
player's map says otherwise" — same caveat as any other
`mechanics/` fact whose value could shift per save, distinct from
the truly fixed facts in `rails.json`/`world.json`.

Source: https://wiki.factorio.com/Power_production
Verified: 2026-08-06
