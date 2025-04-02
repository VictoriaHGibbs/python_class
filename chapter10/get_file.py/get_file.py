import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "py_digits.txt")

# Open the file
with open(file_path, "r") as file:
    data = file.read()
    print(data)

# ----------------------------- 

import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "pi_million_digits.txt")

# Open the file
with open(file_path, "r") as file:
    contents = file.read()
