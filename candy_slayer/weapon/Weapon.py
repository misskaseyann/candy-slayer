class Weapon(object):
    """Basic weapon."""
    def __init__(self, name, attack_mod, num_uses, img):
        """
        Initialize weapon stats.

        :param name: name of the weapon
        :param attack_mod: multiplier of attack
        :param num_uses: uses available for weapon
        :param img: image of weapon
        """
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
