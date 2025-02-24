# fix7.2.py - Even or odd
#
# What is wrong with this program? If I enter the number 10, it displays
# that the number is odd, not even. 
#
# Fix the code so that it produces the correct result.


number = input("Enter a number to determine if it is even or odd")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")