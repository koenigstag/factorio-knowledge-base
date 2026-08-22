def ingredient_ratio(ingredient_amount: float, result_amount: float) -> float:
    """Ingredient units consumed per unit of recipe output.

    This is also the belt-lane ratio between an ingredient and its
    downstream product, independent of machine speed/tier: if the
    downstream item flows at a full belt's items/sec, the ingredient
    is consumed at ingredient_ratio x that same items/sec - which is
    exactly ingredient_ratio "lanes" of the ingredient, assuming both
    sides use the same belt tier.

    ingredient_amount: recipe.ingredients[].amount for this ingredient.
    result_amount: recipe.results[].amount for the recipe's main output
        (recipe.ingredients/results, see datapacks/dump/vanilla/recipe/).
    """
    return ingredient_amount / result_amount
