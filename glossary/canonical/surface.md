# surface

Official Space Age term for a distinct place the game simulates
separately — a planet (`nauvis`, `vulcanus`, `fulgora`, `gleba`,
`aquilo`) or a player-built space platform. Each surface has its own
resources, its own instance of day/night, and a set of **surface
properties** that recipes/entities can be gated on (see
[mechanics/surface-conditions.md](../../mechanics/surface-conditions.md)).

## Surface properties (5 total, `data.raw` `surface-property` prototypes)

`day-night-cycle`, `gravity`, `magnetic-field`, `pressure`,
`solar-power` — each with a `default_value`
(`datapacks/dump/vanilla/surface-property/*.json`) used when a surface
doesn't explicitly override it (`nauvis` only overrides
`day-night-cycle`, implicitly using the default for the other four —
it's the baseline surface every default value is tuned around).

## Per-surface values (`datapacks/dump/vanilla/planet/*.json`)

| surface | day-night-cycle | gravity | magnetic-field | pressure | solar-power |
|---|---|---|---|---|---|
| nauvis | 25200 | 10 (default) | 90 (default) | 1000 (default) | 100 (default) |
| vulcanus | 5400 | 40 | 25 | 4000 | 400 |
| fulgora | 10800 | 8 | 99 | 800 | 20 |
| gleba | 36000 | 20 | 25 | 2000 | 50 |
| aquilo | 72000 | 15 | 10 | 300 | 1 |
| space platform | 0 | 0 | 0 | 0 | (unset) |

`day-night-cycle` is in ticks (60/sec) — vulcanus's 5400-tick cycle is
a 90-second day/night, nauvis's 25200 is 7 minutes, aquilo's 72000 is
20 minutes. `space-platform` isn't a fixed `planet` prototype the way
the five listed above are — a platform is a player-built, dynamically
created surface, grouped here with the planets by the data source for
convenience, not because the game treats it identically (flagged, not
silently equated).

Source: `github.com/KirkMcDonald/kirkmcdonald.github.io`'s
`data/space-age-2.0.55.json` (a third-party structured data file, not
this project's own dump — see `source.json`'s exceptions);
`lua-api.factorio.com/latest/types/SurfaceCondition.html` for the
gating mechanism itself.
Verified: 2026-08-08
