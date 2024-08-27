"""Mimics the users message by displaying exactly what they type"""

__author__: str = "730743185"

""""""


def mimic(message: str) -> str:
    return str(message)


""""""


def main() -> None:
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
