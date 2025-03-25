#   fix9.3.py - Dog all by itself
#
#   When creating a method in Python, you need to write code so the class is 
#   represented. In this program the dog can no longer sit by itself. 
#
#   Run the program, and read the error message to help you figure out what is
#   wrong.  
#   
#   What can you do to fix the problem?

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit():
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog()
your_dog = Dog()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()