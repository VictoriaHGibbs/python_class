# code7.2.py - getting the band together
#
# Objective:
# Write a Python program that allows the band leader to keep a record of each
# band member's first name and the instrument they play. 
#
# The program will continuously prompt the user to enter this information until
# a specific condition is met (e.g., the user enters "done").
#
# Finally, the program will output the collected information in sentence
# format.
#
# Requirements:
#
# Prompt the user to enter a band member's first name and the instrument they 
# play in a loop.
#
# Store this information in a dictionary where the key is the band member's 
# first name and the value is the instrument they play.
#
# The loop should continue asking for inputs until the user types "done".
#
# Once the loop ends, the program should output the information stored 
# in the dictionary in sentence format, listing each band member 
# and the instrument they play.
#
# Output:
#
# Your output should look like the following. Of course it is your
# band, so you can use any names and instrument combinations
# that you like.
#
# Tim plays the banjo.
# Peggy plays the mando.
# Philip plays the fiddle.
#
# Begin code here
#
# Initialize an empty dictionary to store band member information
members = {}
active = True
# Start a loop to continuously ask for user input
while active:
    # Ask for the band member's first name
    name = input("\nWhat is the name of a bank member? ")
    # Ask for the instrument the band member plays
    instrument = input("\nWhat instrument do you play? ")
    # Store the information in the dictionary
    members[name] = instrument
    # Check if the user wants to end the input process
    response = input("\nDo you have more to enter? yes/ no \n ")
    if response == 'no':
        active = False

# Print the collected information in sentence format
for name, instrument in members.items():
    print(f"{name.title()} play the {instrument}.")
