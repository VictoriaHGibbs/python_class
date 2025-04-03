from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info_dictionary = json.loads(contents)
        return user_info_dictionary
    else:
        return None

def get_new_user_info(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    color = input("What is your favorite color? ")
    food = input("What is your favorite food? ")

    user_info_dictionary = {
        'username' : username,
        'color' : color,
        'food' : food,
    }

    contents = json.dumps(user_info_dictionary)
    path.write_text(contents)
    return user_info_dictionary

def greet_user():
    """Greet the user by name."""
    path = Path('chapter10/ch10-coding-exercises/tiy/username.json')
    user_info_dictionary = get_stored_user_info(path)
    if user_info_dictionary:
        print(f"Welcome back, {user_info_dictionary['username']}!")
        print(f"Your favorite color is {user_info_dictionary['color']}")
        print(f"Your favorite food is {user_info_dictionary['food']}")
    else:
        user_info_dictionary = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info_dictionary['username']}!")

greet_user()
