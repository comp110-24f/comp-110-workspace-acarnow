"""File to define Fish class."""

__author__: str = "730743185"


class Fish:
    """Creates fish class with age."""

    age: int

    def __init__(self):
        """Initializes the fish class with age being 0."""
        self.age = 0
        return None

    def one_day(self):
        """After one day, each fish ages by 1."""
        self.age += 1
        return None
