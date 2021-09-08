"""Counting letters in a string."""

__author__ = "730281821"

letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")

count = word.count(letter)

print("Count: ", count)