buffet = ('tacos', 'pizza', 'chicky nuggies', 'steak', 'bbq')
print("Menu:")
for food in buffet:
    print(food)

# buffet[0] = 'burritos'

# Traceback (most recent call last):
#   File "c:\Users\18282\.vscode\extensions\ms-python.python-2024.22.2-win32-x64\python_files\python_server.py", line 133, in exec_user_input
#     retval = callable_(user_input, user_globals)
#   File "<string>", line 5, in <module>
# TypeError: 'tuple' object does not support item assignment

buffet = ('tacos', 'pizza', 'grilled flamingo', 'steak', 'squirrel jerky')
print("\nNew Menu:")
for food in buffet:
    print(food)
