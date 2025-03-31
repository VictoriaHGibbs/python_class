# Chapter 10
# Files and Exceptions



#file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)


# Relative and Absolute Paths

# Relative Paths
# A relative path tells Python to look for a given location in relation to the directory where the currently running program file is stored.
# For example, when you pass the name of a text file to the open() function, Python looks for this file in the directory where the program that’s currently being executed is stored.
path = Path('text_files/relative_path.txt')

# Absolute Paths
# An absolute path, which always begins with the root folder, tells Python exactly where a file is on your computer regardless of where the program that’s being executed is stored.
path = Path('/home/ehmatthes/other_files/absolute_path.txt')

# Accessing a Files Lines

#file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.split('\n')
for line in lines:
    print(line)


# Working with a File’s Contents

#pi_string.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.split('\n')
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# The variable pi_string contains the digits of pi as a string, and the variable len(pi_string) tells us how many characters are in that string.

# --snip--

for line in lines:
    pi_string += line.strip()

# Large Files: One Million Digits

#pi_string.py
from pathlib import Path
contents = Path('pi_million_digits.txt').read_text()

lines = contents.split('\n')
pi_string = ''
for line in lines:
    pi_string += line.strip()
# print the first 52 characters
print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is Your Birthday Contained in Pi?

# use pi_brithdaty file in ch10 folder

# writing to a file

# be careful with write mode, it will overwrite the file

#write_message.py
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming!")

# writing multiple lines

#write_messages.py
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming!\n")


# writing multiple lines
contents = "I love programming!\n"
contents += "I love creating new games.\n"
contents += "I love creating new games.\n"


# Appending to a File
# I didn't see this in the book, but I think it's a good idea to add it here
#append_message.py
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming!\n")
path.write_text("I love creating new games.\n") # This will overwrite the file

# TiY 10-5


# Exceptions

# ZeroDivisionError
# This error occurs when you try to divide a number by zero.
# Python will raise a ZeroDivisionError exception whenever this error occurs.
# print(5/0)

# Using try-except Blocks

#division.py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# The else Block

#division.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# Handling the FileNotFoundError Exception

#alice.py
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

# Analyzing Text

#alice.py
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# Working with Multiple Files

#word_count.py  
from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file."""
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        
filename = 'alice.txt'
count_words(filename)

# Failing Silently

#word_count.py
from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file."""
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

# TiY 10.6

# Storing Data

# Using json.dump() and json.load()

#number_writer.py
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
with path.open(mode='w') as file_object:
    json.dump(numbers, file_object)

#number_reader.py
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text
numbers = json.load(file_object)
print(numbers)

# saving and reading user-generated data

#remember_me.py
import json

username = input("What is your name? ") 
filename = 'username.json'
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print(f"We'll remember you when you come back, {username}!")

#remember_me.py
import json

filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# Refactoring

#remember_me.py
import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()

# TiY 10-13

# Testing the remember_me.py

#remember_me.py
import json

def get_stored_username(path):
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username 
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user(path):
    """Greet the user by name."""
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

filename = 'username.json'
greet_user(filename)

# TiY 10-14












