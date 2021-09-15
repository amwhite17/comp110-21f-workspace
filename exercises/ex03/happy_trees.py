"""Drawing forests in a loop."""

__author__ = "730281821"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

Depth: int = int(input("Depth: "))
i = 0
number = ''
while (i < Depth):
    i = i + 1
    y = 0
    while (y < i):
        number = number + TREE
        y = y + 1
    print(number)
    number = ''
