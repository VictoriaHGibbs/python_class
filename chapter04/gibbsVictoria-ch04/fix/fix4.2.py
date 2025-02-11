# fix4.2.py

# This program is suppose to print the minimum and maximum numbers from 
# a list of numbers starting at 1 and going to 1,000,000. The program
# throws an error. Fix the code so the program displays the minimum and
# maximum numbers.

numbers = list(range(1, 1000001))
lowest = min(numbers)
highest = max(numbers)
print(f"The lowest number is: {lowest}.")
print(f"The highest number is: {highest}.")
