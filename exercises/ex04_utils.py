"""Creates 4 functions that evaluate or alter lists"""

__author__: str = "730743185"

"""Evaluates if one list contains a certain number at all indexes"""


def all(list: list[int], num: int) -> bool:
    index: int = 0
    if len(list) == 0:
        return False
    while index < len(list):
        if list[index] == num:
            index += 1
        else:
            return False
    return True


"""Returns the maximum integer of a list"""


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index: int = 0
        max_int: int = list[0]
        while index < len(list):
            if list[index] > max_int:
                max_int = list[index]
            index += 1
        return max_int


"""Evaluates if two lists are equal"""


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    if len(list_1) != len(list_2):
        return False
    while index < len(list_1) and index < len(list_2):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True


"""adds one lists values onto the end of another"""


def extend(list_1: list[int], list_2: list[int]) -> None:
    index: int = 0
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1
    return None
