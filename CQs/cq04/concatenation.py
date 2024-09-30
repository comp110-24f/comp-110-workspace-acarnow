"""Creates a function that concats two inputs and only
allows that function to run in a module"""

__author__: str = "730743185"

word1: str = "happy"
word2: str = "tuesday"


# function that concats two string inputs together.
def concat(input_1: str, input_2: str) -> str:
    return input_1 + input_2


# only runs concat if it is being run in a module
if __name__ == "__main__":
    print(concat(word1, word2))
