import os
import pygame

from candy_slayer.weapon.Weapon import Weapon


class HersheyKisses(Weapon):
    """Base level weapon HersheyKisses."""
    def __init__(self):
        """Initialize the weapon."""
        super(HersheyKisses, self).__init__("Hershey Kisses", 1, 100,
                                            pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                           "hersheykisses.png")).convert_alpha())
