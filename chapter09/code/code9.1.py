#   code9.1.py - Distance from the sun
#      
#   Create a Planet Class: 
#   This class represents planets in our solar system 
#   with attributes, name and distance_from_sun (the average distance from the
#   sun in million kilometers). Implement an __init__ method that initializes
#   these attributes and a __str__ method to return a string with the planet's
#   information.
#
#   Orbital Period Method: 
#   Implement a method within the Planet class named orbital_period that 
#   calculates the orbital period of the planet around the
#   sun in Earth years using a simplified formula based on the distance from 
#   the sun.
#
#   Instantiate Planet Objects: 
#   Create objects for the following four planets with their actual names and 
#   approximate distances from the sun. 
#   Keep in mind which elements are strings and which are numbers. Remember that
#   strings require quotes and numbers do not.
#
#   earth:      Approximately 149.6 million kilometers from the Sun.
#   mars:       Approximately 277.9  million kilometers from the Sun.
#   venus:      Approximately 108.2 million kilometers from the Sun.
#   mercury:    Approximately 57.9 million kilometers from the Sun.
#
#   Display Planet Information: 
#   For each planet object, print its information and calculate the 
#   orbital period around the sun.
#
#   Print a blank line between each planet to make the output more readable
# 
#   Your output should look like
#
#   Name: Earth, Distance from Sun: 149.6 million km
#   Orbital Period (Earth years, rounded): 1830
#
#   Name: Mars, Distance from Sun: 227.9 million km
#   Orbital Period (Mars years, rounded): 3440
#
#   Name: Venus, Distance from Sun: 108.2 million km
#   Orbital Period (Venus years, rounded): 1125
#
#   Name: Mercury, Distance from Sun: 57.9 million km
#   Orbital Period (Mercury years, rounded): 441
#
#   My apology to all scientists.

class Planet:
    def __init__(self, name, distance_from_sun):
        self.name = name
        self.distance_from_sun = distance_from_sun
    
    def __str__(self):
        return (f"Name: {self.name}, Distance from Sun: {self.distance_from_sun} million km \n"
        f"Orbital Period ({self.name} years, rounded): {Planet.orbital_period(self)}")

    def orbital_period(self):
        # Calculate and round the orbital period to the nearest integer
        return round((self.distance_from_sun ** 1.5))

# Example planet objects
earth = Planet("Earth", 149.6)
mars = Planet("Mars", 277.9)
venus = Planet("Venus", 108.2)
mercury = Planet("Mercury", 57.9)

# Displaying each planet's information and its rounded orbital period
print(earth)
print("")
print(mars)
print("")
print(venus)
print("")
print(mercury)
