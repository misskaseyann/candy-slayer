from random import *

import os
import pygame

from candy_slayer.monster.Monster import Monster


class Werewolf(Monster):
    """
    Werewolf monster.

    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """
    def __init__(self, house):
        """
        Initialize the werewolf monster.

        :param house: the home that the werewolf is connected to
        """
        super().__init__(200, house, "Werewolf", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                                "werewolf.png")).convert_alpha())

    def attack(self, player):
        """
        Attack placed on the player by the werewolf with a range of 0 thru 40.

        :param player: the player the attack is directed towards
        """
        player.set_currhp(player.get_currhp() - randint(0, 40))
