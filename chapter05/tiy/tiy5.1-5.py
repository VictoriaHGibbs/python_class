print("5.2")
food = 'taco'
print("Is food == 'taco'? I predict true")
print(food == 'taco')
print("")

print("Is food != 'taco'? I predict false")
print(food != 'taco')
print("")

print("Is food != 'pizza'? I predict true")
print(food != 'pizza')
print("")

party_food = 'Pizza'
print("Is party_food == 'pizza'? I predict false")
print(party_food == 'pizza')

print("Is party_food.lower() == 'pizza'? I predict true")
print(party_food.lower() == 'pizza')

pizza_amount = 5
pizza_needed = 4
pizza_eaten = 4
print("Is pizza_amount == 3? I predict false")
print(pizza_amount == 3)

print("Is pizza_amount >= 5? I predict true")
print(pizza_amount >= 5)

print("is pizza_amount >= pizza_needed and pizza_amount >= pizza_eaten? I predict true")
print(pizza_amount >= pizza_needed and pizza_amount >= pizza_eaten)

pizza_toppings = ['pepperoni', 'mushrooms', 'sausage', 'onions', 'peppers', 'bacon']
print("Is pepperoni in pizza_toppings? I predict true")
print('pepperoni' in pizza_toppings)

print("Are olives in pizza_toppings? I predict false")
print('olives' in pizza_toppings)

print("")

print("5.3")
alien_color = 'yellow'
if alien_color == 'green':
    print("Yey! You just got 5 points!")

if alien_color != 'green':
    print("Yey! You just got 5 points!")

print("")

print("5.4")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

if alien_color != 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

print("")

print("5.5")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
print("")
