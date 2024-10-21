""""""

__author__: str = "730743185"


def find_and_remove_max(a: list[int]) -> int:
    index: int = 0
    max: int = 0
    if len(a) == 0:
        return -1
    max: int = a[0]
    while index < len(a):
        if a[index] > max:
            max = a[index]
        index += 1
    index: int = 0
    while index < len(a):
        if a[index] == max:
            a.pop(index)
        else:
            index += 1
    return max
