#4.4.py

# planets is a list containing the planets in our solor system. The list is in alphabetical order
# Currently the program generates an error when your run it. Fix the code so the program
# prints out the last 3 planets.

planets = ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
for planet in planets[-:3]
    print(planet)