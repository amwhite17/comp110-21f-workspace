"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730281821"


def test_only_evens_edge() -> None:
    """Edge test for only_evens."""
    a = [-7, -2, 6]
    assert only_evens(a) == [-2, 6]


def test_only_evens_useone() -> None:
    """Use 1 test for only_evens."""
    a = [6, 14, 28]
    assert only_evens(a) == [6, 14, 28]


def test_only_evens_usetwo() -> None:
    """Use 2 for only_evens."""
    a = [2, 16, 18]
    assert only_evens(a) == [2, 16, 18]


def test_sub_edge() -> None:
    """Edge test for sub."""
    a_list = [2, 4, 6]
    assert sub(a_list, -1, 2) == [2, 4]


def test_sub_useone() -> None:
    """Use 1 for sub."""
    a_list = [8, 10, 12]
    assert sub(a_list, 1, 2) == [10]


def test_sub_usetwo() -> None:
    """Use 2 for sub."""
    a_list = [6, 8, 10]
    assert sub(a_list, 0, 2) == [6, 8]


def test_concat_edge() -> None:
    """Edge test for concat."""
    first = [-1, 4, 5]
    second = [7, 8, 11]
    assert concat(first, second) == [1, 4, 5, 7, 8, 11]


def test_concat_useone() -> None: 
    """Use 1 for concat."""
    first = [2, 4, 6]
    second = [8, 10, 12]
    assert concat(first, second) == [2, 4, 6, 8, 10, 12]


def test_concat_usetwo() -> None:
    """Use 2 for concat."""
    first = [1, 3, 5]
    second = [7, 9, 11]
    assert concat(first, second) == [1, 3, 5, 7, 9, 11]