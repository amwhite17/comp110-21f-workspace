"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730281821"


def test_invert_edge() -> None:
    """Test Inverse using Edge."""
    a = {"x": "y", "m": "", "q": "r"}
    assert invert(a) == {"y": "x", "": "m", "r": "q"}


def test_invert_useone() -> None:
    """Test inverse use one."""
    a = {"comp": "123", "school": "456", "class": "789"}
    assert invert(a) == {"123": "comp", "456": "school", "789": "class"}


def test_invert_usetwo() -> None:
    """Test invert use two."""
    a = {"j": "k", "l": "m", "n": "o"}
    assert invert(a) == {"k": "j", "m": "l", "o": "n"}


def test_favorite_color_edge() -> None:
    """Test for favorite color using edge.""" 
    a = {"Matt": "blue", "Lori": "green", "Nate": "red", "Jordan": "red", "Liam": ""}
    assert favorite_color(a) == "red"


def test_favorite_color_useone() -> None:
    """Test color used one."""
    a = {"Abbi": "blue", "Nate": "red", "Jordan": "blue", "Lori": "green"}
    assert favorite_color(a) == "blue"


def test_favorite_color_usetwo() -> None:
    """Test for favorite color use two."""
    a = {"Matt": "red", "Devon": "green", "Nate": "green", "Lori": "purple", "Abbi": "green"}
    assert favorite_color(a) == "green"


def test_count_edge() -> None:
    """Test for count using edge.""" 
    a = ["sun", "sun", "", "cloud", "rain"]
    assert count(a) == {"sun": 2, "": 1, "cloud": 1, "rain": 1}


def test_count_useone() -> None:
    """Test count using use one."""
    a = ["apple", "orange", "lemon", "apple"]
    assert count(a) == {"apple": 2, "orange": 1, "lemon": 1}


def test_count_usetwo() -> None: 
    """Test count using use two.""" 
    a = ["one", "two", "two", "three", "three", "three"]
    assert count(a) == {"one": 1, "two": 2, "three": 3}