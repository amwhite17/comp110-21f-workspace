"""Counting letters in a string."""

__author__ = "730281821"

letter: str = str(input("What letter do you want to search for? "))

word: str = str(input("Enter a word: "))

count = 0

for i in range(len(word)):
    if(word[i] == letter):
        count = count + 1

print("Count: ", count)
