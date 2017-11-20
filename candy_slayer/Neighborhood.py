from candy_slayer.Home import Home


class Neighborhood:
    """A neighborhood filled with homes on a grid."""
    def __init__(self, width, height, manager):
        """
        Initialize the house grid.

        :param width: width of the game grid
        :param height: height of the game grid
        :param manager: game object manager
        """
        self.width = width
        self.height = height
        self.housing_grid = [[Home(manager) for y in range(self.width)] for x in range(self.height)]

    def get_population(self):
        """Find the population of the neighborhood."""
        x = 0
        for row in self.housing_grid:
            for item in row:
                x += item.get_population
        return x
