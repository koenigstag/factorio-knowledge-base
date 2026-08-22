# Offshore pump → boiler → steam engine ratio

How many boilers one offshore pump can feed with water, and how many
steam engines one boiler can then supply with steam, for the basic
(non-nuclear) steam power chain.

Formula: `formulas/boiler_fluid_consumption.py:boiler_fluid_consumption`
(boiler water draw), `formulas/generator_power_output.py:generator_power_output`
(steam engine power output, used here only as a cross-check — the
consumption figure it's built from is taken directly from source, see
below).

## Why this lives in `datapacks/wiki/`, not `datapacks/dump/vanilla/`

`boiler`, `generator` (steam-engine), and `offshore-pump` are all
`data.raw` prototypes (per CLAUDE.md rule 2, this belongs in
`datapacks/`, not `constraints/`), but `datapacks/dump/vanilla/` only
has the late-game siblings actually extracted so far
(`heat-exchanger`, `steam-turbine`, the generic `pump`) — not the
early-game `boiler`/`steam-engine`/`offshore-pump` entities themselves.
No live game install was available in this session to run
`factorio --dump-data` and fill that gap, so per CLAUDE.md rule 5 the
values are recorded in a sibling `datapacks/wiki/` source instead, with
per-entry `source_url`/`verified_date` (wiki.factorio.com, checked
2026-08-22) rather than the dump's shared `source.json` manifest.

## Primitives

| Entity | Field | Value | Source |
|---|---|---|---|
| `boiler` | `energy_consumption` | 1.8MW | `datapacks/wiki/boiler/boiler.json` |
| `boiler` | `target_temperature` | 165°C | `datapacks/wiki/boiler/boiler.json` |
| `water` (fluid) | `heat_capacity` | 2kJ | `datapacks/dump/vanilla/fluid/water.json` (already dumped) |
| `water` (fluid) | `default_temperature` | 15°C | `datapacks/dump/vanilla/fluid/water.json` |
| `steam-engine` | `fluid_usage_per_tick` | 0.5 | `datapacks/wiki/generator/steam-engine.json` — derived from the wiki's stated 30 steam/sec ÷ 60 ticks/sec, same per-tick convention as `UNITS.md`'s `pump.pumping_speed` row |
| `steam-engine` | `maximum_temperature` | 165°C | `datapacks/wiki/generator/steam-engine.json` |
| `steam-engine` | `effectivity` | 1 (assumed) | not stated on the wiki page; taken by analogy with `datapacks/dump/vanilla/generator/steam-turbine.json`'s `effectivity=1` — flagged as an assumption, not a direct citation |
| `steam` (fluid) | `heat_capacity` | 0.2kJ | `datapacks/dump/vanilla/fluid/steam.json` |
| `offshore-pump` | `pumping_speed` | 20 (per tick) | `datapacks/wiki/offshore-pump/offshore-pump.json` — derived from the wiki's stated 1200 water/sec ÷ 60, matching the exact `pump.pumping_speed=20` value and unit convention already dump-confirmed in `UNITS.md` for the sibling `pump` entity |

## Derivation

**Boiler water consumption**: `boiler_fluid_consumption(energy_consumption_kw=1800, heat_capacity_kj=2, target_temperature=165, ambient_temperature=15)` = 1800 / (2 × 150) = **6/s** — matches the wiki's directly stated water-consumption figure exactly, confirming both numbers are internally consistent.

**Boiler steam output = 60/s**: taken directly from the wiki (not derived from primitives held here) — Factorio 2.0's "Fluids 2.0" rework made boilers/heat-exchangers convert water to steam at a fixed 1:10 volume ratio (patch note, quoted verbatim in a Factorio Forums thread on this exact ratio, https://forums.factorio.com/viewtopic.php?t=116305: *"1 Water will now produce 10 Steam in boilers/heat exchangers"*) — this multiplier isn't itself a `data.raw` field held in this repo, so it's cited rather than derived, per CLAUDE.md rule 3's "do we already have the primitives" test.

**Steam engine power output**: `generator_power_output(fluid_usage_per_tick=0.5, effectivity=1, heat_capacity_kj=0.2, temperature=165, ambient_temperature=15)` = 0.5 × 60 × 1 × 0.2 × 150 = **900kW** — matches the wiki's stated power output exactly.

**Ratio**:
- `boiler_steam_output_per_sec` (60) ÷ `steam_engine_steam_consumption_per_sec` (30) = **2 steam engines per boiler**
- `offshore_pump_water_output_per_sec` (1200) ÷ `boiler_water_consumption_per_sec` (6) = **200 boilers per offshore pump**
- 200 boilers × 2 = **400 steam engines per offshore pump**

→ **1 offshore pump : 200 boilers : 400 steam engines**

## This ratio changed in 2.0 — a live example of CLAUDE.md's founding caution

A Factorio short (Xterminator, "Helpful Factorio ratios you shouldn't
ignore", youtube.com/shorts/d8jx7u87EQQ, posted April 2024 — before the
2.0/Space Age release on 2024-10-21) states this ratio as **1:20:40**,
not 1:200:400. That was the correct ratio *pre-2.0*: a Factorio Forums
thread from after the 2.0 release
(https://forums.factorio.com/viewtopic.php?t=116305, "Ratio of boilers
to offshore pumps") documents a player hitting exactly this
discrepancy, tracing it to the 2.0 "1 water → 10 steam" boiler rework
above — old guides/videos citing 1:20:40 went stale across the version
boundary without anyone editing them.

This project's `main` branch tracks the latest supported version (2.0
— see CLAUDE.md "Versioning"), so **1:200:400 is the value recorded
here**. This is functionally the same cautionary pattern CLAUDE.md rule
1 already opens with (the pre-2.0 rail turn radius of 10 tiles vs. the
sourced 11/13 tiles) — a plausible-sounding remembered number that was
correct once, for an older version, and wrong now. The other two
ratios in the same video (smelting furnaces-per-belt, advanced oil
processing cracking ratio) were cross-checked against
`relations/smelting_ratios.json` and `relations/oil_cracking_ratio.json`
and match exactly — those facts didn't change across 2.0, this one did.

Verified: 2026-08-22
