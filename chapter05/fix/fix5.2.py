#fix5.2.py
# What's wrong here? We have a list of members to our website, and Walter is the
# only Admin. There is a syntax error that keeps the program from running. Fix
# the program to eliminate the syntax error.

members = ['Nathanial', 'Walter', 'Erin', 'jean']

for member in members:
    if member = 'Walter':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Welcome {member}.")