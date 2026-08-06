# Nuclear reactor neighbor bonus output

Formula: `formulas/reactor_neighbor_output.py:reactor_grid_output` —
each reactor's output = `base × (1 + neighbour_bonus × adjacent_reactor_count)`,
orthogonal adjacency only.

Inputs, both from `datapacks/dump/vanilla/reactor/nuclear-reactor.json`:
`consumption=40MW` (base output), `neighbour_bonus=1` (+100% per
adjacent reactor).

## total_mw_by_grid

| grid | reactors | total MW |
|---|---|---|
| 2×2 | 4 | 480 |
| 2×4 | 8 | 1120 |
| 2×6 | 12 | 1760 |

All 3 verified by running the formula (grid neighbor-counting, not
hand arithmetic), and all 3 match an independently-published community
figure for the same grid sizes exactly — confirms both the formula
and the `neighbour_bonus=1`/`consumption=40MW` datapack values at
once.

Verified: 2026-08-06
