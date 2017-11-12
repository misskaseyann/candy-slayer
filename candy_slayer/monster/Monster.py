from observed.Observable import Observable

class Monster(Observable):
    """Basic non player character."""

    def __init__(self, hp, house, name):
        self.hp = hp
        self.name = name
        self.observable = Observable()
        self.observable.register(house)
        #self.observable.register(house)


    def attack(self):
        return 0

    def hit(self, attack_val):
        self.hp -= attack_val
        if self.hp < 1:
            self.observable.update_observers()

    # Add future method to drop weapon.
    # Add future method to talk to player.

