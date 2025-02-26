# Title: Creating a Music Shop Inventory

# Objective: Write a program that asks the user to input names of musical 
# instruments for a music shop's inventory. The program should continue 
# asking for inputs until the user types 'done'. Once 'done' is 
# inputted, the program should print the complete list of
# musical instruments entered.

# Requirements:

#     Use the input() function to collect user inputs.
#     Implement a loop to continuously ask for user inputs.
#     Use a conditional statement to break out of the loop when the user
#     inputs 'done'.
#     Store all inputs in a list before 'done' is inputted.
#     After the loop ends, print the list of musical instruments.

# Hints:

#     Initialize an empty list to store the names of the instruments.
#     Use a while loop to keep asking for inputs.
#     Check if the user input is 'done' to exit the loop.
#     Use the append() method to add each instrument to the list.
#
# Beginning of program
#
# Initialize an empty list to store musical instruments
instruments = []
prompt = "\nWhat is the name of a musical instrument?"
# Use a while loop to continuously ask for user input
while True:
    # Ask the user to input the name of a musical instrument
    instrument = input(prompt)
    instruments.append(instrument)
    # Check if the user wants to stop the input process
    response = input("Would you like to stop? yes/no\n")
    if response == 'yes':
        break
    # Add the inputted instrument to the list
    

# Print the list of musical instruments after the loop ends
print("Here's the list of instruments:\n")
for instrument in instruments:
    print(instrument)
