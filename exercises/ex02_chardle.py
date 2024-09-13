"""Takes a 5 character word from the user and a character and displays if there are any
instances of the character in the word."""

__author__ = "730743185"

"""prompts the user to input a word and stops the program if word is not 5 characters"""


def input_word() -> str:
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return user_word


"""prompts the user to input a character and stops the program if character is not a
single character."""


# forgot when to use one equal sign or two when dealing with variable definitons or
# if/else statements.
def input_letter() -> str:
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return user_letter


"""determins if there are any instances of charcter in word and prints messages
accordingly."""


# did not know variable has to have definition stated before it can start counting.
# I thought line 36 wasnt needed.
def contains_char(word: str, letter: str) -> None:
    matches: int = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        matches = matches + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        matches = matches + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        matches = matches + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        matches = matches + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        matches = matches + 1
    if matches == 0:
        print("No instances of " + letter + " found in " + word)
    elif matches == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(matches) + " instances of " + letter + " found in " + word)
    return None


"""main function that calls functions in order to run program"""


def main() -> None:
    contains_char(input_word(), input_letter())


# I dont understand why main() is needed, why cant I paste defintion of main()
# and make that line 75?
"""Makes running program possible as a module and for functions to be reused
and imported."""
if __name__ == "__main__":
    main()
