rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'amazon': 'brazil',
}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

print("\nRivers only:")
for key in rivers:
    print(f"{key.title()}")

print("\nCountries only:")
for value in rivers.values():
    print(f"{value.title()}")
