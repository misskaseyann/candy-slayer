from weapon.Weapon import Weapon


class HersheyKisses(Weapon):
    """Base level weapon HersheyKisses."""

    def __init__(self):
        """Initialize the weapon."""
        super().__init__("Hershey Kisses", 1, -1)