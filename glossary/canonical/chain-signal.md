# chain signal

Same block-based reservation mechanism as a [rail-signal](rail-signal.md),
but its displayed state reflects the next signal(s) ahead rather than
just its own block: it shows the same red/yellow/green as a rail
signal would, plus blue specifically when at least one onward path is
blocked but not all of them. This lets a train entering a chain-signal
block still choose between multiple onward routes instead of
committing to a block that might dead-end into an occupied one.

Typical use: intersections and merges, where a train needs to see past
its immediate block before committing to a path.

Source: https://wiki.factorio.com/Railway
Verified: 2026-08-19
