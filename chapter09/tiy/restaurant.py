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

