#   code10.1.py - Display planets
#   In this exercise you will read the file data/planets.json file and print out
#   All of the planets and the required amount of fuel you will need to reach
#   the planet.
#
#   Your output will look like
#
#   The planet Mercury has fuel available.
#   The planet Venus has fuel available.
#   The planet Earth has fuel available.
#   The planet Mars has fuel available.
#   The planet Jupiter has fuel available.
#   The planet Saturn has fuel available.
#   The planet Uranus has fuel available.
#   The planet Neptune has fuel available.
#   The planet Moon has fuel available.


from pathlib import Path
import json

# Define the path to the JSON file
path = Path('chapter10/ch10-coding-exercises/code/data/planets.json')

# Read the content of the file using read_text
contents = path.read_text()

# Parse the JSON data from the file content
planets_data = json.loads(contents)

# Iterate through the list of planets in the JSON data
for planet in planets_data['planets']:

    # Print the sentence for each planet
    print(f"The planet {planet['name']} has {planet['fuel_required']} fuel available. \n")

