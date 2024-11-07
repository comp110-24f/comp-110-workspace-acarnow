"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730743185"


class River:
    """Creates river class with day, fish, and bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fishes and bears and removes them if they are too old."""
        good_fish: list[Fish] = []
        good_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                good_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                good_bears.append(bear)
        self.bears = good_bears
        self.fish = good_fish
        return None

    def bears_eating(self):
        """If there are at least 5 bears, then 3 fish are eaten and therefore removed."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
            else:
                bear.eat(0)
        return None

    def check_hunger(self):
        """If there are any bears with less than 0 hunger score, they starved and are removed."""
        good_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                good_bears.append(bear)
        self.bears = good_bears

        return None

    def repopulate_fish(self):
        """For every 2 fish, 4 more are born and added."""
        count: int = len(self.fish)
        while count >= 2:
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            count -= 2
        return None

    def repopulate_bears(self):
        """For every 2 bears, one more is born and added."""
        count: int = len(self.bears)
        while count >= 2:
            self.bears.append(Bear())
            count -= 2
        return None

    def view_river(self):
        """Prints the status of the river, including day, and num of bears and fishes."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Runs the river evaluation 7 times to simulate one week."""
        x: int = 0
        while x < 7:
            self.one_river_day()
            x += 1

    def remove_fish(self, amount: int):
        """Removes fish depending on amount given."""
        count: int = 0
        while amount != count:
            self.fish.pop(0)
            count += 1
