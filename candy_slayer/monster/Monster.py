from observed.Observable import Observable


class Monster(object):
    """Basic non player character."""
    def __init__(self, hp, house, name, img):
        """
        Initialize a monster.

        :param hp: health points
        :param house: house monster is located in
        :param name: name of monster
        :param img: image of monster
        """
        self.maxhp = hp
        self.hp = hp
        self.name = name
        self.observable = Observable()
        self.observable.register(house)
        self.monsterimg = img

    def attack(self, player):
        """
        Monster attack.

        :param player: player the attack is directed towards
        """
        pass

    def hit(self, attack_val):
        """
        Get hit by the player.

        :param attack_val: player attack value
        """
        self.hp -= attack_val
        if self.hp < 1:
            self.observable.update_observers()
