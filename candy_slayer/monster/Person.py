import os
import pygame

from monster.Monster import Monster


class Person(Monster):
    """Person and helper character."""
    def __init__(self, house):
        """Initialize the Person stats."""
        super().__init__(100, 0, "Person", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                          "person.png")).convert_alpha())

    def attack(self, player):
        """Gives the player one piece of candy
        which increases their health by +1 points."""
        player.currhp += 1

    def hit(self, attack_val):
        """Do nothing because they are not harmed by
        candy weapons."""