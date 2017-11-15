from random import *

from monster.Monster import Monster


class Ghoul(Monster):
    def __init__(self, house):
        """Initializes the Ghoul monster."""
        super().__init__(randint(40, 80), house, "Ghoul")

    def attack(self):
        """Monsters attack that is from 15-30 damage."""
        return randint(15, 30)

    def hit(self, attack_val, weapon):
        """Player attack on monster."""
        if weapon.name == "Nerd Bomb":
            attack_val *= 5
        super().hit(attack_val)