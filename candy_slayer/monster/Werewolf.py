from random import *

import os
import pygame

from monster.Monster import Monster


class Werewolf(Monster):

    def __init__(self, house):
        """Initializes the Werewolf monster."""
        super().__init__(200, house, "Werewolf", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                          "werewolf.png")).convert_alpha())

    def attack(self, player):
        player.currhp -= randint(0, 40)