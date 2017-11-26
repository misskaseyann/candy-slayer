from random import *

import os
import pygame

from candy_slayer.monster.Monster import Monster


class Ghoul(Monster):
    """
    Ghoul monster.

    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """
    def __init__(self, house):
        """
        Initialize a Ghoul monster.

        :param house: house the Ghoul is attached to
        """
        super().__init__(randint(40, 80), house, "Ghoul",
                         pygame.image.load(os.path.join("candy_slayer/assets/",
                                                        "ghoul.png")).convert_alpha())

    def attack(self, player):
        """
        Attack the player in a range between 15 thru 30.

        :param player: player the attack is aimed towards
        """
        player.set_currhp(player.get_currhp() - randint(15, 30))
