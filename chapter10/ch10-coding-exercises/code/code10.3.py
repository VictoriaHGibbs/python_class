#   code10.3.py - user input
#   In this exercise you will ask the user to enter the name of a planet in our
#   solar system. Use the user input to see if that planet exists. Use the 
#   title() method to make sure the capitalization is the same for the user's
#   entry and the planet name in the data/planets.json file
#
#   If the planet exists, your output will look like
#
#   What planet would you like to go to? venus
#   The planet Venus has 30 units of fuel available.
#



from pathlib import Path
import json

# Get user input
# Your code here


# Define the path to the JSON file
file_path = Path('data/planets.json')

# Read the content of the file using read_text
try:
    file_content = file_path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist")
else:

    # Parse the JSON data from the file content
    planets_data = json.loads(file_content)

    # Iterate through the list of planets in the JSON data
    for planet in planets_data['planets']:
        #   Add your if and print statement here