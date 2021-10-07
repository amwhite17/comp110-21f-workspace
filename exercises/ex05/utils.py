"""List utility functions part 2."""

__author__ = "730281821"


def only_evens(a: list[int]) -> list[int]:
    """The Even Numbers."""
    end: list[int] = []
    for number in a:
        if (number % 2) == 0:
            end.append(number)
    return end


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """The subset."""
    another = []
    if a < 0:
        a = 0
    if b > len(a_list):
        b = len(a_list)
    while a < b:
        another.append(a_list[a])
        a = a + 1
    return another 


def concat(first: list[int], second: list[int]) -> list[int]:
    """Concatination."""
    a_list: list[int] = []
    for number in first:
        if number < 0:
            number = 1
        a_list.append(number)
    for figure in second:
        if figure < 0:
            figure = 1
        a_list.append(figure)
    return a_list