from random import *

import os
import pygame

from monster.Monster import Monster


class Ghoul(Monster):
    """
    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """
    def __init__(self, house):
        """Initializes the Ghoul monster."""
        super().__init__(randint(40, 80), house, "Ghoul",
                         pygame.image.load(os.path.join("candy_slayer/assets/",
                                                        "ghoul.png")).convert_alpha())

    def attack(self, player):
        player.currhp -= randint(15, 30)