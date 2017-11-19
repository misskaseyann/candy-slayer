from random import randint

from Neighborhood import Neighborhood
from Player import Player


class Manager(object):
    def __init__(self):
        self.game = None
        self.neighborhood = Neighborhood((randint(2, 6)), randint(2, 6))
        self.population = self.neighborhood.get_population()
        self.neighborhood.display()
        self.player = Player("Kasey")

    def add_game(self, game):
        self.game = game
