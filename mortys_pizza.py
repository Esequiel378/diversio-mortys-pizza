from typing import Dict, List, Tuple

Pizza = Dict[str, str]
PizzaCount = int
Combinations = List[Tuple[Pizza, PizzaCount]]

Preferences = Dict[str, str]


def build_pizza_preference(
    *, crust: str, seasoning: str, sauce: str, veggies: str, cheese: str
) -> Preferences:
    return {
        "crust": crust,
        "seasoning": seasoning,
        "sauce": sauce,
        "veggies": veggies,
        "cheese": cheese,
    }


def weight_pizza_preference(pizza: Pizza, preferences: Preferences) -> int:
    weight = 0

    for index, preference in enumerate(preferences):
        a = len(preferences) - index
        weight += 1 + a if pizza[preference] == preferences[preference] else -1 - a

    return weight


def find_pizza_combination(
    combinations: Combinations, preferences: Preferences
) -> Pizza:
    betPizza, bestWeight = combinations[0]

    for pizza, pizzaCount in combinations:
        weight = pizzaCount + weight_pizza_preference(pizza, preferences)

        if weight > bestWeight:
            betPizza, bestWeight = pizza, weight

    return betPizza
