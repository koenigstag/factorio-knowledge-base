# Module types: tradeoffs and where each is commonly used

Four module categories exist (`speed`, `productivity`, `efficiency`,
`quality`); this file is the qualitative overview cross-referencing
already-dumped tier-3 numbers, not a new derivation — `beacon_effect.md`
covers beacon stacking/allowed-effects, `quality_upcycling.md` covers
the quality-chance mechanic specifically.

## Tier-3 effects, straight from `datapacks/dump/vanilla/module/`

| module | own effect | side effects |
|---|---|---|
| speed-module-3 | `speed +50%` | `consumption +70%`, `quality -25%` |
| productivity-module-3 | `productivity +10%` | `consumption +80%`, `pollution +10%`, `speed -15%` |
| efficiency-module-3 | `consumption -50%` | none |
| quality-module-3 | `quality +2.5%` (real-percentage reading, see `quality_upcycling.md`'s ×10 note) | (own speed/consumption side effects not separately checked here) |

## Qualitative tradeoffs (sourced from the individual wiki pages)

- **Speed**: faster crafting, no output bonus; costs more power. Often
  placed in mining drills/pumpjacks directly (raw-resource extraction
  has no productivity-module-style "bonus output" ceiling concern the
  way a crafted-item recipe might). Also used to shrink a build's
  machine count for a given throughput — fewer machines means shorter
  belt/bot travel distances, which compounds with
  `mechanics/robot-types.md`'s flight-range/charge-time economics for
  bot-fed builds specifically.
- **Productivity**: bonus items from the same inputs — effectively free
  output — but slows crafting (`speed -15%` on the tier-3 module
  itself) and raises power draw substantially (`+80%`). Cannot go in a
  beacon at all (`beacon_effect.md`'s `allowed_effects` check) — only
  directly in a crafting machine, so productivity's benefit doesn't
  broadcast the way speed does.
- **Efficiency**: pure power reduction, no drawback in the tier-3 data
  above — the wiki's own framing is "none" for cons, unlike the other
  three types which each trade something else away for their main
  effect.
- **Quality**: chance to get a higher-quality output item per craft;
  slows crafting (mirrors productivity's speed penalty, doesn't stack
  with it in the same machine since only one module category typically
  fills a machine's slots in practice, though the game doesn't enforce
  single-category-only). Cannot go in a beacon either — same
  `allowed_effects` restriction as productivity.

**Not imported, pointer only**: `factoriocheatsheet.com`'s
"Productivity Module Payoffs" page (`github.com/deniszholob/
factorio-cheat-sheet`, `src/app/cheat-sheets/game-base/
productivity-module-payoffs/`) tabulates ROI time for productivity
modules across ~30 items, credited there to a third-party spreadsheet
("MadZuri's ROI Calculations") with no stated methodology in the
source. Worth a look for intuition-building, but low enough confidence
(cheat sheet citing a spreadsheet citing unstated assumptions) that
this project isn't importing its numbers — flagged here as a link, not
as data.

Source: https://wiki.factorio.com/Module,
https://wiki.factorio.com/Speed_module,
https://wiki.factorio.com/Productivity_module,
https://wiki.factorio.com/Efficiency_module,
https://wiki.factorio.com/Quality_module
Verified: 2026-08-08
