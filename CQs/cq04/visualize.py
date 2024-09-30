from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# these imports allow concat and get coords to run in this program

"""Create global variables x and y that are used to run concat and get
coords function"""

__author__: str = "730743185"

x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
