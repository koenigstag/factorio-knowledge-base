def cracking_ratio(heavy_produced_per_refinery, heavy_consumed_per_cracker,
                    light_produced_per_refinery, light_produced_per_heavy_cracker,
                    light_consumed_per_light_cracker):
    """Balances a 2-stage cracking chain (heavy -> light -> gas) against zero net
    accumulation of the intermediate fluids, per 1 upstream producer (e.g. refinery).

    All arguments are rates (items or fluid units/sec), typically from
    production_rate() applied to each recipe's relevant ingredient/result amount.

    Returns (heavy_crackers_per_producer, light_crackers_per_producer).
    """
    heavy_crackers = heavy_produced_per_refinery / heavy_consumed_per_cracker
    light_crackers = (
        light_produced_per_refinery + heavy_crackers * light_produced_per_heavy_cracker
    ) / light_consumed_per_light_cracker
    return heavy_crackers, light_crackers
