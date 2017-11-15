from random import *

from monster.Monster import Monster


class Vampire(Monster):
    def __init__(self, house):
        """Initializes the Vampire monster."""
        super().__init__(randint(100, 200), house, "Vampire")

    def attack(self):
        """Monsters attack that is from 10-20 damage."""
        return randint(10, 20)

    def hit(self, attack_val, weapon):
        """Player attack on monster."""
        if weapon.name != "Chocolate Bar":
            super().hit(attack_val)