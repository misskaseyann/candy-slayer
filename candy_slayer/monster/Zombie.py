from random import *

import os

import pygame

from monster.Monster import Monster


class Zombie(Monster):

    def __init__(self, house):
        """Initializes the Zombie monster."""
        super().__init__(randint(50, 100), house, "Zombie", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                          "zombie.png")).convert_alpha())

    def attack(self, player):
        player.currhp -= randint(0, 10)
