from random import *

from monster.Monster import Monster


class Ghoul(Monster):
    def __init__(self, house):
        """Initializes the Ghoul monster."""
        super().__init__(randint(40, 80), house, "Ghoul")

    def attack(self):
        return randint(15, 30)