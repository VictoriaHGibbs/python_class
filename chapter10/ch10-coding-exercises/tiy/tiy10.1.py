import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "learning_python.txt")

# Open the file
with open(file_path, "r") as file:
    contents = file.read()

print(f"Printing the contents by reading in the entire file: ")
print(contents)

print("\n")

print(f"Printing the contents by looping through the lines: ")
lines = contents.splitlines()
for line in lines:
    print(line)
