def module_quality_chance(effect_quality_raw: float) -> float:
    """Real in-game quality-upgrade chance (fraction) contributed by one
    quality module. data.raw stores module.effect.quality at 10x its
    displayed percentage — confirmed by cross-checking quality-module
    tiers 1/2/3 in datapacks/dump/vanilla/module/ (0.1/0.2/0.25) against
    the wiki's stated +1%/+2%/+2.5%: all three divide out to exactly 10x.
    """
    return effect_quality_raw / 10


def tier_jump_distribution(next_probabilities: list) -> list:
    """Probability of landing exactly N tiers above the starting tier,
    given a quality upgrade was already triggered (module_quality_chance
    is a separate, prior roll — this only decides how far it cascades).

    next_probabilities: ordered list of each intermediate quality tier's
    `quality.<tier>.next_probability` field, from the starting tier up
    to (excluding) the target ceiling — e.g. for normal chasing
    legendary: [normal, uncommon, rare, epic] .next_probability, all
    0.1 in the vanilla quality chain (datapacks/dump/vanilla/quality/).
    The last entry is treated as the terminal gate: leftover probability
    mass collapses onto it, since there's nowhere higher to cascade to.

    Returns a list the same length as next_probabilities: index 0 is the
    chance of landing exactly +1 tier, index i is +(i+1) tiers. Sums to 1.0.
    """
    result = []
    remaining = 1.0
    for i, p in enumerate(next_probabilities):
        if i == len(next_probabilities) - 1:
            result.append(remaining)
        else:
            result.append(remaining * (1 - p))
            remaining *= p
    return result
