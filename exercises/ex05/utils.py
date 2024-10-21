"""3 functions that create from or modify a list of integers."""

__author__: str = "730743185"


def only_evens(a: list[int]) -> list[int]:
    """Creates a list with only even numbers of list given"""
    b: list[int] = []
    for i in a:
        # ensures only even numbers are added
        if i % 2 == 0:
            b.append(i)
    return b


def sub(a: list[int], start_index: int, end_index: int) -> list[int]:
    """creates a new list from old list starting and stopping at certain index"""
    b: list[int] = []
    index: int = start_index
    if start_index < 0:
        index = 0
    if end_index > len(a):
        end_index = len(a)
    while end_index != index:
        # allows for each number to be added until end index is reached
        b.append(a[index])
        index += 1
    return b


def add_at_index(a: list[int], value: int, index: int) -> None:
    """modifys a list by adding a certain value at a certain index"""
    idx: int = len(a)
    if index > len(a) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    # creates a slot for adding the new value.
    a.append(0)
    # thought it was idx > 0, took a long time to realize only needs to be moved until index required.
    while idx > index:
        a[idx] = a[(idx - 1)]
        idx -= 1
    a[index] = value
    print(a)
