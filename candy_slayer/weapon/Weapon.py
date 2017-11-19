class Weapon():
    """Basic weapon."""

    def __init__(self, name, attack_mod, num_uses, img):
        """Initialize weapon stats."""
        self.name = name
        self.attack_mod = attack_mod
        self.num_uses = num_uses
        self.img = img

    def is_usable(self):
        """Checks if weapon is past its usage."""
        if self.num_uses == 0:
            return False
        else:
            return True

    def get_attack_mod(self):
        """Returns the attack modifier."""
        return self.attack_mod

    def get_name(self):
        """Returns the weapon name."""
        return self.name