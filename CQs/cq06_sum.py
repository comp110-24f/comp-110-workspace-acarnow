"""Summing the elements of a list using different loops"""

__author__: str = "730743185"


def w_sum(vals: list[float]) -> float:
    total: float = 0.0
    index: int = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for index in vals:
        total += index
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for elem in range(0, len(vals)):
        total += vals[elem]
    return total
