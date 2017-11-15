import random
from weapon.Weapon import Weapon

class ChocolateBar(Weapon):
    """Mid tier weapon SourStraws."""

    def __init__(self):
        """Initialize the weapon."""
        super().__init__("Chocolate Bar", random.uniform(2, 2.4), 4)