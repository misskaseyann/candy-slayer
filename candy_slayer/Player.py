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
        self.hpmax = randint(100, 125)
        self.currhp = self.hpmax
        self.attack = randint(10, 20)
        self.inventory = self.setup_weapons()
        self.currweapon = self.inventory[0]
        self.currhouse = None

    def setup_weapons(self):
        """Initialize weapon inventory at random with the
        exception that the first weapon is always a HersheyKiss"""
        self.weapons = [self.numb_to_weapon(randint(2, 4)) for i in range(9)]
        self.weapons.insert(0, HersheyKisses())
        return self.weapons

    def numb_to_weapon(self, x):
        """Link a value to a weapon object."""
        weapon_val = {
            2: SourStraw(),
            3: ChocolateBar(),
            4: NerdBomb(),
        }
        return weapon_val.get(x, HersheyKisses())

    def attack_monsters(self, monsters):
        if self.currweapon.name == "Hershey Kisses":
            for monster in monsters:
                monster.hit(self.attack * self.currweapon.attack_mod)
        elif self.currweapon.is_usable():
            for monster in monsters:
                monster.hit(self.attack * self.currweapon.attack_mod)
            self.currweapon.num_uses -= 1