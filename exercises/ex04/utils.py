"""List utility functions."""

__author__ = "730281821"


def all(a: list[int], b: int) -> bool:
    """The main funciton for all."""
    i = 0
    if len(a) == 0:
        return False
    while i < len(a):
        if a[i] != b:
            return False 
        i = i + 1
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """The Main Function for is_equal."""
    i = 0
    if len(a) != len(b):
        return False
    while i < len(a):
        if a[i] != b[i]:
            return False 
        i = i + 1
    return True


def max(a: list[int]) -> int:
    """The main function for max."""
    i = 0
    the_max = a[i]
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(a):
        if a[i] > the_max:
            the_max = a[i]
        i = i + 1
    return the_max 