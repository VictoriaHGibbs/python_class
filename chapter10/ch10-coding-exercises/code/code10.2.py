#   code10.2.py - Add a try, except, else 
#
#   This exercise builds on the previous exercise. In this exercise you will add
#   a try, except, else clause to test if the Python can find the file. If it
#   can't find the file, your code will display a message to the user.
#   Test your code with a proper file path and one that you know will not work.
#   
#    With the proper file path, your output will look like
#   The planet Mercury has fuel available.
#   The planet Venus has fuel available.
#   The planet Earth has fuel available.
#   The planet Mars has fuel available.
#   The planet Jupiter has fuel available.
#   The planet Saturn has fuel available.
#   The planet Uranus has fuel available.
#   The planet Neptune has fuel available.
#   The planet Moon has fuel available.
#
#   If Python cannot find the file, your output will look like
#   Sorry, the file planets.json does not exist.


from pathlib import Path
import json


# Define the path to the JSON file
file_path = Path('planets.json')

# Read the content of the file using read_text
# Use the try, except else clause to test if Python can find the file
# Your code here

    # Parse the JSON data from the file content
    planets_data = json.loads(file_content)

    # Iterate through the list of planets in the JSON data
    for planet in planets_data['planets']:
    # Print the sentence for each planet
        print(f"The planet {planet['name']} has fuel available.")

