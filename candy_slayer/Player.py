from random import *

class Player():
    """Player of the game."""

    def __init__(self, name):
        """Initialize stats and inventory."""
        self.name = name
        self.hp = randint(100, 125)
        self.attack = randint(10, 20)
        self.weapons = [0 for i in range(10)]

    def display(self):
        """Test everything is working."""
        print("Testing Player class.")
        print(self.name)
        print(self.hp)
        print(self.attack)
        print(self.weapons)