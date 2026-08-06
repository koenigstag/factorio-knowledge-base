def inserter_throughput(cycles_per_sec, items_per_cycle=1):
    """items/sec = cycles/sec x items grabbed per cycle.

    cycles_per_sec: chest-to-chest cycle rate, cited (not derived) from
        constraints/inserters-throughput.md - see decisions/0001-inserter-throughput-not-derived.md
        for why this input isn't computed from rotation_speed/extension_speed.
    items_per_cycle: items moved per cycle. Unambiguously 1 for inserter,
        burner-inserter, long-handed-inserter, fast-inserter. For
        bulk-inserter/stack-inserter this depends on researched
        "inserter capacity bonus" technology level, not a fixed datapack
        constant - do not default to 1 for those two tiers.
    """
    return cycles_per_sec * items_per_cycle
