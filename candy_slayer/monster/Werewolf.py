from random import *

from monster.Monster import Monster


class Werewolf(Monster):

    def __init__(self, house):
        """Initializes the Werewolf monster."""
        super().__init__(200, house, "Werewolf")

    def attack(self):
        return randint(0, 40)