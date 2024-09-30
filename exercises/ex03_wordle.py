"""A game that gives the user 6 turns to guess a secret word"""

__author__: str = "730743185"


def input_guess(secret_word_len: int) -> str:
    """ensures users guess is the same length as secret word"""
    word: str = input(f"Enter a {secret_word_len} character word: ")
    # creates local variable so program can check if guess is same length as secret word.
    while secret_word_len != len(word):
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks secret word for any instances of certain character"""
    assert len(char_guess) == 1
    counter: int = 0
    while counter < len(secret_word):
        if char_guess == secret_word[counter]:
            # checks if current character in secret word matches character in guess.
            return True
        else:
            counter += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """creates wordle colors based on if character in guess is in correct slot,
    is present in the entire secret word, or is not present at all."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    # misread directions and typed forward slash. Big Mistake!
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    counter: int = 0
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            result += GREEN_BOX
            counter += 1
        elif contains_char(secret, guess[counter]) is True:
            result += YELLOW_BOX
            counter += 1
        else:
            result += WHITE_BOX
            counter += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    while turn_count <= 6:
        guess: str = ""
        print(f"=== Turn {turn_count}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        # forgot emojified dosent print on its own, so need to add print()
        if guess == secret:
            print(f"You won in {turn_count}/6 turns!")
            return None
        turn_count += 1
    if turn_count > 6:
        print("X/6 - Sorry, try again tomorrow!")
        return None


if __name__ == "__main__":
    main(secret="codes")
