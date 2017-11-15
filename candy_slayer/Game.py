from Neighborhood import Neighborhood
from observed.Observer import Observer
from Player import Player


class Game():
    """Initiate the Candy Slayer game."""

    def __init__(self):
        """Initialize neighborhood and player."""
        self.neighborhood = Neighborhood(2 , 2, self)
        self.population = self.neighborhood.get_population()
        self.neighborhood.display()
        self.player = Player("Kasey")
        self.player.display()

    def update(self):
        self.population = self.neighborhood.get_population()