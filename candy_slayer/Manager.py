from random import randint

from Neighborhood import Neighborhood
from Player import Player
from observed.Observer import Observer


class Manager(Observer):
    """Manages the game logic objects."""
    def __init__(self):
        """Initialize game logic objects."""
        self.game = None
        self.neighborhood = Neighborhood((randint(2, 6)), randint(2, 6), self)
        self.population = self.neighborhood.get_population()
        self.player = Player("Kasey")

    def add_game(self, game):
        """
        Set up a game to the class.
        """
        self.game = game  # This is a for now permanent work-around so that game states initialize.

    def update(self):
        """When house population of monsters changes, update the population count."""
        self.population = self.neighborhood.get_population()  # Originally found in Game class.
