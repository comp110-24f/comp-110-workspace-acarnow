from CQs.cq07.find_max import find_and_remove_max

"""3 tests that make sure function performs tasks properly"""

__author__: str = "730743185"


def test_find_and_remove_max() -> None:
    """function should return max"""
    a: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(a) == 5


def test_find_and_remove_max_2() -> None:
    """function should remove max"""
    a: list[int] = [1, 2, 3, 4, 5]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 4]


def test_find_and_remove_max_3() -> None:
    """function should return -1 with empty list"""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
