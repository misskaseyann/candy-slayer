import random
from weapon.Weapon import Weapon

class SourStraw(Weapon):
    """Low tier weapon SourStraws."""

    def __init__(self):
        """Initialize the weapon."""
        super().__init__("Sour Straw", random.uniform(1, 1.75), 2)
