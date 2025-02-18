# A simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points']) 

# Accessing values in a dictionary
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# For more information on dictionaries, see the Python documentation:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries 
# https://docs.python.org/3/library/stdtypes.html#dict

# For a more interesting example, let's track the position of an alien that can move at different speeds.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


# Removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#NOTE: The del statement deletes the key-value pair from the dictionary entirely.

# A dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}   
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")
#NOTE: The key 'sarah' is used to access the value 'c' in the dictionary favorite_languages.

# Using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'No points value assigned.'))
#NOTE: The get() method requires a key as a first argument.
# The second argument is an optional message that will be returned if the key is not found.
# If the key is not found and no second argument is provided, None is returned.

# TiY 6-1 2 3 

# Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#NOTE: The items() method returns a list of key-value pairs.

# Looping through all the keys in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

#NOTE: The keys() method returns a list of keys.

# Looping through all the values in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in favorite_languages.values():
    print(language.title())

# Embedding an IF statement in the FOR loop

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#NOTE: The values() method returns a list of values.

# Looping through a dictionary's keys in order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
#NOTE: The values() method returns a list of values.

# Using set() to avoid repeating values
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    
#NOTE: The set() method returns a list of unique values.

# TiY 6-4 5 6 7 8 9 10

# Nesting dictionaries

# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
# A more realistic example
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# TiY 6.7 - 12















