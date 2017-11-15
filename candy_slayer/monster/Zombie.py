from random import *

from monster.Monster import Monster


class Zombie(Monster):

    def __init__(self, house):
        """Initializes the Zombie monster."""
        super().__init__(randint(50, 100), house, "Zombie")

    def attack(self):
        """Monsters attack that is from 0-10 damage."""
        return randint(0, 10)

    def hit(self, attack_val, weapon):
        """Player attack on monster."""
        if weapon.name == "Sour Straw":
            attack_val *= 2
        super().hit(attack_val)