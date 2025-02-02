# Looping through an entire list
# magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n--------------------------------------------\n")

# Doing more work within a loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("\n--------------------------------------------\n")

# Doing something after a loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
 
print("Thank you everyone, that was a great show!")

# show how indenting the line will alter the output
print("\n--------------------------------------------\n")

exit()

# NOTE - avoid indentation errors
# Python will remind you if you forget to indent

# Making numerical lists
#first_numbers.py

# "off by one" behavior
# range() start counting at the first value but stops when it reaches the 
# second value you provide
for value in range(1, 5):
    print(value)

print("\n--------------------------------------------\n")

# Using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

print("\n--------------------------------------------\n")

# square_numbers.py
# the append method is not needed unless i'm missing something

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(square)

print("\n--------------------------------------------\n")

# even_numbers.py
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n--------------------------------------------\n")

# min, max, sum
# can also do this from the command line
get_max_number = max(range(1, 11))
print(f"In the range of numbers 1 - 10, the maximum is {get_max_number} \n")

print("\n--------------------------------------------\n")

print(f"In the range of numbers 1 - 10, the minimum is {min(range(1, 11))}")

print("\n--------------------------------------------\n")

# list comprehensions
# a list comprehension allow you to generate this same list with one line of code

# squares.py
squares = [value**2 for value in range(1, 11)]
print(squares)

print("\n--------------------------------------------\n")

# other errors - missing the colon
# be careful where you indent
# indenting unnecessarily after the the loop
# play around here

squares = []
for value in range(1, 11):
    square = value ** 2
    print(square)

print("\n--------------------------------------------\n")

# Slicing a list

# players.py
# show different variations
# if you omit the first argument, python assumes 0

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# similarly if you omit the last item
print(players[2:])

print("\n--------------------------------------------\n")

print(players[-2:])

print("\n--------------------------------------------\n")

# looping through a slice

print("Here are the first three players\n")
for player in players[:3]:
    print(player.title())

print("\n--------------------------------------------\n")

# copying a list
# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

print(f"my_foods: {my_foods}\n")
print(f"friends foods: {friend_food}\n")

print("\n--------------------------------------------\n")

# tuples
# immutable: a value that cannot change
# tuple: immutable list

# dimensions.py
# note the () and not []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("\n--------------------------------------------\n")

# looping through all the values in a tuple

for dimension in dimensions:
    print(dimension)

# writing over a tuple
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

# cant do
# dimensions[0] = 22

# can to
dimensions(400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)


