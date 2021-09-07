"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730281821"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
random: int = randint(1, 10) 

if random < 3:
    print("Great things are coming your way! ")
else:
    if 2 < random < 6:
        print("Your talents will soon be recognized! ")
    else:
        if 5 < random < 8:
            print("Relaxation is coming your way! ")
        else:
             7 < random < 11 
             print("Find your inner peace. ")
             

print("Now, go spread positive vibes! ")


