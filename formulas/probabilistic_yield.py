def expected_yield_per_craft(probability: float, amount: float = 1) -> float:
    """Expected quantity of a probabilistic recipe result per craft.

    probability: recipe.results[].probability (0-1)
    amount: recipe.results[].amount
    """
    return probability * amount


def crafts_needed_for_expected_output(probability: float, amount: float = 1, target_output: float = 1) -> float:
    """Average number of crafts needed to expect target_output units of a
    probabilistic result (e.g. how much scrap to recycle for 1 processing-unit)."""
    return target_output / expected_yield_per_craft(probability, amount)
