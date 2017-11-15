from observed.Observable import Observable


class Monster(Observable):
    """Basic non player character."""

    def __init__(self, hp, house, name):
        """Initialize a monster class with a house observer"""
        self.hp = hp
        self.name = name
        self.observable = Observable()
        self.observable.register(house)


    def attack(self):
        """Monster attack."""
        return 0

    def hit(self, attack_val):
        """Player attack on monster. Less than zero hp alerts observers."""
        self.hp -= attack_val
        if self.hp < 1:
            self.observable.update_observers()

    # Add future method to drop weapon.
    # Add future method to talk to player.