"""Finding duplicate letters in a word."""

__author__ = "730281821"

word: str = str(input("Enter a word: "))
bool = False

i = 0

while(i < len(word)):
    z = word[i]
    i = i + 1
    a = i
    while(a < len(word)):
        y = word[a]
        if z == y:
            bool = True
        a = a + 1

print("Found duplicate:", bool)