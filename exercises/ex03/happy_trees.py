"""Drawing forests in a loop."""

__author__ = "730281821"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

Depth: int = int(input("Depth: "))
i = 0
x = ''
while (i < Depth):
    i = i + 1
    z = 0
    while (z < i):
        x = x + TREE
        z = z + 1
    print(x)
    temp = ''
    