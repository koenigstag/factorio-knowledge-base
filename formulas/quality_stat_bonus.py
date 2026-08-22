def default_stat_multiplier(level: int) -> float:
    """Generic quality stat multiplier (applies to health, and to any
    entity-specific stat that doesn't define its own override multiplier
    field). QualityPrototype's default_multiplier field default:
    1 + 0.3 * level (lua-api.factorio.com/latest/prototypes/QualityPrototype.html).
    """
    return 1 + 0.3 * level


def linear_stat_multiplier(level: int) -> float:
    """A handful of specific stat multipliers (tool_durability_multiplier,
    accumulator_capacity_multiplier, flying_robot_max_energy_multiplier)
    default to this steeper formula instead of default_stat_multiplier:
    1 + level, not 1 + 0.3 * level.
    """
    return 1 + level


def capped_range_multiplier(level: int, cap: float = 3.0) -> float:
    """range_multiplier defaults to min(1 + 0.1 * level, cap) - the one
    quality multiplier family with a documented ceiling.
    """
    return min(1 + 0.1 * level, cap)
