"""Creates two lists and doubles one, and with one
being applied to equal the other, they both are in turn doubled"""

__author__: str = "730743185"


def manual_append(list: list[int], num: int) -> None:
    list.append(num)
    return None


def double(list_2: list[int]) -> None:
    index: int = 0
    while index < len(list_2):
        list_2[index] = list_2[index] * 2
        index += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
