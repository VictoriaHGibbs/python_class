print("5.8")
usernames = ['admin', 'derpMcDerp', 'bobberton22', 'meowington', 'sillyoatmeal', 'partywalrus']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, Thank you for logging in again!")

print("")

print("5.9")
# usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, Thank you for logging in again!")
else:
    print("We need to find some users!")


print("")

print("5.10")

current_users = ['Admin', 'derpMcDerp', 'Bobberton22', 'meowington', 'sillyoatmeal', 'partywalrus']
new_users = ['derpMcDerp', 'partywalrus', 'jellojuggler', 'bittersmores', 'gluesniffer']

current_users_lc = [current_user.lower() for current_user in current_users]


for new_user in new_users:
    if new_user.lower() in current_users_lc:
        print(f"Sorry, {new_user} already exists, please pick a different username.")
    else:
        print(f"The username {new_user} is available!")

print("")
