#4.5.py

# planets is now a tuple (not a list) containing planets in our solar system. The list is in alphabetical order.
# For those who still think Pluto should be included, this is for you.
# By definition a tuple's values cannot change. fix the program so Pluto is added to the tuple.

planets = ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
print("The planets in our solar system")
print(planets)
print("Bring back Pluto!")
planets_including_pluto = planets[:]
planets_including_pluto.append('Pluto')
print (planets_including_pluto)
