prompt = "\nEnter your age and I'll tell you the price?"
prompt += "\nType 'quit' to stop.\n"
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print(f"You are {age}, your ticket is free!")
    elif age < 13:
        print(f"You are {age}, your ticket is $10!")
    else:
        print(f"You are {age}, your ticket is $15!")
