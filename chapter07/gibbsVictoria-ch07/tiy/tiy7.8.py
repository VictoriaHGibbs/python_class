sandwich_orders = ['meatball', 'club', 'gyro', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sammich!")
    finished_sandwiches.append(current_order)

# Displaying all sandwiches
print("\nThese sandwiches have been completed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
