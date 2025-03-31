class Restaurant:
    """A class to store restaurant information"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Gives restaurant name and cuisine type"""
        desc = f"The restaurant {self.restaurant_name}, serves {self.cuisine_type} food."
        print(desc)

    def open_restaurant(self):
        """Gives restaurant status"""
        desc = f"{self.restaurant_name} is open!"
        print(desc)

class IceCreamStand(Restaurant):
    """Subclass from Restaurant to add in flavors"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize IceCreamStand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavor(self):
        """Display flavor."""
        print(f"Available flavors are: ")
        for flavor in self.flavors:
            print(f"{flavor}")


iceCreamStand = IceCreamStand('Scoopy-scooooops', 'ice cream', ['chocolate', 'vanilla', 'coffee'])
iceCreamStand.display_flavor()
