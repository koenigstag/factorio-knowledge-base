def yield_ratio_at_cycle(cycles: float, normal: float, minimum: float,
                          infinite_depletion_amount: float) -> float:
    """Current yield fraction (0-1) of an infinite resource after `cycles`
    extraction cycles have occurred since the patch was fresh.

    cycles: extraction cycles elapsed (see cycles_to_floor/time_to_floor
        for converting real-world seconds to this).
    normal: resource.normal (data.raw field) - amount at 100% yield.
    minimum: resource.minimum (data.raw field) - the floor amount;
        yield never drops below minimum/normal once reached.
    infinite_depletion_amount: resource.infinite_depletion_amount
        (data.raw field) - amount lost per extraction cycle.
    """
    amount = max(normal - infinite_depletion_amount * cycles, minimum)
    return amount / normal


def cycles_to_floor(normal: float, minimum: float, infinite_depletion_amount: float) -> float:
    """Extraction cycles until an infinite resource's amount reaches its floor."""
    return (normal - minimum) / infinite_depletion_amount


def time_to_floor(normal: float, minimum: float, infinite_depletion_amount: float,
                   mining_speed: float, mining_time: float) -> float:
    """Real-world seconds until an infinite resource entity reaches its yield
    floor, at 100% uptime with no speed/productivity bonuses.

    mining_speed: the extracting machine's mining_speed (data.raw field).
    mining_time: resource.minable.mining_time (data.raw field) - base
        seconds per extraction cycle at mining_speed=1.
    """
    return cycles_to_floor(normal, minimum, infinite_depletion_amount) * mining_time / mining_speed
