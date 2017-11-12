import random
from weapon.Weapon import Weapon

class NerdBomb(Weapon):
    """High tier weapon SourStraws."""

    def __init__(self):
        """Initialize the weapon."""
        super(NerdBomb, self).__init__("Nerd Bomb", random.uniform(3.5, 5), 1)