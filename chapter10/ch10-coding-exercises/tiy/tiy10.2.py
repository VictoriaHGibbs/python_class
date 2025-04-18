import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "learning_python.txt")

# Open the file
with open(file_path, "r") as file:
    contents = file.read()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
