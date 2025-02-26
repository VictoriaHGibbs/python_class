sandwich_orders = ['meatball', 'pastrami', 'club', 'pastrami', 'gyro', 'tuna', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"\nI made your {current_order} sammich!")
    finished_sandwiches.append(current_order)

# Displaying all sandwiches
print("\nThese sandwiches have been completed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

