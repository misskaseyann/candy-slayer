from random import *

import os
import pygame

from monster.Monster import Monster


class Vampire(Monster):
    """
    Vampire monster.

    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """
    def __init__(self, house):
        """
        Initialize the vampire monster.

        :param house: the home the vampire is attached to
        """
        super().__init__(randint(100, 200), house, "Vampire", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                                "vampire.png")).convert_alpha())

    def attack(self, player):
        """
        Vampire attack from 10 thru 20 on the player.

        :param player: player object that the monster attacks
        """
        player.currhp -= randint(10, 20)
