import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "pi_digits.txt")

# Open the file
with open(file_path, "r") as file:
    contents = file.read()

# file_reader.py
print(f"Running file_reader.py now!\n")
for line in contents.splitlines():
    print(line)


# pi_birthday.py
print(f"Running pi_birthday.py now!\n")

file_path = os.path.join(script_dir, "pi_million_digits.txt")

# Open the file
with open(file_path, "r") as file:
    pi_contents = file.read()

pi_string = ''
for line in pi_contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# pi_string.py
print(f"Running pi_string.py now!\n")

file_path = os.path.join(script_dir, "pi_million_digits.txt")

# Open the file
with open(file_path, "r") as file:
    pi_contents2 = file.read()

pi_string = ''
for line in pi_contents2.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
