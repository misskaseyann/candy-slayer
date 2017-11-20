import os
import pygame

from candy_slayer.monster.Monster import Monster


class Person(Monster):
    """
    Person and helper character.

    Image source by r1k at: http://pixeljoint.com/pixelart/63772.htm
    """
    def __init__(self, house):
        """
        Initialize the person.

        :param house: home that the person is attached to
        """
        super().__init__(100, 0, "Person", pygame.image.load(os.path.join("candy_slayer/assets/",
                                                                          "person.png")).convert_alpha())

    def attack(self, player):
        """
        Gives the player candy which offers +10 health points.

        :param player: player object receiving health
        """
        player.currhp += 10

    def hit(self, attack_val):
        """
        Do nothing because the player gets help from persons.

        :param attack_val: zero value
        """
        pass
