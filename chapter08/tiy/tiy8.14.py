def make_car(manufacturer, model, **features):
    """dictionary that stores info about a car"""
    dictionary = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for feature, value in features.items():
        dictionary[feature] = value

    return dictionary

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
