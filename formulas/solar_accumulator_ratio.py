def solar_accumulator_ratio(dawn_ticks, day_ticks, dusk_ticks, night_ticks,
                             solar_panel_output_kw, accumulator_capacity_mj):
    """Solar panels and accumulators needed per MW of constant base load,
    for a day/night cycle with a linear light-level ramp during dawn/dusk
    (0 -> full over dawn_ticks, full -> 0 over dusk_ticks).

    Sizes solar capacity so its average output over a full cycle equals
    the base load, then numerically integrates net power (solar - load)
    over a steady-state cycle to find the accumulator swing (max - min
    cumulative energy) needed to cover every deficit.

    Returns (panels_per_mw, accumulators_per_mw).
    """
    total = dawn_ticks + day_ticks + dusk_ticks + night_ticks

    def solar_factor(t):
        t = t % total
        if t < dawn_ticks:
            return t / dawn_ticks
        t -= dawn_ticks
        if t < day_ticks:
            return 1.0
        t -= day_ticks
        if t < dusk_ticks:
            return 1.0 - t / dusk_ticks
        return 0.0

    avg_factor = sum(solar_factor(t) for t in range(total)) / total
    solar_mw_per_mw_baseload = 1.0 / avg_factor
    panels_per_mw = (1000 / solar_panel_output_kw) / avg_factor

    energy = 0.0
    history = []
    for _ in range(3):  # run a few cycles so the swing reflects steady state, not the arbitrary start point
        for t in range(total):
            net_mw = solar_mw_per_mw_baseload * solar_factor(t) - 1.0
            energy += net_mw * (1 / 60)  # MW * (1 tick = 1/60 s) = MJ
            history.append(energy)
    last_cycle = history[-total:]
    swing_mj = max(last_cycle) - min(last_cycle)
    accumulators_per_mw = swing_mj / accumulator_capacity_mj

    return panels_per_mw, accumulators_per_mw
