from random import *

import os
import pygame

from monster.Monster import Monster


class Vampire(Monster):
    def __init__(self, house):
        """Initializes the Vampire monster."""
        super().__init__(randint(100, 200), house, "Vampire", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                          "vampire.png")).convert_alpha())

    def attack(self, player):
        player.currhp -= randint(10, 20)