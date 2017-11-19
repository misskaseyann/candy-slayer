from random import *

from monster.Monster import Monster


class Ghoul(Monster):
    """
    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """
    def __init__(self, house):
        """Initializes the Ghoul monster."""
        super().__init__(randint(40, 80), house, "Ghoul")

    def attack(self):
        return randint(15, 30)