"""Establishes Node class and creates definitions for methods that create linked lists."""

from __future__ import annotations

__author__: str = "730743185"


class Node:
    """Establishes the node class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes the node class with value and next."""
        self.value = val
        self.next = next


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def sum(head: Node | None) -> int:
    """Adds the values of all nodes."""
    # base case of when last item of linked list is None.
    if head is None:
        return 0
    else:
        # recursive case triggering the next Node
        return head.value + sum(head.next)


def to_str(head: Node | None) -> str:
    """Creates a str of each Node value."""
    # base case of when last item of linked list is None.
    if head is None:
        return "None"
    else:
        # recursive case triggering the next Node
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node | None) -> int:
    """Returns the last value in the linked list."""
    # base case of when last item of linked list is None.
    if head is None:
        return -1
    if head.next is None:
        return head.value
    else:
        # recursive case triggering the next Node
        return last(head.next)


def value_at(head: Node | None, idx: int) -> int:
    """Returns the value of a certain node in the linked list."""
    if idx < 0 or head is None:
        raise IndexError("Index is out of bounds on this list")
    elif idx == 0:
        return head.value
    else:
        idx -= 1
        # recursive case triggering the next Node
        return value_at(head.next, idx)


def max(head: Node | None) -> int:
    """Returns the highest value of the list of Nodes."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        # base case of when last item of linked list is None.
        if head.next is None:
            return head.value
        else:
            # recursive case triggering the next Node
            biggie: int = max(head.next)
            if head.value > biggie:
                biggie = head.value
            return biggie


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list from a list of values."""
    if len(items) == 0:
        return None
    else:
        # recursive case triggering the next Node
        node: Node = Node(items[0], linkify(items[1:]))
        return node


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies each value of the nodes by a certain factor."""
    # base case of when last item of linked list is None.
    if head is None:
        return None
    else:
        # recursive case triggering the next Node
        new_head: Node = Node(head.value * factor, scale(head.next, factor))
        return new_head
