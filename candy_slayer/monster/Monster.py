from observed.Observable import Observable

class Monster():
    """Basic non player character."""

    def __init__(self, hp, house, name, img):
        self.maxhp = hp
        self.hp = hp
        self.name = name
        self.observable = Observable()
        self.observable.register(house)
        self.monsterimg = img

    def attack(self, player):
        pass

    def hit(self, attack_val):
        self.hp -= attack_val
        if self.hp < 1:
            self.observable.update_observers()

    # Add future method to drop weapon.
    # Add future method to talk to player.

