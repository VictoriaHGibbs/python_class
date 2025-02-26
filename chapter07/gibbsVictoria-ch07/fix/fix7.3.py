# fix7.3.py - Flags
# 
# This program will display the name of any band you type in the prompt;
# however, when you type 'quit' to exit the program, the program keeps
# running. What can you do to fix the code so the program will quit?


prompt = "\nEnter the name of your favorite band and I will display it back to you "
prompt += "Enter 'quit' to end the program"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print (message)
