def get_first(a: list[str]) -> str:
    return a[0]


def remove_first(a: list[str]) -> None:
    a.pop(0)
    return None


def get_and_remove_first(a: list[str]) -> str:
    first: str = f"{a[0]}"
    a.pop(0)
    return first
