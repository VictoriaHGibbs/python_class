import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the text file
file_path = os.path.join(script_dir, "guest_book.txt")

prompt = "\nWhat is your name? "
prompt += "\nType 'quit' to quit. "

guest_names = []
while True:
    name = input(prompt)
    if name.lower() == 'quit':
        break

    print(f"Thanks {name} for adding your name! ")
    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

# Open the file
with open(file_path, 'a') as file:
    file.write(file_string)
