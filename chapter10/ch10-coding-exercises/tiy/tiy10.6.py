#  Get user input 
number1 = input("Enter a number: ")
number2 = input("Enter a second number: ")

try:
    result = int(number1) + int(number2)
    print(f"The result is: {result}")
except ValueError:
    print("That's not a number! Please enter two numbers!")
