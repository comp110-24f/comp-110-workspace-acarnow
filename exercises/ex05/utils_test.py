import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""runs tests on 3 different functions in utils.py to ensure correctness"""

__author__: str = "730743185"


def test_only_evens_edge() -> None:
    """tests if empty list input returns empty list"""
    empty_list: list[int] = []
    assert only_evens(empty_list) == []


def test_only_evens_no_evens() -> None:
    """tests if list with no evens returns empty list"""
    no_evens_list: list[int] = [1, 3, 5, 7, 9, 11, 13, 15]
    assert only_evens(no_evens_list) == []


def test_only_evens_same_even_num() -> None:
    """tests if list with same value even number still shows number twice"""
    same_even_list: list[int] = [2, 2, 3, 5]
    assert only_evens(same_even_list) == [2, 2]


def test_sub_edge() -> None:
    """tests if empty list returns empty list"""
    empty_list: list[int] = []
    assert sub(empty_list, 0, 0) == []


def test_sub_max_index() -> None:
    """tests if max indexes outside of lists range still return whole list"""
    a_list: list[int] = [0, 1, 2, 3, 4, 5]
    assert sub(a_list, 0, 8) == [0, 1, 2, 3, 4, 5]


def test_sub_negative_start_index() -> None:
    """tests if start index at a negative value is still seen as 0 by the program"""
    b_list: list[int] = [0, 1, 2, 3, 4, 5]
    assert sub(b_list, -1, 4) == [0, 1, 2, 3]


def test_add_at_index_edge() -> None:
    """tests if negative index raises indexerror"""
    a_list: list[int] = [0, 1, 2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(a_list, -1, -1)


def test_add_at_index_2() -> None:
    "tests if number can be added at middle of list"
    a_list: list[int] = [0, 1, 2, 3, 4]
    add_at_index(a_list, 5, 3)
    assert a_list == [0, 1, 2, 5, 3, 4]


def test_add_at_index_3() -> None:
    """tests if number can be added to front of list"""
    a_list: list[int] = [0, 1, 2, 3, 4]
    add_at_index(a_list, -1, 0)
    assert a_list == [-1, 0, 1, 2, 3, 4]
