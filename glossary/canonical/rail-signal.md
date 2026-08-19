# rail signal

Splits track into blocks: only one train may occupy a given block at a
time. A signal shows red when the block ahead is occupied, yellow when
a train has already been granted approval to enter it, green when
free. A train spanning multiple blocks occupies all of them at once.

See [chain-signal.md](chain-signal.md) for the variant that looks
ahead past its own block.

Source: https://wiki.factorio.com/Railway
Verified: 2026-08-19
