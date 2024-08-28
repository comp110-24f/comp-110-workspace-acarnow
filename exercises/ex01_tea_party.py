"""Plan a tea party by calculating tea bags, treats, and cost of the party. """

__author__: str = "730743185"


# prints the sentence needed and adds the value that is needed, either based off
# the input of the user or the value from the function, using the value the user inserts
# Make sure to make all parts the same type using str() or int()


def main_planner(guests: int) -> None:
    """Print all info on the party based on num of guests. Use other functions."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the num of tea bags needed based on num of people going to party"""
    return people * 2


def treats(people: int) -> int:
    """Calculates num of treats needed based on num of teas that are expected"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates total cost of the tea party acc. to # of tea bags and treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


# didnt understand what this does, but now I understand its use for allowing
# the code to run properly.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
