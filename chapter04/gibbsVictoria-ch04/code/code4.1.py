# code4.1.py - solar system

# In this exercise, you are required to add Pluto to the list of planets in the solar system
# then print out the 'old' solar system in alphabetical order.

# The planets in our solar system
solar_system = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Copy the list to a new list named solar_system_plus_pluto
solar_system_plus_pluto = solar_system[:]

# Add Pluto to the new list
solar_system_plus_pluto.append("Pluto")

# Print out both lists
print("Original Solar System:")
print(solar_system)

print("\nSolar System Plus Pluto (Alphabetical Order):")
print(sorted(solar_system_plus_pluto))
