"""Plan a tea party by calculating tea bags, treats, and cost of the party. """

__author__: str = "730743185"

"""Print all information on the party based on num of guests. Use other functions."""


# prints the sentence needed and adds the value that is needed, either based off
# the input of the user or the value from the function, using the value the user inserts
# Make sure to make all parts the same type using str() or int()


def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


"""Calculates the num of tea bags needed based on num of people going to the party"""


def tea_bags(people: int) -> int:
    return people * 2


"""Calculates num of treats needed based on num of teas that are expected to be drank"""


def treats(people: int) -> int:
    return int(tea_bags(people) * 1.5)


"""Calculates total cost of the tea party acc. to # of tea bags and treats. """


def cost(tea_count: int, treat_count: int) -> float:
    return (tea_count * 0.5) + (treat_count * 0.75)


# didnt understand what this does, but now I understand its use for allowing
# the code to run properly.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
