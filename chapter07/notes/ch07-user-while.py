# How the input funciton works

# parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# The input() function pauses the program and waits for the user to enter text. When the user presses Enter, the program continues. The text the user entered is stored in the variable message. The print() function then displays the message back to the user.


# Greeter.py
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# The input() function always returns a string, even if the user enters a number. If you want to use the input as a number, you'll need to convert it using the int() or float() functions.

# Using int() to convert a string to an integer
# If you remove int() from the following code, you'll get a TypeError because you can't concatenate a string and an integer. The int() function converts the string to an integer so that it can be concatenated with the other string.``

age = input("How old are you? ")
age = int(age)
print(f"You are {age} years old.")

# Using float() to convert a string to a float
# The float() function works the same way as int(), but it converts the string to a floating-point number.

#rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)   
if height >= 36:
    print("\nYou're tall enough to ride!")
else:    
    print("\nYou'll be able to ride when you're a little older.")   

#Modulo Operator
# The modulo operator (%) divides one number by another number and returns the remainder. It's useful for determining if one number is divisible by another. For example, 4 % 3 returns 1 because 4 divided by 3 is 1 with a remainder of 1.

# Display output in terminal

# Even or Odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#   The modulo operator is useful for determining if a number is even or odd. When a number is divided by 2, the remainder is 0 if the number is even and 1 if the number is odd.

# TiY 7.3 Multiples of Ten
number = input("Enter a number, and I'll tell you if it's a multiple of ten: ")
number = int(number)
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")

# The modulo operator is useful for determining if a number is a multiple of another number. When a number is divided by another number, the remainder is 0 if the number is a multiple of the other number.

# Introducing While Loops
# A while loop repeats a block of code as long as a condition is true. For example, the following code counts from 1 to 5:

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)  

# The program works well, but it prints the word 'quit' as the final message. To fix this, you can use a break statement in the while loop to exit the loop when the user enters 'quit':

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(message)

# Using a Flag
# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our program so it runs while the flag is set to True and stops when any of several events sets the value of the flag to False. As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True. This way, all our other tests can be neatly organized in the rest of the program.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
# Using continue in a Loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)   

# Avoiding Infinite Loops
# Every while loop needs a way to stop running so it won't continue to run forever. For example, the following loop runs forever: 

# x = 1
# while x <= 5:
#     print(x)

# If you accidentally write a loop that never ends, press CTRL-C or just close the terminal window running your program. 

## TiY 7.5 Movie Tickets
prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

# Using a while loop with lists and dictionaries    
# You can use a while loop to manage lists and dictionaries, and to keep track of your position in the list or dictionary.

# Moving Items from One List to Another
# Consider a list of newly registered but unverified users. After we verify these users, how can we move them to a separate list of confirmed users? One way to do this is to use a while loop to pull users from the list of unverified users as we verify them and then add them to a separate list of confirmed users.

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
# Say you have a list of pets with the value 'cat' repeated several times. To remove all instances of that value, you can run a while loop until 'cat' is no longer in the list.

# Start with a list containing duplicate items.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# Remove all instances of 'cat' from the list.
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
# You can prompt for as much input as you need in each pass through a while loop. Let's make a polling program in which each pass through the loop prompts for the participant's name and response. We'll store the data we gather in a dictionary, because we want to connect each response with a particular user.

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
# This program works well, but it assumes that everyone who takes the poll will provide a mountain they'd like to climb. We can add a test to ensure that the dictionary is not empty before we print each person's response.

# Using a while loop to process items in a list
# Lists are used to store collections of items. You can use a while loop to process items in a list one at a time. For example, consider a list of unprinted designs that need to be printed. You can move each design to a separate list of printed designs after it's printed.

# Start with a list of unprinted designs.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)








