#cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']
for cars in cars:
    if cars == 'bmw':
        print(cars.upper())
    else:
        print(cars.title())

# = and == are different
car = 'bmw'
car == 'bmw' # True

# ingoring case when checking for equality
car = 'Audi'
car.lower() == 'audi' # True

# checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")    

# numerical comparisons
age = 18
age == 18 # True
age != 18 # False
age < 21 # True
age <= 21 # True
age > 21 # False
age >= 21 #

# checking multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # False
age_0 >= 21 or age_1 >= 21 # True

# value in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings # True
'pepperoni' in requested_toppings # False

#checking if a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# boolean expressions
game_active = True
can_edit = False

# try it yourself 5.1 or 2

# if statement with a single block
age = 19
if age >= 18:
    print("You are old enough to vote!")

# if-else statement
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote!")

# if-elif-else chain
# if you need to test more than two possible situations, use if-elif-else chain
# Python executes only one block in an if-elif-else chain
# it runs each conditional test in order until one passes
# when a test passes, the code following that test is executed and Python skips the rest of the tests
# if none of the tests pass, the else block is executed
# you can use as many elif blocks as you need
# you can omit the else block if it is not needed
# if you want to test multiple conditions, use a series of simple if statements with no elif or else blocks
# if you want only one block of code to run, use an if-elif-else chain
# if you want to run multiple blocks of code, use a series of independent if statements
# if you want to test multiple conditions, use a series of if statements
# if you want to test multiple conditions, use an if-elif-else chain
# if you want to test multiple conditions, use a series of if statements

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# if you want to test multiple conditions, use a series of if statements
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# if you want to test multiple conditions, use an if-elif-else chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40  
else:
    price = 20
print(f"Your admission cost is ${price}.")

# python does not require an else block at the end of an if-elif chain

# if you want to test multiple conditions, use a series of if statements
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# try it yourself 5.3 or 4 or 5 or 6 or 7 or 8 or 9 or 10

# using if statements with lists
# checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")   
print("\nFinished making your pizza!")

# checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# try it yourself 5.11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40 or 41 or 42 or 43 or 44 or 45 or 46 or 47 or 48 or 49 or 50 or 51 or 52 or 53 or 54 or 55 or 56 or 57 or 58 or 59 or 60 or 61 or 62 or 63 or 64 or 65 or 66 or 67 or 68 or 69 or 70 or 71 or 72 or 73 or 74 or 75 or 76 or 77 or 78 or 79 or 80 or 81 or 82 or 83 or 84 or 85 or 86 or 87 or 88 or 89 or 90 or 91 or 92 or 93 or 94 or 95 or 96 or 97 or 98 or 99 or 100 or 101 or 102 or 103 or 104 or 105 or 106 or 107 or 108 or 109 or 110 or 111 or 112 or 113 or 114 or 115 or 116 or 117 or 118 or 119 or 120 or 121 or 122 or 123 or 124 or 125 or 126 or 127 or 128 or 129 or 130 or 131 or 132 or 133 or 134 or 135 or 136 or 137 or 138 or 139 or 140 or 141 or 142 or 143 or 144 or 145 or 146 or 147 or 148 or 149 or 150 or 151 or 152 or 153 or 154 or 155 or 156 or 157 or 158 or 159 or 160 or 161 or 162 or 163 or 164 or 165 or 166 or 167 or 168 or 169 or 170 or 171 or 172 or 173 or 174 or 175





