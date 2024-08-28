"""Mimics the users message by displaying exactly what they type"""

__author__: str = "730743185"


def mimic(message: str) -> str:
    """returns the message that the user typed in"""
    return str(message)


def main() -> None:
    """asks the user to input a message and then prints it."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
