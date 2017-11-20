import random

import os
import pygame

from weapon.Weapon import Weapon


class NerdBomb(Weapon):
    """High tier weapon NerdBomb."""
    def __init__(self):
        """Initialize the weapon."""
        super(NerdBomb, self).__init__("Nerd Bomb", random.uniform(3.5, 5), 1,
                                       pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                      "nerds.png")).convert_alpha())
