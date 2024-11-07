"""File to define Bear class."""

__author__: str = "730743185"


class Bear:
    """defines bear class with age and hunger score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the bear class with age of 0 and hunger of 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """After one day, each bear ages by 1 and loses a hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases hunger score by num of fish eaten."""
        self.hunger_score += num_fish
