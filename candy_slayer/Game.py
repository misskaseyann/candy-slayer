from Neighborhood import Neighborhood
from Player import Player


class Game():
    """Initiate the Candy Slayer game."""

    def __init__(self):
        """Initialize neighborhood and player."""
        self.neighborhood = Neighborhood(5 , 10)
        self.neighborhood.display()
        self.player = Player("Kasey")
        self.player.display()
        #population = ...