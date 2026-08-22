def energy_per_tile(energy_per_move: float, energy_per_tick: float, speed: float) -> float:
    """Energy cost (same unit as the two energy inputs) to cross 1 tile.

    energy_per_move: robot.energy_per_move (energy per tile moved).
    energy_per_tick: robot.energy_per_tick (energy per tick flown,
        independent of distance).
    speed: robot.speed, tiles/tick - so 1/speed is ticks spent per
        tile, and energy_per_tick/speed is the tick-upkeep cost of
        crossing that one tile.
    """
    return energy_per_move + energy_per_tick / speed


def flight_range_tiles(energy_budget: float, energy_per_move: float, energy_per_tick: float, speed: float) -> float:
    """Tiles a robot can fly on a given energy budget before running out.

    energy_budget: energy available for the trip (e.g. robot.max_energy
        for a theoretical full-charge range, or a smaller usable
        fraction - see relations/robot_flight_range.md).
    """
    return energy_budget / energy_per_tile(energy_per_move, energy_per_tick, speed)
