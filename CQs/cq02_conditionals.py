"""Have the user guess a secret number (that is 7) and display if they were too low,
high, or just right! and display secret number."""

__author__: str = "730743185"


"""assigns secret number variable the value of 7 and asks the user to guess the number,
then prints statment based off answer! """


def guess_a_number() -> None:
    secret: int = 7
    useranswer: int = int(input("Guess a number:"))
    print("Your guess was " + str(useranswer))
    if secret == useranswer:
        print("You got it!")
    elif useranswer < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif useranswer > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
