"""Creates a function that displays each coordinate or sequence of 2 numbers"""

__author__: str = "730743185"


def get_coords(xs: str, ys: str) -> None:
    x_count: int = 0
    y_count: int = 0
    while x_count < len(xs):
        while y_count < len(ys):
            # nested while loop runs through y coords before running through x coords.
            print(f"{xs[x_count]},{ys[y_count]}")
            # allows for less typing and uses of + with a f string.
            y_count += 1
        x_count += 1
        y_count = 0
