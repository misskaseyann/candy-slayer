from random import *

from monster.Monster import Monster


class Zombie(Monster):

    def __init__(self, house):
        """Initializes the Zombie monster."""
        super().__init__(randint(50, 100), house, "Zombie")

    def attack(self):
        return randint(0, 10)
