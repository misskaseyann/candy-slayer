import random

import os
import pygame

from weapon.Weapon import Weapon


class ChocolateBar(Weapon):
    """Mid tier weapon ChocolateBar."""
    def __init__(self):
        """Initialize the weapon."""
        super(ChocolateBar, self).__init__("Chocolate Bar", random.uniform(2, 2.4), 4,
                                           pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                          "chocobar.png")).convert_alpha())
