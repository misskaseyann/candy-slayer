from random import *

from monster.Monster import Monster


class Werewolf(Monster):

    def __init__(self, house):
        """Initializes the Werewolf monster."""
        super().__init__(200, house, "Werewolf")

    def attack(self):
        """Monsters attack that is from 0-40 damage."""
        return randint(0, 40)

    def hit(self, attack_val, weapon):
        """Player attack on monster."""
        if weapon.name == "Hershey Kisses":
            super().hit(attack_val)
        if weapon.name == "Nerd Bomb":
            super().hit(attack_val)