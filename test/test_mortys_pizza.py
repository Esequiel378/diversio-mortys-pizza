from typing import List, Tuple

import pytest

from mortys_pizza import (
    Combinations,
    Pizza,
    build_pizza_preference,
    find_pizza_combination
)

from .mock import groups_1, groups_2, groups_3, groups_4

MORTYS_PIZZA_PREFERENCE = build_pizza_preference(
    crust="Pan", seasoning="Yes", sauce="Tomato", veggies="Broccoli", cheese="No"
)

PARAMETRIZED_GROUPS: List[Tuple[Combinations, Pizza]] = [
    (groups_1, groups_1[0][0]),
    (groups_2, groups_2[1][0]),
    (groups_3, groups_3[3][0]),
    (groups_4, groups_4[2][0]),
]


@pytest.mark.parametrize("group,expected", PARAMETRIZED_GROUPS)
def test_find_pizza_combinations(group, expected):
    assert find_pizza_combination(group, MORTYS_PIZZA_PREFERENCE) == expected


def test_find_pizza_combinations_with_same_id():
    assert id(find_pizza_combination(groups_4, MORTYS_PIZZA_PREFERENCE)) == id(
        groups_4[2][0]
    )
