from random import *

from monster.Monster import Monster


class Vampire(Monster):
    def __init__(self, house):
        """Initializes the Vampire monster."""
        super().__init__(randint(100, 200), house, "Vampire")

    def attack(self):
        return randint(10, 20)