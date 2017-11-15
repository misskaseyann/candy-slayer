from random import *

from weapon.ChocolateBar import ChocolateBar
from weapon.HersheyKisses import HersheyKisses
from weapon.NerdBomb import NerdBomb
from weapon.SourStraw import SourStraw

class Player():
    """Player of the game."""

    def __init__(self, name):
        """Initialize stats and inventory."""
        self.name = name
        self.hp = randint(100, 125)
        self.attack = randint(10, 20)
        self.inventory = self.setup_weapons()

    def setup_weapons(self):
        """Initialize weapon inventory at random with the
        exception that the first weapon is always a HersheyKiss"""
        self.weapons = [self.numb_to_weapon(randint(2, 4)) for i in range(9)]
        self.weapons.insert(0, HersheyKisses())
        return self.weapons

    def numb_to_weapon(self, x):
        """Link a value to a weapon object. A helper function to
        the initialization of the players random inventory."""
        weapon_val = {
            2: SourStraw(),
            3: ChocolateBar(),
            4: NerdBomb(),
        }
        return weapon_val.get(x, HersheyKisses())

    def display(self):
        """Test everything is working."""
        print("Testing Player class.")
        print(self.name)
        print(self.hp)
        print(self.attack)
        for item in self.inventory:
            print(item.name)