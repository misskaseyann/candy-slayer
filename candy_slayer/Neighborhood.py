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

    def get_house(self, housey, housex):
        """
        Get the house located in a specific spot of the neighborhood.
        :param housey: y parameter of the neighborhood grid.
        :param housex: x parameter of the neighborhood grid.
        :return: house object at the x,y point.
        """
        return self.housing_grid[housey][housex]

    def get_width(self):
        """
        Getter for the neighborhood grid width.

        :return: integer value for the neighborhood width.
        """
        return self.width

    def get_height(self):
        """
        Getter for the neighborhood grid height.

        :return: integer value for the neighborhood height.
        """
        return self.height

    def get_population(self):
        """Find the population of the neighborhood."""
        x = 0
        for row in self.housing_grid:
            for item in row:
                x += item.get_population()
        return x
