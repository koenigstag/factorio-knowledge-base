def net_effect(ingredient_amount, result_amount):
    """Net items gained (or lost, if negative) per craft for an item
    appearing on both sides of a recipe (a "catalyst" pattern, e.g.
    kovarex-enrichment-process). result_amount - ingredient_amount."""
    return result_amount - ingredient_amount


def expected_crafts_per_unit(probability):
    """Expected number of crafts needed to get 1 unit of a probabilistic
    recipe result (recipe.results[].probability)."""
    return 1 / probability
