"""Practice with dictionaries."""

__author__ = "730281821"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Return Reverse."""
    invert = dict()
    for x, y in a.items():
        if y not in invert:
            invert[y] = x
        else:
            raise KeyError("Invalid")
    print(invert)
    return invert 


def favorite_color(a: dict[str, str]) -> str:
    """Return color."""
    amount = dict()
    for x in a.values():
        if x not in amount:
            amount[x] = 1
        else:
            if x in amount:
                amount[x] += 1
    favorite_color = max(amount, key=amount.get)
    print(favorite_color)
    return favorite_color


def count(a: list[str]) -> dict[str, int]:
    """Return List."""
    count = dict()
    for x in a:
        if x not in count:
            count[x] = 1
        else:
            if x in count:
                count[x] += 1
    print(count)
    return count