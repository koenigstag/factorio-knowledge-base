# Pipe (underground) crossing gap

The pipe-side analog of `relations/underground_belt_crossing_gap.md`,
closing the gap `glossary/invented/chem-bus.md` flagged when coining
that term (*"this project doesn't have a pipe-throughput/max-distance
formula the way it does for belts... flagged as an open gap"*).

Formula: `formulas/underground_belt_crossing_gap.py:crossing_gap`
(`max_distance − 1`) — **reused as-is, not duplicated**. The function
is generic despite its filename: it only needs a max-distance number
and the same "entrance/exit tiles show graphics, aren't free span"
reasoning, which holds for `pipe-to-ground` exactly as it does for
`underground-belt`.

Input: `datapacks/dump/vanilla/pipe-to-ground/pipe-to-ground.json`'s
`fluid_box.pipe_connections[].max_underground_distance = 10` — the
direct analog of `underground-belt.max_distance`, confirmed present in
the same connection entry that also carries `connection_type:
"underground"`.

## crossing_gap_tiles

| entity | max_underground_distance | crossing gap |
|---|---|---|
| pipe-to-ground | 10 | 9 |

Only one pipe tier exists in vanilla (unlike belts' four tiers) — no
table to fill in beyond this single row.

## The other half of "pipe throughput": flow rate, already covered

`glossary/invented/chem-bus.md`'s gap note bundled *distance* and
*flow-rate* together as one open item, but the flow-rate half was
actually already resolved before this entry existed:
`mechanics/fluids.json`/`.md` (`max_flow_per_connection_sec_practical
= 4200`, theoretical cap 6000/sec) and
`relations/basic_oil_processing_ratio.md` (concrete worked example:
refinery output vs. connection cap) already cover it — just not
cross-linked from `chem-bus.md` until now. Both `pipe` and
`pipe-to-ground`'s `fluid_box.volume = 100` (confirmed identical,
pulled directly) don't change either of those figures — segment
volume affects fill-level dynamics, not the flow-rate cap itself.

**Net**: the "gap" is now fully closed — distance (this file) and
throughput (`mechanics/fluids.md`) are both sourced, tying back to
`glossary/invented/chem-bus.md` and
`layouts/scalable_chem_base.md`'s open-questions list.

Source: `datapacks/dump/vanilla/pipe/pipe.json`,
`datapacks/dump/vanilla/pipe-to-ground/pipe-to-ground.json` (see
`datapacks/dump/vanilla/source.json`'s exceptions entry — Bilka2 gist,
2.0.65, pulled fresh 2026-08-09).
Verified: 2026-08-09
