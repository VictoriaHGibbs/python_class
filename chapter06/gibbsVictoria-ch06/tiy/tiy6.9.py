favorite_places = {
    'sarah': ['mountains', 'home', 'chocolate store'],
    'phil': ['beach', 'sand dunes', 'ocean'],
    'bobbert': ['costco', 'taco bell'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} wants to go to:")
    for place in places:
        print(f" {place.title()}")
