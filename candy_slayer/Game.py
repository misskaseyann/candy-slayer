from Neighborhood import Neighborhood
from Player import Player


class Game():
    """Initiate the Candy Slayer game."""

    def __init__(self):
        """Initialize neighborhood and player."""
        self.neighborhood = Neighborhood(2 , 2)
        self.population = self.neighborhood.get_population()
        self.neighborhood.display()
        self.player = Player("Kasey")
        self.player.display()
        print("Test observer pattern.")
        monsters = self.neighborhood.housing_grid[0][0].get_monsters()
        for item in monsters:
            print(item.name)
        print("Monster is killed.")
        monsters[0].hit(500)
        for item in monsters:
            print(item.name)