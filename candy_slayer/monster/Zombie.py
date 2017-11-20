from random import *

import os

import pygame

from monster.Monster import Monster


class Zombie(Monster):
    """
    Zombie object.

    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """

    def __init__(self, house):
        """
        Initializes the Zombie monster.

        :param house: the home that the zombie is attached to
        """
        super().__init__(randint(50, 100), house, "Zombie",
                         pygame.image.load(os.path.join("candy_slayer/assets/", "zombie.png")).convert_alpha())

    def attack(self, player):
        """
        Zombie attack that ranges from 0 thru 10.

        :param player: the player the attack is directed towards.
        """
        player.currhp -= randint(0, 10)
