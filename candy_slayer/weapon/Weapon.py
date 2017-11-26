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

    def get_img(self):
        """
        Getter for the weapon image.

        :return: png image representation of the weapon.
        """
        return self.img

    def get_num_uses(self):
        """
        Getter for the number of weapon uses.

        :return: integer value for the number of uses a weapon has.
        """
        return self.num_uses

    def set_num_uses(self, uses):
        """
        Setter for the number of weapon uses.

        :param uses: integer value for the number of uses a weapon has.
        """
        self.num_uses = uses

    def get_attack_mod(self):
        """
        Getter for the attack mod.

        :return: floating point of attack modifier.
        """
        return self.attack_mod

    def get_name(self):
        """
        Getter for weapon name.

        :return: the string variable for the weapon name.
        """
        return self.name

    def is_usable(self):
        """Checks if weapon is past its usage."""
        if self.num_uses == 0:
            return False
        else:
            return True
