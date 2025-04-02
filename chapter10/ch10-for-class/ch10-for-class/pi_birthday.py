import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "pi_million_digits.txt")

# Open the file
with open(file_path, "r") as file:
    contents = file.read()

# from pathlib import Path

# path = Path('pi_million_digits.txt')
# contents = file_path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
