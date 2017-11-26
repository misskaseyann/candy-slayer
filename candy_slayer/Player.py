from random import *

from candy_slayer.weapon.ChocolateBar import ChocolateBar
from candy_slayer.weapon.HersheyKisses import HersheyKisses
from candy_slayer.weapon.NerdBomb import NerdBomb
from candy_slayer.weapon.SourStraw import SourStraw


class Player:
    """Player of the game."""
    def __init__(self, name):
        """
        Initialize stats and inventory.

        :param name: name of player
        """
        self.name = name
        self.hpmax = randint(100, 125)
        self.currhp = self.hpmax
        self.attack = randint(10, 20)
        self.inventory = self.setup_weapons()
        self.currweapon = self.inventory[0]
        self.currhouse = None

    def get_attack(self):
        """
        Getter for the player attack.

        :return: the value of the player attack.
        """
        return self.attack

    def get_inventory(self):
        """
        Getter for the player's inventory.

        :return: list of weapons in player inventory.
        """
        return self.inventory

    def get_currhouse(self):
        """
        Getter for the player's current house.

        :return: house object the player is currently in.
        """
        return self.currhouse

    def set_currhouse(self, house):
        """
        Setter for the player's current house.

        :param house: house object the player is currently in.
        """
        self.currhouse = house

    def get_currweapon(self):
        """
        Getter for the player's current weapon.

        :return: weapon object the player is holding.
        """
        return self.currweapon

    def set_currweapon(self, weapon):
        """
        Change the players current weapon.

        :param weapon: a weapon object.
        """
        self.currweapon = weapon

    def get_hpmax(self):
        """
        Getter for player's max hp.

        :return: integer value of the players max hp.
        """
        return self.hpmax

    def get_currhp(self):
        """
        Getter for player's current hp.

        :return: floating value for the players current hp.
        """
        return self.currhp

    def set_currhp(self, hp):
        """
        Setter for the player's current hp.

        :param hp: floating value for the players current hp.
        """
        self.currhp = hp

    def setup_weapons(self):
        """
        Initialize weapon inventory at random with the
        exception that the first weapon is always a HersheyKiss.
        """
        self.weapons = [self.numb_to_weapon(randint(2, 4)) for i in range(9)]
        self.weapons.insert(0, HersheyKisses())
        return self.weapons

    def attack_monsters(self, monsters):
        """
        Attack all monsters in a house.

        :param monsters: list of monsters in a house
        """
        if self.currweapon.get_name() == "Hershey Kisses":
            for monster in monsters:
                monster.hit(self.attack * self.currweapon.get_attack_mod())
        elif self.currweapon.is_usable():
            for monster in monsters:
                monster.hit(self.attack * self.currweapon.get_attack_mod())
            self.currweapon.set_num_uses(self.currweapon.get_num_uses() - 1)

    @staticmethod
    def numb_to_weapon(x):
        """Link a value to a weapon object."""
        weapon_val = {
            2: SourStraw(),
            3: ChocolateBar(),
            4: NerdBomb(),
        }
        return weapon_val.get(x, HersheyKisses())
