"""Searches a certain phrase and returns a count of how many characters match"""

__author__: str = "730743185"

"""Defines counting variables and raises count if the characters in a certain
position match"""


# lines 9 and 10  define variables that will be returned (count) and what keeps track
# of what character is being tested (index)
# Lines 16 and 17 raise count by 1 if match, and raises index by 1 after every search.
def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
