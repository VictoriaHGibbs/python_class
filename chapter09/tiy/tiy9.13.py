from random import randint

class Die:
    """Six sided die class"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die6 = Die(6)

for _ in range(0, 10):
    die6.roll_die()

print("")

die10 = Die(10)

for _ in range(0, 10):
    die10.roll_die()

print("")

die20 = Die(20)

for _ in range(0, 10):
    die20.roll_die()
