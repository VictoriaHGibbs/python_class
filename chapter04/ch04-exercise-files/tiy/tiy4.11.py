pizzas = ['supreme', 'meat lovers', 'greek']
friend_pizzas = pizzas[:]

pizzas.append('veggie')
friend_pizzas.append('pepperoni')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"* {pizza}")

print("\nMy friend's favorite pizzas are:")
for f_pizza in friend_pizzas:
    print(f"* {f_pizza}")
