"""Examples of using listins in a simple 'game'."""


from random import randint 


rolls: list[int] = list() 

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

#remove an item from the list by its index (pop)
rolls.pop(len(rolls) - 1)

print(rolls)


# sum the values of our rolls!
i: int = 0
sum: int = 0 
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")


# #list of ints / list[T] of type T
# #list() is a constructor 
# rolls.append(randint(1, 6))
# #dot calls function on specific variable 
# rolls.append(randint(1, 6))
# #as you append, items get added to the bottom of the list 
# rolls.append(randint(1, 6))

# #access and individual item 
# print(rolls[0])
# print(rolls[1])

# #to access item of a list uses rolls[int expr] 
#         #using subscription notations to access item by their 0-based index 

# #to access the length of a list (number of items)
# print(len(rolls))

# #to access the last item of a list 
# print(rolls[len(rolls) - 1])

# #could also do ...
# #last_index: int = len(rolls) -1
# #print(rolls[last_index])

# #size of the number of items in a list len(rolls)

