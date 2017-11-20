import random

import os
import pygame

from weapon.Weapon import Weapon


class SourStraw(Weapon):
    """Low tier weapon SourStraws."""
    def __init__(self):
        """Initialize the weapon."""
        super(SourStraw, self).__init__("Sour Straw", random.uniform(1, 1.75), 2,
                                        pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                       "sourstraw.png")).convert_alpha())
